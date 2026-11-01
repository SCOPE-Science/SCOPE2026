---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Reconstructed the 105-pairing Isserlis polynomial E=3+6a²+12b²+12c²+48abc+24b²c². For abc≥0, D≥Q. For abc<0, PSD gives x²+s+2xt≤1, s≥2t; minimizing D/Q allows s=2t (y=z=√t), preserving PSD and equality only at y=z when relevant. With u=t and 0≤x≤1−2u, optimize R=1−4u(2x−u)/(x²+4u); the x-stationary/boundary switch u_c=(9−√57)/12 is checked, interior branch decreases and boundary branch has derivative 8(4u²+5u−1)/(4u²+1)². Unique global minimum occurs at u*=(√41−5)/8 and x*=1−2u*, yielding C*=(7−√41)/2. All degeneracies (Q=0 independence, a/b/c zero, t≥2x, singular/PD) handled; nonzero equalities are rank-two PSD with abc<0 and |b|=|c|=√u*, |a|=x*. Independent checker symbolically verified exact identities, all 105 Wick pairings and the branch/critical-point identities, plus 30,000 finite random PSD tests. Finite tests are corroboration, not universal proof.

## originality

PASS

Best-of-knowledge originality: the full sharp quantitative bound with anisotropic quadratic correlation remainder for the first unequal Gaussian exponent case survives direct implication tests against the primary qualitative all-exponent Gaussian-product results and the direct bivariate quantitative source. Qualitative nonnegativity plus equality only at independence cannot determine a uniform strictly positive sharp weighted-correlation coefficient. Searches did not establish equivalent prior coverage, but unsuccessful searches are not novelty proof; the full 2025 paper and older elliptope-polynomial literature are residual risks.

## value

PASS

The exact target is naturally the first unequal positive-integer exponent profile (1,2) after the all-square 3D Gaussian product case, directly motivated by a published question on quantitative 3D GPIs. It establishes a globally sharp positive stability factor relative to the exact second-order anisotropic covariance scale, identifies rank-two extremal geometry, and distinguishes sharpness over singular PSD from unattained nonzero equality under strict PD. The exact coefficient and equality locus are not obtained from the qualitative 3D positivity and may guide comparison for higher exponents; no general exponent theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
