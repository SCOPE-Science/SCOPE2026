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

The reproducible checker is `checker.py` and requires Python 3 and only the standard library. Run `python3 checker.py` alongside this document. The replay of the included program enumerated every binary relation on the \((m+1)\)-world coalescing fan for \(m=1,2,3\), testing each source axiom literally, testing the normal-form predicate, and checking whether every world relates to itself. Its outputs were:

```
m=1: checked=16, all=7, reflexive=4
m=2: checked=512, all=89, reflexive=36
m=3: checked=65536, all=5119, reflexive=1000
VERIFY_OK
```

The checker also independently confirms each top-successor-row stratum for those finite instances and compares the direct closed formula to a differently expressed weighted finite sum for every \(1\le m\le30\). These checks do **not** prove the formulas for arbitrary size; the general argument is in the case classification, binomial identities, and asymptotic expansion of `RESULT.md`.

Verification is mathematical/software replay and self-review only; no independent scientific audit has been conducted, and no external certification is represented.
