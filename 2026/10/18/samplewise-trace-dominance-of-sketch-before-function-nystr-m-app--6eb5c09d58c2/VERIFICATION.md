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

# Verification scope

The theorem is proved in `RESULT.md`, equations (3)–(8). The compression lemma is justified via the positive resolvent integral representation and a Schur-complement inverse inequality; the projector derivative is checked by differentiating its full-rank factorization after restriction to the common spectral support. These analytical steps, rather than sampling, establish the universal statement.

The supplied `verify.py` executed successfully using the declared NumPy dependency, producing: `PASS: exact two-dimensional witness and 38400 finite numerical comparisons`. Its exact witness uses the rational inequality `153>125` and the negative determinant of the difference of two rank-one matrices. Its numerical tests evaluate 3-, 4-, and 7-dimensional positive-definite spectra, multiple sketch ranks, five operator-monotone functions, and three points of the spectral homotopy. Random comparisons cannot certify a universal assertion or novelty. No independent validation has been performed.
