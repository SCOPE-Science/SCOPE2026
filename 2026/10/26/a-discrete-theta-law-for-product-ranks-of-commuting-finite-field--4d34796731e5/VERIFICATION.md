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

The independent-of-formula finite test script `check_commuting_idempotents.py` uses direct matrix multiplication, row-reduction ranks, and explicit enumeration of idempotent matrices over prime fields. It compares every observed rank-stratified commuting-pair count with the fourfold general-linear orbit formula. The tested configurations are \((n,q)=(2,2),(3,2),(4,2),(2,3),(3,3)\); for \((4,2)\), only the balanced rank pair \((2,2)\) is enumerated. The total number of ordered test pairs is \(372{,}920\), and the balancing rank profile for \((4,2)\) is \((560,20160,560)\) across product ranks \(0,1,2\).

Run with Python 3 using `python check_commuting_idempotents.py`; compare standard output to `check_output.txt`. The script requires no third-party packages. It does not test extension-field arithmetic or the infinite asymptotics. The general prime-power statement is established by linear algebra and the positive Euler product, not extrapolated from enumeration.
