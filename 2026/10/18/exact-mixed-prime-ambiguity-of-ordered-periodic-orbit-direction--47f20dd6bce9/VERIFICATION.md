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

# Reproduction and limits

From the package directory, execute `python3 verify.py` with Python 3.9 or later. The script uses only the standard library, enumerates every single cycle at lengths 2 through 10, verifies signatures directly at all nonzero times, checks group class counts, and generates constructive witnesses with pairwise-distinct image lists at lengths 6, 10, 14 and 22. Expected final output is `VERIFIED`.

The uniform formula for all odd primes follows from the written phase-prefix tree proof and block construction. Finite examples do not establish its quantifiers. The exact full class-size distribution for arbitrary composite cycle lengths is not claimed. No independent audit was performed.
