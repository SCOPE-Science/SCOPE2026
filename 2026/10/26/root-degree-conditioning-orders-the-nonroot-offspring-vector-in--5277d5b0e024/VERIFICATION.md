---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS: Reconstructed independent root Bernoulli indicators B_j with P(B_j=1)=1/(j-1) and independent alternative parents U_j uniform in {2,...,j-1}. Conditional on R=k+1, root-attachment subset A has fixed-cardinality weights product_{j in A}1/(j-2)/e_k. The weighted-subset inclusion lemma follows by induction using Newton log-concavity of the elementary symmetric functions and monotonic Bernoulli coupling for the final indicator, then chaining adjacent couplings. Shared U_j yields C_v[k+1]=sum_{j>v}1{j not in A_k}1{U_j=v}, so each coordinate decreases and leaf indicators increase. On independent event U_j=j-1 for every j>=3, probability 1/(n-2)!, each new root attachment deletes the previous parent’s only child, making the leaf count strictly larger at every adjacent k. Independently enumerated exact parent sequences for n=3..8 and checked all strict leaf means and all upward principal leaf-set events by root degree.

## originality

PASS

PASS (best of knowledge, not priority certification): Compared claims and logical implications with the located primary texts and published records. The specific claim is not stated as covered in the materials actually read; any implicit-specialization or inaccessible-full-text risk is separately documented. Neither matching mathematical terminology nor unsuccessful search alone was treated as conclusive originality evidence.

## value

PASS

PASS: This gives a simultaneous multivariate stochastic order under every exact root degree, controlling all increasing functionals of the nonroot offspring vector and all monotone leaf-set events, not merely one covariance or mean. Conditional degree ordering is a natural recursive-tree structural invariant, and exact-level joint control is useful for conditional occupancy and leaf events.

The dated certificate retains the supplied scientific assessment, sources and limitations.
