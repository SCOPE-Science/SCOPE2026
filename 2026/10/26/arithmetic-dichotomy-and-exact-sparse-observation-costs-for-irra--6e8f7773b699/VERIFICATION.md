---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: Independently checked proof from the actual binary coding: a unique circle phase exists because each nonzero phase translation changes the interval indicator on an open arc, sampled densely by irrational rotation. Phase fibers are singleton except endpoint orbits; one-sided limits differ at one time if boundary orbits differ, at two times separated by |k| otherwise. Every winning schedule must hit all translates of [-R,R] or the union of two such intervals. Every nonempty periodic covering schedule separates distinct phases by density of each arithmetic progression n≡r mod period, and separates same-phase endpoints by covering, establishing equality with κ. A finite 2^(q+2R)-state de Bruijn graph attains the covering min mean on a cycle. For q=5,R=1, independently constructed 128 vertices and 252 edges; integer Bellman-Ford relaxation has no negative cycle at cost 11b−2, and a 2/11 period11 schedule covers all shifts. Bounds and algorithm are exact; finite graph is not a proof of irrational phase dynamics.

## originality

PASS

PASS qualified: Ferrari 2026 introduced observer–hider cost and necessary finite-witness covering lower bound; asymptotic Sturmian pairs are classical. The extra global periodic upper bound for irrational rotation codings and exact dichotomy between disjoint/same endpoint orbits is not established by the accessible material. The relevant Ferrari full paper was inaccessible despite OA/arxiv attempts and authorized Oxford tool returned vpn_disconnected, an explicit priority risk rather than automatic O failure.

## value

PASS

PASS: This supplies a complete exact observation-cost solution for a natural minimal, zero-entropy, non-SFT dynamical family. The dichotomy controlled by whether cut endpoints share an irrational orbit is an exact arithmetic-geometric classification, with algorithmic rational costs and a nontrivial 2/11 instance, directly addressing a substantive open model class beyond the source SFT examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
