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

The dependency-free `verify.py` reconstructs all 24 exact rational Bernstein coefficients for the lower polynomial certificate on three intervals and checks that their exact minima exceed two. It verifies the rational upper bound proving the eight-vertex counterexample, and tests 234 Fourier-reconstructed cycle-step matrices against the scalar positivity criterion, along with numerical mass preservation. Four sizes have independently bracketed transition endpoints. Run `python3 verify.py` from the directory containing this document and that source file.

The finite numerical checks are **not** an exhaustive proof over all sizes or steps. The proof uses the positive cycle resolvent, the diagonal ratio comparison, Chebyshev polynomial convexity, and the exact Bernstein positivity certificate. No independent audit has been performed.
