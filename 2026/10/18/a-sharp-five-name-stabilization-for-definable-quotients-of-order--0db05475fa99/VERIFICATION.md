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

# Reproducibility
Run `python3 verify_pair_quotients.py` (Python standard library only). The script enumerates every equality pattern of four atom variables, closes under exchanging the two ordered pairs, and checks equivalence properties via exact finite bitsets. It verifies all six sizes \(n=1,2,3,4,5,6\), printing:

```
PATTERN_ORBITS=15 SYMMETRIC_GROUPS=11
QUOTIENT_COUNTS=1,7,16,15,13,13
EXCEPTIONAL_FOUR_ATOM_MASKS=1185,1193
VERIFICATION_OK
```

The equality-pattern method is exhaustive because a relation invariant under permutations is a union of orbits of quadruples; symmetry is built into the eleven pattern classes; reflexivity is checked for each candidate; transitivity is checked across every triple of pair-points. The six-atom bound controls all possible equality patterns of three pair-points, but the paper's structural proof independently derives the exact formula and validity on every infinite set. The finite checker is not presented as independent validation. The literature comparison leaves the cited preprints' inaccessible full text and unindexed equivalent claims as residual originality risks.
