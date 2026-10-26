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

The standalone `verify.py` recomputes distinct subsequence counts from a last-occurrence dynamic program on 6,561 positive quadruples. It checks the exact conditional maxima for every integer length from 4 through 48 by exhaustive run-composition enumeration and checks the balancing and orientation constraints for every conditional maximizer. The symbolic proof in RESULT.md covers all positive parameters. An independent audit has not been performed.
