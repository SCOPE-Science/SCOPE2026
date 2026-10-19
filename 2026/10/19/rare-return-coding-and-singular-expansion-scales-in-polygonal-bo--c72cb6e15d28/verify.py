"""Exact Markov coding identities and numerical checks for a border-collision family."""
import sympy as sp
import mpmath as mp

z=sp.Symbol('z')
for n in range(3,13):
    N=n+4
    A=sp.zeros(N)
    for i in range(n):
        A[i,i+1]=1
    A[n,n+1]=A[n,n+2]=1
    for i in (n+1,n+2):
        A[i,n+3]=A[i,0]=1
    A[n+3,2]=1
    assert sp.factor(A.charpoly(z).as_expr()) == z*z*(z**(n+2)-2*z-2)
    assert sp.factor((sp.eye(N)-z*A).det()) == 1-2*z**(n+1)-2*z**(n+2)

mp.mp.dps=45
for n in (20,100,500,1000):
    m=mp.mpf(n+2)
    theta=2*mp.pi/m
    cosine=mp.cos(theta)
    g=lambda r: 2*cosine*r**(n+1)-r**n-1
    r=mp.findroot(g,(1+mp.mpf('1e-12'),1+80/m**3))
    right=r*r
    left=-r**(-(n-2))/(1+r*r-2*r*cosine)
    lam=mp.findroot(lambda x:x**(n+2)-2*x-2,
                    (1+mp.mpf('0.3')/m,1+mp.mpf('2')/m))
    assert r>1 and right>1 and left<0 and lam>1
    assert abs(g(r)) < mp.mpf('1e-20')
    print(n, mp.nstr(m**3*(right-1),10),
          mp.nstr(abs(left)/m**2,10), mp.nstr(m*mp.log(lam),10))
print('VERIFY_OK')
