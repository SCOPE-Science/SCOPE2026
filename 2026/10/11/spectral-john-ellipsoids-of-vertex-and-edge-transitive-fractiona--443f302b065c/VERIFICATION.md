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

For connected vertex-and-edge transitive d-regular G, K=BBᵀ=dI+A≥0, tr K=nd, λ≤2d. Φ(t)=t(1+dt)V_G(t)/d is strictly increasing on t>0, Φ(0)=0, Φ(1)≥1, so the scalar root is unique in (0,1]. Vertex transitivity makes diagonal BM^{-1}Bᵀ constant V_G(t), edge transitivity gives constant diagonal M^{-1}=1-tV/d. The root implies L=dt/(1+dt) and V=d/[t(1+dt)]. With center a=t/(1+dt) and Σ=ηM^{-1}, η=t/[d(1+dt)], both edge and degree facet support radii equal their slacks a and 1-da. Each defining inequality is a genuine facet when d≥2. The positive John edge/vertex weights p=dt/(1+dt) and q=d/[2(1+dt)] cancel linear normals by Bᵀ1=2·1 and produce Σ^(1/2)(p/a² I+q/(1-da)² BᵀB)Σ^(1/2)=I; this proves global maximum ellipsoid including nonsymmetric competitors. Rank-nullity transfers K spectrum into edge space to compute all semiaxes/volume. For Kdd, eigenvalues 2d,d^(2d-2),0 yield the stated quadratic root. Cyclic Fourier sum and ∫(1+t+t cosθ)^(-1)=1/sqrt(1+2t) yield golden ratio root. Independently evaluated C5,K4,K3,3 using NumPy/SciPy; edge/vertex contacts and John identities had residuals <2e-15. General assertions follow from analytic identities, not finite examples.

## originality

PASS

The complete-graph K_n specialization is explicitly already covered by a separate published exact John theorem; similarly the doubly-substochastic Kdd case has a separate exact theorem. The claim assessed is the all vertex-and-edge-transitive graph spectral classification, including cycles, hypercubes and Petersen and an asymptotic golden-ratio law. Barvinok–Blekherman develop general orbit-ellipsoid tools, but the inspected general statements do not themselves deliver the displayed two-facet-orbit, freely centered spectral root, all contacts and volume for this nonhomogeneous polytope. The broader family therefore has a substantive uncovered mathematical conclusion.

## value

PASS

A natural infinite graph family of fractional matching polytopes receives an exact spectral center, full anisotropic John ellipsoid, volume and all-facet contact certificate. Special graph spectra produce nontrivial bipartite radical and a golden-ratio limiting cycle parameter; the result is a substantive general classification rather than a special-case recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
