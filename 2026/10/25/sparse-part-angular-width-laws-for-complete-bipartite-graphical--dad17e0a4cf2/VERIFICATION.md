---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

C: The source proof starts from exact zonotope support sum W(U)=sum_{ij}|U_i-U_j|, couples intrinsic U to centered independent Gaussians X,Y via chi radius, and decomposes the two-sample Gini kernel into independent h(X)/p and h(Y)/q projections plus an L2-small degenerate remainder. The key covariance Cov(h(X),X²−1)=mu/2 yields the -2/pi normalization term, avoiding a false unnormalized Gaussian variance. For fixed p the conditional LLN gives (1/p)sum f(G_i); f(x)=b+bx²/2+O(x⁴) gives the exact chi-square small-ball boundary constant (pt/b)^{p/2}/Gamma(p/2+1). The subsequence argument handles arbitrarily oscillating growing aspects. Independent mpmath/SymPy evaluation reproduced mu=1.128379167096, b=0.797884560803, v=0.162751579442 and the positive 0.014386545399 balanced variance. No rate is claimed for all p,q. Full Git tree SHA recomputed from seven retrieved entries.

## originality

PASS

O: The earlier all-graph exact spherical mean/second moment result is expressly prior: it implies formula (6) but not a full weak limit or sharp lower-tail exponent. Padrol–Pilaud–Poullot develop deformations and normal arrangements, and general Gini mean-difference asymptotics supply the statistical method. The proposed combination of finite-side boundary law, all-aspect Gaussian crossover, and intrinsic chi-normalization has a best-of-knowledge gap; a generic normalized Gini-statistic theorem remains a bibliographic risk, not proof of novelty.

## value

PASS

V: The width distribution of a canonical family of centrally symmetric polytopes is geometrically natural; the finite-side p/2 angular-edge signature distinguishes discrete combinatorial size through rotation-invariant data. At balance the radial correction changes the limiting variance by a quantitatively large amount, and the unlimited aspect-ratio dichotomy goes beyond the known first two moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
