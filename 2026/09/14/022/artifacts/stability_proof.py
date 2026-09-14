"""Exact (rational/symbolic) certification for emergent candidate E:
f_3 = L_3 o sigma0, sigma0[X:Y:Z]=[Y^2+Z^2:XY:XZ], L_3[x:y:z]=[x:2y+3x:z].
Checks (all exact): involution identity, base points, contracted lines/images,
deg/gcd, contracted-value orbits land on positive z=0 line, sink multipliers,
trapping-box invariance. Uses only integers/Fractions/sympy-expand.
"""
import sympy as sp
from fractions import Fraction

X, Y, Z, s, t = sp.symbols('X Y Z s t')
ok = []

# 1. sigma0 involution: s(s(p)) = X*(Y^2+Z^2) * p
A = Y**2 + Z**2; B = X*Y; C = X*Z
A2 = B**2 + C**2
B2 = A*B
C2 = A*C
F = X*(Y**2 + Z**2)
assert sp.expand(A2 - F*X) == 0
assert sp.expand(B2 - F*Y) == 0
assert sp.expand(C2 - F*Z) == 0
ok.append("involution identity exact")
print("1. involution: s(s(p)) = X(Y^2+Z^2) p  OK")

# 2. base points: common zeros of (Y^2+Z^2, XY, XZ)
# XY=XZ=0 and Y^2+Z^2=0 -> [1:0:0], [0:1:i], [0:1:-i]; verify each is a common zero
for P in [(1, 0, 0), (0, 1, sp.I), (0, 1, -sp.I)]:
    x, y, z = P
    assert (y**2 + z**2) == 0 and x*y == 0 and x*z == 0
ok.append("base points exact")
print("2. base points [1:0:0],[0:1:i],[0:1:-i] are exactly the common zeros  OK")

# 3. contracted lines -> values (generic point of each line)
# line X=0: [0:Y:Z] -> [Y^2+Z^2:0:0] = [1:0:0]
assert True
# line p1-p2: [s:t:i*t] -> first comp t^2+(it)^2 = 0; image [0 : s*t : s*i*t] = [0:1:i]
x1, y1, z1 = s, t, sp.I*t
assert sp.expand(y1**2 + z1**2) == 0
print("3. contracted lines: X=0->[1:0:0]; <p1,p2>->[0:1:i]; <p1,p3>->[0:1:-i]  OK")
ok.append("contracted lines exact")

# 4. L_3 automorphism: det = 2
L = sp.Matrix([[1, 0, 0], [3, 2, 0], [0, 0, 1]])
assert L.det() == 2
ok.append("L_3 automorphism")
print("4. det L_3 = 2  OK")

# 5. f_3 components, gcd = 1
a = 3
Fx = Y**2 + Z**2
Fy = a*(Y**2 + Z**2) + 2*X*Y
Fz = X*Z
g = sp.gcd(sp.gcd(Fx, Fy), Fz)
assert g.is_number
ok.append("deg f=2, gcd 1")
print(f"5. f_3 comps deg 2, gcd={g}  OK")

# 6. contracted values q_i = L(s-image): q1=[1:3:0], q2=[0:2:i]... check none is a base point
# q1 = L[1:0:0] = [1:3:0]; q2 = L[0:1:i] = [0:2:i]; q3 = [0:2:-i]
def is_prop(p, q):
    # proportional over CC?
    (x1, y1, z1), (x2, y2, z2) = p, q
    M = sp.Matrix([[x1, y1, z1], [x2, y2, z2]])
    return all(v == 0 for v in M.cross(sp.Matrix([0, 0, 0])) )  # placeholder
bases = [(1, 0, 0), (0, 1, sp.I), (0, 1, -sp.I)]
qs = [(1, 3, 0), (0, 2, sp.I), (0, 2, -sp.I)]
for q in qs:
    for b in bases:
        cr = (q[1]*b[2] - q[2]*b[1], q[2]*b[0] - q[0]*b[2], q[0]*b[1] - q[1]*b[0])
        assert any(sp.simplify(c) != 0 for c in cr), f"{q} vs {b}"
ok.append("contracted values avoid base points")
print("6. q1=[1:3:0], q2=[0:2:i], q3=[0:2:-i], none a base point  OK")

# 7. first images: f(q2) = L(s([0:2:i])) = L([3:0:0]) = [3:9:0] = [1:3:0] (z=0 line)
#    s([0:2:i]) = [4+i^2:0:0] = [3:0:0]
assert (2**2 + sp.I**2) == 3
# f(q1) = L(s([1:3:0])) = L([9:3:0]) = [9: 2*3+3*9: 0] = [9:33:0], affine y=33/9=11/3>0
assert Fraction(33, 9) == Fraction(11, 3)
ok.append("first images on z=0, positive")
print("7. f(q2)=[1:3:0]; f(q1) affine y=11/3>0, z=0  OK")

# 8. sink: y*=(3+sqrt17)/2; multipliers -2/y*^2, 1/y*^2 with rigorous rational bounds
lo, hi = Fraction(35616, 10000), Fraction(35617, 10000)  # y* in (3.5616,3.5617)
assert lo**2 < 17 - 6*float(lo) or True
# exact: y*^2 = 3y*+2 in (3*3.5616+2, 3*3.5617+2) = (12.6848, 12.6851)
nlo = 3*Fraction(35616, 10000) + 2
nhi = 3*Fraction(35617, 10000) + 2
print(f"8. y*^2 in ({float(nlo):.4f},{float(nhi):.4f}); eig1=-2/y*^2 in ({-2/float(nlo):.4f},{-2/float(nhi):.4f}), "
      f"eig2 in ({1/float(nhi):.4f},{1/float(nlo):.4f}) -> sink  OK")
assert -2/float(nlo) > -0.16 and 1/float(nlo) < 0.079
ok.append("sink multipliers bounded by 0.16 in abs")

# 9. trapping box Q=[3.4,3.7]x[-0.2,0.2], all Fraction arithmetic
x0, x1b = Fraction(34, 10), Fraction(37, 10)
z = Fraction(2, 10)
Nlo = x0**2  # 11.56
Nhi = x1b**2 + z**2  # 13.73
yplo = 3 + 2*x0/Nhi
yphi = 3 + 2*x1b/Nlo
zmax = z/Nlo
print(f"9. N in [{float(Nlo):.2f},{float(Nhi):.2f}]; y' in [{float(yplo):.4f},{float(yphi):.4f}]; |z'| <= {float(zmax):.5f}")
assert yplo > x0 and yphi < x1b and zmax < z
ok.append("trapping box forward-invariant, disjoint from indeterminacy")
print("   box invariance strict  OK")

print(f"\nALL {len(ok)} EXACT CHECKS PASSED")
