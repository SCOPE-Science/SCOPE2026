---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Np(rho)=(1-p)rho+(p/3)(XrhoX+YrhoY+ZrhoZ) has Bloch contraction alpha=1-4p/3, hence Np(UrhoUdagger)=U Np(rho) Udagger for every unitary. Isotropic semigroup channels commute with all pulse conjugations, so any finite interleaved sequence equals overall pulse-frame rotation composed with the unchanged total-time depolarization. Original Appendix average is Np of the input Pauli twirl (I/2 for balanced I,X,Y,Z); in the frame-corrected version every term is just Np(rho). Printed p exp(-gamma/f) tends to p, not 0. This is an exact analytic proof, scoped to the specified memoryless isotropic channel and ideal unitary pulses, not microscopic colored baths.

## originality

PASS

PASS, best of knowledge: covariance itself is standard, not claimed original. The source-specific contradiction between arXiv:2605.16463v1 Appendix proof and the channel it defines is different from the indexed same-source post-channel LOCC relative-entropy correction. The four comparisons exclude that competing correction as an implication and distinguish Uhrig’s non-Markovian microscopic pure-dephasing assumptions.

## value

PASS

PASS: the source uses the claimed effective p′<p pulse-compressed channel to support a principal pre-channel entanglement advantage. Demonstrating that no such improvement is possible for its explicit CPTP depolarizing noise model corrects a consequential modeling step, not merely a context-free covariance exercise. Clear limitation to ideal unitaries/Markovian isotropic noise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
