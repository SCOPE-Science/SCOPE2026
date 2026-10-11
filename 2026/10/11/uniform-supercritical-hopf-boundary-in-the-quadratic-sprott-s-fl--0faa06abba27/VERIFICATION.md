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
# Verification details

Exact symbolic checks in `verify_hopf.py` reconstruct the Hopf-point Jacobian polynomial, normalized complex eigenvectors, full bilinear second derivative, resolvent terms, first Lyapunov coefficient, and positive crossing rate. The script uses symbolic \(\omega>0\) with \(a=\omega^2\), not finite parameter sampling. It verifies \(l_1(1)=-9/10\). Reproduction: place `verify_hopf.py` in the same directory and run `python verify_hopf.py` with a working SymPy installation.

The nonlinear periodic-orbit existence and its orbital stability follow from the standard nondegenerate Hopf bifurcation theorem once the explicitly verified spectral and sign conditions are established; they are not inferred from experiments. No independent audit has been performed, and no global attractor or parameter-continuation claim is assessed.
