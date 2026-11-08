---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For I_n the undirected untyped incidence graph of K_n (singletons and 2-subsets, no order/sorts), standard rank-q EF equivalence is captured EXACTLY by nested extension-type sets T_{q+1}(a)=(atomic(a),{T_q(a,b):b vertex}) with repetitions discarded. Permutations of unused underlying labels give a complete orbit-representative extension list (old singleton/pair, old+new, new+new). Independently constructed immutable recursive types for n=1..8 and q=1..5; got cutoffs 1,3,4,5,7 and verified the q=5 n7=n8 equality, with 105719 unique (n,tuple,depth) states. The source C++/Python exact recurrence supports n<=10; the support-preserving partial bijection for both n>=2q gives infinite-tail EF equivalence, and finite bridges between cutoff and 2q prove all n. No mere extrapolation of n<=10 is used. Rank-five sharp representative order is 7+binom(7,2)=28, only within this family.

## originality

PASS

Best-of-knowledge PASS: precise 1..5-rank theory thresholds in an unlabeled undirected incidence graph family, distinct from incidence-poset order dimension or matching orbit counts. Numerical cutoff values depend on exact EF types and are not supplied by a general asymptotic graph-depth survey.

## value

PASS

This is a complete sharp finite-rank logical classification for a canonical combinatorial graph family; it gives optimally small family representatives for bounded-depth formulas and reveals a nontrivial fifth-round visibility jump to seven underlying points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
