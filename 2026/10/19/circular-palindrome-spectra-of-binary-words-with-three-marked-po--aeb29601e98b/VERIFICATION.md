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
# Verification and reproducibility

Run `python3 verify.py` using Python 3 and its standard library. The output of the executed packaged program is:

```text
VERIFY_OK direct_gap_triples=2300 extremal_gap_triples=2274994 lengths=3..240
```

The program enumerates actual length-limited circular palindromic factors as strings for all triples with lengths 3 through 25 and compares their number to the theorem's three-case expression. It then enumerates all gap triples for lengths 14 through 240, independently obtains each length's maximum and sorted set of maximizing triples, and compares against the theorem's exact residue-class list. The proof supplies the all-length arguments; these checks alone cannot establish them. The corresponding independent external mathematical audit has not been performed.
