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

The standalone verifier `verification/verify_rooted_pd_unimodality.py` uses exact rational arithmetic and only the Python standard library. It recursively generates every rooted plane full binary shape through nine leaves using all left/right leaf-count splits, checks the Catalan counts, enumerates every leaf subset for every shape, and asserts unimodality of each variance sequence. Since each rooted full binary shape has a plane embedding, this covers all rooted full binary shapes in the stated finite range.

For the ten-leaf witness, the verifier asserts eighteen non-root edges with clade-size counts one (ten), two (five), four (two), and eight (one). It checks the exact variance sequence by direct subset enumeration and independently evaluates the clade-covariance identity for every sample size. It asserts the strict decrease-rise-decrease inequalities and returns `EXACT_CHECK_OK`.

Limitations: this verification is an exact finite result for rooted full binary unit-edge trees and uniform fixed-size sampling without replacement. It does not validate unequal edge lengths, multifurcations, unrooted PD, or any empirical dataset. Independent audit has not been performed.
