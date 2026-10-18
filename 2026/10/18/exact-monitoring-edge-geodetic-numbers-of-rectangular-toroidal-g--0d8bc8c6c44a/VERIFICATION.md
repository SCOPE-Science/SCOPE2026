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

# Reproduction and verification

The universal claim \(\operatorname{meg}(C_m\square C_n)=3\max\{m,n\}\) for \(m,n\ge5\) is proved in `RESULT.md`, using a precise cycle-gap criterion, a Cartesian-product fiber characterization, and a balanced-floor construction with two explicit exceptional placements. No infinite parameter range is certified by finite computation.

To run the optional finite checks, execute `python3 verify.py` using Python 3 and its standard library. The script exhaustively checks the cycle-gap equivalence on all \(8160\) subsets of cycles of orders \(5\) through \(12\), checks all \(5\le m\le n\le11\) boundary inequalities, validates \(5016\) row and column assignments, and independently recomputes distances after individual edge deletions on eight small tori. The full edge-deletion check explicitly includes the two exceptional dimensions \((5,6)\) and \((7,8)\). Its final output ends in `All checks passed (finite verification is not an infinite proof).`

There has been no independent scientific audit. The direct finite tests are reproducibility evidence only, not certification, and relevant publisher works may require additional literature comparison.
