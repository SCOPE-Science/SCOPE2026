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

A diagonal phase gauge makes all weights nonnegative, also when some are zero. For any unit vector, taking componentwise absolute values bounds its numerical-radius Rayleigh expression by the quadratic form of the real symmetrization; a real top eigenvector gives equality. The square of the norm is the supremum of quadratics with common strict convexity modulus 2 sigma_min(W−I)^2>0, since W is nilpotent. At zero the top eigenvalue starts fully degenerate, giving right slope 2(ν−1). At one, write t=1−δ. The first-order perturbation of W*W is δ(W+W*−2W*W); its compression to the top eigenspace has diagonal −2M² and off-diagonal M only between consecutive maximal source indices. The longest of those paths has L vertices, so the compressed top eigenvalue is 2M(c_L−M). To justify using the compression even at a tie, decompose a trial unit vector into that eigenspace and a complement of norm b. The unperturbed loss is at least gap·b² and the cross-term is O(δ b), giving only O(δ²) excess over the compressed first-order maximum; a unit vector in the eigenspace attains that expansion from below. Thus the left slope at one is 2M(M−c_L). Convexity gives the stated three regimes, including equality at either endpoint and strict improvement at an interior minimizer. The cases cannot conflict because ν≤M and c_L<1. For t>1, testing on a maximal source vector gives norm at least sqrt((t−1)²+t²M²)>M, so the optimum persists on t≥0; negative t could not improve the objective either since the spectral radius there exceeds 1. The displayed change of variable maps the physical interval to [0,1+a], giving the claimed scaled optimum.

## originality

PASS

The supported distinct claim is the arbitrary-weight affine-pencil trichotomy, in particular the precise endpoint test from runs in the maximal singular-source set. Do not credit the all-unit Jordan optimization, sine diagonalization of paths, or general convex norm-differentiation tools as new.

## value

PASS

The spectral-radius optimum cannot distinguish weights at all, but the exact worst-case one-pass optimum can differ for two arrangements of the same weight multiset. The theorem identifies which dependence is purely a longest-run obstruction at the nilpotent endpoint and which needs the numerical radius. This provides a useful classification for one-lag transfer without computing the full norm curve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
