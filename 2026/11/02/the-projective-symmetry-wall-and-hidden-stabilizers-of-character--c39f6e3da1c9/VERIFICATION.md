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

# Reproducibility and limits

Run `python3 verify.py` using Python 3 with no external packages. The verifier enumerates the full \(\mathrm{PGL}_3(\mathbb F_2)\) and checks exact characteristic-two defining-equation preservation for \(q=2,4,8,16\). It also computes the kernel dimension of the linearized coefficient constraints modulo projective scalars and tests that the dimension equals three in these cases.

Observed results:

```
q=2: PGL3(F2) stabilizer count=2, Lie dimension=3
q=4: PGL3(F2) stabilizer count=1, Lie dimension=3
q=8: PGL3(F2) stabilizer count=1, Lie dimension=3
q=16: PGL3(F2) stabilizer count=1, Lie dimension=3
VERIFY_OK
```

The exhaustive enumeration is only over \(\mathbb F_2\), not an algebraic closure; the infinite-family classification uses coefficient comparison on the normalization and does not depend on finite computation. The exact closed subgroup scheme is verified algebraically in the proof by \(q\)-th-power identities and an explicit coordinate ring. The complete stabilizer group scheme is not determined. No independent audit has been performed.
