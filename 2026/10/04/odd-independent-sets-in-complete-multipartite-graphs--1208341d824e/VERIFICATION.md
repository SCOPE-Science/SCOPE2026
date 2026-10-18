---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Every nonempty independent subset of complete multipartite K_(n_1,...,n_r), r>=2, lies in exactly one part. Every vertex in another part sees precisely |S| neighbors of S; those in its own part see zero. Therefore such S is odd-independent iff |S| is odd. Summing binomial coefficients yields I_od(x)=1+Σ_i Σ_(j odd) binom(n_i,j)x^j and the maximum is the greatest odd integer <= max_i n_i, giving equality with alpha(G) precisely when max_i n_i is odd. Independent exhaustive direct-definition replay at (2,3,4) yields counts {0:1,1:9,3:5}, maximum3; general proof exact.

## originality

PASS

No independent published covering implication was located under the checked exact and equivalent formulations.

## value

PASS

Complete closed generating polynomial and equality threshold over the natural classical complete multipartite family, extending beyond irregular bipartite cases and addressing the initiating equality question. The proof is elementary, but this is a motivated broad natural family classification, not an arbitrary tiny computation; do not impose a proof-length bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
