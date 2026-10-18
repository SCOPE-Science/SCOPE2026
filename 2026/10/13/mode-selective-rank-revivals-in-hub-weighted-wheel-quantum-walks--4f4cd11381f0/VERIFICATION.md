---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For real g>0, invariant hub/uniform-rim plane has eigenvalues 1±sqrt(1+ng²); rim Fourier projectors Q_k have distinct energies 2cos(2πk/n). Collision with λ_- occurs exactly when a negative µ_k obeys ng²=µ_k(µ_k−2), at one k. The finite-spectrum Cesaro formula Mhat=Σ eigenspace F∘F requires fusion at collision, adding αQ_k with α=(1−(1+ng²)^(-1/2))/n>0. Fourier Schur convolution gives baseline rim nonconstant eigenvalues 1/n for odd n and 2/n on even-indexed modes, zero on odd-indexed modes for even n; hub/uniform sector eigenvalues 1 and β. Thus exact spectrum, rank and kernel follow, including antipodal single-mode revival. Independent direct symmetric Hamiltonian diagonalizations/projector squares verified 39 test cases and seven resonances with max eigenvalue comparison error 1.33e−15; numerical evidence is not the proof.

## originality

PASS

The spectral-projector identity, circulant Fourier calculus, and unweighted wheel parity rank are prior art. The full variable spoke-weight family has exact collision loci and discontinuous extra rank in selected Fourier modes; Lo et al exclude these degeneracies in their stated join result. The novel claim is the precise all-g spectral/rank/kernel classification, not the general Schur-square method.

## value

PASS

The phase-transition-like isolated restoration of modes destroyed by even-cycle Fourier parity is a concrete spectral transport phenomenon, with exact controllable coupling thresholds and full kernel classification for a canonical graph family. Genericity-only formulas miss these physically and mathematically important degeneracies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
