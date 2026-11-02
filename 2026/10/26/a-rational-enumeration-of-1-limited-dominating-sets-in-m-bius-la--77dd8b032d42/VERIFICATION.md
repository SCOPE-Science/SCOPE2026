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

A 1-limited set is encoded by white bits in two-vertex twisted columns; each vertex condition becomes c_{i-1,r}+c_{i+1,r}+c_{i,1-r}<=1+c_{i,r}. The 16-state ordered-column transfer with twist J correctly counts each labeled configuration once. The signed trace splits into 7-dimensional symmetric and 3-dimensional antisymmetric cyclic cores; exact independent symbolic determinants equal (1-tz)(1-Q(t,z)) and 1-tz+t²z. Formal -t partial_t log(det) yields all F_n, and deficit a-b of Q monomials gives the sharp degree and multiplicities. The n=1,2 series coefficients are auxiliary, not claims for simple cubic graphs. The example F3=1+6z+9z², F4=1+8z+12z²+8z³+4z⁴ checks complement weighting. Brute enumeration of all subsets for n=3..8 matches the transfer profiles; no infinite result is claimed from finite checks.

## originality

PASS

The new contribution is the all-cardinality 1-limited domination polynomial and non-0-mod-4 optimum multiplicities, not the previously known minimum cardinality or 4 optimum sets in the 0-mod-4 case. Relevant 2026 1-limited-domination papers study Cartesian products and Goldberg snarks; an OEIS/Möbius-ladder minimal dominating-set count concerns inclusion-minimal ordinary domination, a distinct predicate. Resultary semantic search returned domination polynomial results for chain and multipartite graphs, not this Möbius ladder predicate. This supports qualified best-of-knowledge originality, not absence of unindexed older enumerators.

## value

PASS

The exact generating function simultaneously counts every feasible size of 1-limited dominating sets on a natural, widely used cubic graph family. It refines a previously known extremal domination number and supplies previously uncatalogued optimum multiplicities in two other residue classes. Such enumerators are natural complete invariants and reusable for asymptotic or probabilistic combinatorics; the result is not merely recomputing a small finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
