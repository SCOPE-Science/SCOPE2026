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

The finite-ring argument relies on the exact identities \(f(u)=v\), \(f(v)=u\) and \(f'(u)f'(v)=-4\), followed by a two-sublattice Fourier decomposition of the full two-step derivative. Every fibre has eigenvalues \(a^2\cos^2 k-4(1-a)^2\pm4ia(1-a)\cos k\); their moduli are \(a^2\cos^2 k+4(1-a)^2\), maximized at the admitted zero wave number. The \(\ell^2\) extension uses the operator-valued Fourier multiplier and the pointwise quadratic remainder bound.

The embedded `verify_checker.py` was executed with Python 3 and returned `CHECKS_OK: 997 direct lattice identities and Floquet determinant tests`. It constructs the actual finite-ring Jacobians and verifies their action against the derived Fourier matrices for six even sizes and eight couplings, including the doubled-neighbour convention at size two. This numerical run does not certify the theorem for all sizes or all real parameters: those conclusions depend on the written proof.

At \(a=3/5\), the linear spectrum is neutral; nonlinear critical dynamics is not analyzed. At \(a=1\), the period-two family is nonisolated. The theorem does not identify global attraction basins or exclude other recurrent configurations. Originality evidence is limited by incomplete access to the 2002 Dettmann full text and by the possibility of unindexed equivalent calculations.
