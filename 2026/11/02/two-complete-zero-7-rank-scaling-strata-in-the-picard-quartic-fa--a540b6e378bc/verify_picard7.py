#!/usr/bin/env python3
"""Exact symbolic verifier for characteristic-seven Picard quartic Hasse strata."""
import sympy as S
from itertools import product
x,a,b,c=S.symbols('x a b c')

def red(f):
    return S.Poly(S.expand(f),a,b,c,modulus=7).as_expr()

def coeff(f,k):
    return red(S.Poly(f,x).nth(k))

f=x**4+a*x**2+b*x+c
f2=S.expand(f**2)
f4=S.expand(f**4)
A=coeff(f2,6)
B=S.Matrix([[coeff(f4,6),coeff(f4,5)],[coeff(f4,13),coeff(f4,12)]])
expected=S.Matrix([[-3*a**3*c-a*a*b*b-2*a*c*c-2*b*b*c,-2*a*a*b*c-3*a*b**3-2*b*c*c],[-3*b,-a*a-3*c]])
assert A==2*a
assert all(red(B[i,j]-expected[i,j])==0 for i in range(2) for j in range(2)),(B,expected)
Delta=red(S.discriminant(f,x))
expected_D=2*a**4*c+3*a**3*b**2-2*a*a*c*c-3*a*b*b*c+b**4-3*c**3
assert red(Delta-expected_D)==0,(Delta,expected_D)
R=3*a**4*c+a**3*b*b-3*a*a*c*c-a*b*b*c-2*b**4-c**3
assert red(B.det()-a*R)==0,(B.det(),R)
assert red(Delta-3*R)==0
assert red(B[0,0].subs({a:0})+2*b*b*c)==0
assert red(B[0,1].subs({a:0})+2*b*c*c)==0
assert red(B[1,0].subs({a:0})+3*b)==0
assert red(B[1,1].subs({a:0})+3*c)==0
u=S.Matrix([-2*b*c,-3]); v=S.Matrix([[b,c]])
assert all(red(B[i,j].subs({a:0})-(u*v)[i,j])==0 for i in range(2) for j in range(2))
# Frobenius-twisted rank-one composition: B^(7) B vanishes iff v^(7)u=0.
twisted_scalar=red(-2*b**8*c-3*c**7)
assert red(twisted_scalar+3*c*(c**3-2*b**4)*(c**3+2*b**4))==0
# The factor c^3+2 b^4 is exactly the excluded singularity when a=0.
assert red(Delta.subs({a:0})-(-3)*(c**3+2*b**4))==0

# Independent coefficient expansion by sparse combinatorial convolution in F_7[a,b,c][x].
terms={(4,0,0,0):1,(2,1,0,0):1,(1,0,1,0):1,(0,0,0,1):1}
from collections import defaultdict
P={(0,0,0,0):1}
for _ in range(4):
    Q=defaultdict(int)
    for (i,j,k,l),cf in P.items():
        for (ii,jj,kk,ll),cg in terms.items():Q[(i+ii,j+jj,k+kk,l+ll)]=(Q[(i+ii,j+jj,k+kk,l+ll)]+cf*cg)%7
    P={u:v for u,v in Q.items() if v%7}
for i,k in [(0,6),(0,5),(1,13),(1,12)]:
    j=0 if k in (6,13) else 1
    check=sum(cf*a**jj*b**kk*c**ll for (deg,jj,kk,ll),cf in P.items() if deg==k)
    assert red(check-B[0 if k in (6,5) else 1,0 if k in (6,13) else 1])==0

# Modular matrix calculations, 343 field-rational coefficient triples.
def rank(mat):
    A=[[int(t)%7 for t in row] for row in mat]; rows=len(A); cols=len(A[0]); q=0
    for j in range(cols):
        ii=next((i for i in range(q,rows) if A[i][j]),None)
        if ii is None: continue
        A[q],A[ii]=A[ii],A[q]
        inv=pow(A[q][j],-1,7)
        A[q]=[(v*inv)%7 for v in A[q]]
        for i in range(rows):
            if i!=q:
                z=A[i][j]
                A[i]=[(A[i][t]-z*A[q][t])%7 for t in range(cols)]
        q+=1
        if q==rows:break
    return q

def mul(X,Y):return [[sum(X[i][k]*Y[k][j] for k in range(len(Y)))%7 for j in range(len(Y[0]))] for i in range(len(X))]
rank_counts={}; pr_counts={}; special=[]
for aa,bb,cc in product(range(7),repeat=3):
    sub={a:aa,b:bb,c:cc}
    if int(Delta.subs(sub))%7==0:continue
    t=int((2*a).subs(sub))%7
    M=[[t,0,0],[0,int(B[0,0].subs(sub))%7,int(B[0,1].subs(sub))%7],[0,int(B[1,0].subs(sub))%7,int(B[1,1].subs(sub))%7]]
    r=rank(M)
    rank_counts[r]=rank_counts.get(r,0)+1
    M3=mul(mul(M,M),M)
    pr=rank(M3)
    pr_counts[pr]=pr_counts.get(pr,0)+1
    assert r==(1 if aa==0 else 3)
    if aa==0:
        expected_pr=0 if cc==0 or (cc**3-2*bb**4)%7==0 else 1
        assert pr==expected_pr,(aa,bb,cc,r,pr,expected_pr)
        if pr==0:special.append((bb,cc))
    else:
        assert pr>=1
assert special
print('VERIFY_OK: independently expanded all Cartier entries; discriminant and determinant factorization; Frobenius rank-one scalar and two smooth p-rank-zero loci; smooth F7 checks:',sum(rank_counts.values()),'Cartier rank counts',rank_counts,'p-rank counts',pr_counts,'p-rank-zero pairs',special)
