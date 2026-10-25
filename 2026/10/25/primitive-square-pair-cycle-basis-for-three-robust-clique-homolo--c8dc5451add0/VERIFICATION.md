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

# Reproducibility

Run `python3 verify.py` with Python 3 standard library. The implementation builds all elementary oriented face cycles, their exact integer exterior joins, and the simplicial boundary map; checks every join is a cycle supported on allowable four-vertex simplices; checks linear independence modulo \(2,3,5\) for ten grids \(2\le m\le n\le 5\); and checks the signed action of up to six explicit grid isometries against the face-pair permutation formula. Separately, for five small grids it constructs all valid four-vertex simplices and computes the complete third-boundary rank over \(\mathbb F_3\) directly.

These experiments check only specified finite instances. The infinite-family proof and integer primitivity are mathematical consequences of field-uniform induction, the unique-common-neighbor exterior-algebra lemma, and the known top homology rank. No independent scientific audit has been performed.
