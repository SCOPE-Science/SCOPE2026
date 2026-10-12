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
# Reproducibility and scientific limits

The provided standalone Python script `verify_double_stars.py` requires only Python 3 standard-library modules. From the directory containing this file and the script, run `python3 verify_double_stars.py`; its direct output has been preserved in `verification_output.txt`.

The script independently constructs each labeled double-star, checks every vertex subset for independence, and compares the resulting coefficient tuple with the closed form for all \(0\leq a,b\leq8\). Separately, it computes exact Fraction-valued Routh arrays for all \(0\leq a,b\leq15\) and verifies first-column positivity. This produces the recorded 81 exhaustive graph profiles (1,044,484 subsets) and 256 rational Routh checks.

These checks are finite and cannot establish the theorem for arbitrary parameters; the analytic argument in RESULT.md supplies the infinite proof. No outside independent validation, specialist review, or external certification is asserted.
