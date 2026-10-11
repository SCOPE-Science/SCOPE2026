"""Exact finite arithmetic diagnostics for a complex zero-sum hyperplane inequality.
The all-dimension proof is mathematical and is supplied separately.
"""
from itertools import product
from fractions import Fraction

def check():
    # The two-level real outlier saturates the universal upper moment bound.
    for n in range(2, 21):
        u = [n-1]+[-1]*(n-1)
        B = sum(a*a for a in u)
        Q = sum(a**4 for a in u)
        assert Fraction(Q,B*B) == Fraction(n*n-3*n+3,n*(n-1))
        assert Fraction(n*Q,B*B) == Fraction(n*n-3*n+3,n-1)
    # Every complex vector with rational real/imaginary coordinates whose
    # last coordinate makes the sum zero: no floating-point comparisons.
    for n in range(2,6):
        examined = 0
        for v in product((-1,0,1),repeat=2*(n-1)):
            z = [(v[2*i], v[2*i+1]) for i in range(n-1)]
            z.append((-sum(a for a,b in z),-sum(b for a,b in z)))
            B = sum(a*a+b*b for a,b in z)
            if B == 0: continue
            Q = sum((a*a+b*b)**2 for a,b in z)
            assert n*Q>=B*B
            assert n*(n-1)*Q<=(n*n-3*n+3)*B*B
            examined+=1
        assert examined > 0
        print('exact_grid',n,examined)
    # Algebraic phase-average coefficient identities on symbolic real letters.
    import sympy as sp
    a,b,c,d=sp.symbols('a b c d', real=True)
    # For z=a+ib,w=c+id, the phase average of the squared combined
    # real-part second moment equals (B^2)/4 + |T|^2/8.
    t=sp.symbols('t',real=True)
    # Direct fourth-power constant Fourier coefficient by Laurent expansion.
    zz=sp.symbols('zz')
    X=((a-sp.I*b)*zz+(a+sp.I*b)/zz)/2
    assert sp.expand(sp.expand(X**4).coeff(zz,0)-sp.Rational(3,8)*(a*a+b*b)**2)==0
    B=(a*a+b*b+c*c+d*d)
    T=(a+sp.I*b)**2+(c+sp.I*d)**2
    Y=(((a-sp.I*b)**2+(c-sp.I*d)**2)*zz**2+2*B+T/zz**2)/4
    assert sp.simplify(sp.expand(Y**2).coeff(zz,0)-(B*B/sp.Integer(4)+sp.expand_complex(T*sp.conjugate(T))/8))==0
    print('PHASE_AND_OUTLIER_EXACT_OK')

if __name__=='__main__': check()
