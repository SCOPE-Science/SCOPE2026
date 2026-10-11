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

# Reproducibility and verification

Run `python3 verify_core.py` from this directory. Python's standard library is sufficient. The verifier reconstructs the finite Alexandrov product order directly, enumerates **all** injective ordered triples for each \(2\le n\le12\), and recomputes strict predecessor/successor relations among surviving configurations at each deletion. It confirms the exact four deletion-class sizes, the unique beat-point witnesses, the residual pairwise-incomparable subposet, and minimality by explicitly testing every remaining point for both beat-point types. It also exhaustively resolves the \(24\)-point exceptional case as two \(12\)-cycles with no beat points. A successful run prints `VERIFY_OK`.

The finite verification does not establish an infinite-family statement on its own. The all-parameter proof is supplied in `RESULT.md`, using the two-neighbor incidence structure of the crown and the finite-space beat-point theorem. The calculation does not establish a general homology or fundamental-group formula, and no independent audit has been performed.
