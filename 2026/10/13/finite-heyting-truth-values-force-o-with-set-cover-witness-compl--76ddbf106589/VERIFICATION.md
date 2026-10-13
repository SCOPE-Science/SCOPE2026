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

The general proof in `RESULT.md` is algebraic. The bundled `verify.py` is an independent finite replay of its key optimization identity.

For every labeled poset with at most four points, the script forms the Heyting algebra of upsets. It computes Heyting negation as the largest upset disjoint from a given upset, then double negation, the regular fixed-point Boolean algebra, and its atoms. Across all \(242\) labeled posets it exhausts every family of possible witness truth values. For each family it independently computes:

1. the least number of selected values whose double-negated join dominates the full existential join; and
2. the least number of regularized supports covering all regular atoms below the double negation of that existential join.

The two numbers agree in all \(172740\) cases, and the common value never exceeds the number of regular atoms. The script separately checks the sharp powerset construction for \(k=1,\dots,12\).

Terminal output:

`VERIFY_OK 172740 witness-family checks over 242 labeled posets through four points; sharpness k<=12`

This exhaustive finite replay does not prove the theorem for arbitrarily large finite frames. The proof is the nucleus/atomic-Boolean argument given in `RESULT.md`. No independent audit has been performed.
