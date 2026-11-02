"""Exact checks for the characteristic-seven genus-two bielliptic pencil."""
import sympy as sp
A,B,T,X=sp.symbols('A B T X')
P=7
def rem(e):
    return sp.Poly(sp.expand(e),A,B,T,X, modulus=P).as_expr()
g=1+B*T+A*T*T+T**3
assert sp.Poly(g**3,T).coeff_monomial(T**3).expand()==B**3+6*A*B+3
assert sp.Poly(g**3,T).coeff_monomial(T**6).expand()==A**3+6*A*B+3
ha=A**3-A*B+3; hb=B**3-A*B+3
D=A**2*B**2-4*A**3-4*B**3-27+18*A*B
assert rem(A**3*D.subs(B,(A**3+3)/A)+3*(A**3+1)**3)==0
for z,rad,repeat in [(1,2,3),(2,4,6),(4,1,5)]:
    v=sp.Poly(hb.subs(A,z*B),B,modulus=7)
    assert v==sp.Poly((B-rad)*(B-repeat)**2,B,modulus=7)
    assert sp.Poly(D.subs({A:z*rad,B:rad}), B, modulus=7).is_zero is False
    assert int(D.subs({A:z*rad,B:rad}))%7!=0
    assert int(D.subs({A:z*repeat,B:repeat}))%7==0
    j=sp.diff(ha,A)*sp.diff(hb,B)-sp.diff(ha,B)*sp.diff(hb,A)
    assert int(j.subs({A:z*rad,B:rad}))%7!=0
    assert int(j.subs({A:z*repeat,B:repeat}))%7==0
print('GENUS2_CHAR7_EXACT_CARTIER_HASSE_SNC_INTERSECTION_OK')
