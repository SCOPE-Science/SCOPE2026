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

The mathematical proof is provided in `RESULT.md`; `verify.py` independently reproduces finite examples by original graph definitions. The script enumerates all subsets for board sizes \((2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4)\), determines domination by closed neighborhoods, determines connectivity by breadth-first search on the induced rook graph, and determines inclusion-minimality by testing each selected-square deletion. Each accepted subset is also checked against the one-sided-leaf-tree structural characterization, without relying on the formula to decide admissibility. Coefficient dictionaries are compared against the proved Stirling-number formula. These tests are finite consistency evidence, not an infinite proof.

To reproduce: save `verify.py` as a UTF-8 file and execute with Python 3.9 or later: `python3 verify.py`. The script requires only Python standard-library modules and raises an exception on a mismatch. No unproved complexity claim, third-party certification, or independent audit is asserted.
