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

For K_N every edge pair determines a unique rank-two flat; hence distinct flats meet in at most one edge. A nonstar family contains a triple A,B,C with three distinct pair-intersection edges e,f,g. Their three-edge graph has four admissible incidence types (three disjoint, exactly one meeting pair, two meeting pairs as a 4-path, or a 3-star); a three-cycle would yield duplicate flats. Enumerating every flat meeting the triple yields exactly the 3-,4-,5-member extensions. Full edge stars have size C(N-1,2) and become maximal for N>=5, while N=4 stars extend. Exact counts and boundaries follow from choosing supports. Fresh independent bitset maximal-clique enumeration: n=4 histogram {5:3}, n=5 {6:10,5:15,4:10}, n=6 {10:15,5:45,4:60,3:15}; finite checks corroborate, not prove all N.

## originality

PASS

The primary Cao–Liao–Zhang preprint establishes the known sharp nonstar upper bound five and unique maximum nonstar type, which this assessment expressly credits. Its inspected Lemma 3.6 does not give the smaller inclusion-maximal clique types or the all-N enumeration. No found published mathematical record covers those finer saturation data. Best-of-knowledge novelty restricted to complete inclusion-maximal census, not generic extremal EKR/Hilton–Milner results.

## value

PASS

Inclusion-maximal intersecting families are the saturation/clique spectrum of the natural rank-two partition-flat intersection graph, not simply the EKR maximum. Classifying every maximal form, its occurrence multiplicity and minimum saturated size (5,4,3 at N=4,5,>=6) resolves a well-motivated complete enumeration for all ground sizes; it is not a single arbitrary instance or routine restatement of the largest-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
