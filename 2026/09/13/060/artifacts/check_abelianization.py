# Abelianization arithmetic for G3 = <a,b,c | w3^6 = 1>, w3 = a B a b c c.
# G3^ab = Z^3 / <6*(2,0,2)> = Z^3 / <(12,0,12)>.
# Checks: (i) [R] = (2,0,2) has order exactly 6 in the quotient;
# (ii) [t] = 2*(6,0,6) = (12,0,12) = 0, and k*(2,0,2) = 0 in quotient iff 6 | k.

rel = (12, 0, 12)
R = (2, 0, 2)

def add(u, v):
    return (u[0] + v[0], u[1] + v[1], u[2] + v[2])

def mul(k, u):
    return (k * u[0], k * u[1], k * u[2])

def is_zero_mod_rel(v):
    # v = (x,y,z) is 0 mod <rel> iff y == 0 and (x,z) is a multiple of (12,12),
    # i.e. x == z and x % 12 == 0 (since rel spans {(12m,0,12m)}).
    x, y, z = v
    return y == 0 and x == z and x % 12 == 0

# (i) order of [R]
orders = [k for k in range(1, 13) if is_zero_mod_rel(mul(k, R))]
print("k in 1..12 with k[R]=0:", orders, "=> order of [R] is 6:", orders[0] == 6)

# (ii) [x] = 3[R] = (6,0,6) has order 2 mod rel
x = mul(3, R)
print("[x] =", x, "| 2[x] = 0 mod rel:", is_zero_mod_rel(mul(2, x)),
      "| [x] != 0:", not is_zero_mod_rel(x))

# (iii) [t] = [x]+[y] = 2[x] = 0; conjugacy t ~ R^k forces k[R]=0 forces 6|k
t = mul(2, x)
print("[t] =", t, "is 0 mod rel:", is_zero_mod_rel(t))
ks = [k for k in range(0, 24) if is_zero_mod_rel(mul(k, R))]
print("k in 0..23 with k[R]=[t]=0:", ks, "=> all multiples of 6:", all(k % 6 == 0 for k in ks))
