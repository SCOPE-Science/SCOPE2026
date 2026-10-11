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

Fresh reconstruction of the generalized Petersen graph \(G(8,3)\) gives \(24\) edges and exactly \(11068\) matchings including the empty matching, with face vector \((24,228,1096,2826,3816,2444,600,33)\). Replaying the package's staged edge-toggle matching leaves one critical \(0\)-cell, ten critical \(4\)-cells, and six critical \(5\)-cells; the full reversed-cover digraph has \(53256\) covers and is acyclic. An independent gradient-path calculation gives a \(10\times6\) integral Morse boundary of rank two whose first two determinantal divisors are both one, so its Smith form is \(\operatorname{diag}(1,1,0,0,0,0)\). The \(4\)-skeleton is therefore \(\bigvee^{10}S^4\), and \(\pi_4(\bigvee^{10}S^4)\cong\mathbb Z^{10}\); pre- and postcomposition by unimodular basis changes reduces the attaching map to Smith form. Two \(4/5\)-cell pairs cancel and four \(5\)-cells attach trivially, yielding \(\bigvee^8S^4\vee\bigvee^4S^5\).

## originality

PASS

Donovan and Scoville's complete primary article treats ordinary matching complexes of paths, cycles, centipedes, and Dutch windmills, and targeted full-text searches contain no Möbius--Kantor occurrence. Current Resultary search returns the assigned \(G(8,3)\) record as the exact same-object hit and nearby but different finite matching/Morse complexes. Exact web searches under both Möbius--Kantor and \(G(8,3)\) found no independent homotopy calculation. The manifold-matching, outerplanar, and Möbius-ladder literature concerns different graph classes or different simplicial-complex functors and does not imply this mixed-dimensional wedge.

## value

PASS

The Möbius--Kantor graph is a canonical highly symmetric cubic graph, and its ordinary matching complex is a natural combinatorial-topology invariant. The exact result exhibits sphere summands in two adjacent dimensions and requires a complete signed Morse certificate rather than a small-table lookup, making it a meaningful finite benchmark for how matching-complex topology changes beyond the standard graph families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
