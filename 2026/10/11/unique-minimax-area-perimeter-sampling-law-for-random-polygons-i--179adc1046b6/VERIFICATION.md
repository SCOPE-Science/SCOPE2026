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

# Reproducibility and limits

The analytic proof in `RESULT.md` establishes the exact continuum theorem using the boundary-sampling intrinsic-volume asymptotic, planar ellipse geometry, Hölder's inequality, strict concavity, and uniform Taylor expansion. No external numerical certificate or independent audit is claimed.

Run `python verify_ellipse_minimax.py` using the Python standard library. The program checks ten ellipticities, uses 32,768 midpoint angular samples, computes the unique balancing weight by bisection, verifies that both normalized objectives equal the scalar dual value to a tolerance of \(3\times10^{-10}\), and checks the near-circle \(3/8\) expansion. It terminates with `ELLIPSE_MINIMAX_STANDARD_LIBRARY_CHECKS_OK` if all tests pass. Quadrature results are approximate and provide sanity checks only, not a computer-assisted proof for all inputs.

The checked source date for the motivating theorem is the arXiv version-1 submission on 2026-02-20, rather than the manuscript's displayed internal date. The application addresses only fixed strictly positive continuous sampling densities and leading \(N^{-2}\) asymptotics.
