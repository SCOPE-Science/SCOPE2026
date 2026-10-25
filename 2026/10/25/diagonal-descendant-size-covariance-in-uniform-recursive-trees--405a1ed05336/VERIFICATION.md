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

# Verification and limits

The algebraic proof in `RESULT.md` uses the two-colour urn law for the exact variance and the nested-or-disjoint tree relation to establish the mixed-moment recurrence. This supplies an all-size analytical proof.

Run `python verify.py`. The script enumerates every permissible parent-choice array for \(1\le n\le9\) and evaluates exact integer/rational empirical means, the entire covariance matrix, and path-length variance. It verifies a concrete finite example of dependence and reports `VERIFY_OK 219 exact equality assertions; dependent example validated`.

Finite checks do not certify the all-size statements and are not a substitute for inspecting the proof. There is no independent external audit or publication-priority certification. The arXiv sources quoted in the references concern prior one-point/subtree or related joint observables; they do not validate this newly derived covariance theorem.
