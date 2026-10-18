import sympy as s
A,B,L = s.symbols('A B L')
T=s.symbols('T')
def cheb(h,z):
    x,y=2,z
    if h==0:return x
    if h==1:return y
    for j in range(2,h+1):x,y=y,s.expand(z*y-x)
    return y
for q in (3,5,7,9,11,13):
    h=(q-1)//2;m=h+1
    z=B+1/B
    assert s.cancel(cheb(h,z)-(B**h+B**(-h)))==0
    D=A**(q+1)-2*(B**q+B)-L*(A*A-4*B)**m
    t=A*A/B
    w=A*(B+1)/B
    K=2*cheb(h,w*w/t-2)-t**m+L*(t-4)**m
    assert s.cancel(B**m*K+D)==0
    print('GENERIC_Q_IDENTITY',q)
# characteristic 3 conversion and j formula as rational polynomial mod3
q=3; t,w=s.symbols('t w')
D=A**4-2*(B**3+B)-L*(A*A-4*B)**2
E=w*w-t*((L-1)*t*t+L*t+(L-1))
val=s.cancel(B**3*E.subs({t:A*A/B,w:A*(B+1)/B})-A*A*D)
poly=s.Poly(s.expand(val),A,B,L,modulus=3)
assert poly.is_zero,val
print('ELLIPTIC_MODEL_F3_OK')
R=L/(L-1)
j1=R**6/(R**2-1)
j2=-L**6/((L-1)**4*(L+1))
n,d=s.cancel(j1-j2).as_numer_denom()
assert s.Poly(n,L,modulus=3).is_zero
jprime=s.diff(j2,L)
num,den=s.cancel(jprime/j2-L/(L*L-1)).as_numer_denom()
assert s.Poly(num,L,modulus=3).is_zero
print('J_IDENTITY_AND_DIFFERENTIAL_F3_OK')
for q in (3,5,7,9,11):
    p=next(p for p in (3,5,7,11) if q%p==0)
    h=(q-1)//2;m=h+1
    a,b=s.symbols('a b')
    for lam in range(p):
        if lam in (1,p-1):continue
        f=a**(q+1)-4-lam*(a*a-4)**m
        ff=s.Poly(f,a,modulus=p)
        assert s.gcd(ff,ff.diff()).degree()==0,('not sqfree',q,lam)
    print('BRANCH_FIXED_FIBER_SQUAREFREE',q,p)
print('VERIFY_OK: Chebyshev quotient identities, fixed-point squarefreeness, characteristic-three elliptic and modular formulas')
