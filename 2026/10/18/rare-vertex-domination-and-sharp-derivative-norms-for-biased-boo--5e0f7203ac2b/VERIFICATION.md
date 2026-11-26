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

The coordinate garbling sends rare output probability q=a+(1-a)ρ to (1-q)a/(1-a)=a(1-ρ); its unchanged stochastic matrix is nonnegative for all 0<a≤1/2, including the swap at equality. Tensoring gives the identity simultaneously in ρ for every input. Integrating or differentiating a finite row preserves the identity and stochastic contraction holds for complex row vectors. Multiplying the kernel by μ(x) gives a symmetric matrix even for complex combinations, so the L¹ induced norm (max weighted column absolute sum normalized at the input) equals the L∞ norm (max row absolute sum). At endpoints the derivatives extend polynomially or by the chain rule in time. The channel itself is parameter-independent and remains stochastic; it is the resampling-law interpretation that the interval in the assumptions guarantees. For equal biases, each rare-start mass depends only on the level j. The derivative of (1-q+qz)^n is (n)_k(z-1)^k(1-q+qz)^(n-k); this proves the stated signed difference and vanishing above degree n. For k=1, the total variation of consecutive binomial masses padded with zeros is twice the maximal mass, also for a tied mode, a singleton mass at q=1 or n=1. Interior Hermite convergence can be checked from the score S=k!e_k(η_1,…,η_n), where η_i=(Y_i-q)/(q(1-q)) for iid Bernoulli(q). The normalized power sums of η converge for orders 1 and 2 by the CLT and LLN and vanish above order 2, giving the fixed-order coefficient limit. Distinct k-subset products are orthogonal, yielding the required uniform second moment and absolute-moment convergence. At the boundary the complementary binomial law converges in total variation to Poisson(λ), which controls the maximal atom and its integer-mode ties. The supplied exact rational verifier was inspected without execution; it checks finite row maxima, homogeneous derivative differences and peak formulas, not general asymptotics or every complex mixture. Replay paths for the all-parameter proof and corroborative checks are RESULT.md steps 1–5 and check.py in the source package.

## originality

PASS

Pass the full noise-family result with explicit simultaneous garbling and the exact higher-order correlated derivative profile. Do not credit the one-coordinate convex-order comparison, the first-chaos case, or the standalone homogeneous first-derivative profiles as distinct from the contemporaneous first-chaos treatment. Its lemma actually implies the row-norm domination by conditioning on the other coordinates of any multilinear multiplier, and the garbling can be reconstructed from the same two-point interpolation. The later all-multiplier norming result explicitly covers the norm reduction, but supplies no evidence that it preceded this record and does not give the higher-order finite-correlation binomial and Hermite profiles as its conclusion. Earlier retrieved sources do not cover that combined derivative result.

## value

PASS

The exact sharp endpoint norms concern a natural regularity question for biased product-noise operators. Their single row formula is simultaneous in heterogeneous biases and all derivative orders, while explicit higher-order formulas and Hermite constants quantify regularity beyond one spectral level or a first derivative. The first-order crossover is useful context but not the sole reason for acceptance. No sharp intermediate-Lp or moving-window all-order theorem is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
