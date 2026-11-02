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

For independent common-target random mappings f(i)~p, write Z as sum of empty indegree indicators and T as pairwise 2-cycle indicators. On event f(i)=j,f(j)=i, the other n−2 arrows avoid each v outside {i,j} with probability (1−p_v)^(n−2). Summing p_i p_j yields exact Cov(Z,T)=((1+s2)V−2s2W)/2. If P assumes value p_i with probability p_i and h(t)=(1−t)^(n−2), monotonicity gives V=E[Ph(P)]≤E[P]E[h(P)]=s2 W. Thus Cov(Z,T)≤−s2(1−s2)W/2<0 when at least two positive p_i. Equality for n=2 (h constant) or equal positive probabilities for n>2 (h strictly decreasing). For fixed-point count F, conditional on any vertex absent, outgoing choices renormalize other p_j and E[F|I_v=1]=1, yielding Cov(Z,F)=0 even with zero weights. Independent exact Fraction enumeration checked n=3 uniform p=(1/3,1/3,1/3): −2/27, heterogeneous p=(1/2,1/3,1/6): −1/12, and p=(1/2,1/2,0): −1/16, plus zero Cov(Z,F). Source exact-rational checker was inspected, not treated as infinite proof.

## originality

PASS

Earlier uniform random mapping cycle work (Finch) and Hansen–Jaworski exchangeable-indegree models provide relevant formulas/frameworks, but do not in examined material establish this sharp all-p common-target negative covariance. Nonuniform p-mapping indegrees are generally nonexchangeable, so an exchangeability-only theorem does not directly cover the target; a broader generating-function identity may still imply it and is a priority risk.

## value

PASS

Sources (zero-indegree vertices) and short directed cycles are basic functional-digraph observables. An exact all-n all-common-target-p sign bound, sharp equality cases, and contrasting fixed-point zero covariance reveal a universal dependence phenomenon absent from uniform-only mapping laws. The bound is quantitative and structured, not a routine numerical covariance sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
