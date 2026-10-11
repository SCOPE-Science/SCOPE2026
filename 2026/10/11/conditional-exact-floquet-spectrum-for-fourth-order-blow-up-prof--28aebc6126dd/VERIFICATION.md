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

The Floquet-spectrum claim is algebraic once a nonconstant periodic solution is assumed.

1. The auxiliary linear polynomial is \(P_q(D)=\prod_{j=0}^3(D-\eta+j)\) with \(\eta=-4/(q-1)\).
2. Differentiation gives the phase variational solution \(w'\), hence multiplier \(1\).
3. Direct substitution gives the second variational solution \(e^t(w'-\eta w)\). The cancellation uses only \(4+(q-1)\eta=0\), hence its multiplier is exactly \(e^T\).
4. With \(\sigma=3-2\eta\), reversing the four consecutive factors gives \(P_q(z)=P_q(-\sigma-z)\), so \(L_w^*=e^{\sigma t}L_we^{-\sigma t}\).
5. Formal-adjoint monodromy has reciprocal spectrum, while the exponential conjugacy multiplies every multiplier by \(e^{\sigma T}\). Therefore the spectrum is invariant under \(\mu\mapsto e^{-\sigma T}/\mu\).
6. Applying that involution to \(1\) and \(e^T\) produces the two remaining multipliers. Because the equation is fourth order, the list is complete.

For \(q=3\), \(\eta=-2\) and \(\sigma=7\), so the exact exponents are \(0,1,-7,-8\), matching the prior validated numerical intervals.

Unproved limits: existence for every \(q>1\), uniqueness of the periodic profile, nonlinear basin descriptions, and persistence of the exact pairing after general lower-order perturbations.
