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

Each site update x_v←x_v+sum_neighbor x_u over F2 is an involution; product is bijective. Shore parity quotient is two-dimensional and the full transformation factors as T=I+H Q where H is injective because fixed points are exactly ker Q. Iterate T^k=I+H(sum_{j<k}P^j)Q. The matrices S_A,S_B generate GL₂(F₂)=S₃; odd-length words have transposition order two, giving least periods 1,2,4 in explicit populations; even words either P=I (periods 1,2) or P has order three (periods 1,3). The product of alternating dihedral reflections has translation parity determined by b−2r mod3, and exact labelled orders are a!b!sum binom(m,r)binom(m,b−r). Independent exhaustive bit-level updates for 878 distinct labelled schedules on K_{1,1}, K_{1,2}, K_{2,1}, K_{2,2}, K_{2,3}, K_{3,3} checked each finite state orbit and schedule split, including 16/8 for K22 and 72/648 for K33. The analytic group proof covers all sizes.

## originality

PASS

Classic asynchronous cellular automata papers classify cyclic graph rules and update-order invariance; Huang and Sjöstrand describe whole transvection-group orbits, not periodic cycles of a fixed single-scan Coxeter word. The closest mathematically indexed complete-multipartite parity census uses simultaneous updates, with different map and period behavior. No exact modulo-three scan/labelled schedule classification was identified in these compared results; general Coxeter theory could contain an equivalent implicit theorem.

## value

PASS

An exact complete classification of state orbit periods and labelled schedule frequencies for a natural asynchronous XOR update on every complete bipartite graph. A simple odd/even-position mod-three invariant explains the switch from primitive two- to three-cycles, and the odd-order four-cycle regime. This is a motivated scheduling law, not an arbitrary test graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
