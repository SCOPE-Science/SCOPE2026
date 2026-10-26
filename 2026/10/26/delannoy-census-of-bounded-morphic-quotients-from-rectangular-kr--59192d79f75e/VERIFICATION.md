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

# Reproducible checks
Run `python3 check.py` with standard Python 3. Its first checker constructs all upsets independently and exhaustively tests each surjective map's upward-cone lifting property for every \(1\le a,b\le5\), a total of 25 size pairs. Its second checker implements the transfer-state recurrence separately and compares with the binomial and Delannoy expressions for every \(1\le a\le13\), \(1\le b\le19\), a total of 247 pairs. It also checks the diagonal sequence. The recorded output is in `check_output.txt`.

# Scope
Exhaustive bounded finite tests support the proof but do not certify all dimensions. The all-parameter result depends on the written maximal-zero branching equivalence and generating-function recurrence.
