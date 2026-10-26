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

# Reproduction and limitations

Run the bundled `verify.py` with Python 3. Its field arithmetic uses explicit polynomial-basis representatives of \(\mathbb F_4\), while the square-zero test applies derivations on \(1,x,y,xy\) directly. It enumerates the full \(q^8\)-point ambient space for each of \(q=2\) and \(q=4\), compares an independent basis-action computation of \(D^2\) against the eight coefficient equations, and checks predicted closed-stratum, open-stratum, and total counts. It prints `VERIFY_OK_WITT2_FROBENIUS_ZERO` only if all assertions pass.

The complete proof for algebraically closed fields and all finite extensions in characteristic two is in `RESULT.md`; the tests verify only two small fields. They do not determine the nonreduced scheme structure, nilpotents of higher restricted exponent, or historical originality.
