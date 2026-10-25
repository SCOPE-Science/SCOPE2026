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
# Reproduction and scope

Use Python 3.8 or newer; only the standard library is needed. In the directory containing both this file and `verify_transition.py`, execute:

```sh
python3 verify_transition.py
```

The checker independently constructs the graph, iterates all functions \(f:V\to\{0,1,2\}\) of weight at most six, applies the literal total perfect Roman conditions at every vertex, and compares all minimum functions with the claimed explicit classification. The successfully observed final line was `VERIFY_OK 39 n,k cases; all {0,1,2} labelings of total weight <=6 independently enumerated; exact optimizer witnesses checked`. Its coverage is \(3\le n\le8\), \(0\le k\le n\). This is a finite regression check, not a computer-assisted certificate for unbounded \(n\). The all-parameter argument is in `RESULT.md`; no independent audit has been performed.
