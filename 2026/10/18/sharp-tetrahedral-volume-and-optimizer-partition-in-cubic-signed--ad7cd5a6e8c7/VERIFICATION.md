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

# Reproduction and limits

Run `python3 CHECK.py` using Python 3.8 or later and its standard library only. The program constructs the 48 signed-permutation orbit vertices as integer affine expressions in a real parameter, checks all \(\binom{47}{3}=16215\) triples after fixing one vertex by symmetry, and establishes the exact coefficient bounds \((16,48,64,32)\). It also establishes one anchored equality case, twelve orbit images, their exact partition of the 48 vertices, two opposite-edge length classes, and the centered-zonotope volume coefficients.

The finite check is exhaustive because every vertex quadruple can be carried by a signed coordinate permutation to one containing the chosen anchor, and every remaining three-element subset is enumerated. Since the coefficient inequalities are over integers and the parameter is positive, they imply a bound for **every real** \(q>0\), not merely sampled parameters. The nonvertex exclusion, derivative factorization and single-positive-root argument are proven explicitly in `RESULT.md` and should be reviewed as mathematical arguments rather than inferred from a test run.

The program was executed successfully from the recorded standalone file. Its output is a reproducibility check, not evidence of independent review or comprehensive historical-priority certification.
