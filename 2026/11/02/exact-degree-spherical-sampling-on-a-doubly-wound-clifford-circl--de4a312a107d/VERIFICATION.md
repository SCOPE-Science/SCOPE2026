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

Run `python3 check.py` with a standard Python 3 installation. No external packages or downloaded inputs are required. The checker performs (i) a finite Jacobi-weight support computation from exact integer binomial sums, (ii) a separate exact Chebyshev/Laurent recurrence for the reproducing Gram kernel, (iii) a comparison with the stated support sets, (iv) cyclic rank comparisons for every sample count from 2 through 64 and degrees 0 through 60, and (v) explicit nonmonotonic-rank checks at 6 and 12 samples.

Observed result: PASS — 61 exact Laurent-Chebyshev/Jacobi support identities, 3,843 cyclic rank comparisons, and six rank spot checks. This is an exact-arithmetic *finite corroboration*, not a proof for all degrees or all sample counts. The infinite proof, including its two exceptional Jacobi cancellations, is in RESULT.md. No independent mathematical validation has been performed.
