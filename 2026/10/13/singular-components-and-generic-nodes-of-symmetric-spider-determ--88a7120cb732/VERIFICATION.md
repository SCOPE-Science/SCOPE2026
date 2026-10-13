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

# Reproducibility and scope

Run `python3 spider_checker.py` from the directory containing that file, using Python 3 and its standard library only. Compare every output line against `spider_checker_output.txt`. The finite-field loops enumerate 218,700 assignments of values in `{-1,0,1}` in characteristic 101 for the indicated small spider shapes, comparing exact modular rank with the proposed union of equations. The rational-witness stage checks exact nullity two and a rank-three map to quadratic forms on its kernel for every claimed component of five small shapes. Neither finite enumeration nor rational witnesses prove the infinite family.

The mathematical argument in `RESULT.md` proves the rank criterion, decomposition with all zero-edge strata, primeness and degrees, generic transverse nodes, and normality for every complex spider satisfying its stated assumptions. The unreduced Jacobian scheme away from generic component points, larger tree classes, and singularities at intersections remain unproved.
