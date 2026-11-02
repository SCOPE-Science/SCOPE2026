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

# Computational and mathematical verification

Run `python3 verify.py` with standard Python 3. The program forms the monoid directly from all increasing partial injections on the block indices, attaches every symmetric-group label to each selected arrow, and constructs products by composition of labeled partial arrows. It then generates the proposed complete parameter family, verifies that its images are distinct bijections, and checks the semigroup automorphism equation for every ordered pair of elements.

Observed results:

```
VERIFY_OK k=2 m=2 elements=13 explicit_automorphisms=4 all_pairs_checked=676
VERIFY_OK k=3 m=2 elements=63 explicit_automorphisms=8 all_pairs_checked=31752
VERIFY_OK k=2 m=3 elements=61 explicit_automorphisms=72 all_pairs_checked=267912
```

The program does not enumerate every abstract automorphism independently; completeness follows from the proof using idempotents, natural-order joins, and rank-one groupoid multiplication. No finite computation checks all block sizes or constructs the exceptional automorphism of the six-point symmetric group. Its existence and uniqueness modulo inner automorphisms is a classical theorem proved in the cited work of McCammond. No independent audit has been performed.
