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
# Verification and reproducibility

The accompanying `verify.py` (Python 3 standard library) directly computes the two products defining the partition polynomial with rational coefficients and confirms their reciprocal symmetry. It computes zero power sums by Newton identities and compares the exact differences against the explicit exponential bound for heterogeneous rational edge parameters. It separately obtains all zero angles from the monotone Blaschke-phase equation by bisection, checks quantization and initial-angle asymptotics, and compares finite Fourier data with the predicted coupling moments.

Command: `python3 verify.py`.

Observed result on the packaged source: `VERIFY_OK rational_polynomials=10 exact_power_sum_bounds=55 numeric_fourier_cases=15 phase_roots=275`.

The exact tests cover ten finite graph sizes up to 90 leaves and moment orders at most seven. The phase tests cover five further graph sizes up to 160 leaves. These are finite consistency checks only. The unrestricted proof rests on the Blaschke-circle argument, Cauchy's bound for Taylor coefficients, and uniqueness of Fourier and Hausdorff moments. The finite test suite does not certify a general theorem independently and does not establish stability against noisy zero observations.
