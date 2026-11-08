---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For 0<a<1 the time map has strictly positive derivative rho=(T/2)(1-a cos(2pi(sigma-c))). The physical slew rate of affine pseudotime u=u0+K tau is |K|/rho; saturating the tightest nodal inequality yields exactly (1-a max_node cos(2pi(s-c)))/(1-a). The closest circular node distance increases to half the largest cyclic gap at its midpoint, hence the sharp worst-phase (1-a cos(pi*g))/(1-a). All N cyclic gaps sum to one, so g>=1/N uniquely for equally spaced phases. For the two-point right Radau mesh normalized nodes {0,1/3}, g=2/3 and amplitude a=9/10 gives 29/2. The stated ceiling sample-count, N^-2 expansion and endpoint domain follow by solving this formula. Verified independent numeric mesh instances and exact rational Radau witness; no finite check replaces this proof.

## originality

PASS

Nodewise rate enforcement and harmonic non-affine time maps predate this work, and the circle-covering lemma is elementary/known; the specifically optimized sharp continuous-to-node physical-time rate factor for affine pseudotime controls was not located in relevant inspected results. This is best-of-knowledge priority, not ownership of mesh circle covering or of nodewise constraints.

## value

PASS

Inter-node actuator slew-rate feasibility is operationally and mathematically natural in pseudospectral transcription. The exact amplification for any mesh and phase, unique minimax mesh, sharp N-dependent safety margin and concrete fLGR factor 14.5 form a useful all-mesh quantitative boundary, not an arbitrary grid observation. Its value is limited to the affine-control subspace and the chosen harmonic map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
