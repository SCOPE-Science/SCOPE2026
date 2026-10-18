---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Decodability from a binary linear encoder rowspace R at receiver i is equivalent by finite-dimensional duality to existence in R of an index-i-one vector supported in {i-1,i,i+1}; this is exact for the stated five-receiver C5 scalar unicast instance. Independently enumerated ALL 1,31,155,155,31,1 subspaces of F2^5 by dimension 0..5 and applied this criterion. Valid counts by dimension are 0,0,0,20,16,1, proving scalar minimum length3 and exactly20 row-space classes. Full D10 action on the twenty yields four size-five orbits with stabilizer2; each has a distinct Hamming weight enumerator. |GL(3,2)|=168 bases per rowspace, so precisely3360 full-rank 3x5 matrices. Submitted second 4^5 fitting-matrix census and source representative bases were inspected; independent subspace/D10 calculation verified the key counts without trusting logs. This is an exact finite proof, not a partial search.

## originality

PASS

Classical Bar-Yossef et al. graph minrank theorem already determines length3 for C5, and Ong establishes linear optimality for up-to-five receiver instances. Neither scalar optimum number logically determines how many optimal rowspaces or symmetry stabilizers exist; inspected bibliographic sources do not state the exact count20/four orbit list. Chlamtáč–Haviv semidefinite minrank and Esfahanizadeh et al. matrix completion treat general optimization algorithms, not an enumerated binary optimizer layer in accessible material. The full classic primary manuscripts could not all be examined; priority risk remains especially for published supplemental tables.

## value

PASS

The pentagon is the canonical smallest odd-hole index-coding instance, where minimum codelength alone is classical. Full equality-layer classification of binary scalar optimizers is a natural finite extremal problem: 20 distinct output-basis classes and 4 dihedral orbits with different weight enumerators distinguish genuine codes rather than arbitrary matrix presentations. This is motivated independently of claiming a better broadcast rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
