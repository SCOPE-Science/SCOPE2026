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

Run `python3 verify.py` (stdlib only). The observed output is:

```
n=1: transitive_frames=2, symbolic_profile_checks=4
n=2: transitive_frames=13, symbolic_profile_checks=104
n=3: transitive_frames=171, symbolic_profile_checks=4104
n=4: transitive_frames=3994, symbolic_profile_checks=255616
VERIFY_OK total_frames=4180 total_profiles=259828
```

The tests enumerate every transitive relation on 1–4 labeled worlds, verify the three-level partial-order restriction, the symbolic existence-of-infinite-tail criterion for every source subset, and the converse-well-founded criterion on finite frames. A three-level finite truncation contains no genuinely infinite neighborhoods and is **not** treated as a computational test of infinite omega-accumulation. The exact infinite-neighborhood claim is proved by exhibiting all higher natural-number indices in RESULT.md. The closedness of the omega-perfect witness and its full converse are proved there as well. Infinite and countable generality comes from the proof; external independent validation has not been performed.
