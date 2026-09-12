from fractions import Fraction
# Pic basis order H,E1,E2,E3, intersection diag(1,-1,-1,-1)
def dot(a,b):
    return a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3]
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def smul(c,a): return tuple(c*x for x in a)
H=(1,0,0,0); E1=(0,1,0,0); E2=(0,0,1,0); E3=(0,0,0,1)
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
# divisors
D1=E1
D2=sub(sub(H,E1),E3)   # H-E1-E3
D3=E3
D4=sub(sub(H,E2),E3)   # H-E2-E3
D5=E2
D6=sub(sub(H,E1),E2)   # H-E1-E2
Ds=[D1,D2,D3,D4,D5,D6]
beta=(4,-2,-1,-1)  # 4H-2E1-E2-E3  (coeffs in basis, E coeffs stored positive, subtract)
# careful: class = 4H -2E1 -E2 -E3 -> tuple (4,2,1,1)? Our basis vectors Ei represent +Ei, so class = (4,-2,-1,-1)? No: tuple means coeffs. Let's use signed.
beta=(4,-2,-1,-1)
print("beta",beta)
c1 = lambda c: dot((3,-1,-1,-1),c)  # -K=3H-E1-E2-E3 -> coeffs (3,-1,-1,-1)? dot with (3,1,1,1)? Let's just compute directly
# Actually -K class K=( -3,1,1,1)? c1.beta = 3*bH + b1+b2+b3 where b=(bH,b1,b2,b3) with b1 negative allowed? Since dot((3,-1,-1,-1)... no.
# intersection pairing: dot((h,e),(h',e'))=h h' - e.e'. -K=(3,1,1,1)? Since -K=3H-E1-E2-E3 = 3*H + (-1)E1+... so tuple (3,-1,-1,-1).
Kneg=(3,-1,-1,-1)
print("c1.beta =", dot(Kneg,beta))
print("vdim one-pointed =", 2-3+1+dot(Kneg,beta))
ks=[dot(d,beta) for d in Ds]
print("ks =",ks)
# H relations
print("D1+D2+D3 =",add(add(D1,D2),D3))
print("D3+D4+D5 =",add(add(D3,D4),D5))
# effectivity combo: 2E2+2E3+2L1+L2+L3
combo=add(add(add(smul(2,E2),smul(2,E3)),add(smul(2,D4),D2)),D6)
print("combo =",combo, "== beta?", combo==(4,-2,-1,-1))
import math
fact=1
for k in ks: fact*=math.factorial(k)
print("prod fact =",fact)
# harmonic
def harm(k): return sum(Fraction(1,m) for m in range(1,k+1))
hs=[harm(k) for k in ks]
print("harms =",hs)
# S = sum h_i D_i
S=(Fraction(0),Fraction(0),Fraction(0),Fraction(0))
for h,d in zip(hs,Ds):
    S=tuple(s+h*x for s,x in zip(S,d))
print("S =",S, " H-coeff =",S[0])
print("invariant -1/4*Hcoeff =", -Fraction(1,4)*S[0])
# Mori matrix M_ij = D_i . D_j
M=[[dot(a,b) for b in Ds] for a in Ds]
for row in M: print(row)
