"""Exact spectral identities and rational endpoint certificates for H(F_3).

Run with Python 3, SymPy, NumPy. The infinite-exponent argument is in RESULT.md;
the checker verifies its algebraic premises, rational bounds and endpoint rank.
"""
from collections import Counter, deque
from fractions import Fraction
from math import sqrt
import sympy as sp
import numpy as np

G = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
S = [(1,0,0),(2,0,0),(0,1,0),(0,2,0)]

def mul(g,h):
    return ((g[0]+h[0])%3,(g[1]+h[1])%3,(g[2]+h[2]+g[0]*h[1])%3)
def inv(g):
    x,y,z=g
    return ((-x)%3,(-y)%3,(-z+x*y)%3)

length={(0,0,0):0}
q=deque([(0,0,0)])
while q:
    g=q.popleft()
    for s in S:
        h=mul(g,s)
        if h not in length:
            length[h]=length[g]+1
            q.append(h)
assert len(length)==27
assert Counter(length.values())==Counter({0:1,1:4,2:8,3:12,4:2})
assert all(length[g]==length[inv(g)] for g in G)

# Each nontrivial scalar character falls into one of two fourfold sectors.
chi_coeff={}
for u in range(3):
    for v in range(3):
        coeff=[]
        for k in range(1,5):
            r=Fraction(0)
            for x,y,z in G:
                if length[(x,y,z)]==k:
                    r+=Fraction(1) if (u*x+v*y)%3==0 else Fraction(-1,2)
            coeff.append(r)
        chi_coeff[(u,v)]=tuple(coeff)
assert chi_coeff[(0,0)]==(4,8,12,2)
assert all(chi_coeff[u,v]==(1,-4,0,2) for u,v in [(1,0),(2,0),(0,1),(0,2)])
assert all(chi_coeff[u,v]==(-2,2,-3,2) for u in (1,2) for v in (1,2))

# The two dimension-three irreducibles are complex conjugate; both have
# the following REAL Hermitian Fourier block. Verify it for every shell.
a,b,c=sp.symbols('a b c',real=True)
zeta=-sp.Rational(1,2)+sp.I*sp.sqrt(3)/2
shell=[sp.zeros(3) for _ in range(5)]
for x,y,z in G:
    for t in range(3):
        shell[length[(x,y,z)]][t,(t+x)%3]+=zeta**((z+y*t)%3)
M=sum((shell[k]*v for k,v in enumerate([0,1,a,b,c])),sp.zeros(3))
M=M.applyfunc(sp.simplify)
expected=sp.Matrix([[2-2*b-c,1+a-2*b,1+a-2*b],
 [1+a-2*b,b-c-1,1-2*a+b],
 [1+a-2*b,1-2*a+b,b-c-1]])
assert all(sp.simplify(x)==0 for x in M-expected)

# Eigenvalues are 2a-c-2 and 1-a-c +/- sqrt(3)*(1+a-2b).
lam0=2*a-c-2
lamp=1-a-c+sp.sqrt(3)*(1+a-2*b)
lamm=1-a-c-sp.sqrt(3)*(1+a-2*b)
T=sp.symbols('T')
assert sp.simplify(M.charpoly(T).as_expr()-(T-lam0)*(T-lamp)*(T-lamm))==0

# Enclosures rationally certified by 3rd and 10th integer powers:
intervals={
 (2,2,3): ('1.58740','1.58741'),
 (3,2,3): ('2.08008','2.08009'),
 (4,2,3): ('2.51984','2.51985'),
 (2,7,10):('1.62450','1.62451'),
 (3,7,10):('2.15766','2.15768'),
 (4,7,10):('2.63901','2.63902'),
}
for (base,num,den),(l,r) in intervals.items():
    low=Fraction(l);high=Fraction(r)
    assert low**den<base**num<high**den
assert Fraction('1.73205')**2<3<Fraction('1.73206')**2
L=lambda base,num,den:Fraction(intervals[base,num,den][0])
U=lambda base,num,den:Fraction(intervals[base,num,den][1])
# q(p)=-2+2(2^p)-3(3^p)+2(4^p) is increasing for p>=0:
# f(u)=2u^2+2u-2-3u^beta, beta=log_2(3) in (3/2,5/3).
# f'(1)>1, f''(u)>2/3 for u>=1, hence unique positive root.
assert -2+2*U(2,2,3)-3*L(3,2,3)+2*U(4,2,3)<0
assert -2+2*L(2,7,10)-3*U(3,7,10)+2*L(4,7,10)>0
# The abelian first family remains strictly negative up to 7/10.
assert 1-4*L(2,7,10)+2*U(4,7,10)<0
# At the unique crossing, 1+a-2b is negative. The top 3d-block
# eigenvalue has the following uniform upper bound on [2/3,7/10].
coarse=1-L(2,2,3)-L(4,2,3)+Fraction('1.73206')*(2*U(3,7,10)-1-L(2,2,3))
assert coarse<0

# An independent 27x27 symmetry and rank check. Not a proof by sampling.
D=np.array([[length[mul(inv(g),h)] for h in G] for g in G],dtype=float)
assert np.max(abs(D-D.T))==0
F=lambda p:-2+2*2**p-3*3**p+2*4**p
lo,hi=2/3,7/10
for i in range(100):
    mid=(lo+hi)/2
    if F(mid)<0:lo=mid
    else:hi=mid
pstar=(lo+hi)/2
H=np.eye(27)-np.ones((27,27))/27
for p,neg,z in [(0.5,26,0),(pstar,22,4),(0.8,0,0)]:
    A=H@(D**p)@H
    eig=np.linalg.eigvalsh(A)
    if p!=0.8:
        assert sum(eig<-1e-7)==neg
        assert sum(abs(eig)<1e-7)==z+1
    else:
        assert np.max(eig)>1e-5
assert abs(pstar-0.6776223998116696)<1e-10
print('PASS: shell census; all Fourier blocks and multiplicities; rational endpoint bounds; 27-point numerical cross-check')
print('pstar = %.15f; endpoint squared-Euclidean embedding rank = 22'%pstar)
