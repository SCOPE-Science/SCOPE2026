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

# Reproduction

Execute `python verify_quadrupole.py` alongside this document. The script constructs the five standard degree-two complex spherical harmonics directly from the Cartesian sample coordinates and compares their full Gram matrix with the diagonal formula for six ring sizes, three longitude offsets and ten heights, including the extremal and singular latitudes. It also checks the optimizer identities and 9,999 numeric sample heights. Observed output: `PASS: 180 independent raw harmonic Gram identities; 9999 height comparisons`.

The proof is symbolic: discrete azimuthal orthogonality requires only \(m\ge5\), and all inequalities are explicit elementary polynomial or rational inequalities. The tests are floating-point checks with absolute tolerance \(2\cdot10^{-11}\), not exact arithmetic verification and not independent mathematical validation. No experimental search or numerical scan is used to establish uniqueness for the continuum of heights.
