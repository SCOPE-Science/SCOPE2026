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
# Verification record

The exact proof is given in `RESULT.md`. The standalone executable `verify_ordinal_cycle.py` recomputes \(K_n\) from all disjoint permutation cycles, evaluates all six possible length-three consecutive patterns, and compares exact enumeration against the closed-form table for \(n=3,\ldots,9\). It checks \(168\) position-pattern covariance cells across \(409{,}110\) permutations. It also recomputes the forced-cycle counting identity for \(745{,}506\) pairs of size, position, and pattern through \(n=500\). Both checks completed without assertion failures. Reproduce with:

```sh
python3 verify_ordinal_cycle.py
```

The argument for all \(n\ge3\) rests on the forced-edge contraction bijection and exact image counts, not on extrapolation from the enumerated window. Historical priority beyond the inspected sources is not certified. Independent audit is not yet performed.
