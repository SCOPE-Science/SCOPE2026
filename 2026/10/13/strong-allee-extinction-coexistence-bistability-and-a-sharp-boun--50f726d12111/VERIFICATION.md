---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The proof is analytic and does not depend on numerical enumeration.

The source's exact exponential map yields the strong-Allee branch criterion from \(\eta=de/(f-d)\) and the prey-only quadratic. In the specialized family,
\[
H_\pm=\frac{3\pm\sqrt{25-4\alpha}}2,
\quad (H^*,P^*)=(2,6-\alpha).
\]
The coexistence Jacobian has trace \(4/3\), determinant \(1-\alpha/9\), and strictly positive Schur–Jury expressions
\[
\frac\alpha9,\qquad\frac{6-\alpha}9,\qquad\frac{30-\alpha}9
\]
for every \(4<\alpha<6\). The origin's two multipliers are \(e^{4-\alpha}\) and \(e^{-1}\). The boundary multiplier \(1+H(3-2H)/(1+H)\) equals \(-1\) at the unique \(H\in(2,3)\) given by \((5+\sqrt{41})/4\), hence at \(\alpha_F=(29+\sqrt{41})/8\).

The included `verify.py` checks exact symbolic identities, determinant/traces, the boundary threshold, and direct numerical substitution in the original map at several rational parameter values. These finite checks corroborate the algebra; they are not an exhaustive verification of the universal continuum interval. No independent audit has been performed.
