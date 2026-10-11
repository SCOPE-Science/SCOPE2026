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

# Reproducibility and proof boundaries

Run `python3 verify.py` with Python 3 (standard library only). The program exhausts 3024 generic normals with coordinates in `{1,...,8}`, comparing edge crossing counts to the coordinate-dominance dichotomy. It independently draws 50,000 fixed-seed four-dimensional Gaussian normals to check the approximate frequency of the eight-vertex event against one third.

The proof of the complete generic dichotomy is combinatorial and is given in `RESULT.md`. The measure calculation is analytic, using the Cauchy distribution for a ratio of independent normal variables. Finite enumeration and sampling do not prove either universal combinatorial quantifiers or exact probabilities. Exceptions comprise a union of codimension-one normal sets and have zero Haar measure.
