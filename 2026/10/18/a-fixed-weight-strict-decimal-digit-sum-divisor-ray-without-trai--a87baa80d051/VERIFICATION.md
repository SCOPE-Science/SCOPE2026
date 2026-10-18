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

The proof consists of the separated-block identity and three seed digit sums. Check the exact integer products `448999*448999=201600102001` and `2*448999*448999=403200204002`, whose digit sums are 13 and 17. The seed itself has digit sum 43, while `2*448999*448999<10**12` ensures the three square blocks are separate for each integer k>=12. For any such k, digit-additivity yields sums 86 for the argument and 43 for the square. The final decimal digit is always 9. Strict increase in k proves infinitude.

A reproducibility script is supplied as `checker.py`; run `python3 checker.py`. It uses only exact integers and Python's standard library. It checks the seed arithmetic and 89 finite test instances, k=12..100. It does not enumerate or prove every infinite instance; that step is supplied by the algebraic block identity.

The statement does not purport to be a complete census of the OEIS sequence, a least-weight assertion, or an independent audit.
