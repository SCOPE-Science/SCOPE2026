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

The supplied `verify.py` ran successfully with the Python standard library. The saved `verification_output.txt` records the complete unlabelled-shape census and the strict-positive minimum covariance at each leaf count through thirteen. The script checks all nontrivial sample sizes up to complement symmetry. It enumerates the 135 fourteen-leaf shapes for sample size six, detects exactly one negative shape, confirms it is the caterpillar, and uses two mathematically different ways of calculating the witness moments: split indicators and actual graph pruning.

The exact witness certificate is sample count 3003, marginal sums 47619 and 55627, joint sum 882033, covariance \(-122/7007\). This is an exhaustive finite calculation supported by an isomorphism-complete generation proof; it is not an infinite-size theorem or an external scientific audit. Environmental model validity, unequal branch lengths, and empirical phylogeny uncertainty were not tested.
