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

The standalone `verify.py` artifact was read from its packaged path before replay.

It constructs unit graphs directly from ring addition for \(\mathbb Z/4\mathbb Z\), \(\mathbb Z/8\mathbb Z\), \(\mathbb Z/9\mathbb Z\), and \(\mathbb F_4[\varepsilon]/(\varepsilon^2)\). For each graph it compares every edge with the residue-fiber model and exhaustively tests every vertex subset against the closed zero forcing polynomial.

The exact real rank witnesses are checked entry-by-entry against the graph pattern and row-reduced over the rationals. The verifier also replays the two-white-fiber forcing rule and the algebraic recovery of \(q\) and \(s\) on additional parameter pairs.

Exact replay output:

```text
Z/4Z: q=2, s=2, polynomial={2: 4, 3: 4, 4: 1}
Z/8Z: q=2, s=4, polynomial={6: 16, 7: 8, 8: 1}
Z/9Z: q=3, s=3, polynomial={7: 27, 8: 9, 9: 1}
F4[e]/(e^2): q=4, s=4, polynomial={14: 96, 15: 16, 16: 1}
rank witness q=2, s=2: rank=2
rank witness q=2, s=4: rank=2
rank witness q=3, s=3: rank=2
rank witness q=5, s=5: rank=2
rank witness q=4, s=4: rank=3
PROFILE_AND_RECOVERY_OK
VERIFY_OK
```

The exhaustive calculations are finite corroboration. The arbitrary-ring forcing theorem, the even-order rank-two obstruction, and the parameter-recovery theorem are proved symbolically in `RESULT.md`.
