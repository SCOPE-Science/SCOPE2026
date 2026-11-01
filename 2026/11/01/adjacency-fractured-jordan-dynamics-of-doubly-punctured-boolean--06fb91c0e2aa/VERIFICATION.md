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

# Reproducible verification

Run `python3 verify_twopuncture.py` in a directory containing that standalone script (only the Python standard library is needed). Expected successful final status is `TWO_PUNCTURE_JORDAN_ALL_CHECKS_PASSED`. The program constructs each twice-punctured cube from binary coordinate labels, performs independent characteristic-two bit-matrix multiplication and Gaussian rank elimination, and compares its successive nullities with those implied by the stated Jordan forms. It also independently iterates all labelled initial states for the smaller cubes, comparing measured entry times and primitive periods to the stated exact formulas.

The recorded run verified 35 dimension-distance pairs in dimensions two through eight, totaling 3,514 matrix coordinates across cases; 65,736 state histories were independently checked by direct iteration in dimensions two through four. The verified output is supplied in `verification_output.txt`. In the full proof, the critical exhaustive-infinite argument is not the finite test, but the rank-half square-zero decomposition and two-rank perturbation identities established in `RESULT.md`.

**Unproved limits:** no claim is made about more than two deleted vertices, characteristic-odd fields, nonlinear excitable dynamics, or novelty against papers unavailable in full text. Independent audit: not yet performed.
