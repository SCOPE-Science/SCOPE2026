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

# Verification and scope

Run `python3 verify.py` from a directory containing the separately embedded verification program. Only Python 3 standard-library modules are used. The verification program enumerates the actual minimal winning coalitions rather than merely repeating the closed formula; it calculates each player's normalized Deegan–Packel index by exact rational arithmetic, sums its squares, and checks the theorem's formula for 880 parameter triples. It verifies the exact factorization sign conditions and one-turn signs for sampled cases, checks the 13-seat witness and exclusion of smaller cases in this family, and tests near-\(t\)-fold amplification with explicit parameters.

Expected successful output:

```
PASS: 880 independent coalition-based exact-rational instances
PASS: sharp 13-member petal-family witness and smaller-family exclusion
PASS: exact adjacent increments, comparisons, and near-t-fold amplification
```

These computational checks are finite. The general results for all positive integer parameters follow from the written algebra and limiting argument in `RESULT.md`; the program does not independently prove those infinite statements, does not test every simple game, and does not certify mathematical novelty or independence. Independent external audit has not been performed.
