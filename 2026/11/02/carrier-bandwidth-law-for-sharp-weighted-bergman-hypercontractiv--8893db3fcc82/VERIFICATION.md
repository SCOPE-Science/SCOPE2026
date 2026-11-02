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

# Verification record

The mathematical proof establishes the general claim using a complete two-sided radial comparison for every analytic polynomial, exact weighted Bergman moments, and uniform gamma-ratio asymptotics. The standalone deterministic code in `check.py` evaluates exact finite carrier cases and the derived inequalities from coefficient convolutions. It makes no finite-to-infinite extrapolation claim.

Checked definitions: the area measure is normalized, the frequency support is nonempty, the cutoff is sharp for arbitrary complex coefficients, and the shift-width hypotheses are explicit. The three-frequency circle fourth moments are independently derived from additive pair-sum collisions; their values are treated as known supporting inputs.

The checker requires Python 3 with NumPy and SciPy. To reproduce: `python3 check.py`. All infinite-asymptotic statements depend on the written proof, not on computational sampling. Independent mathematical review and historical-priority audit are not performed.
