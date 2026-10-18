"""Verify exact rank polynomials for weighted bipartite two-cycle wedges.
Run: python3 figure_eight_checker.py
No third-party packages are needed.
"""
from collections import Counter
from itertools import product


def mul4(x,y):
    v=0
    for i in range(2):
        if (y>>i)&1: v ^= x<<i
    if v&8: v ^= 0b1110
    if v&4: v ^= 0b111
    return v


def fmul(x,y,q):
    return mul4(x,y) if q==4 else (x*y)%q


def fsub(x,y,q):
    return x^y if q==4 else (x-y)%q


def inv(x,q):
    if q==4: return (1,1,3,2)[x]
    return pow(x,-1,q)


def rank(M,q):
    if not M: return 0
    A=[row[:] for row in M]
    nr,nc=len(A),len(A[0]); r=0
    for c in range(nc):
        j=next((i for i in range(r,nr) if A[i][c]!=0),None)
        if j is None: continue
        A[j],A[r]=A[r],A[j]
        z=inv(A[r][c],q)
        for i in range(r+1,nr):
            a=fmul(A[i][c],z,q)
            if a:
                for t in range(c,nc):
                    A[i][t]=fsub(A[i][t],fmul(a,A[r][t],q),q)
        r+=1
        if r==nr: break
    return r


def path_polys(n,q):
    P=Counter(); Q=Counter()
    for bits in product((0,1),repeat=2*n-2):
        M=[[0]*n for _ in range(n-1)]
        for i in range(n-1):
            M[i][i]=bits[2*i]
            M[i][i+1]=bits[2*i+1]
        # Binary values give identical ranks for every nonzero weighting: support is a forest.
        r=rank(M,2)
        rin=rank([row[1:-1] for row in M],2)
        wt=(q-1)**sum(bits)
        P[r]+=wt
        Q[r]+=wt*q**(r-rin)
    return P,Q


def predict(n,m,q):
    Pn,Qn=path_polys(n,q); Pm,Qm=path_polys(m,q)
    base=Counter(); zero=Counter()
    for i,ci in Pn.items():
        for j,cj in Pm.items(): base[i+j]+=ci*cj
    for i,ci in Qn.items():
        for j,cj in Qm.items(): zero[i+j]+=ci*cj
    out=Counter()
    for r in set(base)|set(zero):
        out[r]+=zero[r]
        out[r+1]+=q**4*base[r]-zero[r]
    return +out


def brute(n,m,q):
    hist=Counter()
    for values in product(range(q),repeat=2*(n+m)):
        A=[[0]*(n+m) for _ in range(n+m-1)]
        for i in range(n):
            row=0 if i==0 else i
            A[row][i]=values[2*i]
            A[row][(i+1)%n]=values[2*i+1]
        for i in range(m):
            row=0 if i==0 else n-1+i
            A[row][n+i]=values[2*n+2*i]
            A[row][n+(i+1)%m]=values[2*n+2*i+1]
        hist[rank(A,q)]+=1
    return +hist


def main():
    cases=[(2,2,2),(2,2,3),(2,2,4),(2,2,5),(2,3,2),(2,3,3),(3,3,2)]
    for n,m,q in cases:
        observed=brute(n,m,q); expected=predict(n,m,q)
        assert observed==expected,(n,m,q,observed,expected)
        assert sum(expected.values())==q**(2*n+2*m)
        print(f"PASS n={n} m={m} q={q} rank_hist={sorted(expected.items())}")
    for n,m,q in [(3,4,2),(2,4,3),(4,5,5)]:
        expected=predict(n,m,q)
        assert sum(expected.values())==q**(2*n+2*m)
        assert max(expected)==n+m-1
        print(f"FORMULA_TOTAL_PASS n={n} m={m} q={q}")
    print('ALL_FIGURE_EIGHT_RANK_CHECKS_PASSED')

if __name__=='__main__':main()
