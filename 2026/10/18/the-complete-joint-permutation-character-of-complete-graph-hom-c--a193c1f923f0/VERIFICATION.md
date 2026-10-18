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

# Reproducibility and limits

The theorem follows from a general fixed-point Euler argument, not from experiments. `verify_hom_character.py` is a standard-library Python script that separately enumerates each original product-of-simplices cell and evaluates the signed cellular trace for every tested group element. The independent calculation explicitly handles the Koszul orientation sign for source-factor permutations and the internal simplex orientation signs for target-color permutations.

The reproducible command is `python3 verify_hom_character.py`. Tests cover all simultaneous actions for parameter pairs \((2,3),(2,4),(3,4),(3,5),(4,5)\), selected additional actions for \((3,6)\), numerical identity ranks from the known non-equivariant formula, and the diagonal source-and-target quotient character average for several values of \(n\). The already known target-only quotient may be checked as a consistency condition but is not original.

Checks establish consistency of the closed-form character with exact finite cellular traces. They do not computationally verify all parameter values, prove the all-parameter statement without the manuscript proof, determine integral group representations, or independently assess novelty. A full independent external mathematical audit has not been performed.
