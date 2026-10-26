"""Exact finite-chain resonance checks for a loss at an A site of an SSH chain.

Python 3 and SymPy are required.  All algebraic equality tests are exact.
"""
from functools import lru_cache
from itertools import combinations
import sympy as sp

x = sp.symbols('x')

@lru_cache(None)
def modulus(L):
    return sp.Poly(sp.cyclotomic_poly(2*L, x), x, domain=sp.ZZ)

def differences(L, terms):
    """terms=(coefficient, exponent); represent a polynomial in a 2L-th root."""
    data={}
    for coef,exponent in terms:
        p=exponent%(2*L)
        data[p]=data.get(p,0)+coef
    return sp.Poly.from_dict({(p,):v for p,v in data.items() if v},x,domain=sp.ZZ)

def B(L,m,k):
    # zeta^(m*k) - zeta^(-m*k) = 2i sin(m*k*pi/L)
    return differences(L,[(1,m*k),(-1,-m*k)])

def is_zero_mod(L,poly):
    return poly.rem(modulus(L)).is_zero

def sine_sign(L,m,k):
    n=m*k
    if n%L==0:return 0
    return -1 if (n//L)%2 else 1

def positive_k(L,u):
    return [k for k in range(1,L) if sine_sign(L,u,k)*sine_sign(L,u+1,k)==-1]

def classify(N):
    facts=[]
    for s in range(2,N):
        u=s-1; L=N-s+1
        positives=positive_k(L,u)
        for k,l in combinations(positives,2):
            # Compare r_k = -sin((u+1)k*pi/L)/sin(u*k*pi/L).
            expr=B(L,u+1,k)*B(L,u,l)-B(L,u+1,l)*B(L,u,k)
            if is_zero_mod(L,expr):
                # r_k ==1 iff sin((u+1)*theta)+sin(u*theta) ==0.
                r_eq_one=is_zero_mod(L,B(L,u+1,k)+B(L,u,k))
                facts.append((N,s,k,l,'unit' if r_eq_one else 'nonunit'))
    return facts

if __name__ == '__main__':
    all_earlier=[]
    for N in range(2,14):
        vals=classify(N)
        all_earlier += vals
        print('N=',N, 'resonant pairs:',vals)
        assert all(row[-1]=='unit' for row in vals), ('Earlier nonunit pair',N,vals)
    assert any(r[1]==3 and r[2:4]==(5,11) and r[-1]=='nonunit' for r in classify(14))
    print('First nonunit example:',[row for row in classify(14) if row[-1]=='nonunit'])
    # Four-site left block at the first nonuniform multiplet (a=1,b=sqrt(2)).
    a=sp.Integer(1); b=sp.sqrt(2); z=sp.symbols('z')
    K=sp.zeros(2)
    for i in range(2):
        K[i,i]=a
        if i>0:K[i,i-1]=b
    left=sp.factor((z*sp.eye(2)-K.T*K).det(),extension=b)
    expected=sp.expand(z**2-4*z+1)
    print('left determinant:',left)
    assert sp.simplify(left-expected)==0
    for kk,target in [(5,2+sp.sqrt(3)),(11,2-sp.sqrt(3))]:
        theta=sp.pi*sp.Rational(kk,12)
        zz=sp.simplify(1+b*b+2*b*sp.cos(theta))
        assert sp.simplify(zz-target)==0,(kk,zz,target)
        assert sp.simplify(expected.subs(z,target))==0
    print('exact result: PASS')
