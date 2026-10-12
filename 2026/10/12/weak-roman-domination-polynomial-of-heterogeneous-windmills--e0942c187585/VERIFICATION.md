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

The theorem is proved symbolically for every \(r\ge2\) with \(m_i\ge2\). Computation is used only as an independent stress test.

`verify.py` constructs each windmill from its center and clique blades, then checks weak Roman domination literally: for every zero vertex it tests each positive neighbor as a possible donor, performs the one-unit move, and tests whether the resulting positive support dominates. It compares that direct definition against the three-case center/empty-blade criterion and against every coefficient of the closed polynomial.

The tested tuples are \((2,2)\), \((2,3)\), \((3,3)\), \((2,2,2)\), \((2,2,3)\), and \((2,3,3)\). It also checks the minimum weight and its multiplicity.

Expected output:

`VERIFY_OK cases=6 labelings=31590 coefficient_checks=78 minimum_checks=6 max_order=9`

These finite checks do not prove the unbounded statement; that follows from the exact center/blade case analysis in `RESULT.md`.
