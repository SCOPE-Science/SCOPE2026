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
The symbolic proof reduces both defining neighborhood conditions to exact counts outside each partite class. The finite checker then independently evaluates the literal graph definition on every subset of every nondecreasing complete-multipartite profile through order \(9\), for every admissible \(k\).

Replay with:

`python3 verify.py`

Expected output:

`VERIFY_OK profiles=87 parameter_checks=341 subset_checks=104892 valid_sets=28609 coefficient_checks=3000 minimum_checks=341 max_order=9`

The checker verifies three things: literal-definition equivalence with the profile inequalities, coefficient-by-coefficient agreement with the stated generating function, and agreement of the least nonzero coefficient with brute-force minimization. The finite range is not an exhaustive proof for arbitrary order; the infinite statement rests on the exact neighborhood-count argument in `RESULT.md`.
