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
# Verification

The mathematical proof has two independent halves. The upper bound is the height-window argument in Lemma 5.2 of arXiv:2610.05384v1. The lower bound is an explicit path family in a height-\(2n\) subtree: traverse both root children while replacing each bottom cutoff vertex by its \(a\)-jump. This gives exactly \(2L_{2n-2}\) edges and visits only one grid height, so it has no crossing.

The bundled `verify.py` reconstructs the graph directly from the recursive word and tree-vertex definitions. It computes longest crossing-free paths by dynamic programming over the allowed single grid height. The recorded run verifies the exact maxima for \(1\le n\le6\) at \(N=2n\), and for \(1\le n\le4\) at \(N=3n\), and ends with `VERIFY_OK`.

The finite computation is not an exhaustive proof for arbitrary \(n\). The infinite proof is the upper bound plus the explicit construction. The exactness conclusion is only about the graph-theoretic crossing threshold. The smaller exponent in the nilpotency theorem is a uniform consequence of that threshold and is not asserted to be the exact nilpotency index of every represented polynomial.
