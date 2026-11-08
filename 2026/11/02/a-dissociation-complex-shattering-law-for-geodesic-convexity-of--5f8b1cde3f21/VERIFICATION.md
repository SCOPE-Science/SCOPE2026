---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For wheel W_{m+1}=K1∨C_m, m>=5, rim pairs distance 2 force both hub and intermediate rim vertex. Hence convex sets without hub are only empty, singletons, adjacent pairs, and hub-containing convex sets correspond exactly to rim 0/1 words avoiding local 101. A rim support cannot shatter if it contains a triple of cyclic consecutive rim vertices; otherwise every positive trace T is realized by including hub and making each designated negative rim vertex and at least one neighbor outside the support negative, so no 101 remains. Hub-containing supports have at most one queried rim vertex or two adjacent rim vertices by the hub-negative trace. The rim-support face numbers therefore equal D(C_m;z), with additional z+m z²+m z³. Marking a zero in cyclic words with ones-runs <=2 gives exact m/(m-k)[t^k](1+t+t²)^(m-k). Summing triple inequalities gives |S|<=floor(2m/3), achieved by runs of 110; hub triples tie at m=5 only. Independent actual geodesic convex-set enumeration verified the full support structure for m=5..9 and polynomial coefficients. This is a proof for every m>=5, not extrapolation from small wheels.

## originality

PASS

The dissociation complex of a cycle is a classical combinatorial object, and the graph-convexity learning framework is also prior. The new scientific claim is the exact equivalence between all shattered geodesic-convex supports of a wheel and cyclic dissociation configurations together with precisely classified hub exceptions and exact face polynomial. The primary 2022 graph convex online-learning paper gives general bounds but not this wheel complex; 2023 dissociation enumeration is not itself a learning-theory shattering statement.

## value

PASS

The result gives a natural complete shattering-complex classification on an infinite graph family, exact VC dimension and all face numbers including the exceptional boundary. It identifies how adding one universal hub changes convex learning combinatorics, not an arbitrary finite slice or known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
