---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Independently reconstructed Edholm–Mathew (1.4c)-(1.4h) including Q=s^{1-2n}P(s,s). Exact standalone derivation of floor-block power sums with the important h=4 upper endpoint capped at t=m-1 proves all four claimed polynomial identities SYMBOLICALLY in q, with coefficient degree ≤3; independent direct coefficient comparisons hold for each 5∤n<61. Separately recalculated all 384 rational Bernstein coefficients from B_r/C_r and compared each exactly with actual BERNSTEIN_CERTIFICATE.json from pinned Git blob; all match and each is strictly positive (B minima 1841/480,29/48,119/480,83/30; C minima 107/20,77/40,81/40,289/40). Factored (x+2)(4x²+2x−1)² has nonnegative coefficient for q≥0, hence no unit circle zeros. Reciprocity and nonzero endpoints imply exactly 5 reciprocal root pairs; (s,s) lies inside H_{m/n}, and original denominator is nonzero for 0<|s|<1. No extrapolation from finite experiments.

## originality

PASS

Fresh independent literature and published-record comparisons support best-of-knowledge originality. Edholm–Mathew (2026) explicitly leaves fixed gap five open while providing the source formula; the full all-coprime difference-five positivity argument is new relative to reported gaps 1–4 and 6, published gaps 7–17, the n=1 integer-slope result and the m=2n+1 slice. Edholm–McNeal 2017 proves weaker kernel-zero existence for gamma>=2. The exact identical semantic hit is self material, never counted as independent prior evidence.

## value

PASS

The exact unit-circle behavior of the canonical rational-Hartogs diagonal Bergman numerator at fixed gap k=5 is a named natural unresolved subcase of Edholm–Mathew Conjecture 4.20; the source expressly singles it out as more difficult because φ(5)=4. The all-n four-residue strict positivity theorem and exact rational Bernstein certificate are substantial new parameter-uniform geometry, not a tiny numerical instance or a textbook formula substitution. The result determines the complete five-root count and genuine kernel zeros for infinitely many domains tending toward exponent one, without claiming the unrestricted conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
