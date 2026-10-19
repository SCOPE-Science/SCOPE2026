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

The proof is unrestricted in positive integer Hermite order, while the standalone reproducibility checks are finite. Run `python verify_all_orders.py` in a Python 3 environment with SymPy and mpmath; its actual output is provided in `checker_output.txt`.

The checker evaluates an exact symbolic Laguerre-ratio differential identity for orders one through twelve, isolates the critical-polynomial roots for those degrees, independently integrates the original STFT for ten test points spanning orders one through five, verifies the degree-two exact threshold, and samples threshold counts through order seven. Its greatest defining-integral discrepancy was below 1e-45. The exact proof of all-order uniqueness of critical points is the polynomial degree plus Rolle argument in `RESULT.md`, not the numerical checks.

At a fold, the real Jacobian is rank one, with nonzero radial second derivative and nonzero angular imaginary derivative; no false assumption that its Taylor vanishing order is two is made. Counts are distinct zeros including the equality thresholds. The oriented complex-plane index convention is explicit.

External publication priority is not independently certified.
