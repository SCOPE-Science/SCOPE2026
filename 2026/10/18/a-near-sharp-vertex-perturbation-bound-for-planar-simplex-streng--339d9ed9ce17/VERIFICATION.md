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

# Reproduction of exact algebra checks

The standalone file `checker.py` requires Python 3 and SymPy and should be executed from the same directory using `python checker.py`. Successful output reports `PASS` and the analytic coefficient bracket.

The program checks the elliptic-coordinate gradient identity symbolically; expands the inequality \(|\nabla\sigma|^2\le9/1024\) to the stated exact polynomial; verifies the tail positivity expansions after shifting \(t\) by \(1/2\); calculates all rational degree-seven Bernstein coefficients on each of eight rational subintervals for both polynomials; and differentiates the explicit isosceles witness. The analytic proof in `RESULT.md` explains how these computations imply the global result, including collinear and coincident-vertex cases.

These are ordinary reproducible algebra checks; no independent external mathematical audit or optimality proof of \(3/32\) is asserted.
