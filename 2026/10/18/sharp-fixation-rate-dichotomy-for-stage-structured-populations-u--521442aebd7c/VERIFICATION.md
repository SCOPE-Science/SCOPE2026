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

# Verification of the mathematical finding

The mathematical theorem follows from the four proof steps in `RESULT.md` and classical Perron–Frobenius comparison for positive matrices. The executable diagnostics supplement, rather than certify, that proof.

Run `python verify.py` after installing the three packages in `requirements.txt`. The script symbolically recomputes both marginal allele-survival ratios and the exact full-dominance quadratic susceptible-mass loss. It then simulates a three-stage positive Metzler semigroup and verifies that (i) the resistant-dominant asymptotic values are close to their weighted inverse-selection coefficient, and (ii) with partial dominance the logarithmic rate is close to the Perron root ratio. It also computes four distinct biologically admissible full-dominance selection examples from the source's four-stage life-history data and reported susceptible-genotype pulse survivals.

Observed diagnostic output (rounded): dominant weighted prediction 2.509656225; observed stagewise values after 20000 pulses 2.51103304, 2.51124986, 2.51099521. Partial-dominance log prediction -0.172992259; observed values at 1000 pulses -0.17311655, -0.17279733, -0.17318671. Four-stage inverse-pulse coefficients for selection in egg, larva, pupa and adult are approximately (8.06272989, 2.93680651, 122.22632820, 3.99529147). In each scenario the selected stage has strength 0.5 and resistant-homozygote pulse survival twice the source's susceptible-genotype pulse survival, making all probabilities admissible.

The program tests representative configurations only. It does not produce machine-formal verification of the infinite-time assertions, and it does not substitute for mathematical checking of the uniform mixing, contraction and weighted drift arguments. The publication priority assessment is not independently audited.
