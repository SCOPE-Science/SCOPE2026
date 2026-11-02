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

# Computational verification

Use Python 3.10+ standard library only. Run `python3 verify.py` in the directory containing the embedded checker. The verifier independently enumerates actual three-vertex paths in each labelled cycle for every vertex subset at cycle orders three through fourteen; cross-checks the minimal 2-star-forming predicate with the 9-bit rule at cycle orders nine through fourteen; checks all 512 windows and all 332 exact height inequalities from the literal 256-digit certificate; checks 242 tight arcs and exactly two simple directed cyclic SCCs with sizes three and six; and directly confirms the optimal counts at cycle orders divisible by three.

Replayed output:

```
VERIFY_OK windows=512 allowed_arcs=332 potential_heights=0..4 tight_arcs=242 cyclic_SCCs=(3,6) brute_n=3..14 counts={3: 3, 4: 6, 5: 10, 6: 9, 7: 14, 8: 8, 9: 3, 10: 60, 11: 33, 12: 9, 13: 91, 14: 14}
```

The universal bound is a deduction from summing the fully checked potential inequalities around an arbitrary closed walk, and the universal equality classification from the fully checked tight SCC structure. Brute-force cycle samples alone are not taken as infinite proofs. This verification is neither independent mathematical audit nor external certification.
