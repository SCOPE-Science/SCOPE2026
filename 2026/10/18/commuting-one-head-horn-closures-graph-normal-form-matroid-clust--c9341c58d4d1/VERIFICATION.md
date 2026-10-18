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

# Reproducibility

Run `python3 verify.py` with Python 3.9+; the script uses only the standard library and prints `VERIFY_OK` on success.

The verifier exhaustively tests all ordered pairs of one-head Horn rules for every \(1\le n\le4\) and all distinct complete families of such rules for these sizes. It then enumerates every undirected graph for \(1\le n\le5\). For every graph and starting set it compares explicit forward and reverse update orders against the one-pass formula, then tests closed-set complements. It directly checks matroid exchange for all subsets and head pairs and independently checks union closure of the closed-set family, comparing both to their graph structural characterizations and their Bell/matching enumerations.

Observed labelled graph counts by \(n=1,2,3,4,5\): \(1,2,8,64,1024\). Observed exchange counts: \(1,2,5,15,52\). Observed Boolean-submodular counts: \(1,2,4,10,26\). An optional independently computed inclusion-exclusion expectation identity is also tested, but is not needed for acceptance of the main theorem.

**Limits:** The verifier is exhaustive only in those finite ranges; it cannot establish the theorem for unrestricted \(n\), which is proved in RESULT.md. No external or independent scientific certification is asserted.
