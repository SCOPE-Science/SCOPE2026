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

# Verification of exact language and rational census

Run `python3 verify.py` from the directory containing the standalone verifier. It uses only the standard library. `verify_output.txt` is the recorded output of an actual successful execution.

The verifier constructs each of 32 edge orientations, both directed edge transitions per undirected edge, and the complete five-vertex subset action. It explores every reachable product tuple until transition closure, proving a count of 23 reachable accepting tuples plus one rejecting sink. It then performs stable Myhill–Nerode partition refinement, obtains 18 classes and compares the canonical reduced transition table to the one printed in the result.

The series check uses exact integers and the full 18-state transition table. It verifies that the coefficients through degree 26 in the proposed polynomial identity vanish. Since the unreduced transfer-series denominator divides a degree-at-most-18 determinant and its numerator has degree at most 17, the relevant polynomial difference has degree at most 26. Thus the finitely verified coefficient identity proves the **infinite formal power series equality**.

For an additional independent finite cross-check, the verifier tests all 8191 binary words of lengths 0 through 12 directly against all 32 oriented walk graphs. This cross-check alone is not used as proof for arbitrarily long words. It also checks the two separating words against all triangle and pentagon orientations.

Full-text literature comparison is not a mathematical computation and remains incomplete; only the explicitly reported scientific overlap comparisons have been made. There has been no independent audit.
