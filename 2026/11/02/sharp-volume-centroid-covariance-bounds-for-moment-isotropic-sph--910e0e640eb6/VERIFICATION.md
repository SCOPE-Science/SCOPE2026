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

# Verification and limits

The analytic argument in `RESULT.md` proves the statement for all integer dimensions \(d\geq2\) and all Borel probability distributions satisfying the stated second-moment constraints. The exact-rational standalone checker `verify.py` exhausts the product sample spaces for the two extremal finite families and a nonextremal unequal simplex/opposite-simplex mixture in each of dimensions \(d=2,3\), checks the mean squared volume, third-tensor cubic contraction, squared-barycenter expectation, weighted mixed moments, the covariance identity, and both equality bounds. It uses Gram matrices only, so irrational Cartesian coordinates are not approximated.

Run: `python verify.py` (Python 3 standard library; deterministic). The finite checks do not establish a theorem in arbitrary dimensions and do not verify the historical uniqueness of the claim. Independent audit has not been performed.
