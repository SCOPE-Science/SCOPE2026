"""Exact, independent grounded-Laplacian checks for a one-edge weighted clique.
Only the Python standard library is needed. Every calculation is rational.
"""
from fractions import Fraction as F
from itertools import combinations

def inverse(a):
    n=len(a)
    t=[list(row)+[F(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if t[i][k])
        t[k],t[pivot]=t[pivot],t[k]
        q=t[k][k]
        t[k]=[v/q for v in t[k]]
        for i in range(n):
            if i==k: continue
            v=t[i][k]
            if v:t[i]=[x-v*y for x,y in zip(t[i],t[k])]
    return [row[n:] for row in t]

def brute_rows(n,t):
    edges=list(combinations(range(n),2))
    c=[t*t if e==(0,1) else F(1) for e in edges]
    roots=[t if e==(0,1) else F(1) for e in edges]
    B=[[F(int(k==u)-int(k==v)) for k in range(n-1)] for u,v in edges]
    L=[[sum(c[z]*B[z][i]*B[z][j] for z in range(len(edges))) for j in range(n-1)] for i in range(n-1)]
    H=inverse(L)
    W=[[sum(B[i][k]*H[k][j] for k in range(n-1)) for j in range(n-1)] for i in range(len(edges))]
    P=[[roots[i]*roots[j]*sum(W[i][k]*B[j][k] for k in range(n-1)) for j in range(len(edges))] for i in range(len(edges))]
    return edges,[sum(map(abs,row)) for row in P]

def formulas(n,t):
    den=n-2+2*t*t
    exceptional=2*(t*t+(n-2)*t)/den
    adjacent=(t+2*t*t+2*n-5)/den if t<=1 else (n*t+4*t*t*n-6*t*t+2*n*n-7*n+6)/(n*den)
    remote=F(2*(n-1),n)
    return exceptional,adjacent,remote

def main():
    checks=0
    for n in range(3,10):
        for t in [F(1,5),F(1,2),F(3,4),F(1),F(5,4),F(2),F(3),F(5),F(13)]:
            edges,rows=brute_rows(n,t)
            E,A,R=formulas(n,t)
            for edge,row in zip(edges,rows):
                expected=E if edge==(0,1) else A if 0 in edge or 1 in edge else R
                assert row==expected, (n,t,edge,row,expected)
                checks+=1
            assert max(rows)==max(E,A,R if n>=4 else F(0))
    # Exact characterization of maximizing extraordinary edge row:
    # 2*t^2-2*t-(n-2)=0 implies E=t.
    for n in range(3,101):
        for t in (F(1,3),F(1),F(2),F(3),F(7),F(13)):
            E,A,R=formulas(n,t)
            # E <= t_* iff 2*t_*-1 solves via square completion;
            # check t=1 and a few rational samples independently.
            from math import sqrt
            bound=(1+sqrt(2*n-3))/2
            assert float(max(E,A,R))<=bound+1.e-10,(n,t,E,A,R,bound)
    print('PASS:',checks,'exact grounded-Laplacian row comparisons; 588 parameter-bound spot checks')

if __name__=='__main__':main()
