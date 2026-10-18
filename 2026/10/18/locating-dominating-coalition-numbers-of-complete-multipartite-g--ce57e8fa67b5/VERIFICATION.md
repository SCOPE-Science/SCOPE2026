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

Run `python verify.py` with Python 3.10 or later. The script independently derives the locating-dominating predicate from actual open-neighbourhood masks, enumerates each set partition canonically, and compares computed coalition maxima to the stated closed form for all 86 complete multipartite part-size profiles with orders from three through nine. It checks the vertex-cover reduction on every non-star case and separately tests the quotient-cover support lemma on 1,024 five-vertex loopless simple graphs.

Observed results:
```
PASS: 86 isomorphism-type part-size profiles for 3 <= n <= 9;
each possible vertex subset and every set partition was checked.
PASS: 1,024 five-index loopless quotient graphs satisfy the cover-support lemma.
```

The verifier is finite and does not establish priority or give an infinite verification certificate. General validity rests on the complete constructive proof in RESULT.md. No external independent audit has been performed.
