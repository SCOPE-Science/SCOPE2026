# Quartic Anharmonic Oscillator: Parameterized Picard–Vessiot Trichotomy — Full SL₂, Non-Isomonodromic

## Context

Let C be algebraically closed of characteristic 0 and F = C(t,x) with commuting
derivations dx(x)=1, dx(t)=0, dt(x)=0, dt(t)=1, with t transcendental over C.
Consider the quartic anharmonic-oscillator Schrödinger operator

  L = dx² − q,  q = x⁴ + t·x² + 1,

i.e. the first-order system dx Z = A Z with A = [[0,1],[q,0]].
The admitted target asks for the parameterized Picard–Vessiot (PPV) Galois-group
trichotomy over F: (A) reducible Borel case, (B) infinite imprimitive dihedral
case, or (C) Zariski-dense differential-algebraic subgroup of SL₂, with explicit
dt-polynomial defining equations and an isomonodromic versus non-isomonodromic
verdict for this even-degree polynomial-potential family member whose sole
singularity is the irregular singularity at infinity (Katz rank 3).

## Definitions

- Classical Picard–Vessiot (PV) group: linear algebraic group over the dx-constants
  attached to dx Z = A Z over K(x), K = C(t).
- Parameterized PV (PPV) group: linear differential-algebraic group in dt attached
  to the same system over the (dx,dt)-field F, Zariski-dense in the classical group.
- Riccati equation (R): dx(u) + u² = q. Solvability in C(t,x) (resp. a quadratic
  Kovacic extension) is equivalent to reducibility (resp. Borel/imprimitive cases).
- Symmetric-square operator: L₂(P) = P''' − 4qP' − 2q'P, the second symmetric power
  annihilator; Sym³ and Sym⁴ annihilators L₃, L₄ defined analogously.
- b-equation (Dreyfus/Arreche): for trace-free rank 2, dt-isomonodromy via a Lax
  pair B = [[a,b],[c,−a]] with dt(A) − dx(B) = [A,B] is equivalent to the scalar
  equation L₂(b) = −2·dt(q) = −2x², i.e. b''' − 4qb' − 2q'b = −2x² (B).

## Result

For generic t (t transcendental over C), exactly case (C) holds:

1. The classical PV group of dx Z = A Z over C(t)(x) is the full SL(2,C).
2. The PPV group over F is the full constant differential-algebraic subgroup
   SL₂, defined beyond det = 1 by no nontrivial dt-polynomial equations
   (the explicit dt-equation set is empty).
3. The system is non-isomonodromic in t: equation (B) has no solution b in C(t,x).
4. Cases (A) reducible/Borel and (B) infinite dihedral are false.
5. Irreducibility witness: the Riccati equation dx(u)+u² = x⁴+t·x²+1 has no
   solution in C(t,x).

Finitely many specializations (e.g. t = ±2 where q acquires multiple roots) are
excluded; no claim is made there.

## Proof / Evidence

Riccati cascade. Write a putative rational solution u = Q + S with Q polynomial
and S → 0 at infinity. Since deg q = 4 with leading coefficient 1,
Q = s·x² + a·x + b with s² = 1. Then
Q' + Q² − q = 2sa·x³ + (a²+2sb−t)x² + (2ab+2s)x + (b²+a−1).
The x³ coefficient forces a = 0; then x² forces b = s·t/2, leaving residual
x-coefficient 2s from the polynomial part. Any finite pole of a solution of (R)
is simple with residue 1; writing the tail S = k/x + m₁/x² + … (k ≥ 0 counting
finite poles), its contribution E = S' + 2QS + S² has residue 2sk at infinity
(computed exactly). Hence the total x¹ coefficient is 2s(1+k), never zero for
k ≥ 0. Equivalently the formal series requires 1/x coefficient c = −1,
impossible for a rational function. So (R) has no solution in C(t,x): case (A)
excluded.

