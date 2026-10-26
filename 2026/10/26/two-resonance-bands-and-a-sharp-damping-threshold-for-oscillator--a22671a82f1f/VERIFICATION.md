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

# Verification of the tree cosine phase classification

Run `python verify.py` using Python 3 standard library. The checker tests exact quadratic/discriminant identities at rational parameters and boundary identities, and builds an explicit finite rooted-tree matrix with exact rational entries. The exact negative quadratic form at \(q=2\), \(r=2/3\), \(	heta=\pi/3\) is \(-49/243\), independent of floating-point rounding.

The all-parameter theorem is established analytically using the regular-tree adjacency resolvent, its full spectral interval, and Schur-product contraction. Computational sampling and the one finite obstruction alone do not prove the universal statement. The positivity proof covers every finite set and all endpoints, but the sources inspected do not constitute an exhaustive originality proof. Independent audit has not been performed.
