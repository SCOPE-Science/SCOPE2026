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

The proof reduces the signed-domination condition to exact closed-neighborhood sums on the center and each clique blade. No numerical approximation is used.

`verify_signed_windmill.py` independently constructs each tested graph and evaluates the original definition on every sign labeling. It checks that the raw definition agrees with the structural criterion, that the complete weight distribution equals the product formula, and that the predicted minimum weight and number of minimizers agree.

Replay result:

`VERIFY_OK tuples=226 labelings=188952 criterion_checks=188952 coefficient_checks=893 minimum_checks=102207 max_order=11`

The exhaustive range is \(2\le r\le4\), \(1\le m_i\le4\), with total graph order at most \(11\); an additional bounded algebraic scan checks the branch-minimum comparison for larger parameter tuples. These finite checks do not prove the infinite theorem. The proof of the all-parameter statement is the exact neighborhood-sum and parity argument in `RESULT.md`.
