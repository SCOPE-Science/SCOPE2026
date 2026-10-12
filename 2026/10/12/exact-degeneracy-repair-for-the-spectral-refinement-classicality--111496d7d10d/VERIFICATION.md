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

The accepted claim is proved analytically in finite dimension. No finite experiment is used as evidence for an infinite statement.

The critical checks are:

1. A product basis diagonalizing a classical-classical state necessarily refines the spectral subspaces of both reduced states after taking partial traces.
2. Conversely, commutation with all rank-one projectors from one complete product refinement makes the state diagonal in that product basis.
3. If the commutation holds for every spectral refinement, then inside each \(P_\alpha\otimes Q_\beta\) block the state commutes with every rank-one product projector. These projectors generate the full matrix algebra on the block, so the state is scalar there.
4. For \(\rho_{cc}=\tfrac12(|00\rangle\langle00|+|11\rangle\langle11|)\), computational-basis dephasing fixes the state, whereas local \(X\)-basis dephasing gives \(I/4\).

The literature comparison distinguishes the new theorem from the already-known observation that measurement-induced disturbance is ambiguous for degenerate marginals. The remaining originality risk is an obscure prior statement of the same elementary commutant characterization.
