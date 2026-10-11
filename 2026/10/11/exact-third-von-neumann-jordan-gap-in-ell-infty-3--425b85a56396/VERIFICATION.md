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
The proof was checked from the defining quotient through the fixed-radius convexity reduction, the projective sign classification, and the sharp one-variable factorization.

The companion `verify.py` performs two replayable checks. First, it enumerates all \(4^3\) projective sign-row configurations and confirms that the modified numerator is at most \(28\). Second, it performs exact arithmetic in \(\mathbb Q(\sqrt3)\) to verify the unrestricted equality witness and the coefficient identities behind
\[
\frac{3+\sqrt3}{2}-\frac{r^2+2r+4}{r^2+2}
=
\frac{(1+\sqrt3)(r-(\sqrt3-1))^2}{2(r^2+2)}.
\]
The finite enumeration is not used as a proof over the continuous unrestricted domain; that upper bound is analytic. No independent audit has been performed.
