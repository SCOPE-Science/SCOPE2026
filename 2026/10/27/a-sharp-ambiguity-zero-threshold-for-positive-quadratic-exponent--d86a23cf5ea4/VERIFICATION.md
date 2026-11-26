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

Use evenness in delay and conjugation at opposite frequencies. For T≥0 shift the integration variable by T/2; the lower support endpoint is then zero, and integrating each monomial of (1+d(v+T)^2)(1+dv^2) against exp(−zv) gives the stated quartic divided by z^5, z=2+iω. At T=0 its z²-roots are −2d±2i√5 d, giving real part magnitude √[d(√6−1)] for z and hence exactly d_* and the stated angular frequency at the crossing. At d=0 the transform is an elementary nonvanishing reciprocal times a phase. Independently expanded the imaginary-axis test of Q(s)=P(s+2): writing its coefficients as a_4,…,a_0, positive coefficients rule out s=0 and at s=iω with ω≠0 its imaginary part forces ω²=a_1/a_3. Substitution into its real part gives exactly −Δ_3/a_3². Reconstructing from the integral integrand recovers all seven coefficients in the record. For 0<d≤d_*<3 the constant is nonnegative and positive-degree coefficients are positive by the displayed d²<3d and d³<9d bounds. This proves no nonzero-delay zero through the threshold, independently of the stronger Hurwitz conclusion. For d>d_* the rightmost real part starts above 2 and tends to zero, since the normalized quartic tends to z²(z²+2d) with fixed degree and nonzero leading term. The rightmost real part is continuous, so crosses 2 at a positive delay; a positive-coefficient polynomial cannot vanish at z=2. This gives the advertised pair and its delay reflection, without asserting a count. The pure quadratic endpoint has numerator 2T²z²+12Tz+24, stable for T>0 and constant at T=0. Exact symbolic reconstruction and critical-root substitution were run independently; the frozen quadrature and root examples were inspected, not treated as proof of infinite-parameter assertions.

## originality

PASS

Credit is confined to the sharp mixed-window threshold, exact threshold pair and universal existence of nonzero-delay zeros above it. The pure-window endpoints, ambiguity/STFT correspondence, polynomial integration and stability criteria are known. The inspected prior statements do not settle the sign transition for this positive mixture.

## value

PASS

This is a concrete sharp failure of closure under positive addition for zero-free self-ambiguity in a natural minimal causal family. The endpoints are individually zero-free; identifying where cancellation first occurs and proving off-axis delay zeros at every larger weight materially strengthens a single example or a finite parameter sweep.

The dated certificate retains the supplied scientific assessment, sources and limitations.
