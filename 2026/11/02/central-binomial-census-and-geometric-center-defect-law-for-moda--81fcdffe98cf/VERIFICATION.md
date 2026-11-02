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

The general proof is in `RESULT.md`. Reproduce the finite comparisons with Python 3 and the standard library only:

```sh
python3 checker.py
```

The direct implementation tests the three universal modal equations on each function, separately computes the proposed plateau criterion, and asserts agreement. It enumerates every function on the three-element and five-element chains (27 and 3,125 functions respectively), all monotone unary functions on odd chains of sizes three through nine (26,162 maps in total), and the two exact binomial identities through parameter 60.

Observed result:

```text
half_width=1 accepted=5 normal=3 centered=4 both=2
half_width=2 accepted=40 normal=21 centered=36 both=18
half_width=3 accepted=415 normal=210 centered=400 both=200
half_width=4 accepted=4956 normal=2485 centered=4900 both=2450
ALL_CHECKS_OK full_functions=3152 monotone_maps=26162 binomial_ranks=60
```

The count on all monotone unary maps is exhaustive within the domain justified mathematically by meet preservation. The binomial checks are finite identity tests, not substitutes for the hockey-stick proof. The geometric asymptotic follows from explicit coefficient ratios and Stirling's formula, not numerical extrapolation. No external independent audit has been performed.
