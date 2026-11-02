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

# Verification of the exact free-algebra theorem

The stand-alone `checker.py` checks the finite consequences of the algebraic/semantic classification without relying on precomputed counts. Its independent depth-two signature function compares the root's colour and the first two successor observations against a separate structural type classifier. It enumerates all partial maps with at most one successor on each labelled carrier of sizes one through six and selects those satisfying \(f(f(x))\in\{x,f(x)\}\) wherever defined. Every binary valuation and rooted world is checked, giving 5,596,204 pointed coloured cases.

The same program tests all predicted canonical types and every corresponding characteristic formula for colour counts \(q=1,2,3\). It verifies the depth-one indistinguishability and depth-two separation witness. Expected terminal output:

```
q= 1 types= 3 pairwise distinct depth2; characteristic formulas=OK
q= 2 types= 12 pairwise distinct depth2; characteristic formulas=OK
q= 3 types= 27 pairwise distinct depth2; characteristic formulas=OK
n= 1 valid partial maps= 2
n= 2 valid partial maps= 9
n= 3 valid partial maps= 44
n= 4 valid partial maps= 267
n= 5 valid partial maps= 1812
n= 6 valid partial maps= 13771
ALL_CHECKS_OK; examined rooted coloured cases= 5596204
```

Run `python3 checker.py` with Python 3 (standard library only). The exhaustive finite checks validate the tested finite instances, not an infinite case; the universal proof is Steps 1–5 of `RESULT.md`. The classification and all-rank count were reviewed for scope, quantifiers, and edge cases, including \(k=0\), absent successors, loops, two-cycles and monochromatic bisimulations. No independent external audit or formal proof assistant certification was performed.
