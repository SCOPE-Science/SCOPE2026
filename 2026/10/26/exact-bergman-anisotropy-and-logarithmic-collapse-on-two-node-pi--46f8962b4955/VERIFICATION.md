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

# Verification evidence

The proof uses explicit pseudohyperbolic disk slices, the identity between the squared norm of the symmetric coordinate and the domain volume, swap-invariant first-order Bergman Gram matrices, biholomorphic covariance, and exact logarithmic moment integration. These identities are sufficient to establish the claim for the entire indicated parameter range.

Reproduction: from the directory containing the embedded `check.py`, run `python check.py` with Python 3 and the installed `mpmath` and `sympy` packages. The output observed here was `CHECK_OK: beta-moment identities, positivity, both singular coefficients`. The checker evaluates both integral forms and closed forms for six parameters, checks moment positivity and a separate variance formula, and computes both singular limit coefficients symbolically.

Finite tests do not prove an infinite-domain statement: the analytic lemmas in RESULT.md are the proof. No complete characterization of the metric off the diagonal, higher-point bodies, or independent assessment is asserted. Relevant earlier characterization work was not available in full and remains a priority-risk source.
