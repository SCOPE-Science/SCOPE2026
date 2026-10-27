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

# Reproducibility and boundaries

Execute `python3 verify.py` from the package directory with Python 3. No third-party dependencies or online services are required.

The finite checker implements the weighted minimal-power divisor coefficients and the candidate sparse-convolution coefficients by separate prime-factor formulas. It then independently reconstructs the convolution through divisor-multiple accumulation. For \(r=2,3,4,5\), all integers through 2500 are compared using Python's exact `Fraction` representation: 10,000 coefficient cells. It checks eight selected complete summatory ranges per parameter (32 total), and the local Euler factors at the first 25 exponents per parameter (100 total). Expected output:

`VERIFY_OK independent_dirichlet_coefficient_cells=10000 full_summatory_checks=32 local_euler_checks=100 exact_fractions=PASS finite_only=YES`

The checks verify neither the general primewise identity for infinitely many exponents nor the classical Selberg--Delange theorem; both are justified in `RESULT.md`. The analytic product convergence and strict positive discrepancy are established by mathematics, not extrapolated from finite data. Independent external audit has not been performed.
