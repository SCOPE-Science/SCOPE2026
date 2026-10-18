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

# Reproducible verification

Run `python verify.py` using Python 3 with no third-party packages. The program enumerates all unordered three-element subsets of the cyclic groups of orders 3, 4, 6, 8, 9, 10, 12, 15, 18, 21 and 24 and checks the Fourier Hadamard condition by comparing four exact modular products to the two primitive-cube-root patterns. It independently computes the predicted multiplicity from valuations, the valuation-stratum histogram, and the all-pairs product formula. It asserts exact agreement for every row triple and the complete totals. `verification_output.txt` is the saved successful output of this program.

The general proof requires no floating-point calculation, numerical singularity tolerance, or computer algebra: its nonstandard content is the root-of-unity reduction, prime-power CRT counts and exact divisor-sum factorization, each spelled out in the main proof. The executable checks finite examples and cannot establish the universal claims alone. Literature checks do not replace independent priority verification.
