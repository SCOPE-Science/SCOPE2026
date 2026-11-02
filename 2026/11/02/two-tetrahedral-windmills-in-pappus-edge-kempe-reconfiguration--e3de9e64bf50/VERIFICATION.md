---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact verification

The certificate records all 27 graph edges, all 120 named proper colourings as ternary words in lexicographic edge order, all 324 undirected Kempe moves as symmetric adjacency lists, the two named-colour components, the 20 colour-unlabelled palette orbits and their quotient adjacency, the two tetrahedral-windmill components, and the switching base-graph automorphism.

To regenerate and compare the certificate using the LCF construction, run:

`python3 verify_lcf.py --check certificate.json`

To independently reconstruct the base graph from nine point-line incidence triples, enumerate its 42 perfect matchings and all 20 one-factorizations, recompute the Kempe graph and its all-source distances, and compare the complete result to the certificate, run:

`python3 verify_incidence.py certificate.json`

Both scripts use only the standard library and were executed successfully from the delivered source files. The first prints `LCF_EXHAUSTIVE_KEMPE_PASS`; the second prints `INCIDENCE_MATCHING_INDEPENDENT_PASS` and `INCIDENCE_KEMPE_METRIC_PASS`. Exact checks include 120 states, 324 edges, two isomorphic components of size 60 with 162 edges each, radius and diameter four, degree multiplicities (54,6) at (5,9), unordered distance counts (162,540,738,330), and both quotient components \(K_1\vee(3K_3)\). Searches or computations on smaller subsets alone would not establish the global claim; these scripts enumerate every state.

Limitations: the result certifies exact finite arithmetic and exhaustive graph enumeration for this specified graph, not scientific priority in all historical publications. Independent external audit was not performed.
