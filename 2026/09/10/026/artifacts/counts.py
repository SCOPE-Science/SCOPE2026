"""Point counts C(F_q), Jacobian orders #J(F_p) for C: y^2 = x^5-5x^3+4x+1.
Formula (genus 2): #J(F_p) = (N1^2 + N2)/2 - p, N1=#C(F_p), N2=#C(F_{p^2}).
One smooth point at infinity over every F_q (odd-degree model).
F_{p^2} built as F_p[t]/(m), m = first monic irreducible quadratic found.
Exact integer arithmetic throughout. Run: python3 counts.py
"""
import itertools

def f_int(x):
    return x**5 - 5*x**3 + 4*x + 1

def count_affine_Fp(p):
    n = 0
    pts = []
    for x in range(p):
        v = f_int(x) % p
        for y in range(p):
            if (y*y) % p == v:
                n += 1
                pts.append((x, y))
    return n, pts

def find_irred_quad(p):
    for a in range(p):
        for b in range(p):
            ok = True
            for t in range(p):
                if (t*t + a*t + b) % p == 0:
                    ok = False
                    break
            if ok:
                return (a, b)
    raise ValueError("no irreducible quadratic")

def add(u, v, p, mod):
    return ((u[0]+v[0]) % p, (u[1]+v[1]) % p)

def mul(u, v, p, mod):
    a, b = mod
    # (u0+u1 t)(v0+v1 t), t^2 = -a t - b
    c0 = (u[0]*v[0] - b*u[1]*v[1]) % p
    c1 = (u[0]*v[1] + u[1]*v[0] - a*u[1]*v[1]) % p
    return (c0, c1)

def f_Fp2(u, p, mod):
    # u^5 - 5 u^3 + 4u + 1 in F_{p^2}
    one = (1, 0)
    u2 = mul(u, u, p, mod)
    u3 = mul(u2, u, p, mod)
    u4 = mul(u2, u2, p, mod)
    u5 = mul(u4, u, p, mod)
    c5 = ((-5) % p)
    c4 = (4 % p)
    r0 = (u5[0] + c5*u3[0] + c4*u[0] + 1) % p
    r1 = (u5[1] + c5*u3[1] + c4*u[1]) % p
    return (r0, r1)

def count_affine_Fp2(p):
    mod = find_irred_quad(p)
    elts = [(i, j) for i in range(p) for j in range(p)]
    # squares
    sq = {}
    for y in elts:
        z = mul(y, y, p, mod)
        sq[z] = sq.get(z, 0) + 1
    n = 0
    for x in elts:
        v = f_Fp2(x, p, mod)
        n += sq.get(v, 0)
    return n, mod

def main():
    print("C: y^2 = x^5 - 5x^3 + 4x + 1")
    orders = {}
    for p in [3, 5, 7, 11, 13]:
        n1, pts = count_affine_Fp(p)
        N1 = n1 + 1
        n2, mod = count_affine_Fp2(p)
        N2 = n2 + 1
        J = (N1*N1 + N2)//2 - p
        assert (N1*N1 + N2) % 2 == 0
        orders[p] = J
        print(f"p={p}: aff(Fp)={n1} N1={N1} aff(Fp2)={n2} N2={N2} "
              f"mod_poly=t^2+{mod[0]}t+{mod[1]} #J(Fp)={J}")
    import math
    g = 0
    for p, J in orders.items():
        g = math.gcd(g, J)
    print("gcd of #J(Fp):", g)
    print("prime factors of each #J(Fp):")
    import sympy as sp
    for p, J in orders.items():
        print(f"  p={p}: {J} = {sp.factorint(J)}")

if __name__ == "__main__":
    main()
