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

# Reproducible verification

Run `python3 verify_theta_recovery.py` using standard Python 3.9 or later. No third-party dependencies are required. The script independently builds the graph and for each target edge enumerates all subsets of edges not including the target, determines endpoint connectivity by traversal, computes its exact recovery expectation using a subset-size probability identity, and compares this value with the closed rational formula. It also tests the identity \(\sum_e\mathbb E\tau_e=N(N-r+1)\) and the exact strict comparisons. The tested graph length vectors are listed in the source and span three to five paths.

Expected final output begins `VERIFY_OK`. A successful replay from the embedded script is evidence for these finite tests alone. Universal validity rests on the alternate-route characterization, Poisson thinning and the sign-definite integral identity in `RESULT.md`. No independent external audit has been performed. Earliest source dates are verified from the cited arXiv version-one submission records, rather than any revision dates.
