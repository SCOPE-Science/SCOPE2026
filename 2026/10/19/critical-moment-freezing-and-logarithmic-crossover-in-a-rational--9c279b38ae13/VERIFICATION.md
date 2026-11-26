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

The normalized stationary law follows from U=√[β(1−X)/X] being standard positive half-Cauchy. For its symmetric signed version of scale τ=β^(−1/2), the Cayley coordinate has Poisson pole p=(1−τ)/(1+τ); the Nth power has pole p^N by its Fourier coefficients. The Chebyshev map acts by absolute tangent multiplication followed by division by α. The resulting scale ratio is precisely the binomial quotient for α, including either sign of p. Expanding that quotient gives β(N−α)→K_N. For the low moments, domination by U^(2q) gives the secant constant; for the high moments, in g=1−x the rescaled density is bounded by g^(−3/2)(1−g)^(−1/2)/π, and the limit is the asserted beta integral. Independently, for q=1/2+s/log β, π√β M_q is the integral of g^(s/log β)(1−g)^(−1/2)/[g+(1−g)/β] on (0,1). The part below β^(−1) is O(1) uniformly for bounded s by integrating βg^(s/log β). Above β^(−1), replacing the denominator by g costs O(1) by the bound β^(−1)/g² away from the integrable endpoint g=1; dropping the (1−g)^(−1/2) factor also costs O(1) since its difference from 1 is O(g) at 0. The integral left is (log β)∫₀¹ exp(−st)dt, proving uniformity including s=0. The exact M₁=1/(1+√β) also follows by partial fractions in the Cauchy integral (at β=1 by continuity). This is a fixed-N stationary result, not a statement about temporal correlations or uniqueness. Frozen check.py and VERIFICATION.md were inspected, not executed.

## originality

PASS

Credit the known map, density and parameter branch, the standard half-Cauchy transform, and the fixed-order hypergeometric endpoint regimes. The supported distinct part is the calibrated compact-uniform moving-order gap-moment asymptotic for this stationary family. The exact connection formula provides an alternative route but is not itself a uniform moving-order asymptotic. No inspected statement establishes that joint asymptotic for this law.

## value

PASS

At the natural stationary concentration endpoint, the typical gap is order β^(−1), but the mean gap is order β^(−1/2). The normalized critical window quantitatively joins the typical-scale and rare-excursion observables, including the logarithmic enhancement, rather than merely renaming the known invariant density. The moving-order uniform estimate and calibrated comparison of observables are the contribution; this is not a claim of a general response theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
