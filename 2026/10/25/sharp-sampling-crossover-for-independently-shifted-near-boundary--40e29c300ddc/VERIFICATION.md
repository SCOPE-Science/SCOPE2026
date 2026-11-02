---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS: Fourier aliasing of the periodic Poisson kernel P_r gives exact N-point shifted average P_(r^N)(N Theta); a uniform cell shift makes its argument uniform. Thus mean 1 and Var(A)=2r^(2N)/[m(1-r^(2N))]. In a triangular array q=r^N→1, set epsilon=1-q and L=m epsilon. At L→0, absent hits within epsilon-scaled angular core (probability O(mKepsilon)), while outer-arc expectation is asymptotically 1-2 arctan(K)/pi; then K→∞ and Markov prove A→0 in probability despite unbiasedness. At L→lambda∈(0,∞), scaling u=epsilon x and domination by 1/(1+x²) in the exact Laplace transform yields the Poisson shot noise of intensity lambda/(2pi) with mark 2/[lambda(1+x²)]; Campbell formulas give mean 1, variance 1/lambda. At L→∞, exact variance gives L² consistency and maximum normalized triangular summand O(1/sqrt(L)), hence Lindeberg CLT sqrt(L)(A-1)⇒N(0,1). The three subsequential cases prove iff L→∞ for convergence in probability/mean square; q→1 also implies epsilon~N(1-r). Independently verified Fourier aliasing numerically at 36 parameter values. Finite comparisons do not replace the weak-convergence proof.

## originality

PASS

PASS qualified: exact Poisson-kernel Fourier aliasing and randomized trapezoids are classical; Goda/Kazashi/Suzuki analyze randomized rules for fixed Gaussian-weighted Sobolev classes, while Bao et al and af Klinteberg address deterministic near-singularity correction. None of inspected results states this joint m,N,r boundary regime or Poisson shot-noise critical law with m(1-r^N) threshold, although the limiting point-process theorem is standard. Possible unindexed stochastic sampling/rare-event shot-noise result remains a material equivalent-formulation risk.

## value

PASS

PASS: A natural near-boundary analytic kernel has an unbiased yet typically zero Monte Carlo quadrature in the under-sampled regime, a nondegenerate Poisson critical law, and an exact Gaussian/consistent over-sampling transition. The sharp necessary-and-sufficient total sampling budget mN(1-r)→∞ is useful for identifying rare-spike failure mechanisms that ordinary unbiasedness and deterministic trapezoid accuracy miss. Claim deliberately restricted to independently refreshed grids and q→1, not arbitrary integrands.

The dated certificate retains the supplied scientific assessment, sources and limitations.
