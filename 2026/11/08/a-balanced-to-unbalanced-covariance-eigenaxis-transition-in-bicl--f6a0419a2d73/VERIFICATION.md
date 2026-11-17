---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Stable sets are precisely 2^p+2^q−1 distinct 0–1 vertices in one part or the other. Direct indicator moments yield Σ=(a/2 I+(a/2−a²)J, −ab Jcross; symmetric B block). Orthogonal contrasts have a/2 and b/2, while remaining modes are exact eigenvalues of 2×2 L. Its strictly negative offdiagonal gives simple λ+ larger than either contrast and opposing signed principal-axis blocks. For p=q=k, explicit diagonalization gives λ−=a(1−k/N)/2<a/2; for p>q, the exact determinant det(L−bI/2)=qb[(2^p−1)(2^p−2^q)−p·2^p]/(8N²)>0 and positive first leading minor imply λ−>b/2, so full least eigenspace is B contrasts. Independent exact rational/SymPy evaluation checked this determinant and eigenordering for all 121 profiles 2≤p,q≤12. Scaling a→1/2, b~2^{q−p−1} confirms λ+→1/4 and κ~2^{p−q}. Finite experiments corroborate rather than replace the symbolic inequalities.

## originality

PASS

Best-of-knowledge distinct uniform **discrete vertices** covariance theorem. The closest previously published complete-bipartite inertia result samples uniform **interior volume**, yielding a different transition at |p−q|=1/2 and bounded balanced κ→4. Stable-set skeleton and extension-complexity articles do not assert Euclidean discrete vertex sampling covariance. A general Bernoulli-mixture covariance identity might allow easy rederivation but no inspected source states this sharp global eigenspace classification.

## value

PASS

Complete spectral classification of a natural graph polytope under a canonical discrete vertex distribution (uniform stable sets), and a sharp discontinuity in least-eigenspace dimension under a one-vertex block perturbation, are meaningful exact geometric-statistical invariants. Explicit exponential anisotropy along unbalanced families differs strongly from uniform-volume behavior; this is more than a single numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
