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

The exact proof is in `RESULT.md`. Reproduce the finite, independently coded checks by running `python3 verify.py` with Python 3 (only standard library); a complete successful execution is preserved in `verify_output.txt`, ending in `VERIFY_OK`.

Checks performed: the five quartic restriction coefficients in each of all six Grassmann row-echelon charts were compared as symbolic polynomial identities over characteristic three; all rational lines were enumerated from distinct row-echelon matrices over \(\mathbb F_3\) and \(\mathbb F_9\), producing respectively \((40,10,10)\) and \((112,10,10)\) for parameters \((0,1,-1)\); and the matrix Frobenius relation on each additive root space was verified to have order exactly eight on its eight nonzero vectors. No numerical approximation is used.

What the code does not claim: exhaustive enumeration over a finite number of fields cannot prove the orbit structure over every extension; that conclusion follows from the algebraic root-space identities, Grassmannian chart exhaustion and finite-étale argument in the proof. These checks are not an independent scientific audit.
