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

# Verification of the real \(L^4\) skew first-order result

The analytic proof in RESULT.md is primary. It uses the exact fourth-power polynomial identities, Hölder bounds on mixed moments, a uniformly bounded second derivative of the fourth root near one, the smooth finite-exponent power mean, and the nonnegative identity
\[
\int\!\left(xy+\frac{x^2-y^2}{\sqrt2}\right)^2=1+\sqrt2\int xy(x^2-y^2)
\]
for real \(L^4\) unit vectors. Equality is solved pointwise and then normalized in two disjoint components; these operations do not require measure-space compactness.

The portable `verify.py` file uses only the Python standard library. Run `python verify.py` from the same directory as the other files. The actual invocation produced:

`VERIFY_OK: polynomial expansion, two-band algebra, finite stress, endpoint slopes`

The program checks polynomial expansions on rational samples, the two algebraic ratio roots and their unit-band normalization, and the defect identity on random finite real vectors in dimensions 2, 5, and 23. It also compares finite-difference slopes for outer means 1, 2, and 3.5. Such finite experiments are **not** a certificate for arbitrary measure spaces or infinitely many vectors; the uniform analytic estimates in the proof supply those quantifiers.

No independent audit or external validation has been performed. Possible mathematical limitations are listed in RESULT.md; an exact positive-parameter minimization and complex-scalar analogues remain unproved here.
