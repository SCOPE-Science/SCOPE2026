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

# Reproduction notes

The package includes `verify.py`, a complete Python 3 standard-library checker. Run `python3 verify.py` in the directory containing the file. Expected terminal marker: `VERIFY_OK`.

The program computes exact coefficients of the sixth power of \(F(z)=(z-1)(z^2+t z+1)\) over \(\mathbb F_{13}[t,z]\), compares the four critical factor identities, constructs the full \(5\times5\) Hasse--Witt matrix, and verifies its rank over every smooth \(\mathbb F_{169}\) parameter. It also checks the determinant polynomial and all six exceptional parameters. The explicit factor identities and prime-field diagonalizing basis supply the infinite-algebraically-closed-field proof; the finite census is a regression test.

Scope exclusions: parameter-isomorphism quotient, Newton polygons, and global characteristic variation. No independent mathematical audit has been performed.
