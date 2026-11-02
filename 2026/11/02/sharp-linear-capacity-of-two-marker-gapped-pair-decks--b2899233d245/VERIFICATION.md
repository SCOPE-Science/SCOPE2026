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

# Reproducibility and limits

Run `python3 verify_gapped_weight2.py` with Python 3 (standard library only). The program enumerates all strings with exactly two ones by their marked positions. For short lengths it constructs each allowed separated index pair literally and compares all four counts with the coordinate formula. For each enumerated parameter pair it counts distinct analytic decks and checks the theorem or the sharp boundary wherever applicable.

A completed run produced:

```
VERIFY_OK gap_values=2..18 cases=748 literal_pair_observations=14535 position_pairs=540294 theorem_instances=442 sharp_boundary_instances=17
EXACT s=2 n=5 capacity=10 next=15
EXACT s=3 n=8 capacity=28 next=36
EXACT s=4 n=11 capacity=51 next=61
EXACT s=5 n=14 capacity=80 next=92
EXACT s=7 n=20 capacity=156 next=172
EXACT s=10 n=29 capacity=315 next=337
```

The literal pair loop is restricted to \(n\le19\) for runtime; the other cases use the coordinate formula. Neither the code nor these logs prove the all-integer result, whose proof appears in RESULT.md. No external or independent review is claimed.
