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

Using J²=−I, the corrector is multiplication by (1−η²W₁W₂)I−ηW₂J; since z and Jz are orthogonal and have the same norm, the squared norms differ by the stated scalar multiplier. Writing W_i=a+ξ_i gives the second moments directly; the centered fourth mixed moment is v²+2(ρv)², the odd moments vanish, and expansion gives H_ρ, including the degenerate Gaussian at ρ=1. The current pair is independent of z_n, though W₂ need not be conditionally unbiased at the predictor, so the expected multiplier iterates exactly. With s=η²>0 the difference from one is s(sH_ρ−D_ρ), and H_ρ>0. Equality leaves the mean-square error unchanged, so the stability inequalities are strict. At fixed stable ρ the optimal s is D_ρ/(2H_ρ). At fixed s the factor is strictly convex in ρ, with derivative 2vs[−1+2s(a²+ρv)]; projection of its zero gives the three stated regimes, including equality at the endpoints. The witness has ρ=5/12 and factors 26437/31250, 26462/31250 and 26486/31250 for interior, independent and identical sampling respectively. For two Gaussian averages with k common observations the covariance is kτ²/B², giving v=τ²/B, ρ=k/B, and the stated strict criterion. The analytic calculation establishes all parameters; the provided code and recorded output were inspected, not executed.

## originality

PASS

The generic equal-step scalar norm multiplier, its expectation, and the sign test for stability follow from the earlier Resultary coupling-reversal result's proof. The Gaussian polynomial and noise threshold follow by substituting standard Gaussian moments, so neither the generic formula nor its algebraic sign test is credited as independent novelty. The supported distinct claim is the sharp, sometimes strictly interior correlation optimum for jointly Gaussian coefficients, with a contracting parameter regime where both endpoint policies are worse. The strongest earlier optimizations use fixed two-point laws with an affine dependence on the coupling parameter, and do not cover this nonlinear Gaussian family. Later generic formula coverage and the different Bernoulli whole-sample reuse policy do not establish earlier coverage of that optimizer.

## value

PASS

With fixed Gaussian marginals and exact minibatch overlap, greater reuse increases stabilizing second-order damping but also increases the fourth-order cost nonlinearly. It is useful to know that partially overlapping batches can strictly beat both named endpoint policies even when all three contract, rather than merely locating a crossover between endpoints. The threshold gives an exact benchmark for the equal-step algorithm under a concrete sampling design; it does not depend on the small numerical gain of the illustrative example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
