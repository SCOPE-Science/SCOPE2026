---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Verified endpoint antiderivative and scale reduction rho=a/b: rational F=2(1-rho)P_rho(w²)/(3(w²-rho²)^3(w²-1)^3). Fresh symbolic computation independently recomputed polynomial numerator and its discriminant -108 rho³(1-rho)²(1+rho)^6Q(rho), with all 11 coefficients of Q strictly positive. For 0<rho<1 the discriminant is negative, so P has exactly two simple real roots and a nonreal conjugate pair. Signs P(0)>0, P(-rho)<0, P(-infinity)>0 locate both real roots strictly negative. Every negative root has one positive-imaginary square root; each nonreal conjugate root similarly contributes a unique upper-half-plane root, paired by symmetry. P(0)>0 and simple quartic roots ensure no w multiplicity; denominator poles all real. Four rational rho examples independently checked numerically; arbitrary parameters proved by sign/discriminant argument.

## originality

PASS

Standard Cauchy-wavelet phase retrieval describes general analytic zeros and implications for uniqueness, while rational integration and quartic discriminants are classical. The claimed additional fact is a complete, gap-uniform, exactly four-simple-zero classification of this natural two-band symmetric step input, including off-axis geometry and no collisions. Mallat–Waldspurger primary full text has general zero theory but does not explicitly determine this particular signal, and no exact equivalent source was found.

## value

PASS

A symmetric two-band indicator is a natural elementary nonconnected signal for analytic Cauchy-wavelet transforms. A uniform root-count and geometry classification across the gap ratio provides meaningful structural information about analytic zeros, independently useful as a benchmark for wavelet-zero methods; it does not assert unproved phase-retrieval stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
