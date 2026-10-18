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
Execute the two complete included Python files with a stock Python 3.9+ interpreter: `python verify_refinement.py` and `python verify_moments.py`. Both use only the standard library. `refinement_checks.txt` and `moment_checks.txt` record the expected stdout, which is reproduced by the scripts.

The first enumerates all vertices and disjointness edges for 42 parameter configurations in the stated theorem range, totaling 9,263 vertex instances. It computes exactly three refinement rounds and compares the resulting colours **bidirectionally** to the four-region orbit profiles; checking only the class count would not suffice. The second makes independent direct subset enumerations for 28 configurations, totaling 4,723 vertex instances. It checks the exact weighted-neighbour identity, reconstructs the triple intersection, and checks all orbit-size formulas and the coefficient total. Each script checks the sharpness case \(KG(8,3)\).

## Mathematical argument and limits
The infinite theorem follows from the explicit injectivity of \(s\mapsto\binom{n-2k+s}{k}\) in the specified range, the ordered-pair double-counting identity for the weighted neighbourhood moment, and transitive region-preserving permutations of the ground set. The finite computations corroborate rather than replace any of those arguments. No independent external audit has been conducted. Novelty against every possible earlier specialist result is not certified, and no identification theorem for arbitrary comparison graphs is asserted.
