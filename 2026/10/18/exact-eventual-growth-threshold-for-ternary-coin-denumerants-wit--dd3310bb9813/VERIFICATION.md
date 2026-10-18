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

The exact arithmetic verifier is `artifacts/verify.py`, executable with `python3 artifacts/verify.py` from the package root. It uses only the Python standard library and independently constructs the coin-denumerant sequence by dynamic programming. It compares 408502 exact identities or differences, including the six-residue two-coin formula, all adjacent differences in a finite two-parameter test window, the last plateau for each coprime parameter, and repeated descents for noncoprime parameters. Expected output: `VERIFY_OK 408502`.

The all-parameter theorem is proved analytically by an exact residue formula; bounded computation cannot validate infinitely many parameters or indices. Earlier possible literature coverage is a residual risk. Independent mathematical audit has not been performed.
