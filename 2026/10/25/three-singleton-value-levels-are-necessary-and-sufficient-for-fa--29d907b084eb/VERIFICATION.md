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

# Verification and proof boundary

The standalone `verify.py` file uses only standard Python and integer operations. Run `python3 verify.py` next to the packaged files; the expected complete output is included as `verification_output.txt`. The script generates each of \(3^4=81\) complete assignments of four labeled goods to three labeled agents. It evaluates all EFX inequalities directly because every singleton utility is strictly positive. It determines integral PO by comparing each outcome with all eighty-one assignments, and asserts the precise five allocations simultaneously EFX and PO. It then reconstructs the ordered envy surpluses for pairs \((1,2)\), \((1,3)\), and \((3,2)\), checking the integer dual identity \(3d_{13}+d_{32}=-y\) and the subsequent contradiction.

The finite computation is genuinely exhaustive for **this specified instance**; it is not used as a proof over infinitely many utility matrices. The universal two-value positive side rests on Bu et al.'s published bi-valued theorem. The result does not compare fractional Pareto efficiency of its five deterministic support candidates, does not assert impossibility for ex-post EF1 or merely ex-post EFX, and does not constitute an independent audit.
