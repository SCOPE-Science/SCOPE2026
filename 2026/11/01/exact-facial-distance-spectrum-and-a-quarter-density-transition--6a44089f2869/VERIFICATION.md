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

# Reproducibility and scope

Run `python3 verify_hypersimplex.py` with Python 3.10 or later, from the directory containing the extracted file. Its exact-arithmetic tests compare the symbolic one-simplex quadratic minimum with the proposed face formula for each face-type pair in ambient dimensions 3 through 30, enumerate actual one-swap outside-vertex orbits in small hypersimplices, and exhaustively compare the integer objective over all valid face types against the piecewise global formula. The result in this package was `PASS: 49100 exact rational/integer and vertex-orbit checks`.

Separately, constrained optimization of the two convex hulls with SciPy `SLSQP` was performed on 41 representative face types through dimension ten. The observed numerical squared distances matched the analytic values to approximately \(3\times10^{-13}\) or better. This secondary check used floating-point arithmetic; the embedded standalone verifier requires no SciPy.

The proof in `RESULT.md` covers all integer dimensions and ranks via symmetry, a positive-definite quadratic minimization with explicitly attainable endpoints, and a discrete concave maximization. The finite tests cannot independently certify its universal quantifiers. The special case \(n=2\) is derived directly as a line segment. No external audit, formal proof assistant or third-party certificate is claimed.
