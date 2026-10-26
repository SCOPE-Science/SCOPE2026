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

# Finite verification

Compile the attached C99 source with `cc -O2 -std=c99 -Wall -Wextra four_confluence_verification.c -o check` and run `./check`. No external libraries are required. The source independently evaluates all four quantified relational conditions and the endpoint normal form on every relation with at most four worlds. A separate row-mask recursive enumeration checks the six finite totals, and an insertion test checks every intermediate relation on the constructive edge spectrum through seven worlds.

The source was compiled and run from the actual assembled research file; the observed output was:

```
DIRECT_CONFLUENCE_OK 1 2
DIRECT_CONFLUENCE_OK 2 5
DIRECT_CONFLUENCE_OK 3 34
DIRECT_CONFLUENCE_OK 4 538
ENDPOINT_ENUMERATION_OK 1 2 explored=1
ENDPOINT_ENUMERATION_OK 2 5 explored=6
ENDPOINT_ENUMERATION_OK 3 34 explored=79
ENDPOINT_ENUMERATION_OK 4 538 explored=2854
ENDPOINT_ENUMERATION_OK 5 23415 explored=374659
ENDPOINT_ENUMERATION_OK 6 3567130 explored=195589840
FOUR_WAY_CONFLUENCE_VERIFICATION_OK
```

All-size statements (endpoint criterion, exact polynomial, gap-free edge counts, and quadratic entropy) are proved mathematically in RESULT.md, not extrapolated from this output. Exhaustive testing of all relations stops at four worlds; the larger exhaustive search uses the mathematically derived endpoint pruning. No other semantic or historical-priority certification is claimed.
