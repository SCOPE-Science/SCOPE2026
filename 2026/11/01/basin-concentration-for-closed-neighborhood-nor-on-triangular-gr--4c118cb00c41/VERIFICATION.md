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

PASS: For the line graph L(K_n), a target edge is disjoint from every initially active base edge exactly when both endpoints are outside U(S), giving the literal self-inclusive F(S)=E([n]\U(S)). The case |U|>=n-1 maps to empty; 2<=|U|<=n-2 maps to complementary complete-edge set, then back, so F³=F and no fixed point. Unordered complementary vertex sets with both sides>=2 yield 2^(n-1)-n cycles; support-exact labelled graphs are c_m by inclusion–exclusion. Thus the full basin sizes follow. c_n>= (2^(n-2)-1)² c_{n-2}>2c_{n-2} shows strict dominance. Under G(n,1/2), exceptional basins are exactly the union of events two specified isolated vertices, EXCEPT the empty graph; Bonferroni pair/triple/four-isolate probabilities yield C(n,2)2^-(2n-3) and relative error O(n2^-n). Independent literal closed-neighborhood state enumeration n=4,5,6 (33856 states) matched all cycle/basin claims; proofs cover all n.

## originality

PASS

PASS with disclosed risk: The general NOR/minterm or maxterm two-cycle restriction is already known in Aledo et al, and the 2020 periodic-point classification explicitly covers some regular graphs. The full 2020 article was materially inspected, including Proposition 1, Corollary 3 and its (N-2)-regular cases; its counts do not give a separate initial-state attraction-fiber census or probability of a single basin. Here the complete individual basins c_m+c_{n-m} plus sharp isolate-pair asymptotic are the distinctive contribution. The 2012 maxterm/minterm primary source is abstract-only; authorized full-text retrieval failed due institutional VPN, recorded as risk not NOT_COVERING.

## value

PASS

PASS: L(K_n) is a canonical vertex-transitive graph family with exponentially many periodic orbits. Exactly which orbit is reached from a typical state is a natural dynamical invariant unavailable from period-count results. The theorem gives all individual basin cardinalities and the sharp exponentially small fraction avoiding the unique dominant basin, a nontrivial structural asymptotic over all n, not an arbitrary small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
