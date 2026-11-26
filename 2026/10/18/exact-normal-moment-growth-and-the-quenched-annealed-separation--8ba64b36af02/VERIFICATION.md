---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Lee et al.'s Type-2 equations yield the invariant logistic axis and the normal multiplier bx−a, independent of c. Doubling with x=sin²(πt) pushes Haar to the stated arcsine law; the logarithm is integrable even at endpoint/double zeros. Jensen applied to z²+(2A/B)z+1 gives the two log-integral branches, including a=b. For a>b the positive branch argument is strictly increasing with a, and solving for argument 1 yields a=(1+b/4)² when b<4; the b=4 and b>4 cases follow from the value at a=b. For C=cos(2πt), doubling transfer deletes odd Fourier orders and halves even ones, giving L(w²)=A²+B²/2+(B²/2)C and L(w²C)=AB(1+C). Transfer duality then gives (Mⁿ)₁₁. Its determinant is A³B; A<0 gives a strictly positive matrix and visible Perron mode, A>0 a negative determinant and positive trace with visible positive dominant eigenvalue, and A=0 has the direct power (B²/2)ⁿ. On the centered line the sine quotient has 2ⁿ unit Fourier coefficients and its fourth moment counts pairs with equal sums, giving (2·2³ⁿ+2ⁿ)/3 before multiplying by (b/4)⁴ⁿ. The exact b=3 rates are log(3/4) and log(9/8); continuity of the all-parameter formulas gives an open set. As a finite independent check the off-center case (a,b)=(7/4,3), n=2 gives 469/256, and the centered case (3/2,3), n=2 gives second/fourth moments 81/64 and 72171/16384. The uploaded verifier was inspected, not run; those finite checks are not used as the limiting proof. Scope is linear normal growth along the exact axis, not nonlinear extinction.

## originality

PASS

The distinct result supported by comparison is the all-offset exact second-moment transfer and the resulting open separation of the Lyapunov and raw second-moment growth signs in the Type-2 model. The logistic conjugacy, log-cosine integral, and centered sine-quotient law are not independent originality claims. In particular the centered finite-time distribution has a directly equivalent antecedent in the Ulam-map literature, and the displayed centered moments can be recovered from it. No inspected source supplies the off-centered transfer and comparison; the decision is best-of-knowledge, not exhaustive priority.

## value

PASS

The exact rank-two reduction applies throughout a natural two-parameter transverse stability problem, rather than just at a solvable resonance. It explains why a negative almost-sure exponent does not guarantee small average squared amplification and identifies a genuine open region without extrapolating from numerical plots or asserting nonlinear population extinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
