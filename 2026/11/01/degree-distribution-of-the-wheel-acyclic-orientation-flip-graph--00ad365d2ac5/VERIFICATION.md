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

# Reproducibility of the wheel acyclic-orientation degree theorem

The self-contained scripts use Python 3 with only standard-library modules. Run `python3 verify_direct.py` to independently generate and test every acyclic orientation of the wheel with rim length \(3\le m\le8\). The program checks DAG status by topological sorting, tests an individual reversal by deleting its directed arc and checking residual reachability, and verifies all printed degree histograms and both total-count checks. It does not use the proposed formula to decide whether an orientation or a flip is legal.

Run `python3 verify_formula.py` for an independent exact arithmetic check of the coefficient formula against a cyclic-run-composition calculation for \(3\le m\le12\). This script also tests the Lucas-number minimum-degree count, maximum-degree multiplicities, total orientations and total exchanges.

Observed terminal results:

`ALL_DIRECT_WHEEL_CHECKS_PASS`

`ALL_FORMULA_WHEEL_CHECKS_PASS`

All checks completed on the included files. These experiments exhaust the **stated finite ranges only**; the mathematical proof in `RESULT.md` establishes the result for every integer \(m\ge3\). Independent external scholarly validation has not been performed.
