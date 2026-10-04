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

The source vector field was checked against both the conference full text and the expanded journal article. Direct elimination shows that every equilibrium has \(x=y\); either \(x=0\), giving the full line \((0,0,z)\), or \(z=0\) and \(a|x|-bx^3-x^2=0\), which yields the isolated branches described in RESULT.md.

`artifacts/verify_equilibria.py` reconstructs the isolated-equilibrium Jacobian and verifies symbolically that its characteristic polynomial is
\[
\lambda^3+3r^2\lambda^2-br^3\lambda+3r^4(1+2br).
\]
It also verifies the exact source-parameter roots and the \(ab=2/9\) factorization. The script was executed from the packaged path and its output was recorded in `artifacts/verification_output.txt`.

The proof does not use finite-time simulation to establish equilibrium existence, eigenvalue counts, or hidden-attractor status. The final basin-related statement is only that the source's line-only argument is insufficient; no unproved basin intersection is asserted.
