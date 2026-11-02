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

# Verification and limits

Execute `python3 verify.py` using the Python standard library. Reproduction output:

```text
p=3: full commutator-fiber distribution verified, null_nonzero=20, anisotropic=60; PASS
p=5: full commutator-fiber distribution verified, null_nonzero=104, anisotropic=520; PASS
p=7: nonzero contractions rank 3 and no decomposable kernel; PASS
p=11: nonzero contractions rank 3 and no decomposable kernel; PASS
VERIFY_OK
```

For \(q=3\), every one of \(3^8=6561\) ordered quotient pairs was checked against the four target coordinates and the target quadratic form. For \(q=5\), all \(5^8=390625\) ordered quotient pairs were checked similarly. The checker also verifies surjectivity and every nonzero contraction for the four indicated prime fields. These calculations do not exhaust prime powers or prove the general theorem. The mathematical proof establishes the universal result using the Plücker equation, the norm map, and an exact quadratic-cone count.

No external or independent assessment is represented by these tests.
