---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Read original printed equation (5.2) and Hamiltonian/costates (5.3) from the actual publisher PDF page 8. Differentiation w.r.t S gives −∂H/∂S=λ1(aE+v)−λ2 aE, a=(1−u2)θ(I),v=µ+z0u1; print has −λ2(aE+v), introducing −vλ2. Independently expanded all three Hamiltonian gradients by symbolic differentiation (SymPy), which agrees with source for costates 2 and 3 but not costate 1. With terminal λ3=λ2=λ1=0 and positive infection penalty C3, λ3(T−τ)=C3τ+..., hence λ2(T−τ)=α C3 τ²/2+...; since v≥µ>0, the source discrepancy is nonzero near T, not algebraically equivalent. This diagnoses necessary conditions, not actual implementation or displayed numerical trajectories.

## originality

PASS

The paper itself prints the inconsistent first costate; no published erratum or exact replacement equation was found by author-title, DOI, equation 5.3, costate and corrigendum searches. Resultary contains unrelated SEIR/SQEIAR adjoint corrections in distinct models and an earlier same-model endemic-equilibrium finding that does not analyze Pontryagin adjoints. Elementary derivation does not make an unreported, consequential specific published error known before this correction.

## value

PASS

A printed necessary condition in a concrete published optimal-control epidemic model has an active sign/variable error, changing the backward boundary-value system and therefore the mathematical basis for reported optimal interventions. Identifying and correcting that specific inconsistency with a nonvanishing terminal witness is useful even though differentiation itself is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
