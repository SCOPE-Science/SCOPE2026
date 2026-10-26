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

Run `python3 verify_cyclic_k3.py` with standard Python 3. It uses no external packages or network access. Observed exact arithmetic output:

```
n=1: q=2; critical_points=1; resolved_points=9
n=2: q=4; critical_points=3; resolved_points=33
n=3: q=8; critical_points=7; resolved_points=129
n=4: q=16; critical_points=3; resolved_points=321
n=6: q=64; critical_points=21; resolved_points=5505
FROBENIUS_CYCLES=[1, 2, 3, 3, 6, 6]
VERIFY_OK
```

The checker enumerates \(\mathbb P^2(\mathbb F_{2^n})\), recomputes partial derivatives, the critical-point count and local mixed second derivative, and verifies the node orbit decomposition for the full splitting field. These finite experiments do not by themselves prove the all-\(n\) assertion; the symbolic elimination, reducedness, local normal form, and orbit/count generating-function arguments in `RESULT.md` do. General K3/supersingularity is a cited existing theorem, not a newly verified computation. Independent audit is not performed.
