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
# Verification of the spectral Dirichlet criterion

The supplied `verify.py` reconstructs the six complex Bloch vertex equations of Exner--Pekař, equations (3), (17), and (18). At \(ak=m\pi\) with all four half-period phases it symbolically calculates the exact determinant and compares it with the reduced expression; only a nonzero factor \(64ik^2pq\) and a harmless Bloch-label transposition separate them. The calculation uses symbolic Laurent polynomials with no fitting or numerical root guesses.

The explicit irrational witness is checked using the formula for \(r\) and a direct residual. The mathematical proof that \(0<r<0.017\) uses \(3<\pi<4\), \(\sqrt2,\sqrt3<2\), \(\sin t<t\), and \(\cos t\ge 1-t^2/2\); finite machine precision is not its justification.

The density-one and spectral-interior claims are proved analytically in `RESULT.md` by torus equidistribution and continuity. The verifier does not purport to establish this infinite assertion by enumerating finitely many indices. Run `python3 verify.py` (requires SymPy); a successful run prints `VERIFY_OK`.
