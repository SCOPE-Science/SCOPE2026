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

# Verification record

Exact standard-library calculations executed successfully using `code/enumerate_by_pairs.py` and `code/verify_rref.py`. The reference output is `data/reference_output.txt`; the latter program's generated catalogue matches `data/census_catalogue.json` as parsed JSON.

The pairwise-pencil implementation enumerates \(781\) projective binary quartics, checks \(600\) squarefree forms by affine Euclidean gcd and the point at infinity, and identifies \(20\,306\) distinct pencils by their six normalized projective members. It finds \(3\,820\) all-squarefree pencils, with base-divisor counts \(3710,70,40\) at degrees \(0,2,3\).

The RREF implementation independently enumerates all coefficient planes, checks squarefreeness by the exact quartic invariant identity, computes all \(120\) source projectivities through the binomial substitution formula, and classifies the \(3\,820\) pencils into \(47\) disjoint projective orbits. It independently computes the common-factor distribution and the \(14\) Frobenius splitting profiles by irreducible polynomial division. All tabulations agree.

All loops terminate after finite exhaustive ranges. The scripts are intended for replay on ordinary Python 3; no packages outside the standard library are required. This record is not an external audit or formal theorem-prover certificate.
