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

# Verification of the Bayesian last-success posterior phase theorem

The proof is a finite-horizon proof with explicit real-shape quantifiers. Its critical steps are: (1) predictive Beta-binomial probabilities for every binary path; (2) normalization by the no-future-success probability to establish unique strict monotone crossings; (3) two assertions propagated jointly by induction over remaining horizon; (4) a strict first-success-branch improvement below the quadratic boundary; (5) solving two exact inequalities when two trials remain. No asymptotic, external certificate, or simulation is used to close these steps.

## Reproducible finite checks

Run `python verify_bayes_last_success.py` in the folder containing this document and the program. The program uses only the Python standard library, computes all probabilities as rational numbers, and prints:

`PASS: 1181 exact finite assertions, including exhaustive stopping-policy checks`

The suite independently evaluates every deterministic success-only policy for remaining horizons 1–4 in selected posterior states, compares with Bellman dynamic programming, checks the quadratic boundary and strict gap for horizons 1–7 on integer grids, tests several rational values, and tests the two-trial algebraic inequalities. Exhaustive enumeration at small horizons is not exhaustive over all horizons or positive real posterior shapes. The universal conclusions rely on the displayed mathematical argument.

## Limitations

No verification outside the stated Beta mixture, fixed finite horizon, or single selection right is claimed. Independent audit has not been performed.
