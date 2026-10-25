"""Exact rational/symbolic checks for [3/3] Padé diffusion on strongly regular graphs."""
from itertools import combinations, product
from sympy import Matrix, Integer, Rational, Symbol, Poly, factor, diff, simplify, cancel, eye, zeros, invert

z = Symbol('z', real=True)
P = lambda w: 120 - 60*w + 12*w**2 - w**3
Q = lambda w: 120 + 60*w + 12*w**2 + w**3
R = P(z) / Q(z)
assert factor(diff(R,z) + 24*(z**4-30*z**2+600)/Q(z)**2) == 0
assert factor(diff((R-1)/z,z) - 2*(z**4+120*z**2+1200*z+3600)/Q(z)**2) == 0


def graph(label, arg):
    if label == 'cycle':
        v=list(range(arg))
        edge=lambda a,b: (a-b)%arg in (1,arg-1)
    elif label=='petersen':
        v=list(combinations(range(5),2))
        edge=lambda a,b: len(set(a).intersection(b))==0
    elif label=='triangular':
        v=list(combinations(range(arg),2))
        edge=lambda a,b: len(set(a).intersection(b))==1
    elif label=='rook':
        v=list(product(range(arg),range(arg)))
        edge=lambda a,b: a[0]==b[0] or a[1]==b[1]
    else: raise ValueError(label)
    n=len(v)
    A=Matrix(n,n,lambda i,j: Integer(i!=j and edge(v[i],v[j])))
    return A


def srg(A):
    n=A.rows
    k=sum(A.row(0))
    assert 0<k<n-1
    assert all(sum(A.row(i))==k for i in range(n))
    a,b=[],[]
    for i in range(n):
        for j in range(i+1,n):
            ncommon=sum(A[i,t]*A[t,j] for t in range(n))
            (a if A[i,j] else b).append(ncommon)
    assert len(set(a))==len(set(b))==1
    lam=a[0]; mu=b[0]
    assert mu>0
    assert A*A == (lam-mu)*A+(k-mu)*eye(n)+mu*Matrix.ones(n)
    return int(k),int(lam),int(mu)


def check(A,h):
    n=A.rows
    k,lam,mu=srg(A)
    S=2*k-lam+mu
    W=n*mu
    L=k*eye(n)-A
    M=Poly(z*(z*z-S*z+W),z,domain='QQ')
    # Inverse of the Padé denominator in the quotient algebra.
    inv=invert(Poly(Q(h*z),z,domain='QQ'),M)
    reduction=(Poly(P(h*z),z,domain='QQ')*inv).rem(M)
    assert reduction.nth(0)==1
    b,c=reduction.nth(1),reduction.nth(2)
    T_direct=(120*eye(n)-60*h*L+12*h*h*L*L-h**3*L**3)*(120*eye(n)+60*h*L+12*h*h*L*L+h**3*L**3).inv()
    T_reduced=eye(n)+b*L+c*L*L
    assert T_direct==T_reduced
    assert c>0 and -b-(S-mu)*c>0
    nonedge=mu*c
    adjacent=-b-(S-mu)*c
    diag=1+k*b+(k*k+k)*c
    assert all(T_direct[i,j]==(diag if i==j else adjacent if A[i,j] else nonedge) for i in range(n) for j in range(n))
    assert all(sum(T_direct.row(i))==1 for i in range(n))
    assert all(T_direct[i,j]>0 for i in range(n) for j in range(n) if i!=j)
    return n*n

cases=[('cycle',5),('petersen',None),('triangular',5),('triangular',6),('rook',3),('rook',4)]
count=0
for kind,arg in cases:
    A=graph(kind,arg)
    for h in (Rational(1,3),Rational(1),Rational(4)):
        count+=check(A,h)
h=Symbol('h',positive=True)
f=lambda x:P(x)/Q(x)
petersen_diag=cancel((1+5*f(2*h)+4*f(5*h))/10)
assert factor(petersen_diag-(-20*h**6+30*h**5+12*h**4+147*h**3+324*h**2+180*h+360)/((h**3+6*h**2+15*h+15)*(25*h**3+60*h**2+60*h+24)))==0
assert petersen_diag.subs(h,3)==Rational(163,22231)
assert petersen_diag.subs(h,4)==Rational(-4057,82955)
print(f'VERIFY_OK: scalar derivative identities; {len(cases)} strongly regular graphs; {count} exact matrix-entry comparisons; off-diagonal positivity; stochasticity; Petersen sign crossing')
