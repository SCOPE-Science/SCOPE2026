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
# Verification details

Run `python3 checker.py` using ordinary Python 3 and no third-party packages. Expected output:

```
PERMUTATION_TENSE_GENERATORS_EXACT_OK 948 checks
GENERATION_SQUAREFREE_IDENTITY_OK 76 10
```

The first line confirms exhaustive comparison of temporal-itinerary separation and the conditional primitive-necklace product on all permutations through six points at two colours and through four points at four colours, plus independent exhaustive primitive-word counts. The second line confirms the first nineteen formal-series coefficients at four alphabet sizes and ten exact averaged permutation totals. The checker reconstructs the count directly from permutations and colour assignments rather than trusting the formal generating function. The proof for unbounded size is the separately stated partition and formal-series argument; finite enumeration cannot certify every \(n\). The source files are read as delivered; no external files, services or certificates are needed.
