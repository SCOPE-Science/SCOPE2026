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

It checks every at-most-one-white valuation-layer profile for
\[
q\in\{2,3,4,5\},\qquad 2\le\ell\le10,
\]
and confirms that the only failed profile is the one-vertex boundary.

It computes the layer quotient rank exactly through \(\ell=12\).

For six small parameter pairs it exhaustively enumerates every vertex subset and reproduces the full zero forcing polynomial. It also constructs five prime-power residue-ring graphs directly from modular multiplication and checks every edge against the valuation criterion.

Exact replay output:

```text
PROFILE_THEOREM_OK
QUOTIENT_RANK_OK
(q,ell)=(2,2): sizes=[1], N=1, polynomial={1: 1}
(q,ell)=(3,2): sizes=[2], N=2, polynomial={1: 2, 2: 1}
(q,ell)=(2,3): sizes=[2, 1], N=3, polynomial={1: 2, 2: 3, 3: 1}
(q,ell)=(3,3): sizes=[6, 2], N=8, polynomial={6: 12, 7: 8, 8: 1}
(q,ell)=(2,4): sizes=[4, 2, 1], N=7, polynomial={4: 8, 5: 14, 6: 7, 7: 1}
(q,ell)=(2,5): sizes=[8, 4, 2, 1], N=15, polynomial={11: 64, 12: 120, 13: 70, 14: 15, 15: 1}
Z/4Z direct graph OK: N=1
Z/8Z direct graph OK: N=3
Z/16Z direct graph OK: N=7
Z/9Z direct graph OK: N=2
Z/27Z direct graph OK: N=8
PARAMETER_RECOVERY_OK
VERIFY_OK
```

The exhaustive computations are finite corroboration. The arbitrary finite-chain-ring theorem follows from the symbolic valuation-layer, forcing, and rank arguments.
