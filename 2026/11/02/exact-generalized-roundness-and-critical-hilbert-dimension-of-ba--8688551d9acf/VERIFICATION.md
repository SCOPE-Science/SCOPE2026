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

Run `python3 verify_bistar_roundness.py` using a standard Python 3 interpreter. The checker enumerates shortest paths from the explicit graph, compares their prescribed distance shells, checks ten nontrivial rational zero-sum vectors at each of three integer exponents for each \(1\le q\le12\), verifies the critical root and null-vector quadratic identity numerically, and tests the stated leading asymptotic coefficient for several larger parameters. The recorded final marker is `ALL_BALANCED_BISTAR_ROUNDNESS_CHECKS_OK`.

The exact rational checks validate the algebraic decomposition only in the enumerated cases. The numerical root computations are finite diagnostics, not proofs of root uniqueness or nonnegative type at all real exponents. The general proof uses monotonicity, strict concavity and the invariant-space decomposition in `RESULT.md`. The independent audit channel has not been performed; no outside certification or formal proof assistant is claimed.
