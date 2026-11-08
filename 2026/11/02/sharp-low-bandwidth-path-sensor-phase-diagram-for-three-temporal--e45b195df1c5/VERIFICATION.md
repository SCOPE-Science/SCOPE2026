---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The normalized path has cosine eigenvectors |v_k(x)|²=c_k d_x cos²(πkx/M). On the first K eigenmodes, K consecutive time samples factor into an invertible spectral Vandermonde times diag(v_k(x)), giving ratio d_x^K∏_{k=1}^{K−1}cos²(πkx/M). K=2,3 reduce to elementary trigonometric monotonicity and finite small M. For K=4 the signed product reduces to P(u)=8u³−10u²+3u; its derivative and bound |P(u)|<1/3 on u≤3/4 plus first-neighbor P(cos²(π/M))>1/3 at M≥9 and exact M=3,…,8 classify every tie. Independently enumerated all predicted maximizing locations for every M≤100, K=2,3,4, PASS. Symbolic polynomial bounds and Vandermonde furnish all-length proof; finite data alone does not.

## originality

PASS

Full-spectrum endpoint-optimal theorem materially compared and not logically dominant; 2026 motivating primary paper inaccessible in full, with explicit residual overlap risk and only bounded originality judgment.

## value

PASS

A complete and motivated fixed-low-band D-optimal sensor-location classification for normalized paths, including nonmonotone finite phase transitions and an endpoint-to-neighbor shift, useful for dynamical sampling design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
