---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: For odd n>=5 the explicit even/odd relabeling sends each selected even E_s to odd neighbors O_{s-1},O_s,O_{s+1}. If B consists of selected odd indices, maximality forces A=Z_n\N(B) and cardinality n-2 forces |N(B)|-|B|=2. Circular gap contributions min(g_i,2) imply B is a single proper interval [a,a+b-1] of length 1<=b<=n-3; each such interval yields exactly one maximal independent set. Legal slides add or remove one endpoint, giving the n-by-(n-3) cyclic strip, n(n-3) states, 2n(n-4) edges, degrees 2/4, bipartite connectivity. Lift (a,b) to (L,R)=(a,a+b-1): edges alter one coordinate by a unit while maintaining valid width; monotone interleaving yields the exact L1 geodesic in the strip, modulo diagonal n-translation. The upper distance n from closest lifts and explicit opposite offset at adjacent width show every eccentricity exactly n. Independently enumerate original graph maximal independent sets, all legal slides and BFS for n=5,7,9: vertex counts 10,28,54, all eccentricity sets {5},{7},{9}, degrees n=7 {2:14,4:14}, n=9 {2:18,4:36}. Infinite assertion rests on interval and strip proofs, not enumeration.

## originality

PASS

PASS best of knowledge: graded Möbius-ladder independent domination enumeration already implies vertex number n(n-3), so that number is not claimed new. Relevant token-sliding literature covers unrestricted independent sets, minimum independent dominating sets, or claw-free hosts. An odd Möbius ladder has induced claws and this move must preserve maximality and exact size. None inspected states the complete interval-slide graph, exact all-pair metric, or universal eccentricity n. Related homotopy of independence complexes has a different invariant.

## value

PASS

PASS: Exact shortest paths and self-centeredness are substantive structural invariants of a natural constrained reconfiguration graph, not routine enumeration. The connected nonregular self-centered infinite family (n odd >=7) and canonical geodesic formula are independently reusable in token-slide geometry and independent dominating set reconfiguration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
