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

# Computational verification and proof boundaries

Run `python checker.py` with Python 3 (standard library only). The checker builds literal substitution iterates, reconstructs all contiguous factor sets and independently builds absent candidates by checking both one-shorter borders. It also tests the two occurrences of the repeated length-\(h-1\) factor and absence of any repeated length-\(h\) factor.

Actual replay passed for every level \(k=3,4,5,6,7,8,9\), with finite word lengths \(8,16,32,64,128,256,512\). Maximal minimal-absent lengths were \(5,9,17,33,65,129,257\), with exactly one maximal word at each checked level.

The theorem for all levels is established by the induction and context proof in `RESULT.md`. No finite test proves uniqueness for untested levels or a formula for the total number of minimal absent words. No independent audit or outside proof certification has been conducted.
