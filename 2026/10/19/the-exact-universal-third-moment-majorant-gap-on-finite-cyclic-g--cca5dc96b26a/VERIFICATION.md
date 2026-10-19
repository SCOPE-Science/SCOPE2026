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

# Reproducibility and limits
Run `python3 artifacts/verify_majorant_gap.py` with Python 3. The program uses standard-library integer arithmetic (`math.isqrt`, `math.factorial`, and `fractions.Fraction`), not floating-point comparisons, for every certified inequality. Its proof obligations are: exact error bound on a 30-term Machin arctangent expansion for \(\pi\), error below \(800\cdot10^{-30}\) for a degree-forty-four cosine expansion, error below \(50000\cdot10^{-30}\) for each difference of cubed moduli, finite strict inequalities on 124 distinct orders, and an independent order-1000 bound.

The script's expected output ends with `VERIFY_OK exact-integer trigonometric enclosure, all finite orders and continuous bridge`. The infinite conclusion uses the separate analytically proved \(18420/N^3\) Fourier alias bound, not numerical extrapolation. The order-ten value follows from exact algebraic trigonometric identities given in RESULT.md and is not inferred from decimal calculations.

Independent scientific validation has not been performed. Complete primary-text review of the 1996 discrete-uniform thesis and 2026 continuous-conjecture paper was unavailable. The certificate establishes only the stated fixed-support, cubic-power norm gap.
