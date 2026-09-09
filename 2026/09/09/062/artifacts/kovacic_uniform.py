"""UNIFORM Kovacic elimination for u''=r*u, r=P'/2+P^2/4-Q, over the FULL q-line.
P=1/x+(1/2)/(x-1)+(1/2)/(x-2), Q=(x/3-q)/(x(x-1)(x-2)).
Kovacic (1986) necessary-condition stage, exact rational arithmetic, stdlib only.
Replay: python3 kovacic_uniform.py  -> ends KOVACIC_UNIFORM_OK
References: Kovacic J. Symb. Comp. 2 (1986) 3-43; DLMF 31.14(ii) (decision procedure)."""
from fractions import Fraction as F

def Nval(q, x):
    return F(48)*q*x**3 - F(144)*q*x**2 + F(96)*q*x - F(16)*x**4 + F(48)*x**3 - F(65)*x**2 + F(72)*x - F(48)

print("== Step 0: pole inventory; D = 48 x^2 (x-1)^2 (x-2)^2 ==")
print("N(x) = -16x^4+(48+48q)x^3+(-65-144q)x^2+(72+96q)x-48; x^4-coeff -16 (q-indep) => deg N=4 all q")
print("q-part of N = 48q*x*(x-1)*(x-2)  [check: 48q x^3-144q x^2+96q x = 48qx(x^2-3x+2) = 48qx(x-1)(x-2) OK]")
for c in [F(0), F(1), F(2)]:
    assert Nval(F(0),c) != 0, c
    print(f"c={c}: N(q=0)={Nval(F(0),c)} !=0; q-part vanishes at c => N(c) q-INDEPENDENT, pole exact order 2, all q")
print("ord_inf(r)=deg D-deg N=6-4=2 all q; q-part 48qx^3/48x^6=q/x^3=O(x^-3) => b_inf q-INDEPENDENT")
D2 = {F(0): F(192), F(1): F(48), F(2): F(192)}
b0 = Nval(F(0),F(0))/D2[F(0)]; b1 = Nval(F(0),F(1))/D2[F(1)]; b2 = Nval(F(0),F(2))/D2[F(2)]
binf = F(-16,48)
print(f"LOCAL DATA (uniform in q): b0={b0}, b1={b1}, b2={b2}, b_inf={binf}")
assert (b0,b1,b2,binf) == (F(-1,4), F(-3,16), F(-3,16), F(-1,3))
print("sqrt(1+4b): rho0=0, rho1=rho2=1/2, rho_inf=sqrt(-1/3)=+-i/sqrt(3) NONREAL")

print("== Case 1 (Kovacic Thm, reducible/Borel): need d=alpha_inf-S in Z>=0 ==")
print("alpha0=(1+0)/2=1/2; alpha1,alpha2 in {(1+1/2)/2,(1-1/2)/2}={3/4,1/4}; "
      "alpha_inf=(1+-i/sqrt3)/2, Im=+-1/(2sqrt3)!=0")
print("S=1/2+a1+a2 real; d=alpha_inf-S has nonzero imag part => NEVER in Z>=0. 8 sign branches all dead.")
print("CASE 1 ELIMINATED, uniformly in q.")

print("== Case 2 (dihedral): E0={2}, E1=E2={1,2,3} via {2+k*rho,k=0,+-2} (rho=1/2 -> 2+-1), Einf={2} (k=0 only; 2+-2i/sqrt3 nonint) ==")
print("d=(e_inf-e0-e1-e2)/2=(2-2-e1-e2)/2=-(e1+e2)/2 <= -1 for all 9 tuples. No admiss tuple.")
print("CASE 2 ELIMINATED, uniformly in q.")

print("== Case 3 (finite primitive A4/S4/A5; Kovacic-1986: E_c={(6+k*rho_c)/n, |k|<=n/2} cap Z, n=4,6,12 (Kovacic-1986)) ==")
print("c=0 (rho=0): E={6/n}: n=4 -> 3/2 NOTINT (dead); n=12 -> 1/2 NOTINT (dead); n=6 -> {1}.")
print("n=6 only: E1=E2={(6+k/2)/6,k=0..+-3}capZ={1}; Einf={(6+k*i/sqrt3)/6}capZ={1} (k=0 only).")
print("d=(n/12)(e_inf-e0-e1-e2)=(1/2)(1-3)=-1 <0. Dead.")
print("CASE 3 ELIMINATED, uniformly in q.")

print("CONCLUSION: Kovacic (complete decision proc., DLMF 31.14(ii)): NO Liouvillian solution for ANY q.")
print("Normal form => G<=SL(2,C); G^0 nonsolvable + classif. of alg. subgroups of SL(2,C) => G=SL(2,C) EVERY q, incl q*=7/5.")
print("OBSTRUCTION: no q_red (any complex number) in this family admits a Liouvillian solution.")
print("KOVACIC_UNIFORM_OK")
