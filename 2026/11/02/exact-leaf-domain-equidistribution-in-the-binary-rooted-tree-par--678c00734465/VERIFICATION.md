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

# Reproducibility and boundaries

Run `python3 verify.py` using the standard Python library only. The verifier lists every prefix-closed rooted domain subtree to height three, groups image subtrees by unlabelled rooted-tree shape, multiplies by the exact domain automorphism count, and groups the resulting maps by their fixed terminal-domain subset. This is a different finite counting procedure from the proof's first-level rank classification.

Observed output:

```
n=0 root_subtrees=1 map_count=1 fixed_nonempty=1 zero=0 by_rank=[0, 1]
n=1 root_subtrees=4 map_count=7 fixed_nonempty=2 zero=1 by_rank=[1, 4, 2]
n=2 root_subtrees=25 map_count=127 fixed_nonempty=8 zero=7 by_rank=[7, 32, 48, 32, 8]
n=3 root_subtrees=676 map_count=32767 fixed_nonempty=128 zero=127 by_rank=[127, 1024, 3584, 7168, 8960, 7168, 3584, 1024, 128]
VERIFY_OK
```

The finite tests are exhaustive within these four heights only. The unrestricted proof consists of the top-child partial injection split, the recurrence \(C_n=2C_{n-1}^2\), and the count of the empty-terminal-set case \(Z_n=C_n-1\). They do not prove any independent novelty or external certification. The classical binomial central limit theorem is used only after the exact total-variation comparison. All domains contain the root, even when their bottom-level domain set is empty.
