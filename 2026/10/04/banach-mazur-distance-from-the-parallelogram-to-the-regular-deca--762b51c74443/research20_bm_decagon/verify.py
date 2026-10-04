from sympy import symbols, sqrt, simplify, factor

u,v = symbols('u v', real=True)
q = (sqrt(5)-1)/2
phi = (1+sqrt(5))/2
mu = phi/2 + q
ustar = 1/(4+q)
E = phi-q*u*(1-v)
A = 2-u+q*v
B = phi+v-q*u
C = 2+q*(u+1-v)
vA = (1+phi**2*u)/2
vB = q+2*q**2*u
checks = [
    simplify(q**2 - (1-q)),
    simplify(phi*q-1),
    simplify(A.subs(v,vA)-C.subs(v,vA)),
    simplify(B.subs(v,vB)-C.subs(v,vB)),
    simplify((A-mu*E).subs(v,vA) - u*(1-(4+q)*u)/4),
    simplify((C-mu*E).subs(v,1-u) - (3-2*q)*(u-ustar)*(u+phi)/2),
    simplify((B-mu*E).subs(v,1-u) - (3-2*q)*(ustar-u)*(phi-u)/2),
    simplify((B-mu*E).subs(v,vB) - (1-2*u)*(5-7*q)*(u-ustar)/2),
    simplify((C-mu*E).subs(v,1) - q*(2*u-1)/2),
    simplify(vA.subs(u,ustar) - (1-ustar)),
    simplify(vB.subs(u,ustar) - (1-ustar)),
    simplify(vB.subs(u,symbols('u'))),
]
assert all(c == 0 for c in checks[:11]), checks
# derivative numerators after common positive denominator E^2
num_dA = simplify(q*E - A*(q*u))
num_dB = simplify(E - B*(q*u))
num_dC = simplify(-q*E - C*(q*u))
assert simplify(num_dA - q*(1-u)*(phi-u)) == 0
assert simplify(num_dB - (phi*(1-u)+q**2*u**2)) == 0
assert simplify(num_dC + q*(E+u*C)) == 0
# exact conjectured constant
assert simplify(mu - (3*sqrt(5)-1)/4) == 0
print('VERIFY_OK exact symbolic identities')
