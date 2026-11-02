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
# Verification

`verify.py` is a standalone Python 3 program requiring SymPy and SciPy; run `python verify.py` after installing packages in `requirements.txt`. It checks, without floating-point approximation, the general root-curve derivative, Jacobian determinant and trace identities, and the critical cubic center-manifold coefficient for \(\omega=1,q=2\). It checks an exact nonzero endemic solution and Jacobian sign at \(q=3,\omega=1,\tau=2\), identifies both roots for the bistable example at \(\tau=39/20\), and numerically integrates two long-run critical trajectories with explicit comparison tolerances. Numerical trajectories are demonstrations, not proofs of the asymptotic theorem or exhaustive parameter classification.

The mathematical proof is in `RESULT.md`. Its nonstandard steps are the cooperative corner squeeze, the exact determinant/root-slope identity, and the center-manifold degeneracy calculation. They are reconstructed there without relying on the script, external programs, or prior ledger files. Independent audit and experimental verification of stochastic finite-population dynamics have not been performed.
