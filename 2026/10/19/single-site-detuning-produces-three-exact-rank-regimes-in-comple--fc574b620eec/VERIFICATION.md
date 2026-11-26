---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Grouping by distinct eigenvalues gives the sum of squared Frobenius norms of E_λ diag(x) E_λ as the quadratic form of the mixing matrix; no degenerate eigenspace may be split. For τ≠0 put p=a−1. The cell-constant subspace on the marked singleton, p unmarked vertices, and b vertices has determinant −τpb, so the zero spectral projector is exactly 0⊕P_p⊕P_b. In a size-s cell the zero-projector compression implies x_i+x_j=0 for each pair, forcing zero when s≥3, allowing exactly a contrast when s=2, and giving no constraint when s=1. Vanishing of all compressions also implies tr(diag(x)H_τ)=τx_w=0 and tr(diag(x))=0. These trace identities kill the marked coordinate and the possibly singleton unmarked coordinate (the other cells already have zero sums). Conversely a surviving size-two contrast has zero mean on each cell, so kills compression to every bright eigenspace and to the dark space. At τ=0 the dark space instead decomposes over the original two parts, each of size at least two; the same pair tests and zero-cell-mean sufficiency give exactly the two possible original part contrasts. Thus the change is +1 for a=2, −1 for a=3 and 0 otherwise, for every b≥2; b=2 keeps the same contrast. The frozen alternative intensity proof is valid: the bright quotient is irreducible tridiagonal after permutation, and the diagonal moments of powers 0,1,2 have determinant −τb. The reported 100 exact commutant tests were inspected, not reexecuted; the proof covers all real potentials, including the distinct τ=0 collision.

## originality

PASS

The strongest inspected general mixing method and the explicitly marked balanced biclique search family are prior ingredients, not the joint all-real-mark, all-size exact kernel and rank-change theorem. The relevant indexed exact rank laws concern different graph families. The assessment is bounded to the new kernel/transition statement, not the general compression method or the ordinary biclique spectrum.

## value

PASS

A single tunable site potential in a standard graph family can raise, lower or leave unchanged the rank of the long-time transition statistic, and the law identifies the exact vectors rendered invisible. In particular, increasing the number of distinct bright spectral components can lower rank by creating a two-vertex dark-cell contrast. The all-real nonzero result rules out additional exceptional marks. It is more informative than either a spectral list or one numerical rank change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
