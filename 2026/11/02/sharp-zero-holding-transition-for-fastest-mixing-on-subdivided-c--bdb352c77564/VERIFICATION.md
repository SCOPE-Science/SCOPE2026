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

For real symmetric stochastic kernels the objective on the constants' orthogonal complement is the convex norm ||P−J||₂; automorphism averaging is legitimate even if the optimizer itself is not orbit-invariant. There are precisely two orbit weights a≤1/q and b≤1/p, with subdivision holding nonnegative throughout their rectangle. Decomposing the p×q edge-vertex array into constant, row-only, column-only and doubly centered parts yields the stated dimensions and spectra. At saturation the nonstationary constant-sector eigenvalues are 0 and −s, with s=1/p+1/q; row and column blocks have off-diagonals 1/√q and 1/√p and common diagonal pair 0, 1−s. Hence the saturated SLEM is max(F,s), where F is the positive root of x²−(1−s)x−1/p. The sign polynomial 2s²−s−1/p is negative throughout the allowed s interval for p≥3 (convex with both endpoints negative), and for p=2,q≥4 (increasing there, with value −1/8 at 3/4). It is positive in precisely the two stated exceptions. For any orbit weights the saturated F-eigenvector with entries 0 on U, t_j on V, and Ft_j on W for nonzero zero-sum t tests the Laplacian. Its squared edge differences summed in each orbit are strictly positive since 0<F<1; lowering either weight strictly reduces its quotient below 1−F. Thus saturation is uniquely optimal among averaged weights in the main range and every unrestricted optimizer has zero original holding, by nonnegativity of the averaged diagonals. In the exceptions adding a small identity component strictly decreases the unique active modulus −s, while all others have strict slack; zero original holding would average back to the nonoptimal saturated matrix. Implicit differentiation at 1/q=0 gives the coefficient p/(p+1). No unrestricted matrix uniqueness or exceptional optimum values are assumed. The frozen spectral/threshold verifier was inspected but not executed; the exact decomposition and Rayleigh argument prove the result for all parameters.

## originality

PASS

The supported distinct contribution is the two-exception original-row saturation classification (including the all-optimizer conclusion) and exact optimum in the main range, for single-edge subdivisions of complete bipartite graphs. Convexity, orbit reduction, and the eight-cycle exception as a cycle instance are not distinct contributions. The strongest inspected catalog and literature comparisons change the graph or the allowed kernel family, or give general optimization methods rather than the exact result.

## value

PASS

An exact fastest-mixing solution on this natural family decides when complete use of the original rows is optimal, even for optimizers that break graph symmetries. The two smallest exceptions isolate the competing negative mode, and the explicit formula resolves the fixed-small-part gap scale. This is more than a finite numerical minimization or an orbit count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
