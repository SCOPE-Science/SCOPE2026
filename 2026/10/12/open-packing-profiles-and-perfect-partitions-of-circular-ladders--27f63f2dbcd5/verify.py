"""Exact trace/determinant identities and independent small-case open-packing check.
Run with Python 3.9 or newer, standard library only: python verify.py.
"""
from collections import defaultdict
from itertools import combinations
from math import comb

STATES = [(a, b) for a in range(4) for b in range(4)]
INDEX = {s: i for i, s in enumerate(STATES)}

def compatible(a, b, c):
    return not (((a & 1) and (b & 2)) or ((a & 2) and (b & 1)) or
                ((a & 1) and (c & 1)) or ((a & 2) and (c & 2)))

def polynomial_add(a, b, scale=1):
    result = dict(a)
    for k, v in b.items():
        result[k] = result.get(k, 0) + scale * v
    return {k: v for k, v in result.items() if v}

def polynomial_mul(a, b):
    out = defaultdict(int)
    for k, v in a.items():
        for l, w in b.items():
            out[k+l] += v*w
    return {k: v for k,v in out.items() if v}

def transfer():
    out = [[{} for _ in range(16)] for _ in range(16)]
    for i, (a, b) in enumerate(STATES):
        for c in range(4):
            if compatible(a, b, c):
                out[i][INDEX[(b, c)]] = {c.bit_count(): 1}
    return out

def matrix_mul(a, b):
    n=len(a)
    out=[[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if not a[i][k]: continue
            for j in range(n):
                if b[k][j]:
                    out[i][j] = polynomial_add(out[i][j], polynomial_mul(a[i][k], b[k][j]))
    return out

def matrix_trace(A):
    r={}
    for i in range(len(A)):
        r=polynomial_add(r,A[i][i])
    return r

def traces(N):
    T=transfer(); power=T
    for k in range(1,N+1):
        yield matrix_trace(power)
        if k<N: power=matrix_mul(power,T)

def determinant_coefficients():
    """Newton identities: det(I-tT)=sum c[k]*t**k."""
    tr=list(traces(16)); coeffs=[{0:1}]
    for k in range(1,17):
        p={}
        for j in range(1,k+1):
            p=polynomial_add(p, polynomial_mul(coeffs[k-j],tr[j-1]))
        assert all(v%k==0 for v in p.values()), (k,p)
        coeffs.append({e:-v//k for e,v in p.items()})
    return coeffs

def formula_det():
    """(1-t-2*x*t^2-x^2*t^3) ((1+x*t^2)^2-x^4*t^6)."""
    A={(0,0):1,(1,0):-1,(2,1):-2,(3,2):-1}
    B={(0,0):1,(2,1):2,(4,2):1,(6,4):-1}
    C=defaultdict(int)
    for (i,j),a in A.items():
        for (k,l),b in B.items(): C[i+k,j+l]+=a*b
    return [{j:v for (k,j),v in C.items() if k==i and v} for i in range(17)]

def trace_profiles(max_n):
    return list(traces(max_n))

def brute_profile(n):
    """Direct open-neighborhood disjointness; independent of transfer rule."""
    N=2*n
    neighborhood=[]
    for i in range(n):
        for rail in range(2):
            neighborhood.append({2*((i-1)%n)+rail,2*((i+1)%n)+rail,2*i+(1-rail)})
    conflicts=[]
    for u in range(N):
        conflict=0
        for v in range(N):
            if u!=v and neighborhood[u]&neighborhood[v]: conflict|=1<<v
        conflicts.append(conflict)
    r=defaultdict(int)
    for mask in range(1<<N):
        feasible=True
        cur=mask
        while cur:
            bit=cur&-cur;u=bit.bit_length()-1
            if conflicts[u] & (cur ^ bit):
                feasible=False;break
            cur ^= bit
        if feasible:r[mask.bit_count()]+=1
    return dict(r)

def max_formula(n):
    r=n%6
    return {0: (2*n//3,9),
            1: (2*n//3,n*(2*n+1)//3),
            2: (2*(n//3),(n*(n+1)//6)**2),
            3: (2*n//3,3),
            4: (2*(n//3),n*n),
            5: (2*n//3,2*n)}[r]

def check():
    dc=determinant_coefficients(); expected=formula_det()
    assert dc==expected,(dc,expected)
    print('Exact determinant via 16 Newton identities: PASS')
    all_tr=trace_profiles(60)
    assert all_tr[0]=={0:1} and all_tr[1]=={0:1}
    print('Small-cycle trace correction: tr(T)=tr(T^2)=1')
    for n in range(3,9):
        actual=brute_profile(n)
        assert actual==all_tr[n-1],(n,actual,all_tr[n-1])
    print('Direct open-neighborhood subset comparisons n=3,...,8: PASS (87,360 subsets)')
    for n in range(3,61):
        p=all_tr[n-1]
        degree=max(p)
        assert (degree,p[degree])==max_formula(n),(n,degree,p[degree],max_formula(n))
        assert all(v>0 for v in p.values())
    print('Degree and extremal coefficient for n=3,...,60: PASS')
    for n in range(3,10):
        p=all_tr[n-1]
        print('n',n,'coefficients',sorted(p.items()))

if __name__=='__main__':check()

# Extra independent check for exact covers by maximum open packings.
def perfect_packing_partition_count(n):
    N=2*n
    neighborhoods=[]
    for i in range(n):
        for rail in range(2):
            neighborhoods.append({2*((i-1)%n)+rail,2*((i+1)%n)+rail,2*i+(1-rail)})
    conflicts=[]
    for u in range(N):
        conflicts.append(sum((1<<v) for v in range(N)
                             if u!=v and neighborhoods[u].intersection(neighborhoods[v])))
    max_k = max_formula(n)[0]
    if N % max_k: return 0
    masks=[]
    for mask in range(1<<N):
        if mask.bit_count()!=max_k: continue
        selected=[v for v in range(N) if mask & (1<<v)]
        if all(not(conflicts[u] & (1<<v)) for j,u in enumerate(selected)
               for v in selected[j+1:]):
            masks.append(mask)
    by_vertex=[[] for _ in range(N)]
    for mask in masks:
        for v in range(N):
            if mask & (1<<v):by_vertex[v].append(mask)
    from functools import lru_cache
    @lru_cache(None)
    def covers(rem):
        if not rem:return 1
        first=(rem&-rem).bit_length()-1
        return sum(covers(rem ^ mask) for mask in by_vertex[first] if rem & mask == mask)
    return covers((1<<N)-1)

if __name__ == '__main__':
    for n in range(3,9):
        actual=perfect_packing_partition_count(n)
        expected = (1 if n%3==0 and n%2 else
                    6 if n%3==0 else 24 if n==4 else 1176 if n==8 else 0)
        assert actual==expected,(n,actual,expected)
        print('n',n,'perfect maximum-packing partitions',actual)
    print('Exact-cover census n=3,...,8: PASS')

def cycle_square_independence(N):
    return {k:(1 if k==0 else N*comb(N-2*k,k)//(N-2*k))
            for k in range(N//3+1)}

if __name__=='__main__':
    tr=list(traces(60))
    for n in range(3,61):
        a=cycle_square_independence(2*n if n%2 else n)
        expected=a if n%2 else polynomial_mul(a,a)
        assert tr[n-1]==expected, (n,tr[n-1],expected)
    print('Direct cyclic gap formula versus transfer coefficients n=3,...,60: PASS')
