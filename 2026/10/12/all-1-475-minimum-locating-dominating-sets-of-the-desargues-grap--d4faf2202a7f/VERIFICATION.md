---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The graph is the twenty-vertex bipartite Kneser H(5,2), ten two-subsets on each shore with adjacency on disjointness. Ordinary open-neighborhood locating-domination is imposed only on vertices outside the chosen code. For any seven-vertex code, the 10-b right-side unchosen signatures have to be distinct nonzero subsets of a left a-set; this and its symmetric counterpart force (a,b)=(3,4) up to shore swapping. Six signatures on three selected left edges must use exactly nine available incidences: three singleton and three doubleton signatures. The three left edges must be mutually intersecting. Triangle forces a forbidden triple signature from the complementary right edge; a three-edge star forces the right code to be the four star edges and leaves the fourth left star edge undominated. Thus no seven-code exists and monotonicity eliminates smaller codes; five explicit double-star eight-codes show sharpness. Independently enumerated all C(20,8)=125970 eight-masks by directly generating open signatures from the actual H(5,2) graph: exactly 1475 valid, distributed 300/875/300 for left weights 3/4/5. Independently generated the S5 permutations plus side exchange, verifying the supplied thirteen representatives have disjoint orbits covering all 1475 with listed sizes. The distance-two graph on either shore is L(K5), whose five size-four maximal star cliques recover S5 and show the automorphism group has order 240. The source verify.py also implements the complete 2^20 all-code cross-check, but its success log is not substituted for this proof or the independent eight-mask census.

## originality

PASS

Best-of-knowledge novelty is the exact 1475-code census and thirteen orbit representatives, not the known Desargues incidence model, 240 automorphisms, or location-domination definitions. Similar graph-identification parameters, identifying codes, global location-domination, and complete multipartite location-domination do not imply the reported Desargues optimum orbit count.

## value

PASS

The twenty-vertex Desargues graph is a canonical exceptionally symmetric cubic bipartite graph. Its exact optimum locating-dominating sets and all thirteen full-automorphism orbit types form a motivated self-contained finite code classification not implied by the graph degree, automorphism count, or a bare known domination number; they provide explicit canonical benchmark data for location codes and incidence geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
