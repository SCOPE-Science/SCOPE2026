---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The specified 2L side vertices and L+1 backbone vertices yield BB*=K with diag(2,4,...,4,2) and off-diagonal g=2cos(φ/2). For 0<φ<2π, B has full backbone row rank, so the initially populated backbone has no zero side-mode component; when g!=0 irreducibility ensures a sink-observed component in every nonzero K mode. The exact dissipative reduction q’=w−(γ/2)E0q, w’=−Kq has energy norm |q|²+w*K^{-1}w with derivative −γ|q0|². At g=0 the distal ±i√2 oscillator is spectrally separated; the normalized distal eigenmode qL=1 propagates q0=−2g^L/(γs2^(L−1))(1+O(g)) to the sink and has physical squared norm →2. Its loss rate is g^(2L)/(γ4^(L−1))(1+O(g)); its two modes carry total leading survival weight one. Other damped modes contribute lower-order integrals; oscillatory interference terms have bounded integrals. Since g∼−(φ−π), T∼γ4^(L−1)|φ−π|^(−2L). At φ=π, g=0 blocks backbone propagation and survival is identically one. Independently verified exact Gramian formulas for L=1,2,3,4, consistent with the asymptotic coefficient; separately constructed magnetic complex Hamiltonian active-space Gramians matched checks for L=1..5 at two fluxes and two loss rates. Tests support but never replace the perturbation proof for every fixed L.

## originality

PASS

Best-of-knowledge originality: the sharp remote-end mean absorption detuning coefficient is not stated or directly implied by the inspected sources. Prior art owns AB caging, graph sink criterion, and some flux-dependent hopping mechanisms; this final theorem additionally requires the source-specific distal eigenmode amplitude and energy dissipation calculation. Literature gaps, especially inaccessible primary full text, remain recorded; no exhaustive priority claim.

## value

PASS

A natural first-passage observable for the canonical AB-caged magnetic diamond chain is not captured by knowing only that the half-flux spectrum cages. It quantifies how the distance of a terminal sink across L rhombi sharply amplifies phase-detuning sensitivity: the exponent grows by two per plaquette, with an explicit loss-dependent prefactor. This precise nonuniform tolerance boundary is a natural useful transport fact for finite photonic/excitonic interferometric arrays, not an arbitrary small numerical slice or textbook normalization check. It does not promise uniform growing-length or weak-loss limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
