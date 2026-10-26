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

The included `verify_rook.py` uses Python standard library only. It constructs explicit full assignments and checks that every uncolored cell has exactly the whole degree-sized palette among its neighbors. It tests 917 feasible cases with \(2\le m\le15\), \(m\le n\le m+6\) and every eligible number of uncolored cells. An independent backtracking solver for the internal shared-neighbor conflict coloring checks 51 small cases. Selected exact optima and counts are printed in `verification_output.txt` and the output concludes `VERIFY_OK`.

Run with `python3 verify_rook.py` from the directory holding that file; compare stdout with `verification_output.txt`. No supplementary downloads, nondeterminism or external dependencies are required. The exhaustive backtracking checks concern only the explicitly specified small cases; the infinite result is supported by the proof, not the finite computations. The edge-index argument is given in the proof and can be checked independently of the code.
