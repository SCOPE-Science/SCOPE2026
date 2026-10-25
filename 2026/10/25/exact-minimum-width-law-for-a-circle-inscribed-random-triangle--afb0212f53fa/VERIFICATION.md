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
# Reproducibility and verification

Execute `python verify_inscribed_triangle_width.py` after installing NumPy, SciPy and SymPy. No external data files are needed. The program must print `ALL_RANDOM_INSCRIBED_TRIANGLE_WIDTH_CHECKS_OK` upon success.

The verification checks the normalization \(12/\pi^2\) of the ordered simplex, exact symbolic moment identities, and a direct Cartesian reconstruction of the minimum altitude independently of the cyclic-gap expression. It independently integrates the first two moments numerically and compares the complete CDF at eight thresholds against 450,000 arclength-uniform samples. The limiting endpoint coefficients are tested against direct CDF quadrature.

The proof uses exact angular geometry and two asymptotic rescalings; finite numerical tests and symbolic antiderivatives corroborate but do not prove unseen parameter ranges. The numerical tolerance and pseudorandom seed are visible in the standalone script. The claim does not assert independent validation.
