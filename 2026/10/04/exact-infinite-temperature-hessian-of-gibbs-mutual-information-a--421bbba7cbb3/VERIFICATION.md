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

The analytic proof uses only finite-dimensional matrix calculus. The critical identities checked are:

1. For \(h=H-\operatorname{Tr}(H)I/d\), the Gibbs state satisfies \(\rho_\beta=I/d-\beta h/d+O(\beta^2)\).
2. The entropy Hessian at \(I_n/n\) on traceless Hermitian directions is \(-n\operatorname{Tr}(X^2)\).
3. The decomposition \(h=h_A\otimes I_B+I_A\otimes h_B+H_{\mathrm{int}}\) is Hilbert--Schmidt orthogonal, with both partial traces of \(H_{\mathrm{int}}\) equal to zero.
4. Therefore the local quadratic entropy corrections cancel and leave exactly \(\operatorname{Tr}(H_{\mathrm{int}}^2)/(2d)\).
5. For disjoint Ising bonds, tensor-product additivity reduces the calculation to one bond, where direct diagonalization gives \(x\tanh x-\log\cosh x\).

`verify.py` uses a deterministic two-qubit Hamiltonian containing local and noncommuting interaction terms. It computes the Gibbs state by diagonalization, evaluates the three von Neumann entropies, and checks convergence of \(I/\beta^2\) to the analytic coefficient. It separately checks the interaction projection's zero partial traces, the Pauli crossing-string coefficient, and the exact Ising formula. Successful replay prints `VERIFY_OK`.

The numerical replay is not an exhaustive proof and does not certify a thermodynamic limit. No claim is made beyond fixed finite-dimensional systems and the explicitly solved disjoint-bond family.
