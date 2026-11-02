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

The self-contained `checker.py` was executed using the Python standard library. It enumerates 35 finite \((n,d)\) grid instances (1,281 mass vectors), compares complete binary-threshold observational fibers with singleton profiles and pairwise products, checks the exact count and fiber-size formulas, independently evaluates 3,445 Walsh identities, and tests 42 excluded-singleton witnesses. The recorded terminating marker was `ALL_CHECKS_OK`.

These enumerations are exact finite checks, not certificates for arbitrary real probability vectors. The general claim is established by the coordinate-complement/normalization argument, the sign-Walsh identity, and disjoint class counting in `RESULT.md`. Source overlap was assessed using the specified semantics paper, existing phase-retrieval literature and published mathematical records; coverage outside inspected materials remains a risk. No external independent audit or formal-proof certificate is claimed.
