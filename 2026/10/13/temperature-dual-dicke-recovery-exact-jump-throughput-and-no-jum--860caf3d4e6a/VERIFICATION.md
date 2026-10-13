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

# Verification details

Run `python -m pip install -r requirements.txt` and `python verify.py` with Python 3.10 or newer. The actual package's script returned `VERIFY_OK 1348 exact/combinatorial and full-Kraus checks`.

The verifier uses rational binomial moments to check the exact variance coefficient across the admissible weight pairs through length 24 and six bath parameters. It checks the formula for normalized no-jump coherence at interior and endpoint bath parameters, and explicitly composes all tensor-product Kraus operators with the three recovery operators for code lengths 5 and 6 at two damping strengths. The latter verifies the first-order success slope and quadratic conditional-infidelity behavior, not an infinite-dimensional or all-parameter assertion.

The complete all-size proof is in `RESULT.md`: orthogonality of the three excitation sectors; the exact Dicke lowering/raising overlaps; contraction bounds; first-order branchwise scalarization; hypergeometric projection and strict Cauchy–Schwarz; and the binomial variance giving the coherence coefficient. The script cannot establish scientific novelty, optimality among arbitrary recoveries, finite-time hardware fidelity, or large-block uniformity.
