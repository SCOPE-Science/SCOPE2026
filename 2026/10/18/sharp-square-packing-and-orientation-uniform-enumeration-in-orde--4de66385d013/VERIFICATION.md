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

# Verification

Execute `python3 verify.py` using Python 3.9+; no additional modules are required. Its direct Euler expansion confirms the prescribed square orientations for every choice when alphabet sizes are 2, 3, or 4; selected patterns are checked for sizes 5–7. The fraction-free Laplacian determinant algorithm returns exact tree counts 1, 108, and 3538944 for sizes 2, 3, and 4 respectively. An independent literal Euler-tour traversal, rooted at the unique 000 triple, exhaustively enumerates all binary and ternary cycles; the ternary square-count histogram is {0:27648, 1:124416, 2:165888, 3:55296} and every one of the eight maximum orientations occurs 6912 times. Output ends with `SQUARE_RICH_DEBRUIJN_CHECKS_PASSED`. All these finite checks were executed.

Proof of the unrestricted result relies on the strong connectivity of the nonalternating de Bruijn core, balanced Euler tour existence, the reversible artificial-loop contraction and the BEST/matrix-tree count. These are symbolic mathematical arguments, not exhaustive finite checks. No independent audit, expert assessment, or machine-checked formal proof was performed.
