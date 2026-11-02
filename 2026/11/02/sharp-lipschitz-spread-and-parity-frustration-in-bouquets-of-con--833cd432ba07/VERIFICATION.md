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

Run `python3 verify_cycle_roses.py` using a standard Python 3 installation. The checker was run from this package before acceptance, with the following exact-arithmetic output:

```text
EXACT_ROOTED_CYCLE_VERTEX_MAXIMA_OK 3926
EXACT_ALL_EXTREME_PETAL_STATES_BOUQUET_OK 56
DIRECT_LABELLED_EXTREME_POTENTIALS_OK 58780
EXACT_PARITY_SAWTOOTH_INEQUALITIES_OK 9850
ALL_CONGRUENT_CYCLE_BOUQUET_SPREAD_CHECKS_OK
```

The cycle enumeration covers only small lengths; each feasible polytope vertex has all but at most one tight edge, and each petal combination is optimized exactly by integer dynamic programming. No finite checker exhausts the infinite parameter range. The analytical argument in RESULT.md supplies the unrestricted proof, depending on the established single-cycle strict-convex permutation reduction from Yancey's Section 2.3. The numerical checker does not independently reprove that published lemma.

No independent scientific audit has been performed.
