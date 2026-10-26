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
# Reproducible mathematical verification

Run `python3 CHECK_PAIR_COUNTS.py` and `python3 CHECK_SUBALGEBRAS.py` from the directory containing these files. No third-party Python packages are required. `CHECK_PAIR_COUNTS.py` independently enumerates ordered pairs over prime fields of orders two and three, reconstructs their Lie spans and compares dimension/class frequencies with the formula. It also checks the projective criterion on seeded odd-characteristic samples at order five. `CHECK_SUBALGEBRAS.py` enumerates generated linear subspaces by reduced row-echelon bases, deduplicates them, and checks their isomorphism labels in characteristic two and three.

Observed output from the package source:

- Order two: 4,096 ordered pairs; rank frequencies \((1,189,834,1920,1152)\) for dimensions zero through four; 80 Heisenberg and 12 filiform distinct subalgebras.
- Order three: 531,441 ordered pairs; rank frequencies \((1,2912,38640,139968,349920)\); 324 Heisenberg and 90 filiform distinct subalgebras.
- The first program's terminal line is `N4_TWO_GENERATOR_CHECK_OK`. The second program's terminal line is `N4_SUBALGEBRA_CLASSIFICATION_OK`.

The finite tests do not prove the formulas for all prime powers. That proof is the projective-plane and generator-fiber argument in the theorem. Characteristic-two extension fields are covered mathematically, not by an exhaustive computational test.
