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

The self-contained `verify.py` uses only the Python standard library. It computes the unnormalized four-row Fourier determinants by the independent Leibniz sum over all 24 permutations and compares their modulus with the six-chord factorization. It then enumerates every four-frequency subset for each ambient size from 4 through 24. The total is 53,130 distinct subsets; all match the predicted sharp maximum, optimizer gap criterion, and count.

To reproduce, run `python3 verify.py` from the package directory. The final expected line is `CHECK_OK 53130`. The checker uses floating-point complex arithmetic and checks with absolute tolerance \(3\cdot10^{-10}\), so it is a finite consistency test, not a proof for arbitrary ambient size. The all-moduli proof is the five-step strict-concavity argument in `RESULT.md`; no independent audit has been performed.
