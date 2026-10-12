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

The proof in `RESULT.md` has two exact components. First, the source negation table gives the count recurrence
\[
(t_{n+1},u_{n+1},f_{n+1})=(u_n+f_n,u_n+f_n,t_n),
\]
from the base \((1,0,1)\). Second, the source support condition is applied directly to every \(\mathbf U\)-entry, yielding the four surviving row patterns for every \(n\ge2\).

`verify_negation_tower.py` independently performs literal row generation and repeated support deletion through depth \(13\). It checks the full survivor set, not only its cardinality. It also checks the closed Fibonacci formulas and recurrence through depth \(200\).

Replay:

```text
python3 verify_negation_tower.py
```

Recorded terminal line:

```text
VERIFY_OK 919 exact assertions
```

The finite replay is corroborative only; the universal result is established by the recurrence and support argument in `RESULT.md`. Independent audit has not been performed.
