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

## Reproduction

Run `python3 verify_succession.py` in the directory containing the program. It uses Python's standard library only.

The executable recomputes stationary fractions from an exact rational generator linear system and compares them with the independently derived survival-product formula. For stage counts two through eight it checks the two-component peak bounds and one-component trough bounds using rational arithmetic, and calculates illustrative Shannon entropies. It reproduces the polynomial interval-sign certificates and the exact discriminant identity from fifteen integer specializations of a degree-at-most-fourteen polynomial identity.

All 49 generator/product checks, 245 inequality checks and fifteen exact resultant identities passed in the packaged script. The mathematical induction-free all-stage existence proof and its entropy bounds are contained in `RESULT.md`. Numerical exploration over finite stage counts is not used to establish the universal quantifier.

## Boundaries

The strict inequalities show existence of distinct interior maxima, not their exact locations for every parameter value. The general construction does not claim at most \(n-1\) maxima. The separate three-stage Gini–Simpson classification uses the discriminant/sign certificates and is valid for all positive rate ratios. No independent mathematical audit has been performed.
