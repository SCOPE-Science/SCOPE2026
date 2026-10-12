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
# Reproducible finite verification

Extract `checks/verify.py` into the indicated relative path and run `python3 checks/verify.py`. The program requires only Python 3's standard library, and independently solves absorbing-generator Poisson systems over rational numbers. It verifies 385 exact-rational threshold/KKT systems and 100 independently solved exact-rational hitting-time systems, then checks 1,815 feasible normalized random price allocations and the explicit price triple \((1,3,100)\). Program failure raises `AssertionError`; success prints `VERIFY_OK` and a count summary.

These tests are supplementary. Universal validity is established by the formula for the forward directed path, the weighted Cauchy--Schwarz inequality, the strict-concavity threshold derivation, and equality construction. The tests neither exhaust positive real parameters nor certify historical novelty or independent validation.