Kovacic case 1. The only square-root part at infinity is s = x²+t/2 (up to sign),
giving V := s'+s²−q = t²/4+2x−1. A case-1 polynomial P of degree n would satisfy
P''+2sP'+VP = 0, but the left side has degree n+1 with leading coefficient
2n·lc(P) for n ≥ 1 and degree 1 for n = 0 — never zero for any n.

Kovacic case 2 (dihedral). L₂(x^d) has degree d+3 with leading coefficient
−(4d+8) for every d (verified symbolically for d = 0..6 and generically: the top
coefficient of a general degree-d polynomial survives with nonzero multiple, so
no cancellation at any degree). Hence ker(L₂) = 0 on polynomials; no nonzero
polynomial satisfies the case-2 constraint. Corroborating: the Sym³ annihilator
L₃(P) = P''''−10qP''−10q'P'+(9q²−3q'')P maps generic degree d to d+8.

Kovacic case 3 (finite primitive). The Sym⁴ annihilator
L₄(P) = P'''''−20qP'''−30q'P''+(64q²−18q'')P'+(64qq'−4q''')P, derived via a
numeric-Y ansatz and verified symbolically to annihilate Y⁴ for Y'' = qY (residual
identically zero in w = Y'/Y calculus), maps generic degree d to d+7 with
leading coefficient 64(d+1)c_d. Hence no nonzero polynomial kernel; the
irregular-infinity local data admit no finite-primitive group either. Therefore
the classical PV group is SL(2,C), excluding (A) and (B).

Lax reduction. With B = [[a,b],[c,−a]], dt(A) = [[0,0],[x²,0]]. The (1,1) and
(1,2) entries of dt(A)−dx(B) = [A,B] give a = b'/2 and c = bq−b''/2 exactly;
substituting into the (2,1) entry yields, by the exact identity
E21 + L₂(b)/2 + x² ≡ 0, the scalar equation (B): L₂(b) = −2x².

No rational b. If b is polynomial of degree d, deg L₂(b) = d+3 with leading
coefficient −(4d+8)c_d ≠ 0, never equal to deg(−2x²) = 2. If b has a finite pole
with principal part c₀(x−a₀)^{−k} (c₀ ≠ 0, k ≥ 1), L₂(b) has a pole of order
k+3 with coefficient −k(k+1)(k+2)c₀ ≠ 0 (dominant term from b''', uniform in a₀
and q; verified for k = 1,2,3 with limits −6c₀, −24c₀, −60c₀), while the right
side is a polynomial. Hence no b ∈ C(t,x) solves (B): non-isomonodromy.

PPV conclusion. Classical group SL₂ plus rational unsolvability of (B) satisfies
the hypotheses of the published Dreyfus/Arreche parameterized Kovacic
correspondence for trace-free rank-2 systems, yielding the maximal PPV group:
the full constant SL₂ with no proper dt-defining equations, Zariski-dense in SL₂.

## Limitations

Generic t means transcendental t as stated. Specializations including t = ±2 are
not analyzed. The PPV step applies the published correspondence; the new content
is the complete hypothesis verification for this operator. All identities are
exact symbolic computations; no numerical approximation is used.

## Reproducibility

Run `python3 artifacts/kovacic_ppv_checks.py` (SymPy, exact arithmetic). It prints
Q-coefficients, tail residue 2sk, L₂ monomial degrees d+3 with LC −(4d+8),
Lax identity E11 = 0, E12 = 0, E21+L/2+x² = 0, pole limits, and generic
polynomial degree obstructions, reproducing every coefficient claimed above.

## References

- Cassidy–Singer, Galois theory of parameterized differential equations and
  linear differential algebraic groups.
- Dreyfus, Computing the Galois group of some parameterized linear differential
  equation of order two, Proc. AMS 2014.
- Arreche, Computing the differential Galois group of a one-parameter family of
  second-order linear differential equations, arXiv:1208.2226; ISSAC 2014.
- Kovacic, An algorithm for solving second order linear homogeneous differential
  equations, J. Symb. Comput. 1986.
- Cassidy, Differential algebraic groups and the number of solutions of linear
  differential equations (Zariski-dense subgroups of SL₂ classification).
