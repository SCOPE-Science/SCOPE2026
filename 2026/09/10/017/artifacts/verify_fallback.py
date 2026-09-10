"""PRESET FALLBACK certificate: D* = D_7 (least eliminated twist), v* = 2.
X_31: y^2 = f = g1*g2, g1=x^2+1, g2=x^4+30x^2+1, Res(g1,g2)=28^2.
Cover family D_d (d|28 squarefree, d>0): d u^2=g1(x), d v^2=g2(x).
(i)   D_1(Q),D_2(Q) nonempty: (0,1,1),(1,1,4). Least eliminated twist: D_7.
(ii)  D_7(Q_2)={}: mod-8 primitivity wall + 2-adic descent; Hilbert (7,-1)_2=-1.
      D_7(R) nonempty, so v*=2 is the least non-soluble place in (R,2,7,...).
      (Also D_7(Q_7)={} via Lemma A; recorded as cross-check.)
(iii) Hence D_7(Q)={}.
Stdlib only. Prints VERIFY_OK."""
import math

def g1(x): return x**2+1
def g2(x): return x**4+30*x**2+1
def f(x): return x**6+31*x**4+31*x**2+1
for x in range(-9,10):
    assert g1(x)*g2(x)==f(x)
print("(0) factor identity OK; Res = 28^2.")

# (i)
assert 1*1==g1(0) and 1*1==g2(0)
assert 2*1==g1(1) and 2*16==g2(1)
print("(i) D_1(Q)ni(0,1,1); D_2(Q)ni(1,1,4). D* = D_7 = {7u^2=x^2+1, 7v^2=x^4+30x^2+1}.")

# (ii-a) R soluble: (x,u)=(0,1/sqrt7)
print("(ii-a) D_7(R) nonempty: x=0, u=1/sqrt(7).")

# (ii-b) mod-8 wall: every mod-8 solution of X^2+Z^2=7U^2 is all-even
sols=[(X,Z,U) for X in range(8) for Z in range(8) for U in range(8) if (X*X+Z*Z-7*U*U)%8==0]
prim=[t for t in sols if (t[0]%2,t[1]%2,t[2]%2)!=(0,0,0)]
assert prim==[], prim
print("(ii-b) mod-8 wall: all %d solutions of X^2+Z^2=7U^2 mod8 are (even,even,even); no primitive lift." % len(sols))

# (ii-c) 2-adic descent: no Q_2 point. Clearing denominators: X^2+Z^2=7U^2 over Z_2,
# not all in 2Z_2 (primitivity = at least one unit). Mod 8 this is impossible by (ii-b)
# (units square to 1 mod8; non-units are even). By infinite 2-descent (divide by 4),
# only (0,0,0); the conic, hence D_7, has no Q_2 point.
print("(ii-c) 2-adic descent: any Z_2 solution reduces mod8 to all-even, forcing v2>=1 on all")
print("        coords; iteration gives only (0,0,0). So D_7(Q_2)={}. v* = 2 (least: R ok, 2 fails).")

# (ii-d) Hilbert log: (7,-1)_2 = -1.
# Tame formula (a,b)_2 = (-1)^{e(u)e(v)+a1*w(v)+a2*w(u)}, a=(u)2^{v}... for (7,-1): e=0 terms vanish,
# (7,-1)_2 = (-1)^{((7-1)/2)((-1-1)/2)} = (-1)^{-3} = -1.
e1,e2=(7-1)//2,(-1-1)//2
assert (e1*e2)%2==1
print("(ii-d) Hilbert log: (7,-1)_2 = (-1)^{(%d)(%d)} = -1: X^2+Z^2=7U^2 has no nontrivial Q_2 zero." % (e1,e2))

# cross-check at 7: only trivial zero mod7
assert [(x,z) for x in range(7) for z in range(7) if (x*x+z*z)%7==0]==[(0,0)]
print("(ii-e, cross-check) D_7(Q_7)={} too (mod-7 lemma + clearing denominators).")

# (iii)
print("(iii) D_7(Q_2)={} => D_7(Q)={}: one certified pruned twist.")
print("VERIFY_OK")
