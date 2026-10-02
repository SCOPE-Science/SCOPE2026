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
2. The PPV group is the full differential-algebraic group SL₂: beyond det = 1
   there are no nontrivial dt-polynomial defining equations.
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
finite poles), its contribution E = S' + 2QS + S² has residue 2sk at infinity.
Hence the total x¹ coefficient is 2s(1+k), never zero for k ≥ 0. Equivalently
the formal series requires 1/x coefficient c = −1, impossible for a rational
function. So (R) has no solution in C(t,x): case (A) is excluded.

Kovacic case 1. The only square-root part at infinity is s = x²+t/2 (up to sign),
giving V := s'+s²−q = t²/4+2x−1. A case-1 polynomial P of degree n would satisfy
P''+2sP'+VP = 0, but the left side has degree n+1 with leading coefficient
2n·lc(P) for n ≥ 1 and degree 1 for n = 0, never zero.

Kovacic case 2 (dihedral). For the symmetric-square equation
L₂(P)=P'''−4qP'−2q'P=0, a rational solution cannot have a finite pole because
P''' has strictly highest pole order. A polynomial of degree d is also
impossible because L₂(P) has degree d+3 with leading coefficient
−(4d+8)lc(P). Thus there is no nonzero rational symmetric-square solution, so
the infinite dihedral case is excluded.

Kovacic case 3 (finite primitive). The irregular singularity at infinity has
nontrivial exponential part, hence the classical group is infinite; a finite
primitive group is therefore impossible. Together with the previous two
exclusions, the classical PV group is SL(2,C).

Lax reduction. With B = [[a,b],[c,−a]], dt(A) = [[0,0],[x²,0]]. The (1,1) and
(1,2) entries of dt(A)−dx(B) = [A,B] give a = b'/2 and c = bq−b''/2 exactly;
substituting into the (2,1) entry yields
L₂(b) = −2x².

No rational b. If b is polynomial of degree d, deg L₂(b) = d+3 with leading
coefficient −(4d+8)c_d ≠ 0, never equal to degree 2. If b has a finite pole
with principal part c₀(x−a₀) to the power −k, then L₂(b) has a pole of order k+3 with
coefficient −k(k+1)(k+2)c₀ ≠ 0, while the right side is a polynomial. Hence no
b ∈ C(t,x) solves the Lax equation, so the family is non-isomonodromic.

PPV conclusion. Arreche's parameterized second-order framework and Cassidy's
classification say that a Zariski-dense differential-algebraic subgroup of
SL₂ is either all of SL₂ or is conjugate to the dt-constant subgroup. The
latter is the isomonodromic case. Since the Lax equation has no rational
solution, the constant alternative is excluded. Hence the PPV group is the
full differential-algebraic SL₂, with no dt-equations beyond det = 1.

## Limitations

Generic t means transcendental t as stated. Specializations including t = ±2 are
not analyzed. The PPV step applies the published parameterized-Galois
classification; the operator-specific content is the exact hypothesis
verification above. No claim is made that the general PPV algorithm itself is
new.

## Reproducibility

The stored `artifacts/kovacic_ppv_checks.py` gives exact symbolic checks of the
Riccati, symmetric-square and Lax identities. The audit independently
reconstructed the decisive pole and degree arguments rather than treating the
stored success log as proof.

## References

- Cassidy–Singer, Galois theory of parameterized differential equations and
  linear differential algebraic groups.
- Dreyfus, Computing the Galois group of some parameterized linear differential
  equation of order two, Proc. AMS 2014.
- Arreche, Computing the differential Galois group of a one-parameter family of
  second-order linear differential equations, arXiv:1208.2226.
- Kovacic, An algorithm for solving second order linear homogeneous differential
  equations, J. Symbolic Computation 1986.
- Cassidy, Differential algebraic subgroups of SL(2) and strong normality in
  simple extensions.
