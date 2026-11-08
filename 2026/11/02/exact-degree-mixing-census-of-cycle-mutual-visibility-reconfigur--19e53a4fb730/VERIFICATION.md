---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The visibility criterion for three occupied cycle vertices is the exhaustive positive cyclic gap constraints a,b,c<=floor(n/2), with sum n; each clockwise slide transfers one gap unit subject to min1/maxh. Counting oriented ordered compositions and dividing by three gives all degree counts. Boundary gap classifications and edge-type handshakes give each exact even/odd joint-degree matrix. At n=3..6 all exceptional cases were separately checked. Independent original-cycle geodesic BFS and slide graph construction for n=3..24 match the complete vertex/edge-type tables; the all-n formulas follow from the gap and handshake proof rather than test extrapolation.

## originality

PASS

Primary same-model 2026 mutual-visibility cycle manuscript provides the gap criterion and layer connectedness; prior visibility polynomial counts configurations by size, and related local distance/isometry result gives graph metric. None of the inspected or accessible statements supplies these complete endpoint-degree transition matrices. Best-knowledge PASS with limited full-text access.

## value

PASS

Three-token mutual visibility is the maximum nontrivial layer for cycles. The complete endpoint-degree adjacency matrix characterizes a natural reconfiguration Markov chain far beyond connectivity or pairwise distance, including parity-sensitive transitions and stationary bottleneck mass; a researcher may need these exact edge counts, without implying spectral mixing times.

The dated certificate retains the supplied scientific assessment, sources and limitations.
