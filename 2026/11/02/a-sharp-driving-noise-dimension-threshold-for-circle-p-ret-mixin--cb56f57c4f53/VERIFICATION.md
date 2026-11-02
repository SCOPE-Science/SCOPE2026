---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The proof is analytic. The accompanying standard-library `check.py` independently performs 377 supplementary tests of the beta moments, special Fourier multipliers, numerical Bessel integral, strict spectral inequality on representative parameters, and representative rational resonances. It was run successfully before packaging and is replayed from the embedded final package during validation.

The formula \(\rho_{r,k}=\mathbb E[\cos(k\sqrt{rh}U)]\) is derived from the exact p-Ret transition; the strict inequality for all nonzero frequencies when \(r\ge2\) follows from absolute continuity and Riemann–Lebesgue, not numerical sampling. The lack of a uniform spectral gap for \(r=1\), the total-variation dichotomy and the Poisson counterexample require genuine infinite-frequency arguments as given in RESULT.md.

Independent audit: not performed. No external certificate is claimed.
