"""Independent finite checks for the zero-forcing census of the subdivided wheel with pendant spokes.

Run: python3 hybrid_forcing_verify.py
No external packages.
"""
from collections import Counter
from itertools import combinations
from math import comb


def adjacencies(m):
    """Vertices: 0 hub; 1..m rim; m+1..2m inserted; 2m+1..3m leaves."""
    n=3*m+1
    a=[0]*n
    def edge(u,v):
        a[u] |= 1<<v
        a[v] |= 1<<u
    for i in range(m):
        v=1+i
        edge(0,v)
        edge(v,2*m+1+i)
        x=m+1+i
        edge(v,x)
        edge(x,1+(i+1)%m)
    return a


def forcing(a,S):
    n=len(a)
    blue=sum(1<<i for i in S)
    allblue=(1<<n)-1
    while blue != allblue:
        add=0
        for i in range(n):
            if blue>>i&1:
                w=a[i]&~blue
                if w and (w&(w-1)) == 0:
                    add |= w
        if add == 0:
            return False
        blue |= add
    return True


def unique_matching(T,Q,m):
    """Count perfect matchings of the induced bipartite incidence graph, stopping at 2."""
    if len(T)!=len(Q):
        return False
    adj=adjacencies(m)
    neigh=[tuple(j for j in Q if adj[1+i]>>j&1) for i in T]
    order=sorted(range(len(T)),key=lambda j:len(neigh[j]))
    count=0
    def rec(k,used):
        nonlocal count
        if count>1:
            return
        if k==len(T):
            count+=1
            return
        for j in neigh[order[k]]:
            if j not in used:
                rec(k+1, used|{j})
    rec(0,set())
    return count==1


def predicted(m,S):
    if any(1<=v<=m for v in S):
        return False
    T={i for i in range(m) if 2*m+1+i in S}
    if not T:
        return False
    W={0}|set(range(m+1,3*m+1))
    Q=W-set(S)-{2*m+1+i for i in range(m) if i not in T}
    return unique_matching(T,Q,m)


def run_weight_count(m):
    total=0
    for bits in range(1,(1<<m)-1):
        runs=[]
        for i in range(m):
            if (bits>>i)&1 and not ((bits>>((i-1)%m))&1):
                k=1
                while (bits>>((i+k)%m))&1:
                    k+=1
                runs.append(k)
        assert runs
        a=1
        for ell in runs:a*=ell+1
        b=sum(ell * (a//(ell+1)) for ell in runs)
        total+=a+b
    return total


def gf_coefficients(M):
    # (1-z)(1-3z+z^2)^2 * F(z) = 6z^2-18z^3+10z^4-z^5.
    den=[1,-7,17,-17,7,-1]
    num={2:6,3:-18,4:10,5:-1}
    out=[0]*(M+1)
    for n in range(M+1):
        out[n]=num.get(n,0)-sum(den[k]*out[n-k] for k in range(1,min(5,n)+1))
    return out


def main():
    total_checked=0
    genuine_count=[]
    for m in range(3,8):
        adj=adjacencies(m)
        n=len(adj)
        found=0
        for S in combinations(range(n),m+1):
            actual=forcing(adj,S)
            if actual:
                found+=1
            theory=predicted(m,S)
            assert actual==theory, ('classification',m,S,actual,theory)
            total_checked+=1
        assert found==run_weight_count(m),(m,found,run_weight_count(m))
        genuine_count.append(found)
    # The rank-nullity lower bound proves that no smaller forcing set exists.
    coeff=gf_coefficients(15)
    for m in range(3,16):
        assert coeff[m]==run_weight_count(m), ('generating_function',m)
    assert genuine_count==[24,76,225,649,1848]
    assert coeff[3:11]==[24,76,225,649,1848,5220,14658,40964]
    print('VERIFICATION_OK cases=5 full_size_layers='+str(total_checked)+' min_counts='+','.join(map(str,genuine_count))+' gf_checked_orders=3..15')


if __name__=='__main__':main()
