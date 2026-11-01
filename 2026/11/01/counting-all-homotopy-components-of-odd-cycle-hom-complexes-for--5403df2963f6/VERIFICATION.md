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

Run `python3 theta_hom_checker.py` with Python 3 and the standard library; it requires no external packages and performs complete finite colorings, recoloring adjacency, and finite CW-cell enumeration for the listed test cases.

The saved execution output `theta_hom_checker_output.txt` ends with:

`ALL_PARALLEL_PATH_HOM_CASES_PASS cases=19 colorings=6950 cells=51624`

Each verified connected component is compared to the integer-interval winding-class formula, and its Euler characteristic matches the predicted contractible or circle type. Examples include \(q=5\), path lengths \((3,4,6)\), giving two circular and ten contractible components, and \(q=7\), lengths \((2,3,4)\), giving an empty Hom complex. These are finite regression checks; the universal theorem is proved by signed-walk recoloring connectivity and the published directed-cycle criterion.

The present review is non-independent and should not be represented as external certification.
