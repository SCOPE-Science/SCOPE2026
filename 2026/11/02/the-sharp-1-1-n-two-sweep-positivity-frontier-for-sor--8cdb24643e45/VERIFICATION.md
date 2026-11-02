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

# Reproduction and evidence limits

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses only `fractions.Fraction` and built-in operations. It returns:

```text
VERIFY_OK exact assertions = 11368
```

The executable reconstructs each of the first two forward SOR sweeps for basis-vector inputs and compares the resulting exact rational response matrices with the separately computed finite-resolvent formula. Its deterministic cases include symmetric and nonsymmetric strict parts; dimensions \(1\)–\(12\); several relaxation parameters below, at, and above \(1+1/n\); and symmetric path witnesses through dimension \(20\). Exact nonnegativity at the threshold and strict negativity just above are tested in the latter family.

The proof in `RESULT.md` establishes the theorem for **all** integers \(n\ge2\), nonsingular \(M\)-matrices, and nonnegative right-hand sides. Finite tests do not establish universal quantifiers by themselves. No external certified or independent mathematical assessment has been performed. Historical source access limitations and the already-published \(n=2\) case are documented in `REVIEW.md`.
