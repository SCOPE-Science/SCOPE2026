---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For a fixed tree, the contribution of an edge to the degree-weighted transmission about a root is 2k−1 where k is the size of the component away from the root. Summing gives Σ_v deg(v)s(v)=4W−n(n−1), with unordered W and undirected degrees. The uniform leaf increment pair is (2deg(V)+2,n+s(V)); taking its conditional covariance gives 8W/n²−2(n−1). The path maximizes W by leaf deletion and the bound that ordered distances from one vertex increase by at most one. Thus the conditional covariance is at most −2(n−1)(n−2)/(3n). The conditional means have respective drifts 6−4/n and n+2W/n. Total covariance then gives c_(n+1)=(n+2)c_n/n+8E[W_n]/n²−2(n−1). The mean E[W_n]=n(n+1)H_n−2n² follows from its recurrence at n=1. Dividing the mixed recurrence by (n+1)(n+2) gives the exact increment 8H_n/[n(n+2)]−(2n+14)/[(n+1)(n+2)], the difference of the frozen harmonic bracket at n+1 and n. That bracket vanishes at n=2. Order three is deterministic for both indices; strict negativity follows inductively from the conditional term for every n≥4. The bracket has leading term −2 log n; the two verified primary variance constants give correlation coefficient −3/√(31−3π²) multiplying log(n)/√n. Independent exact-rational enumeration of all 5913 recursive trees across orders 2–8 confirmed the mixed and conditional identities and signs (e.g. c_4=−4/9, c_8=−19953/1225). It did not execute the frozen verifier or substitute for the proof.

## originality

PASS

The supported new increment is the exact mixed covariance of first Zagreb and Wiener indices under the uniform increasing-parent law. The deterministic degree-distance identity and the published marginal constants are credited, as is the exact same pair under the distinct Cayley law. The one-step calculation makes the mixed recurrence possible but is a short consequence of the classical deterministic identity, not an independently broad novelty claim. Neither the same-model root-count profile nor the Cayley calculation gives the recursive-tree degree-square formula.

## value

PASS

Joint size and sign of dependence matter when contrasting a local structural statistic with a global distance statistic on a standard growth model. The exact finite-size covariance shows strict negative dependence in the covariance sense despite a vanishing asymptotic correlation, identifies the log(n)/√n rate and constant, and relates the sign across all sizes to a uniform tree-by-tree growth mechanism. This adds an informative mixed invariant beyond independent marginal variance results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
