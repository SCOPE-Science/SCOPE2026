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

The included `verification/verify.py` uses Python 3 standard library only. Execute from the package directory with:

```sh
python3 verification/verify.py
```

It independently enumerates every monotone frame map in three feasible small cases and checks surjectivity and every upward back condition over the actual finite inclusion relation. It also enumerates every proper labelled edge-colouring of \(K_2\), \(K_4\), and \(K_6\) and evaluates the theorem's closed expression for \(m=2,3,4,5\). The embedded `verification/verify_output.txt` is the output obtained by executing that program directly before packaging.

This checks only the listed finite instances. The proof's unrestricted quantifiers, factorization correspondence, uniqueness, and parity restriction are established by the mathematical argument in `RESULT.md`, not by extrapolation from data. Computational enumeration is reproducibility evidence, not an independent proof certification. Independent audit: not performed.
