---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The equality fibre product W={u^a=v^b} is path connected: each finite solution follows (t^b u,t^a v) to (0,0) and infinity connects to (1,1) by reciprocal scaling, while both projections are onto. A strict planner near (0,0) would induce continuous functions h(x)^b=x^a and k(y)^a=y^b on small endpoint slices; winding around punctured disks forces b|a and a|b, hence a=b. Unequal exponents have no local planner even near one point, so TC=∞ despite synchronizability. Equal exponents duplicate any 3-set standard sphere path planner. Homotopy invariant lower bound follows because (a u-b v)^2=-2ab uv is nonzero in Q[u,v]/(u²,v²); upper bound pulls back a 3-set sphere ordinary planner to F,G. Independently checked exact fibre-product scaling identity for 128 exponent/time pairs; cohomology and winding arguments are exact universal proofs.

## originality

PASS

The full 2026 García-Calcines–Vilches Alarcón primary paper defines both invariants, proves general inequalities and in Example 3.4 obtains only cohomological lower bound two for arbitrary degree-2 and degree-3 maps S²->S². It does NOT determine strict infinity for the explicit branched power maps or the all-parameter winding classification. The homogeneous unbranched circle-cover examples and nonsynchronizable examples are mathematically different. Thus the exact strict-vs-homotopy gap is not a corollary of the example; priority remains best-of-knowledge.

## value

PASS

The exact branch-order criterion distinguishes pointwise synchronized motion feasibility from existence of even a single continuous local planner; it gives an all-positive-exponent classification and an infinite-versus-two gap in a canonical simply connected branched setting, directly sharpening a concrete degree-two/three example from the defining primary work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
