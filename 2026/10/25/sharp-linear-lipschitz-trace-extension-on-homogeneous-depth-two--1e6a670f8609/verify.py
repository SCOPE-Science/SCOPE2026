"""Exact rational checks for optimal linear Lipschitz extension on depth-two trees.

Usage: python verify.py [max_m max_k]
No third-party packages are required.
"""
from fractions import Fraction as F
import sys

def predicted(m, k):
    return F(4*(2*m*k-k-1),m*(3*k+1))

def alpha_opt(m, k):
    return F(2*m*k-k-1,(m-1)*(3*k+1))

def kr_tree_norm(w,m,k):
    """Transport norm on leaf measures of total mass zero in unit-edge tree."""
    assert sum(w)==0
    return sum(abs(x) for x in w)+sum(abs(sum(w[i*k:(i+1)*k])) for i in range(m))

def compute(m,k):
    n=m*k
    a=alpha_opt(m,k)
    lam=predicted(m,k)
    assert 0<a<1
    uni=[F(1,n)]*n
    branch=[]
    for i in range(m):
        row=[(a*F(1,k) if j//k==i else F(0))+(1-a)*F(1,n) for j in range(n)]
        assert sum(row)==1
        branch.append(row)
    # Root-to-branch and branch-to-leaf edge norms, each computed separately.
    for i in range(m):
        w=[uni[j]-branch[i][j] for j in range(n)]
        assert kr_tree_norm(w,m,k)==lam,(m,k,'root edge',i)
        for j in range(i*k,(i+1)*k):
            w=[branch[i][t]-(F(1) if t==j else F(0)) for t in range(n)]
            assert kr_tree_norm(w,m,k)==lam,(m,k,'leaf edge',j)
    # Lower-bound witness: leaf values +2 at the leaf a, 0 at other
    # leaves of its branch and -2 in all other branches (1-Lipschitz).
    i=0; j=0
    f=[2 if t==j else (0 if t//k==i else -2) for t in range(n)]
    for x in range(n):
        for y in range(x+1,n):
            d=2 if x//k==y//k else 4
            assert abs(f[x]-f[y])<=d
    assert sum(f[t]*((F(1) if t==j else F(0))-branch[i][t]) for t in range(n))==lam
    assert (lam>2)==((m-2)*(k-1)>4)
    return n+m,lam

def main():
    hi_m=int(sys.argv[1]) if len(sys.argv)>1 else 8
    hi_k=int(sys.argv[2]) if len(sys.argv)>2 else 8
    cases=edges=0
    for m in range(2,hi_m+1):
        for k in range(2,hi_k+1):
            n_e,lam=compute(m,k)
            cases+=1;edges+=n_e
            if (m,k) in [(2,2),(2,3),(3,2),(3,3),(4,3)]:
                print(f'(m,k)=({m},{k})  exact norm={lam}')
    print(f'PASS: {cases} parameter pairs, {edges} exact tree-edge dual-norm identities, plus dual witnesses and phase thresholds')

if __name__=='__main__':main()
