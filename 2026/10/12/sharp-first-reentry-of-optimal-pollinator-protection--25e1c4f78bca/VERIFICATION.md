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

# Verification

The package contains the complete program `verify.py`, requiring only the Python standard library. Execute:

```sh
python3 verify.py
```

Expected terminal line:

```
VERIFY_OK plant_species=13 primary_species=4 exact_masks=48 coefficient_cases=2 roots=(5+-sqrt(5))/10
```

The program constructs the thirteen separate plant-neighborhood records; independently sums gain over the sixteen primary extinction masks at each of three rational values of \(q\); confirms all four exact coefficient lists and unique maximizing choices; enumerates all integer quadratic coefficient triples of total absolute weight at most twelve whose two roots lie strictly inside \((0,1)\); and checks the symbolic coefficient inequalities used for the stronger global-optimality obstruction. All computations use exact integer or rational arithmetic, with no probabilistic approximation.

The lower bound for every smaller network follows from the proof in `RESULT.md`, not from a finite search over networks. The program does not independently verify the mathematical novelty assessment, an empirical model, or an infinite family outside the stated proof. No independent scientific audit has been performed.
