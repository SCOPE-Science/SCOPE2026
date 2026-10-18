---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The exact bond-percolation objective is M_v(p)=1+2S_v(p)/(n-1), S_v counting connected residual unordered pairs by unique path length. Reimplemented all 18,248 Prüfer-word labeled trees for n=2..7, independently counted the distance coefficient profiles, verified a candidate vertex with nonnegative degree-five Bernstein coefficients of every S_u-S_w; the certificate covers the entire real p interval, not just sampled p. Independently derived all eight spider S_v for arms (1,1,5) and the exact optimizer switch at α²+α³=1. For n>=8, center uniquely wins for small p from unique maximal degree three, but at p=1 center has S_c−S_b=n−7>0; continuity forces failure near one. The finite census proof is exact for n<=7, while all-n construction is symbolic.

## originality

PASS

Newman, Chen et al. establish susceptibility/pair-connectivity framework, and Holme analyzes vaccination effect/optimizers on small networks; none of the inspected main results asserts the sharp n<=7 universal tree optimum in independent-edge transmission or the exact eight-vertex threshold switching. Related rank-order dependence and a potentially relevant Holme 2004 article pose residual risk.

## value

PASS

An exact first-order counterexample and universal cutoff for all smaller finite trees resolve a natural structural optimal-intervention question. The all-n spider proves the threshold is not a tiny one-off instance, and the switch parameter is exact; model assumptions remain narrow and explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
