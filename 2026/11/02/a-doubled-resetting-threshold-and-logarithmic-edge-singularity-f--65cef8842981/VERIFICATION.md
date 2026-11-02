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

The analytical statement is proved in `RESULT.md`. Execute `python verify.py` from the extracted package directory with NumPy and SciPy installed. The reviewed execution completed `PASS: 231 checks`.

The program implements the killed-walk Bessel kernel separately from the closed finite Bessel sum, uses numerical quadrature to test its renewal stationary mean against the exact stationary pair recurrence, and directly constructs and solves the full two-to-the-number-of-spins generator on six- and eight-spin periodic rings with Poisson resets. It checks the finite-ring correlation identity against those independently assembled generator solutions. Further numerical checks test the late-time Bessel coefficient and the exactly solvable zero-coupling boundary.

Universal correctness depends on the generator hierarchy, the killed semigroup image representation, positive strict derivative, the fixed-order Bessel expansion, and monotone change-of-variables of an exponential age. Computational checks cover finitely many parameters and are not exhaustive. They do not independently certify the infinite-volume theorem or its publication priority. In particular, edge asymptotics are for each fixed positive integer separation, and the nonzero-coupling logarithmic prefactor is not uniform at vanishing coupling.
