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

# Reproducibility and checks

Place `verify.py` and `spectrum.csv` in the same folder and run `python3 verify.py` using Python 3 standard library only. It first checks the palindrome recurrences against literal enumeration of every binary word through length nine, and reconstructs both complete de Bruijn cycle sets (65,536 possible edge pairings versus independent Euler tours) and compares them exactly. All 32 rotations of all 2048 cycles are checked by two independent dynamic programs, making 65,536 paired palindrome-length computations. Each `spectrum.csv` row is checked against the complete re-derived table. The program also verifies exact frequencies, mean, variance, and the 528 symmetry orbits under reversal and complementation.

Expected key output: `VERIFY_OK cycles=2048 pairings=65536 DFS=2048 independent_LPS_methods=2 rotation_comparisons=65536 histogram=25:76,26:114,27:1380,28:286,29:192 mean=13925/512 variance=178215/262144`. The orbit counts are additionally asserted and printed. A successful run was obtained on the complete bundled CSV and both algorithms.

The infinite-order generalization and independent historical-priority determination are not claimed. Finite exhaustive evidence here is backed by mathematical completeness of the 2-choice/vertex pairing parametrization and of the interval palindrome recurrence; it is not a substitute for those arguments.
