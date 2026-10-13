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

The theorem was checked in two independent ways: a symbolic proof by cases and an exhaustive finite replay.

The proof uses only the following local facts. A black peripheral vertex in blade \(B_i\) has \(w_i\) white neighbors when the center is black and \(w_i+1\) white neighbors when the center is white. A full-white blade has no peripheral black vertex and therefore can only be cleared by the center. Once all nonfull blades have cleared, the center sees exactly \(fm\) white neighbors from the \(f\) full blades. These observations produce the exact conditions in the theorem without an unproved auxiliary lemma.

The packaged checker constructs \(W_{r,m}\), simulates the \(\ell\)-forcing process from every subset, compares the outcome with the claimed structural criterion, compares the complete cardinality distribution with the closed polynomial, and checks the minimum size and minimum-set count. Its tested range is \(2\le r,m\le4\) and \(1\le\ell\le rm\). The replay result is:

`VERIFY_OK parameter_pairs=81 subset_checks=2312832 polynomial_checks=81 minimum_checks=81 max_order=17`

This finite replay does not prove the infinite theorem; it checks boundary behavior and the algebraic counting formulas against direct dynamics. The proof supplies the general argument. Literature originality remains subject to the residual access and indexing risks stated in the review.
