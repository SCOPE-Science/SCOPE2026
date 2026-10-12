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

Run `python3 verify.py` with Python 3. The script uses only the standard library. Its checks exhaust nonempty subsets of 17 finite abelian groups in invariant-factor form of order at most 12, compute their power collision indices and periods, compare the minimum bound and equality normal forms, and check 130 explicit constructed pairs with independent subset arithmetic.

Observed output:
```
GROUP_PROFILES=17 NONEMPTY_SUBSETS=13309 OPTIMAL_SUBSETS=325
OBSERVED_INDEX_PERIOD_PAIRS=29 EXPLICIT_WITNESSES=130
VERIFY_OK
```

The universal theorem is established mathematically by the strict translated-sumset growth and quotient-period argument in the proof. These finite computations do not certify an infinite family or exhaust all literature. The 2025 publisher full text and 1980 historical paper were not available in full for comparison. No independent audit was performed.
