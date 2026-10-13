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

Run `python3 verify_di.py` with Python 3 and its standard library. The checker enumerates all reflexive transitive relations on one, two, and three labelled worlds, all binary modal relations on those worlds, and all persistent valuations of the three propositional variables. It compares the semantic implication test with both the finite-join identity for \(I_w\) and the quantified principal-cover condition (PC), and checks the explicit nondirected fork.

Exact output after successful completion:

```
n=1: preorders=1, frames=2
n=2: preorders=4, frames=64
n=3: preorders=29, frames=14848
fork: distributivity valid, R[w] not downward directed
VERIFY_OK: frames=14914; valid=9587; invalid=5327
```

The theorem for arbitrary finite size follows from a symbolic proof, not induction from these small-frame tests. No proof is supplied for infinite frames. An external independent audit has not been performed.
