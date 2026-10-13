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

The analytic proof establishes the classification for all integers \(n\ge3\) and \(k\ge1\). The finite program `verification.py` independently implements the graph and the generalized propagation rule rather than calling the closed-form classifier as its simulation oracle.

It exhausts every subset for \(3\le n\le8\) and every \(1\le k\le n\), totaling \(669888\) subset/parameter checks. For each of the \(33\) parameter pairs it also compares the entire cardinality distribution with the coefficient formula and checks the predicted minimum value and number of minimizers. Finally it explicitly checks the \(n=5\), \(k=1\) mixed-pair counterexample to the published \(n-k\) formula.

Expected output:

`VERIFY_OK n_range=3..8 parameter_pairs=33 subset_checks=669888 minimum_checks=33 counterexample=n5_k1_mixed_pair`

These computations are finite corroboration only. They do not certify untested orders or replace the analytic proof. The direct full PDF of the 2019 comparison source was not locally retrievable because of interactive publisher verification; that access limitation does not affect the proof or the checker.
