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

# Finite verification of the BLAL implication census

The included `checker.py` uses Python 3 standard library only. Run `python3 checker.py` to enumerate every strict-lower-triangle assignment on bounded chains with sizes 1, 2, 3, and 4. Its implementation follows Theorem 16's eleven equations and three quasi-equations **exactly** and evaluates all variable triples. The reduction to lower-triangle assignments is proved by the published Proposition 21 and reproduced in `RESULT.md`.

Expected output:

```
ALL_CHECKS_OK counts=(1,1,4,25) candidates=(1,1,8,729)
BLAL_C4 witness A,B,C,D valid; M invalid at E8(3,2,0)=1
No join of C,D and no meet of A,B
```

The finite computation enumerates all 729 candidate tables on the four-element chain. Direct checks establish that A,B,C,D satisfy the complete BLAL axiom set, M fails E8 and all possible lattice-bound candidates are excluded. The symbolic order proof in the result derives missing joins and meets from the coordinatewise bounds. No extrapolation to larger carriers is made. Historical priority under alternate descriptions remains subject to further examination; independent audit has not been performed.
