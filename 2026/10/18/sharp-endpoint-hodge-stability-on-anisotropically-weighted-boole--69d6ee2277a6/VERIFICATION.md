---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

On actual frozen RESULT.md c929b4..., checked Walsh eigenvalue 2 sum_{k∈S} c_k, gradient derivative −2sqrt(c_i) chi_S, heat-kernel integrals (4)–(5) with strictly positive factors 1±exp(−c_k t). Same-direction |row| mass sums to 1; cross-direction mass sqrt(c_i c_j)/(c_i+c_j). Matrix induced ℓ∞ norm is max absolute row sum; AM–GM provides upper (d+1)/2 and equal-weight equality, geometric anisotropy approaches unattained 1. All d≥2 c_i>0 constant per direction, energy normalization explicit; real/complex ℓ∞. Independently rebuilt grounded weighted Laplacian projector (not Walsh) for d=2,3,4 with 3 diverse weight vectors: norms 1.5, 1.86153846, 2.35854875 match, idempotence/symmetry within 1.4e−15.

## originality

PASS

Best-of-knowledge no statement discovered of the simultaneous anisotropically weighted Boolean-cube ℓ² edge-gradient projection exact ℓ∞ norm, all signed row entries and complete range; known transfer-current kernel and Walsh techniques are credited, not independent discoveries.

## value

PASS

Graph Hodge projection is foundational. Direction-sensitive ℓ∞ amplification controls worst bounded edge-data error under a Hilbert-optimal reconstruction, including exact anisotropy suppression and extremizing signs; it is nontrivial as Euclidean orthogonality offers no ℓ∞ norm bound below r-type growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
