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

## Reproduction
Use Python 3 with SymPy and run `python verify.py`. The program recursively enumerates all perfect matchings with one through seven chord pairs. It checks 84 rational mean/covariance identities involving crossings, nestings and alignments, explicitly enumerates 90 interleavings of three labeled chords, and independently evaluates the exact projection integrals symbolically. The recorded check was `VERIFY_OK 146599 84`.

## Mathematical limits
A finite matching census cannot establish the claimed weak convergence as the number of chords tends to infinity. That follows from the proof's exact independent-chord representation, first-order projection covariance, degenerate-remainder variance bound, and multivariate central limit theorem. The complete finite-sample bivariate generating function is known in the literature; the asserted contribution is the joint asymptotic independence statement.
