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

Run `python3 verify.py` with Python 3 and its standard library. The verifier constructs independent symmetrized internal-state tensors; evaluates the Dirichlet Mellin law using exact integer fractions; samples normalized independent exponentials using a fixed seed; compares finite-size scaled log-moments to their Stirling limits; and checks representative positive mean–typical gaps and Gaussian variance coefficients. Expected output is:

`VERIFY_OK internal_symmetrization=3 exact_integer_Mellin=162 normalized_exponential_samples=3 finite_to_limit_SCgf=12 mean_typical_variance=4`

The symmetrization check includes distinguishable, partially distinguishable and identical internal vectors. The random finite sampling and asymptotic numerical comparisons are corroboration only. The analytic proof explicitly establishes the Dirichlet identity, the full moment domain \(t>-1\), the steep limiting cumulant function needed for the large-deviation principle, the central-limit normalization, and the strict positivity of the typical–mean exponent. There is no external independent validation or publication-priority certification.
