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

Execute `python3 verify.py` from the package directory with Python 3.9 or later; no optional dependencies are required. The program branches over all uniformly selected starting vertices and length-one neighbor outcomes, builds the resulting labeled graphs, tests the star property directly, and accumulates exact `Fraction` probabilities. It compares those probabilities with the analytic product for five starting star sizes, five rational walk-length mixtures, and eight time horizons, and performs additional exact gamma-product, telescoping and geometric-bound checks. The extracted package's checker returned `PASS 4694 exact assertions`.

The proof in `RESULT.md` establishes the infinite tail, expectation and crossover theorems; direct enumeration only checks finite cases. No external or independent audit has been conducted. The statements do not apply to general seed graphs or walks longer than one step.
