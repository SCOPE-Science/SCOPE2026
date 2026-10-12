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

# Reproducible checks and limits

The accompanying `checker.py` uses the standard library only. Run `python3 checker.py` from the directory containing the extracted files; successful execution ends with `VERIFY_OK`.

For each enumerated square matrix over a prime field, the program explicitly calculates its matrix square, each defining relation's target degree-two normal coordinates, the augmentation scalar, and the rank. It compares the resulting joint multiplicity table to the Gaussian-coefficient formula rather than using that formula for acceptance. Cases: \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)\).

Rectangular maps are tested directly against all quadratic relations and counted for \((n,m,q)=(2,3,2),(3,2,2),(2,2,3),(3,2,3)\), matching \(q^{1+n(m-1)}\). These checks are finite and are not a proof for arbitrary field orders or generator numbers. The general proof is the PBW-normal-form calculation in `RESULT.md`.

No independent audit or validation has been performed.
