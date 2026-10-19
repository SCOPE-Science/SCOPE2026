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
# Verification record

Execute `python verify.py` using the standalone Python 3 standard library. The executed package's direct checker reported:

```
PASS exact ordered-configurations: 392400
PASS distinct bounded-degree missing-edge graphs: 270
PASS exact matching law n=3,4 and exact cycle law n=4; matching stochastic cross-check n=5,10,25
```

The direct checker enumerates orders independently of the proof's inclusion-exclusion calculation. It also tests the equivalence of the first-arrival exceptional event and direct cross-part acceptance and checks the mixed-output size bound. The exact cycle four-by-four checks give 21,504 count-three and 18,816 count-four outputs among 40,320 orders. The analytical all-size conclusion relies on the proof in `RESULT.md`, not finite enumeration or a Monte Carlo extrapolation.

No independent audit or external certification has been performed. The full text of an older 1989 adsorption source was not available during the literature comparison; its abstract and publicly available bibliographic description were considered without treating them as evidence about unread sections.
