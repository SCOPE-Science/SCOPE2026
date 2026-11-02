---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For K_p square K_q (2<=p<=q), an empty row/column forces weight >=2p; otherwise all row/column supports are nonempty, changing every label two to one lowers weight without invalidating positive support or zero-site two-neighbor requirements. The associated bipartite incidence graph then has no isolated vertices or single-edge component. With c<=min(p,floor((p+q)/3)), at least p+q-c edges are needed, and a spanning forest construction attains that bound. For p=q=n, ceil(4n/3)<2n, so every optimum has no twos, and equality forces a forest with floor(2n/3) components of order>=3. The bipartite Cayley tree count a^(b-1)b^(a-1) plus excess-vertex profiles (all size3, one size4, or one size5/two size4) derives the three rational closed formulas, including n=2 boundary. Independently checked all labelings for five rectangular boards and coefficient-DP counts n=2..10.

## originality

PASS

Classical double-domination equivalence and scalar rook-graph 2-tuple domination are acknowledged. The assessed novel result is complete structure and enumeration of every minimum labeled configuration across all n, not the scalar minimum itself. Full 2009 rook article remains a substantial priority risk but abstract advertises bounds/scalar values rather than the complete forest census.

## value

PASS

The complete labeled census of optimal double-dominating supports is a natural infinite graph family invariant, with a structural spanning-forest bijection and nontrivial modular enumeration. This is more substantial than the already-known scalar minimum and uses the mathematical geometry of row/column incidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
