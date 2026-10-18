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

# Verification and reproducibility

The finite check uses `verify.py` and only the Python standard library. Run `python verify.py` from a directory containing the extracted file. Successful output:

```
VERIFY_OK exact_two_way_checks=2398 additional_large_checks=5
```

For every integer \(3\le n\le2400\), one implementation enumerates mixed lower-plus-upper Wythoff representations using exact floor values derived from integer square roots. A distinct implementation counts the three cases of the rotation formula by evaluating signs in \(\mathbb Q(\sqrt5)\) exactly. The two counts agree for all 2398 tested integers and five further larger values satisfy the permitted bound. The checker also confirms \(0\le r(n)\le K(n)\).

The checker is finite; it does **not** certify the infinite error bounds or a universal originality claim. The analytic proof of all infinite statements, including the atom and the uniform distribution error, is in `RESULT.md`, Sections 1–6. No independent external review or validation has been performed.
