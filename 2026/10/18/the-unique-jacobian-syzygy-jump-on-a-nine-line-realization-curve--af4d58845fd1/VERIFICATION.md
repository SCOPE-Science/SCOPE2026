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

# Exact verification and scope

Run `python verify.py` with Python 3 and SymPy. The script checks all \(84\) triple determinants for the nine displayed dual points, identifying exactly \(11\) prescribed zeros. Every other nonzero determinant has only the factors \(a\), \(a-1\), \(a^2-a+1\), proving that there are no hidden additional triple flats anywhere in the stated parameter domain.

The script constructs the \(20\times12\) matrix for degree-four logarithmic derivations by restricting to the four remaining line equations. It verifies the exact selected minor
\[
a^{14}(a-2)(a-1)^{20}(a^2-a+1)^3,
\]
proves the displayed vector lies in the kernel at \(a=2\), and verifies a second selected minor equals \(-5898240\) there. All equalities are carried out in \(\mathbf Q[a]\) or \(\mathbf Q\); the infinite-dimensional parameter conclusion follows by symbolic factorization and the proof in `RESULT.md`, not by sampling. A standard degree-five relation follows from a fourfold point and Euler's identity and is established algebraically in `RESULT.md`.

Checks do not concern excluded degeneration parameters or positive characteristic. No independent audit has been performed.
