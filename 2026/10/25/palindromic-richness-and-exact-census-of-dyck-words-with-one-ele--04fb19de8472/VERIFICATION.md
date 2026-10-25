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

Run `python3 rich_one_excursion_verify.py` using Python 3 standard library. It independently enumerates palindromic substrings for \(1\le a\le21\), \(0\le u,v\le21\), and re-enumerates admissible words at semilengths \(2\le n\le40\). Expected `RICH_SINGLE_EXCURSION_PASS triples= 10164 n=2..40`. The checker does not certify infinitely many parameters; the exact proof is in RESULT.md. Current scientific risks concern potentially unindexed equivalent prior literature. Independent audit has not been performed.
