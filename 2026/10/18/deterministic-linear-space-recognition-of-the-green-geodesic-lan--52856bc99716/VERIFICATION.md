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

The standalone `artifacts/verify.py` checks direct word enumeration in ranks one, two and three. It uses finite Munn-tree class keys independently of the closed length formulae, then compares class minima obtained by enumeration with the four candidate expressions.

Replay: `python3 artifacts/verify.py`.

Observed replay:

```
rank=1 maximum_length=10 words=2047 total_geodesic_words_H_R_L_D=(171, 51, 51, 21)
rank=2 maximum_length=6 words=5461 total_geodesic_words_H_R_L_D=(4281, 3053, 3053, 2297)
rank=3 maximum_length=4 words=1555 total_geodesic_words_H_R_L_D=(1483, 1237, 1237, 1057)
VERIFY_OK: 9063 complete words; four Green-class distance formulae tested independently
```

The enumerations cover only these finite length ranges. The full theorem, its polynomial running-time guarantee and its \(O(n)\) deterministic work-space bound depend on the independent mathematical arguments in the proof, not on extrapolation from the enumerated words. No external audit or infinite computation has been performed.
