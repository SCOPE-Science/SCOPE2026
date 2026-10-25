---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For H=span{1,e^{it}}, normalized 2x2 concentration Gram matrix has diagonal a/pi and offdiagonal Z/(2pi), yielding top eigenvalue a/pi+|Z|/(2pi). Rotate by Fourier moment phase so Z=|Z|>0. Missing density inside centred arc and added density outside each have mass m, values [0,1]. Strict monotonicity of cos geodesic distance gives sharp bathtub rearrangements: missing inside contributes at least 2(sin a-sin(a-m/2)); added outside contributes at most 2(sin(a+m/2)-sin a). Thus |Z|<=2sin a(2cos(m/2)-1), yielding the exact deficit and m<2pi/3 since |Z|>0. Equality uniquely fixes both boundary caps as indicator densities, giving the explicit central arc plus two outer caps E_{a,m}; direct phase integration verifies Z>0 and realizes every geometrically feasible m. Taylor coefficient sin a/(4pi) follows. Symbolic cap integration and 200 independent 4096-grid phase-centred random soft-mask comparisons corroborate; grid tolerance is nonrigorous.

## originality

PASS

Two-mode sharp cosine-profile quantitative rigidity at fixed Fourier-centred exchanged mass and uniqueness among all fractional masks are more precise than the known arc-maximizing qualitative concentration theorem; related sphere-polynomial and real-line stability results concern different spaces and may inspire proofs but do not directly give this exact profile.

## value

PASS

Natural exact rank-two spectral concentration and stability modulus: sharp nonlinear loss plus all equality masks, robust even to fractional observation, clarifies both geometrically feasible exchange and phase-alignment threshold. A self-contained sharp finite-dimensional extremal inequality with boundary characterization, not a mere endpoint exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
