---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For each key a, conditional on m=|X_a|, every Y-value in X_a creates m-1 mismatches and every Y-value outside creates m; independent Bernoulli Y facts give (1-r+rt^{m-1})^m(1-r+rt^m)^{q-m}. Binomial averaging and independence of all q keys give exactly the stated PGF G_q(t)^q, with m=0 interpreted as one. W=0 per key iff X_a empty, Y_a empty or X_a=Y_a an identical singleton; inclusion/exclusion gives the exact probability. In balanced sparsity each key has one mismatching pair with probability ab/q+o(1/q) and multiple pair mass o(1/q), yielding Poisson(ab). In asymmetric sparsity the rare Y singleton occurs with probability b/q+o(1/q) and the number of mismatches converges from Bin(q-1,p_q) to Poisson(a); the PGF limit exp{b(exp(a(t-1))-1)} is compound Poisson with jump distribution Poisson(a). The expectation q²(q-1)pr -> ab and compound variance ab(1+a) check role and normalization. Independently enumerated all relation pairs for q=1,2,3 (4,256,262144 cases), exact zero counts (4,81,5832), and the first moments; that finite enumeration is regression evidence only.

## originality

PASS

Polyteam Semantics defines the cross-team poly-dependence atom but does not analyze independent tuple sampling. The 1998 single-table random functional-dependency model gives an exponential rare-violation law for a different sampling scheme, and Amarilli–Kimelfeld investigates complexity of query reliability, not this full PGF or asymmetric compound-Poisson limit. No directly covering result was retrieved through Resultary/web queries in cross-team relation sampling and random database integrity. Related general rare-subgraph/join Poisson approximation could subsume one or both limits; the originality conclusion is best-of-knowledge subject to this concrete residual risk.

## value

PASS

A natural database integrity atom leads to an explicit finite satisfaction polynomial and two sharp sparse laws at the same limiting mean but inequivalent clustering and violation-free probabilities. This exposes the distributional effect of sharing one rare tuple with multiple matches, a mechanism that the expected count cannot distinguish; useful for calibrating random database reliability beyond generic model-counting complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
