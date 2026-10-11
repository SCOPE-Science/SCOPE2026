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
# Verification

The algebraic checker `check.py` was executed from the packaged path before assembly. It verifies exactly that
\[
\frac{d}{dt}\frac{x^2+y^2}{2}=y^2z.
\]
For the hypothetical invariant case \(z=0\), it substitutes the general harmonic solution and verifies that \(x(1+a y)-c\) has constant coefficient \(-c\) and first cosine coefficient \(R\). Thus it cannot vanish identically when \(c\ne0\).

The remaining steps are analytic: compact-support invariance gives zero mean Lie derivative; a continuous nonnegative function with zero integral vanishes on the support; the support is invariant; and every nonempty compact invariant set carries an invariant probability measure by time averaging.

No finite trajectory sample is used to prove the infinite-time statement. The source's reported Lyapunov exponents and bifurcation plots are not replayed and are not part of the proof.

Limits: the theorem assumes compact recurrence and \(c\ne0\), proves no existence statement, and supplies no quantitative lower bound on half-space mass or excursion size.
