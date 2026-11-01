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

# Reproduction and limits
Run `python3 verify_derangement5.py` with Python 3 (standard library only). The complete expected output is bundled as `verification_output.txt`; success terminates in `VERIFY_OK`. The verifier reconstructs each oriented simplex and its augmented boundary from the defining board, tests every boundary composition, then uses only invertible integral unit-pivot cancellations to produce a zero-differential chain complex with residual degrees two and three of ranks one and thirteen. All 240 automorphisms of the board are enumerated and their degree-two actions and signed cellular Lefschetz traces checked. The use of a prime field is **only** to distinguish \(+1\) and \(-1\) on a separately established rank-one integral group. The computation is exhaustive for the five-by-five finite board; no theorem for other board sizes, homotopy classification, or independent validation is asserted.
