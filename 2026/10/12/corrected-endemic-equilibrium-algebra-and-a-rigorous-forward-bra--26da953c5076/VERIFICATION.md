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

The proof is analytic and follows directly from the printed SEIQHRA equations.

The verification script performs the following independent checks:

1. Reconstructs the source baseline parameters and confirms \(R_0=\lambda/\lambda_c\).
2. Solves the corrected scalar equation \(\Psi(A,\lambda)=0\) by bisection.
3. Reconstructs \(S,E,I,Q,H,R,A\) and verifies that every ODE residual is numerically zero.
4. Evaluates the source's printed infected coordinate at the same \(S^*\) and \(A^*\).
5. Confirms that its susceptible residual equals
\[
(\Pi-dS^*)\frac{cA^*}{1+cA^*}
\]
to numerical precision.
6. Checks the signs \(\Psi_\lambda>0\) and \(\Psi_A<0\) at the disease-free threshold, which imply \(dA/d\lambda>0\) locally.

Unproved limits: global uniqueness of endemic equilibria away from the threshold, the full endemic spectrum, and the reported Hopf bifurcation diagram are not certified here.
