---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Reconstructed edge-to-edge line distance as 1+minimum endpoint Hamming distance (off-diagonal); Walsh edge-axis sectors give diagonal F_(n-1)(s,p)-1 and off-diagonal 2 F_(n-2)(s,p). For 0<p<1 Bernstein integral J proves negative all axial/nonprincipal transverse modes; only axis-constant zero-sum multiplicity n-1 has eigenvalue S_n(p)-1. S_n increases from 0 to 2^(n-2); n=2 boundary p=1 handled separately. Centered Schoenberg Gram rank gives n2^(n-1)-n at endpoint; binomial B_n∼2^(n-1)/n and p B_n≤S_n(p)≤p n^p B_n yield p_n∼n/2^(n-1). Independently compared direct BFS cube-edge powered-distance spectra to sector eigenvalues for n=2..4 at distinct powers; no inference for infinite n from finite eigenvalues.

## originality

PASS

Best-of-knowledge comparison of exact final claim against primary mathematical statements and published semantic records; no inspected result covers it. Source access and residual uncertainty are documented, not construed as certainty of novelty.

## value

PASS

Identifies sharp generalized roundness and endpoint isometric embedding dimension of a natural edge-adjacency metric. Intrinsic line-graph metric differs from familiar Hamming vertex metric; explicit cutoff, multiplicity, and dimension dependence are useful for negative-type embeddings and finite metric geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
