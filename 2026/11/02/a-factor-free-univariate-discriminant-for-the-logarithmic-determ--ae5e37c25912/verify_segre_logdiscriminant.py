"""Exact independent checks for the Segre pencil-eliminant identity.
Requires SymPy. This is an arithmetic check, not an infinite proof."""
import sympy as sp

U=sp.symbols('U')

def eliminant(a,b,s,v,nu):
    m=len(nu)
    assert len(a)==m+1 and len(b)==m+1
    factors=[a[i]+b[i]*U for i in range(1,m+1)]
    G=sp.prod(factors)
    A=a[0]+b[0]*U
    S=s+sum(nu)
    return sp.expand((S*U*b[0]+v*A)*G-U*A*sum(nu[i-1]*b[i]*sp.prod(factors[:i-1]+factors[i:]) for i in range(1,m+1)))


def check():
    a0,a1,b0,b1,s,n,v=sp.symbols('a0 a1 b0 b1 s n v')
    p=eliminant([a0,a1],[b0,b1],s,v,[n])
    Delta=a0*b1-a1*b0
    source=sp.expand(a1**2*b0**2*s**2 + Delta*(Delta*(n**2+v**2)-2*a1*b0*s*(n+v)-2*(a0*b1+a1*b0)*n*v))
    assert sp.expand(sp.discriminant(p,U)-source)==0, 'square formula not reproduced'
    for m in range(1,9):
        a=[3*i*i+2*i+11 for i in range(m+1)]
        b=[7*i*i+3*i+5 for i in range(m+1)]
        ns=[i*i+i+2 for i in range(1,m+1)]
        s0,v0=13,17
        p=eliminant(a,b,s0,v0,ns)
        assert sp.degree(p,U)==m+1
        assert sp.discriminant(p,U)!=0
        assert p.coeff(U,0)==v0*sp.prod(a)
        assert p.coeff(U,m+1)==b[0]*sp.prod(b[1:])*(s0+v0)
        # Exact rational-function reconstruction, with symbolic U.
        A=a[0]+b[0]*U
        S=s0+sum(ns)
        f=sp.Rational(s0,S)*A
        tt=[-sp.Rational(ns[i-1],S)*A/(a[i]+U*b[i]) for i in range(1,m+1)]
        reconstructed=A+sum(tt[i-1]*(a[i]+U*b[i]) for i in range(1,m+1))
        assert sp.cancel(reconstructed-f)==0
        residual=v0*f+s0*U*(b[0]+sum(tt[i-1]*b[i] for i in range(1,m+1)))
        G=sp.prod(a[i]+b[i]*U for i in range(1,m+1))
        assert sp.cancel(residual*G*sp.Rational(S,s0)-p)==0
    print('VERIFY_OK: square identity, eight nonzero discriminants, endpoint coefficients, and exact critical-equation reconstruction')

if __name__=='__main__':check()
