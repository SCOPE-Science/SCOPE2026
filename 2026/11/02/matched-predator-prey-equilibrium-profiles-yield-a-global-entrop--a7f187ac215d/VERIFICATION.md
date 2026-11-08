---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For heterogeneous Neumann predator-prey reaction diffusion with positive equilibrium U,V and fixed A,B>0 satisfying AbU=BcV pointwise, the ground-state transform p=u/U,q=v/V converts diffusion to U^-2 div(U² grad p) and V analogue. Derivative of E=integral[A U² h(p)+B V² h(q)] cancels cross-reaction exactly and leaves strictly coercive reaction squares plus nonpositive Fisher terms. Logistic bounds, parabolic regularity, L² dissipation and uniform continuity imply uniform convergence for any strictly positive initial profiles. Symbolically verified cancellation and the explicit nonproportional U,V example with positive r, negative m.

## originality

PASS

Weighted Lyapunov energies and global stability exist for competitive, delayed, or saturating predator-prey models. This finding isolates an exact pointwise matching condition for the specific two-species opposite-sign mass-action Neumann system, with arbitrary positive diffusion and separate nonconstant equilibrium profiles; no generic Hopf obstruction is claimed.

## value

PASS

The checkable structural matching identity prevents heterogeneous predator-prey Hopf oscillation even where positive equilibrium uniqueness alone is insufficient, producing a useful global-stability criterion with an explicit heterogeneous example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
