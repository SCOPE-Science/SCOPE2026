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

# Reproducible computation

Run the five Python programs in `verification/` with Python 3, NumPy and SciPy. On the recorded runs SciPy 1.17.0 and NumPy 2.3.5 were used. Four full mixed-integer optimizations terminated with reported HiGHS optimal status and upper bounds strictly below the next integer; no timeout or merely feasible incumbent is treated as proof.

Shadow formulation: length nine has 715 candidate codewords, 495 output shadows, 2475 nonzero incidences and a witness of size 143; length ten has 1001, 715, 3575 and witness 201. Each solver's returned binary point is rounded and tested against the entire constraint matrix. Independently generated conflict edges number 4950 and 7150 and give the same two integer optimal objectives. The combinatorial script proves the generated graphs coincide exactly and verifies the zero-syndrome witness.

Numerical dual-bound rounding is separated by almost one unit from the next forbidden integer, reducing but not eliminating numerical robustness risks. Solver soundness and exact branch traces are not independently certified. The computation establishes no result for lengths above ten.
