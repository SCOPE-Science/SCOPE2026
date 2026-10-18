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

# Reproducibility and bounds of the checks

Run `python3 verify.py` with Python 3 and the standard library. The program uses an explicit cyclic realization of the seven Fano lines and exact `fractions.Fraction` arithmetic. It independently computes completion tails in two ways: inclusion-exclusion over all \(2^7=128\) absent-point subsets, and forward distribution propagation on at most \(128\) covered-point states. It compares exact results for each integer \(t\) from \(0\) to \(12\), checks the signed avoidance-factor counts, and checks the two known expectation constants and their difference. No external paper, private file, data download, or hidden dependency is required.

The analytic proof of positivity for **all** later integers is in `RESULT.md`. The finite computation does **not** certify an infinite collection of inequalities or absolute originality. No external or independent audit has been performed.
