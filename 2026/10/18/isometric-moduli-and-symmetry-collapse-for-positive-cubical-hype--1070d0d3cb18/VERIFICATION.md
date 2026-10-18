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

# Reproducibility and limits

Run `python3 checker.py` with a standard Python 3 interpreter. The program uses only standard-library `fractions`, `collections`, `itertools`, and `math`. It executes an exact-rational finite sweep of nondecreasing weight vectors in dimensions three through six, verifies the relative-interior points supporting every coordinate facet in balanced cases, tests the unique dual linear relation, enumerates permitted signed-permutation actions in small balanced dimensions, and checks dominant-coordinate elimination.

An actual run reported `PASS` with 441 representative vectors, 417 balanced cases, 24 dominant cases, 4374 relative-interior facet witnesses, and 396 further permutation/dominance tests. The test program does not use approximate floating point arithmetic. These are finite consistency checks, **not** an exhaustive study of all real weight vectors and **not** a substitute for the all-dimensional proof in RESULT.md.

The proof is self-contained apart from standard finite-dimensional facts: facets of a polar polytope correspond to vertices of the dual, and a surjective linear isometry maps unit-ball faces and dual extreme points bijectively. The exact boundary \(2\max_i a_i=\sum_i a_i\) is included in the cubical regime. Literature checks are not an independent audit or a proof of novelty.
