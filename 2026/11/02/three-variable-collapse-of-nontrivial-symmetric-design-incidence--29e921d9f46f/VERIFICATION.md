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

# Reproduction of finite checks

All code uses only the Python standard library. From the directory containing the two scripts run:

```
python3 verify_extension.py
python3 verify_pebble.py
```

The first program reconstructs five cyclic designs and checks their parameters, all point-pair and block-pair intersections, their eight ordered-pair extension profiles, the excluded trivial boundary, and the number of four-cycles in two fourteen-vertex incidence graphs. The second program independently iterates three-variable, non-counting tuple-colour refinement to a stable fixed point on four designs of different parameters. Its use of sets rather than multisets is essential: counting colours would test a different logic.

`verification_output.txt` records the actual successful execution. The scripts are finite corroborations only. The theorem for all symmetric designs of every admissible size rests on the explicit incidence count identities and the infinite three-pebble strategy in `RESULT.md`. The Fano/complement four-cycle separation is additionally checked directly by enumeration. No independent audit has been performed.
