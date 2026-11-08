---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Fulsche–Hagger's Fourier–Weyl identity for true polyanalytic order k gives vanishing quantization iff a tempered Fourier transform is supported on the finite union of Laguerre-zero circles; for k=1 the multiplier has no zeros and quantization is injective for any bounded symbol. For k>=2 isolate roots by smooth compact Fourier cutoffs whose inverse transforms are Schwartz; Young preserves Lp. Because every Laguerre root is simple, each Fourier-localized term solves (Delta+4lambda)u=0 globally. Angular Fourier separation and smoothness at the origin force each mode c_m J_|m|(2sqrt(lambda)r); Jensen plus the oscillatory asymptotic J_m~r^-1/2 rules out any nonzero Lp mode for p<=4, including critical p=4. For p>4 average null plane waves over a root circle to obtain nonzero real bounded a(z)=J0(2sqrt(lambda)|z|), which is in Lp iff p>4. Integrating its cos^4 leading term gives exactly 3/(4pi lambda) log R +O(1) for critical fourth-power mass. No extrapolation from finite roots is used.

## originality

PASS

Best-of-knowledge comparison of the full theorem, not just its title: Bounded null-symbol construction and L1 boundary are NOT new, but the full sharp p<=4 injectivity and p>4 Bessel null witness are not contained in the inspected source statements; Fourier-restriction methods are classical ingredients. Existing theorems jointly make the threshold accessible, but the exact bounded-symbol all-k Lp equivalence with endpoint logarithmic coefficient was not stated by inspected literature. An older general Lp Helmholtz theorem could imply the uniqueness half as a special case; priority risk acknowledged.

## value

PASS

Identifies the exact Lebesgue integrability boundary at which noninjectivity first becomes possible for Hermite-window Fock localization, for every order, and quantifies the critical logarithmic obstruction. The p=4 endpoint and Bessel symbol connect Fock quantization to planar Fourier restriction and are natural mathematical invariants rather than arbitrary examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
