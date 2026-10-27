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

The standalone `verify.py` is self-contained Python 3. It enumerates all source words on the three-color palette for every friendship graph with \(1\le m\le6\). For each hub choice it explicitly evaluates both orientations of every peripheral edge, rather than using the symbolic closed-form delta cases from the proof. Feasible-profile sources are separately filtered and ordinary and weak distance maxima recomputed. It also checks source multiplicities, sharp constructions, and the cyclicly relabeled three-copy witness for \(2\le m\le100\).

To reproduce from extracted files, run `python3 verify.py`. Completed result:

```
VERIFY_OK m=1..6 all_words=1793610 legal_words=15590 construction_m=2..100
```

The executable checks exactly \(1{,}793{,}610\) words and \(15{,}590\) feasible-profile words in the small instances. The numerical tests do not certify the infinite theorem: its correctness rests on the hub-cost decomposition, all-order extremal witnesses, finite exceptional parity cases, and cyclic color relabeling proof in RESULT.md. The result is not independently audited.
