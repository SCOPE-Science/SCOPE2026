"""Machine verification of the four exact homomorphism-density identities
used in the proof that m=4 forces 2-block step graphons.

Identities (symbols: a in (0,1), b=1-a, q11,q12,q22; d1=a q11+b q12, d2=a q12+b q22):
 (I1) t(K2) = a d1 + b d2
 (I2) t(P3) = a d1^2 + b d2^2            [2-star]
 (I3) t(S3) = a d1^3 + b d2^3            [3-star]
 (I4) t(P4) = a d1^3 + b d2^3 - a b q12 (d1-d2)^2   [3-edge path]
Regular slice (d1==d2==d, u=d-c, c=q12, q11=c+u/a, q22=c+u/b):
 (R1) t(triangle) = d^3 + u^3
 (R2) t(diamond)  = K(c,d) + u^5/(a b), K=4c^5-19c^4 d+34c^3d^2-28c^2d^3+10cd^4
Moment relations: v=m2-m1^2 = ab(d1-d2)^2; mu3 = ab(a-b)(d1-d2)^3 with
  the sign convention below (verified factors).
"""
import sympy as sp

a, q11, q12, q22 = sp.symbols('a q11 q12 q22')
b = 1 - a
d1 = a*q11 + b*q12
d2 = a*q12 + b*q22
Q = [[q11, q12], [q12, q22]]

def t_of(n, edges):
    tot = sp.Integer(0)
    for mask in range(1 << n):
        phi = [(mask >> i) & 1 for i in range(n)]
        w = sp.Integer(1)
        for k in phi:
            w *= (b if k else a)
        for (i, j) in edges:
            w *= Q[phi[i]][phi[j]]
        tot += w
    return sp.expand(tot)

checks = []
checks.append(("I1 K2", sp.expand(t_of(2, [(0,1)]) - (a*d1 + b*d2))))
checks.append(("I2 P3", sp.expand(t_of(3, [(0,1),(0,2)]) - (a*d1**2 + b*d2**2))))
checks.append(("I3 S3", sp.expand(t_of(4, [(0,1),(0,2),(0,3)]) - (a*d1**3 + b*d2**3))))
checks.append(("I4 P4", sp.expand(t_of(4, [(0,1),(1,2),(2,3)]) - (a*d1**3 + b*d2**3 - a*b*q12*(d1-d2)**2))))

c, d = sp.symbols('c d')
u = d - c
r11 = c + u/a
r22 = c + u/b
Q2 = [[r11, c], [c, r22]]
def t_of_r(n, edges):
    tot = sp.Integer(0)
    for mask in range(1 << n):
        phi = [(mask >> i) & 1 for i in range(n)]
        w = sp.Integer(1)
        for k in phi:
            w *= (b if k else a)
        for (i, j) in edges:
            w *= Q2[phi[i]][phi[j]]
        tot += w
    return sp.expand(tot)

T = t_of_r(3, [(0,1),(1,2),(0,2)])
checks.append(("R1 triangle", sp.simplify(T - (d**3 + u**3))))
D = t_of_r(4, [(0,1),(0,2),(0,3),(1,2),(1,3)])
K = 4*c**5 - 19*c**4*d + 34*c**3*d**2 - 28*c**2*d**3 + 10*c*d**4
checks.append(("R2 diamond", sp.simplify(D - (K + u**5/(a*b)))))

m1, m2, m3 = sp.symbols('m1 m2 m3')
e1, e2, e3 = sp.symbols('e1 e2 e3')
# moment factor checks with generic symbols
A, D1, D2 = sp.symbols('A D1 D2')
B = 1 - A
n1 = A*D1 + B*D2; n2 = A*D1**2 + B*D2**2; n3 = A*D1**3 + B*D2**3
checks.append(("M var", sp.expand((n2-n1**2) - A*B*(D1-D2)**2)))
checks.append(("M skew", sp.expand((n3-3*n1*n2+2*n1**3) + A*B*(A-B)*(D1-D2)**3)))

ok = True
for name, r in checks:
    good = (r == 0)
    print(f"{name}: {'OK' if good else 'FAIL: '+str(r)[:300]}")
    ok = ok and good
print("ALL OK" if ok else "FAILURES PRESENT")
assert ok
