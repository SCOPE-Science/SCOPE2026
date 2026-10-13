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
# Verification
The analytic proof was checked against the anchor's exact zero-wave-number resolvent. The key domain fact is \(\operatorname{spec}(S^{-1})\subset[0,\tau_g]\), which makes the coefficient sequence a compactly supported positive moment sequence. The proof distinguishes the global relaxation time \(\tau_g\) from the largest relaxation time actually coupled to a chosen conserved direction.

The standalone checker uses exact rational arithmetic. It verifies the Catalan coefficient identity, the adjacent-ratio law
\[
\frac{A_{n+1}}{A_n}=4\mathfrak D-\frac{6\mathfrak D}{n+3},
\]
and its monotonicity through multiple orders. It also verifies representative Hausdorff finite differences and Hankel positivity for finite positive relaxation spectra. Those finite checks are corroborative; the all-order statements are proved analytically in RESULT.md.

The Fokker-Planck specialization reproduces the anchor's printed coefficient \(\mathfrak D_{nn10}=2\mathfrak D^2\) and the relaxation edge \(\tau_g=4\mathfrak D\).
