---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Condition on Pi(i)=i, delete that fixed entry, and standardize to uniform sigma in S_{n-1}. Inserting i retains all old upper records, adding exactly one when the first m=i-1 standardized values are {1,...,m}; the event has probability 1/binom(n-1,m). On that event the two blocks are independent uniform permutations, so E[t^R|fixed_i]=[t^(overline(n-1))+(t-1)t^(overline(i-1))t^(overline(n-i))]/(n-1)!. Reflection of the two block sizes gives full conditional distribution symmetry. Differentiation yields Cov(1_{Pi(i)=i},R)=1/(n binom(n-1,i-1))-1/n². Binomial unimodality proves positive exactly i=1,2,n-1,n for n>=5, negative otherwise, and sum over i proves total-fixed-point covariance positive with n times covariance approaching 1. Independent exact enumeration of permutations for n=2..7 verified every conditional mean and reflection, not the all-n theorem. All-complex-t polynomial identity, n>=2; four-label sign result n>=5.

## originality

PASS

Qualified best-of-knowledge: classical record Bernoulli/Stirling law and mesh-pattern expansions are prior, as are total-fixed-point-conditioned asymptotics. The explicit exact generating polynomial for conditioning on a particular one-line fixed point, reflection of the pinned label, four-boundary covariance sign classification and positive aggregate despite negative interiors were not stated/implied by the materially inspected named earlier results.

## value

PASS

The complete conditional law of a standard random permutation statistic under a natural label-pinning event, unexpected reflection symmetry of a directional record count, and position-dependent sign reversal form a coherent finite-sample dependence classification. This is not a relabeling of the marginal Stirling generating function.

The dated certificate retains the supplied scientific assessment, sources and limitations.
