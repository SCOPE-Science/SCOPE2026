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

# Verification details

The analytic proof in `RESULT.md` controls all odd primes, all positive rational anisotropic hopping ratios, and all positive absorption strengths. It also handles all nonresonant real ratios outside an explicit finite set. The exact finite-dimensional spectral support argument includes defective non-Hermitian Jordan blocks because their eigenvalues have strictly negative imaginary part on the bright sector.

Run `python -m pip install -r verification/requirements.txt` and `python verification/verify_prime_torus.py`. The recorded run of this packaged standalone program completed with:

`VERIFY_OK prime_sizes=5 rational_coupling_pairs=4 exact_spectrum_groups=20 Fourier_site_checks=1492 direct_loss_models=4`

The script groups Bloch energies using exact integer polynomial coefficients modulo the prime cyclotomic polynomial, then compares projector sums with the sitewise law at every vertex of its sample systems. Separate finite-dimensional matrix exponentiation checks decay in four small systems. Floating-point tolerances are stated in the program. Finite samples neither prove all primes nor certify uniqueness against unpublished prior work; the analytic cyclotomic lemma, spectral bright/dark splitting, and character-orthogonality calculation provide the general proof.
