---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The target square classes V_b=Σ_{h≠b}T_h are independent since their coefficient matrix is J−I with eigenvalues s−1 and −1; a zero product therefore means Euclidean orthogonality in every target part. Distinct image columns are blockwise and globally orthogonal. If a column is zero, its square shows that the sum of the columns in all other source parts is zero. Orthogonality forces them all zero, and any one of those zeros also forces the remaining columns in the initial part to vanish. Thus nonzero maps have N nonzero orthogonal columns and are invertible. The N positive projection occupancies exhaust the sum of the target block dimensions because each block fits at most its own dimension; hence each column has exactly one target block. Invariance of dim E² gives r=s. Equal squares in each source part force its columns to the same target block and norm because their squares are nonzero multiples of independent V_b; occupancy gives a bijection of parts and matching sizes. The blocks are t_b O_b. For a≠b, comparing the target block at π(b) in the square relation yields t_b O_b 1=(d_{π(a)}/c_a)t_a²1. Taking norms and using positivity gives t_b=β_a t_a² and O_b1=1. With at least three parts each two a share a third b, so all β_a t_a², and hence all t_b, coincide with t=c_a/d_{π(a)}. For two parts t₂=β₁t₁² and t₁=β₂t₂², giving the displayed unique positive cube roots. The part permutation, column norms and normalized blocks are recovered from each map; conversely the equations ensure all squares and off-diagonal products are preserved. For graph weights 1 and 1/(N−n_a), the criterion gives precisely the bipartite or equal-size cases and zero maps in both directions otherwise. Inspected the frozen rational checker without executing it. Independent replay: python3 -I /workspace/independent_reproductions.py checks the products coordinate by coordinate for two different rational reordered examples (including a Householder block fixing ones and unequal bipartite scales); both passed. These examples do not certify the infinite theorem.

## originality

PASS

The classification of all real homomorphisms for the specified positive one-weight-per-part model, including the orthogonal mixing and distinct two-part scaling, is the supported distinct contribution. The known nonsingular and sufficient regular/biregular graph cases, and the earlier conjecture, are not claimed here as new. Later catalogue records do overlap with parts of the graph isomorphism corollary; they are not evidence of earlier priority and do not cover the full homomorphism theorem.

## value

PASS

Complete multipartite graph algebras supply a natural infinite family of singular adjacency matrices whose twin classes admit real continuous orthogonal mixing. Determining every morphism and its permissible block scalings resolves considerably more than existence, and in particular supplies the zero-map conclusion in a published conjecture’s singular regime for this family. The separate bipartite case is forced by the multiplication equations, rather than an arbitrary cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
