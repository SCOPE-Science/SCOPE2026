---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Reconstructing the graph from the published overlap definition gives exactly 81 vertices and 237 undirected loop-free edges. The supplied colouring assigns all vertices to three classes of sizes 28, 30 and 23 and the verifier checks every edge is bichromatic. The three vertices 0000, 0001 and 1000 form a triangle, so two colours are impossible. A fresh independent DSATUR-style reconstruction found a valid three-colouring and independently confirmed the same vertex/edge counts and triangle. The standard theorem then implies word-representability.

## originality

PASS

Petyuk's defining paper states the opposite universal conjecture for all \(n\ge4,k\ge3\). The later Huang–Kitaev–Pyatkin paper was materially read in full: it explicitly restates that conjecture, recalls that every 3-colourable graph is word-representable, and proves positive results only for restricted induced subgraphs \(S_m(n,k)\), not the full \(S(4,3)\). A current MathDB entry still labels the conjecture open and records no progress. Resultary searches found no prior colouring or positive full-graph statement.

## value

PASS

This is the smallest parameter pair in the conjectured negative region and a complete finite certificate directly refutes an explicit conjecture that a later paper and current problem database still treat as open. That is a decisive natural boundary result, not an arbitrary graph computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
