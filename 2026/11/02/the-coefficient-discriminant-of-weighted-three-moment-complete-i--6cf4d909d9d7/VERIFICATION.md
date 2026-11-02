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

Three exact finite-field enumerations were executed using the standalone standard-library script `verification.py`: prime 5 with weights `(1,4,1,1,1,1)` and `(1,1,1,1,1,1)`, and prime 7 with weights `(1,6,2,3,4,6)`. Each exhaustively enumerated rational projective points, identified points on the three power sums, calculated the Jacobian rank by modular row reduction, and matched the singular support against every proper zero-weight subset. All comparisons returned `matches: True`, followed by `VERIFY_OK`.

Run: `python3 verification.py`. These checks involve only finite rational points over the stated prime fields; they cannot certify singularities over their algebraic closures or prove the universal statement. The universal conclusion is supplied by the Jacobian and quadratic-form proof in `RESULT.md`. No independent mathematical audit has been performed.
