---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Color \(K_{t+2}\) red on a Hamilton cycle and blue off the cycle. For a proposed left pair \(x,y\), an orderable coloring of the whole \(K_{2,t}\) requires one of the two alternating classes \(V_{rb},V_{br}\) to be empty. On a cycle, each of \(x,y\) has a neighbor not shared in the required direction, so both alternating classes are nonempty; hence no orderable spanning \(K_{2,t}\) occurs. With only two colors there is no rainbow triangle, proving both lower bounds. The actual verifier checks all left pairs for \(3\le t\le50\) and directly checks all orderings for the smallest cases. Substitution into the cited upper \(r'_2(K_{2,t})\le CR(K_{2,t},K_3)\le\lfloor4t/3\rfloor+2\) gives 7 and 8 for \(t=4,5\).

## originality

PASS

Li’s primary abstract gives the \(4t/3+o(t)\) asymptotic for \(K_{2,t}\) and exact values for infinitely many t, but targeted searches did not locate the universal Hamilton-cycle lower bound or the specific exact pairs \(t=4,5\). The earlier small canonical-Ramsey paper studies \(K_{2,4}\) against bipartite rainbow targets, not the audited \(K_3\) target in the material located.

## value

PASS

The Hamilton-cycle coloring is a uniform explicit obstruction for a natural new Ramsey parameter, and matching it to the best available upper bound settles the first two nontrivial biclique cases beyond the smallest example. The result is modest but mathematically motivated and not just a table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
