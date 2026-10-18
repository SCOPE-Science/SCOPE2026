---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The high-frequency decomposition u=a+v+z, first harmonic v and complement z, has exact d²=2(1−a), s=d²−d⁴/4, spectral high-mode energy excess Q(z)>=p||z||² with p=q_n or 1. For any candidate sequence with bounded Δ/d⁴, a cubic-deficit coercivity estimate completes the square to force Q(z)=O(d⁴), excluding hidden high-frequency competitors; then z=d²w. The second harmonic g=e²−1, ||g||²=1/2, eigen-excess p gives minimal limiting cubic term 1/4−1/(8p), and the entropy Taylor remainder gives +1/4, yielding 3/4−1/(4p). The explicit first-plus-second harmonic family attains equality. Independently evaluated normalized finite-cycle functions at n=5,6,9,13 for nearest-neighbor and word-length models with r=.002; observed ratios approach all eight predicted constants (maximum discrepancy about 1.7e−4), confirming normalization, not proving arbitrary-direction bound.

## originality

PASS

Chen–Lam–Lu 2026 supply the first/second harmonic family and report these numerical expressions as global upper bounds, but the accessible abstract describes their global lower bounds only at 1/3 and leaves exact global constants unknown for n>=5. The new theorem establishes matching local lower bound across ALL perturbations approaching the constant by high-frequency coercivity; one trial-family upper bound does not imply local optimality. A directly relevant full primary paper remained inaccessible through lawful arXiv/OA attempts and authorized Oxford (vpn_disconnected), a substantial explicitly recorded priority risk; no unfounded whole-paper negative coverage asserted.

## value

PASS

The exact local curvature of the quartic log-Sobolev deficit is a natural variational invariant at its critical constant extremizer. The result resolves whether the known first-plus-second harmonic test construction truly controls all near-constant competitors, and distinguishes local sharpness from unknown global constants, including the circle and word-length cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
