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

Directly from open-neighborhood trace definitions, an LD-set of K_{m,n}, m,n≥2, omits at most one vertex per shore, giving gamma_L=m+n-2. For K_{1,n} (n≥2), gamma_L=n. The explicit partition V\{y1,y2}, {y1}, {y2} with y1,y2 in a shore of size ≥3 supplies three coalition blocks; P3 uses all singleton blocks. K2,2 has four singleton coalition blocks and the general bound n-gamma_L+2≤4. For any hypothetical four-block partition of a larger biclique, two coalition partners cover all but exactly one vertex on each shore, hence the other two blocks are opposite-shore singletons; analyzing their required partners forces an LD two-vertex set and therefore m=n=2, contradiction. K2 has none because each singleton is already LD. An independent complete set-partition enumeration for all m≤n,total vertices≤8 confirmed 16 small profiles; this corroborates the all-size structural proof.

## originality

PASS

The initiating Chellali et al paper proves a universal upper bound n-gamma_L+2, plus paths/cycles and extremal graph classes, which cover P3 and C4 as small cases but give only ≤4 for a generic nonstar biclique. The proof of the infinite exact value 3 needs a nontrivial four-block partner-complement obstruction. An actual text search of the complete primary PDF found no occurrence of bipartite.

## value

PASS

Provides the complete first canonical nontrivial biclique family for the newly defined coalition invariant, with a sharp unique four-block exception and an all-size obstruction argument. The classification improves the universal upper bound on infinitely many graphs and goes beyond a numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
