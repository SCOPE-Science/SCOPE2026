---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Indicator linearity gives EF1=sum_i a_i*C(N-a_i,k-1)/C(N,k). The exact marginal D(a)=f(a+1)-f(a) decreases then increases (terminal zero tail), permitting pairwise transfers: concentrate all but at most one high abundance, and balance the low remaining entries. For k=2 f(a)=a(N-a) is globally concave and optimal balanced. Thus at least one global maximizing profile has the stated one-distinguished-L, S-1-nearly-equal shape. For k_N/N->rho in (0,1), singleton probability p_N(a) converges uniformly in a>=1 to h_rho(a)=a*rho*(1-rho)^(a-1), whose unique integer maximum away from reciprocal rho is m=floor(1/rho). Since one abundance must diverge with N and the other S-1 slots can equal m, a strict gap forces eventual unique maximizing multiset. Independently exhaustive all integer abundance partitions across 1,029 triples 3<=N<=21, 2<=S<=6, 2<=k<=N matched the finite envelope. Finite checks do not prove the asymptotic statement.

## originality

PASS

Heck et al. address mean/variance of *richness*, not the maximization of expected sample-singletons at fixed N,S,k. Locey-White study feasible abundance distributions rather than this objective. Bhimaraju et al. prove a general concave/convex continuous resource-allocation structural optimization, which is relevant prior methodology but not the discrete hypergeometric envelope or fixed-S reciprocal-density staircase. Their structural method is openly credited; the proposed combined ecology-specific theorem remains a best-of-knowledge contribution.

## value

PASS

Sample-singleton counts drive ecological richness diagnostics and coverage estimators; an exact worst-case expected singleton envelope at fixed community richness/abundance is a mathematically natural uncertainty/benchmark question. The reciprocal sampling-fraction staircase and eventual unique macroscopic-versus-rare species structure reveal a nontrivial qualitative change, beyond merely recomputing known rarefaction expectations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
