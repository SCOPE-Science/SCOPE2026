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
The supplied `verify.py` is self-contained Python 3 code requiring no third-party packages. Run `python3 verify.py`; successful completion prints `VERIFY_OK`.

The checker calculates closed-neighborhood identifying signatures directly, and separately implements the two local inequalities. For every \(7\le n\le18\), it tests every subset, computes a seven-state transfer-matrix trace weight distribution, verifies equality with the direct enumerator, extracts all minimum codes, and constructs the complete one-vertex exchange graph. Results include \(n=13\): \(26\) optimal codes and \(39\) edges, one connected component; \(n=15\): \(35\) optimal codes, \(45\) edges and components of sizes \(30,1,1,1,1,1\); \(n=17\): \(34\) optimal codes and \(51\) edges, one connected component. Even orders \(8,10,12,14,16,18\) have exactly two isolated minima. For odd \(n=19,21,23,25,31,41,51,99\), the prescribed cyclic templates are validated as identifying codes and their complete pairwise exchange adjacency is compared to the theorem; the predicted degree profiles and component sizes hold in these tests.

Mathematical certification for all orders is the finite-state determinant plus the symbolic low-excess coefficient extraction and the complete one-token exchange classification in `RESULT.md`. The finite checker is corroborating evidence and does not assert a proof of untested orders. The inaccessible full primary texts noted in `RESULT.md` remain a limitation of the prior-art comparison.
