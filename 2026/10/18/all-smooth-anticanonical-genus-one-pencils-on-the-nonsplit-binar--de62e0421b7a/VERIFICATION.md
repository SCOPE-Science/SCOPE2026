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

Reproduce the complete finite calculation with `python3 verify.py` from the package directory, using Python 3 and SymPy. The source checks every one of the 511 quadratic section masks modulo the defining equation, every smooth pencil, all 120 rational quadric automorphisms, and all 36 pencil orbits. Geometric smoothness and base-scheme reducedness are decided by exact Gröbner unit-ideal tests on four projective affine charts. The rational-point bound also has a direct proof from the 15 reducible sections vanishing on the rational five-point ovoid. The complete expected orbit list and numerical totals are in `data/expected.json`.

Executed checks returned three PASS lines: exact 511-section and 4,020-pencil coverage with 36 orbits; exact smoothness/reducedness and the ovoid kernel; and the extremal degree pattern \((1,1,1,5)\). The executable uses exhaustive finite search and algebraic criteria, not finite-extension sampling. The source code and output data allow a later independent replay, but **no independent audit has been performed**. The field is only \(\mathbf F_2\); no statement for other fields is certified.
