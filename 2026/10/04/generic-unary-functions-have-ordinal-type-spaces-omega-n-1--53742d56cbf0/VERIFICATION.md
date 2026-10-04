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

The mathematical proof in `RESULT.md` is the primary verification. The bundled checker tests the two local term-diagram operations on which the Cantor--Bendixson induction rests.

For every canonical mixed diagram on at most five variables obtained from fixed-point finite components and free infinite components, and for observation depths through six, it records all equalities among the terms \(f^a(x_i)\) visible up to that depth. It then closes each free component into a cycle strictly after the observation horizon and confirms that the visible equality diagram is unchanged while the number of infinite components drops by exactly one.

Separately, for one-variable eventually periodic diagrams with tail lengths and cycle lengths through six, it constructs the finite conjunction consisting of the first repeated equality together with all earlier inequalities and checks that this finite data uniquely fixes all later equalities in a bounded replay.

Replay command:

`python3 artifacts/verify.py`

Recorded output:

```text
prefix_closure_checks 4186
one_variable_eventual_periodic_checks 14665
VERIFY_OK
```

These are finite consistency checks only. They do not replace the infinite proof that every first new equality beyond a stabilized prefix either closes one ray or merges two rays, nor the induction identifying all Cantor--Bendixson derivatives.
