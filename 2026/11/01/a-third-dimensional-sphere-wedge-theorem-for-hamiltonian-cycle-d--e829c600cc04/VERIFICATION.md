---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS. Graph G_n=K_(n,n) with the alternating Hamiltonian 2-factor a_i b_i and a_i b_(i+1) deleted has faces of Ind_2 precisely vertex sets of induced degree<=1. The proof partitions by selected B subset: zero, one, two adjacent/nonadjacent, three and >=4 fibers under sequential toggles in A. For nonconsecutive B pairs there is one four-vertex critical mixed face each, count n(n-3)/2; subsequent B stages pair all remaining pure independent triples and leave (n^2-3n-2)/2 pure critical four-faces and lone a_0. Thus one critical 0-cell and n^2-3n-1 critical 3-cells. The inspected Deshpande–Singh Proposition 2.10 supplies sequential-matching acyclicity, and Forman gives integral wedge of exactly that many S3 (not merely homology). INDEPENDENT Python construction of all graph faces, sequential matching, directed Hasse acyclicity and exact critical sets for n=4..10 corroborated counts 3,9,17,27,39,53,69; infinite n follows from enumerated fiber cases and cited general matching proposition. At n=3 G3 is a matching so Ind2 is a simplex.

## originality

PASS

PASS on best-of-knowledge search and primary comparison. Taylan path/cycle/forest higher-independence cases cover at most isolated n=4 cycle, not the all-n dense bipartite 2-factor deletion. Deshpande–Singh Theorem 3.5 computes higher-independence of *complete* multipartite graphs, n>=4 deleted-edge family is not complete bipartite and its homotopy shifts from S1 to S3. Graph-metric Rips of deleted factor and ordinary independence are different face conditions. No stronger inclusion/duality theorem found to determine the claimed all-n wedge count.

## value

PASS

PASS. Hamiltonian-cycle deletion is a canonical spanning 2-regular factor modification of a dense bipartite graph. The first higher-independence complex changes dimension and gains explicit quadratic sphere count; a full infinite uniform integral homotopy type supplies useful base case for deleted 2-factor topology, not a small arbitrary enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
