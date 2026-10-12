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

`verify_gap_rank.py` checks the claimed distribution in three independent ways.

1. It directly enumerates all pairs of weakly increasing interior-value sequences through \(n=5\) and bins them by the number of strict coordinates.
2. It runs the exact terminal-state prefix-sum recurrence through \(n=12\), independently of the direct Cartesian enumeration.
3. It checks the ballot closed form, its Catalan row sum, and the exact first two factorial moments through \(n=50\).

The first nontrivial rows recovered are
`[3,3]`, `[10,20,20]`, `[35,105,175,175]`,
`[126,504,1134,1764,1764]`, and
`[462,2310,6468,12936,19404,19404]`.

Replay:

```text
python3 verify_gap_rank.py
```

The recorded terminal line is `VERIFY_OK 364 exact assertions/components`.
Independent audit has not been performed.
