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

Run `python3 verify_poisson.py` with Python 3.9 or later. No third-party packages or datasets are required.

The script computes coefficient arrays through outbreak size 32 via two separate exact finite expressions (the logarithmic derivative of the generating function and the conditional-Poisson sum), evaluated at 67-digit Decimal precision. It also compares generating-function values on a grid and checks the signs of the illustrative tail differences. The actual packaged script passed 646 checks.

The universal tail limit is justified analytically in `RESULT.md`: the upper bound is Chernoff's inequality applied at \(z_n=(\log n-2\log\log n)/d\), and the lower bound is the single event with first-generation count \(\lfloor n/\log n\rfloor\) and remaining cases in generation two. Stirling estimates match the \(-n\log\log n+n\log d\) log probability. Numerical checks are not an infinite proof.

No separate independent audit or validation has been performed. The results assume a Poisson branching reservoir, not a finite-susceptible epidemic.
