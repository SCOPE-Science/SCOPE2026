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

The proof is symbolic and valid for arbitrary finite order. A separate exhaustive checker supplies a finite stress test. It generates every canonical connected chain-graph degree profile through order \(10\), computes open-neighborhood twin classes, and for every initial subset runs the skew color-change rule directly. It then compares that result with the criterion that at most one white vertex lies in each twin class.

The same checker independently multiplies the class factors \(x^{|T|}+|T|x^{|T|-1}\), compares every coefficient with direct enumeration, and checks the least exponent and the number of minimum sets. The recorded run was:

`VERIFY_OK graph_profiles=511 subset_checks=349524 coefficient_checks=5119 max_order=10`

Finite enumeration is not used as a proof for arbitrary order. The general correctness rests on the stalled-twin necessity argument and the nested-neighborhood induction given in RESULT.md.
