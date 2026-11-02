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

# Mathematical verification

Run `python verify.py` using the Python standard library. It enumerates all binary signal pairs and both possible focal ballots, constructs each reward directly from the winning coalition and headcount threshold, uses exact `fractions.Fraction`, and compares to the derived coefficient and posterior formula. The tested grid contains 1,000 positive effort profiles, including equal and three-way unequal profiles; all efforts are at most one half. Verified output:

```
PASS: 1000 heterogeneous/equal effort triples, 6000 exact state-payoff checks, 18000 posterior identities, 270 evaluated tie cases.
```

The mathematical proof rests on the positive-coefficient inequality derived in `RESULT.md`; the program only checks finite examples. Tie randomization is represented exactly by `Fraction(1,2)`. The effort-choice equilibrium is not investigated, and no independent scientific validation is claimed.
