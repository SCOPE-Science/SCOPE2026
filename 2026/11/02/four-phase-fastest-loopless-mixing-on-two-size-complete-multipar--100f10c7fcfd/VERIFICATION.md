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

For p,q>=2 independent parts of sizes a,b>=1, group-averaging any symmetric row-stochastic zero-diagonal nonnegative kernel over within-part and same-size part permutations does not increase centered operator norm. The invariant family has one variable x=qb w_AB in [0,min(1,1/r)], r=pa/(qb), and exact nonconstant eigenvalues -(1-x)/(p-1), -(1-rx)/(q-1), and 1-(1+r)x plus zeros. Thus SLEM is max of three affine absolute-value branches; decreasing-vs-increasing minimax gives unique invariant x*=min(cap,max(p/(p+(p-1)r),q/(q-1+qr))). This yields four exact r-phases with boundaries 1/q,p/q,p; global optimality follows by convex averaging, not uniqueness of all global kernels. Independent exact-rational scalar minimax on 6 parameter configurations and 501-point rational grids reproduced the branches and boundary deletion patterns; a finite grid cannot prove global optimality, supplied convex proof does.

## originality

PASS

Best-of-knowledge PASS: Boyd–Diaconis–Parrilo–Xiao reduce a broader complete multipartite fastest mixing problem to a block-diagonal SDP with holding transitions, but do not solve the zero-diagonal two-part-size minimax or identify its four thresholds in inspected Section 5.3.2. The full invariant solution and support deletion boundaries are neither a trivial rescaling nor implied by their displayed with-loops SDP.

## value

PASS

PASS: fastest symmetric mixing with no self-loops is a natural constrained Markov-chain optimization; the attained global SLEM, four sharp analytic phases and support deletion transitions for all p,q,a,b give exact nontrivial structural results beyond general SDP formulations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
