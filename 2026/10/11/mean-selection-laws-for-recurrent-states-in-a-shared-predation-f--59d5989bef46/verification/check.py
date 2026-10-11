import sympy as sp

v, vb, k = sp.symbols("v vb k", positive=True)
reciprocal = (
    1/(1+k*v)
    - (
        1/(1+k*vb)
        - k*(v-vb)/(1+k*vb)**2
        + k**2*(v-vb)**2/((1+k*vb)**2*(1+k*v))
    )
)
assert sp.simplify(reciprocal) == 0

A1,A2,a1,a2,r1,r2,p1,p2,C,J1,J2 = sp.symbols(
    "A1 A2 a1 a2 r1 r2 p1 p2 C J1 J2", positive=True
)
B1 = p1+r1*C
B2 = p2+r2*C
D = A1*B1/a1 + A2*B2/a2
dv = (A1*r1*J1/a1 + A2*r2*J2/a2)/D
du1 = (r1*J1-B1*dv)/a1
du2 = (r2*J2-B2*dv)/a2
assert sp.simplify(A1*du1+A2*du2) == 0

q1 = r1/B1
q2 = r2/B2
assert sp.simplify((q1-q2) - (r1*p2-r2*p1)/(B1*B2)) == 0

W1,W2,J = sp.symbols("W1 W2 J", positive=True)
Q = (W1*q1+W2*q2)/(W1+W2)
assert sp.simplify((q1-Q) - W2*(q1-q2)/(W1+W2)) == 0
assert sp.simplify((q2-Q) + W1*(q1-q2)/(W1+W2)) == 0

print("VERIFY_OK")
