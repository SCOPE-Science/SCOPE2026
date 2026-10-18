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

# Exact checks and independently testable limits

The standalone exact checker is `artifacts/check_five_puncture_morse.py`, run with Python 3 and SymPy. Its expected terminal line is `FIVE_PUNCTURE_ACCIDENTAL_MORSE_OK`. The checker starts from the printed symmetric matrix, not an assumed expansion. It confirms the determinant expansion and the normal Hessian factorization symbolically over the rational polynomial ring, as well as a concrete rank-four matrix witness.

The continuous mathematical conclusion for **all** \((s,t)\in (\mathbb C\setminus\{\pm2\})^2\) comes from the nonzero polynomial identity for the Hessian determinant, the analytic Morse lemma with parameters, and the global square root governing the complex-orthogonal orientation cover. Finitely many numerical samples would not establish it. The integral monodromy statement is about moving **along** the singular stratum; the Picard–Lefschetz action in the smoothing parameter is not being claimed trivial.

The analysis does not inspect the unaccessible complete earlier Simpson chapter, so prior-coverage uncertainty persists. It does not extend the singularity assertion to the excluded parameter boundary or to the full twenty-coordinate character variety. No independently performed mathematical audit is claimed.
