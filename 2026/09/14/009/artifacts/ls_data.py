"""Exact Lyapunov-Schmidt data for symmetric inscribed triangles.

Chord expansion: for vertices a,b with h=cos(5.), q(eps)=|gamma(a)-gamma(b)|,
  q = q0 + eps q1 + eps^2 q2 + eps^3 q3 + O(eps^4),
  q1 = Q1/(2q0), q2 = Q2/(2q0)-Q1^2/(8q0^3), q3 = Q1^3/(16q0^5)-Q1 Q2/(4q0^3).
Symmetric family at apex A: L(A,t) = q(A,A+t)+q(A,A-t)+q(A+t,A-t).
Output (verified): at t*=2pi/3, for A in {0, pi/5},
  L1*=0, L2*=3s3/16, F1*=+/-63/4, F2*=-81/32, G0*=-3s3/2, G1*=+/-183s3/8,
  H0*=3/4, H1*=-/+6759/16, T0*=9s3/8, L3*=-/+3s3/64, F3*=-/+9/128,
  G2*=309s3/64 (upper sign at A=0).
Lyapunov-Schmidt gives reduced actions ell(A;eps) with K1=0, K2=111s3/4
at both apices and K3(0)=+855s3/2, K3(pi/5)=-855s3/2.
Run: python3 ls_data.py
"""
import sympy as sp

t, A = sp.symbols('t A')
h = lambda x: sp.cos(5*x)
ts = 2*sp.pi/3


def chords(a, b):
    d = a - b
    q0 = sp.sqrt(2 - 2*sp.cos(d))
    Q1 = 2*(h(a) + h(b))*(1 - sp.cos(d))
    Q2 = h(a)**2 + h(b)**2 - 2*h(a)*h(b)*sp.cos(d)
    q1 = Q1/(2*q0)
    q2 = Q2/(2*q0) - Q1**2/(8*q0**3)
    q3 = Q1**3/(16*q0**5) - Q1*Q2/(4*q0**3)
    return q0, q1, q2, q3


s = chords(A, A+t)
s2 = chords(A, A-t)
b = chords(A+t, A-t)
L0 = s[0] + s2[0] + b[0]
L1 = s[1] + s2[1] + b[1]
L2 = s[2] + s2[2] + b[2]
L3 = s[3] + s2[3] + b[3]
F0 = L0.diff(t); F1 = L1.diff(t); F2 = L2.diff(t); F3 = L3.diff(t)
G0 = F0.diff(t); G1 = F1.diff(t); G2 = F2.diff(t)
H0 = G0.diff(t); H1 = G1.diff(t); T0 = H0.diff(t)
data = {'L1': L1, 'L2': L2, 'L3': L3, 'F0': F0, 'F1': F1, 'F2': F2,
        'F3': F3, 'G0': G0, 'G1': G1, 'G2': G2, 'H0': H0, 'H1': H1, 'T0': T0}

if __name__ == '__main__':
    for Aval in [sp.Integer(0), sp.pi/5]:
        print('A =', Aval)
        for k, v in data.items():
            val = sp.simplify(v.subs({A: Aval, t: ts}))
            print(f'  {k}* = {val}')
        print()
    s3 = sp.sqrt(3)
    for sgn, tag in [(1, 'A=0'), (-1, 'A=pi/5')]:
        F1v = sgn*sp.Rational(63, 4); F2v = sp.Rational(-81, 32)
        F3v = sgn*sp.Rational(-9, 128)
        G0v = -3*s3/2; G1v = sgn*183*s3/8; G2v = 309*s3/64
        H0v = sp.Rational(3, 4); H1v = sgn*sp.Rational(-6759, 16)
        T0v = 9*s3/8; L2v = 3*s3/16; L3v = sgn*(-3)*s3/64
        u1 = -F1v/G0v
        u2 = -(G1v*u1 + H0v*u1**2/2 + F2v)/G0v
        u3 = -(G1v*u2 + H1v*u1**2/2 + H0v*u1*u2 + T0v*u1**3/6
               + G2v*u1 + F3v)/G0v
        e = sp.symbols('e')
        u = u1*e + u2*e**2 + u3*e**3
        ell = (3*s3 + G0v*u**2/2 + H0v*u**3/6 + T0v*u**4/24
               + e*(F1v*u + G1v*u**2/2 + H1v*u**3/6)
               + e**2*(L2v + F2v*u + G2v*u**2/2) + e**3*(L3v + F3v*u))
        ell = sp.expand(ell)
        print(tag, 'u1 =', sp.simplify(u1), 'u2 =', sp.simplify(u2),
              'u3 =', sp.simplify(u3))
        for k in range(5):
            print(f'  K{k} =', sp.simplify(ell.coeff(e, k)))
        print()
