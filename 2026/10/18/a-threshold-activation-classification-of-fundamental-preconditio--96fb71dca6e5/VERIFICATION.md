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
# Verification details

Execute `python3 verify_pentagon_preconditionals.py` with Python 3 standard library. The program constructs the long-pentagon meet and order operations directly and checks all original five preconditional axioms, conditional identity, semicomplementation, and double-negation inflation. Independently, for arm lengths \(1\le m\le4\), it enumerates all row operations compatible with the necessary local constraints and filters by the entire axiom system; the resulting set of full operation tables equals the set built from the threshold–activation normal form, not just its cardinality. For arm length five the normal-form generator checks all 407 canonical tables but does not exhaust the unrestricted space of binary operation tables.

Recorded output:

```
m=1 F=2 by_negation={0: 1, 1: 1} exhaustive=True
m=2 F=5 by_negation={0: 2, 1: 2, 2: 1} exhaustive=True
m=3 F=17 by_negation={0: 6, 1: 6, 2: 4, 3: 1} exhaustive=True
m=4 F=75 by_negation={0: 24, 1: 24, 2: 18, 3: 8, 4: 1} exhaustive=True
m=5 F=407 by_negation={0: 120, 1: 120, 2: 96, 3: 54, 4: 16, 5: 1} exhaustive=False
LONG_PENTAGON_PRECONDITIONAL_VERIFY_OK
```

The general theorem is established by the four-step mathematical proof in `RESULT.md`; the executable verifies concrete instances and does not by itself prove statements for unbounded \(m\).
