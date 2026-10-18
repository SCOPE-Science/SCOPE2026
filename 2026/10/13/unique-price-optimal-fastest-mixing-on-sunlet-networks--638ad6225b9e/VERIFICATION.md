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

The continuous-time unnormalized Laplacian gap lambda_2 is concave in nonnegative edge conductances, so rotational averaging shows a symmetric optimum exists. With pendant a, rim b, Fourier mode k has 2x2 matrix [[a+b mu_k,-a],[-a,a]]. The minimum positive mode is mu=4sin^2(pi/n), and gap h=a+mu b/2-sqrt(a^2+(mu b/2)^2). An AM-GM price lower bound for gap r yields n(ta+b)>=n r(t+2/mu+2sqrt(t/mu)); at budget1 equality forces all a=R(1+1/sqrt(mu t)), all b=R(2+sqrt(mu t))/mu with R=mu/[n(2+mu t+2sqrt(mu t))]. For arbitrary maximizing edge allocation, cosine and sine Fiedler modes of its rotational average must be eigenvectors of each rotation: leaf equations force all pendant weights; independent consecutive chord vectors for n>=3 force all rim weights. This establishes global uniqueness, including n=3. mu~4pi^2/n^2 gives all asymptotic scalings. Independent full 2n-by-2n Laplacian eigenspectra at n=3,4,5,7 and prices t=.2,1,3.7 (12 cases) reproduce exact predicted gap within 1e-10; finite numerics do not establish global optimality.

## originality

PASS

Sun–Boyd–Xiao–Diaconis 2006 solves general fastest mixing Markov-process edge-rate design as an SDP and explicitly solves pure cycles, which is a general algorithmic framework but not a closed price-dependent sunlet optimum with complete uniqueness over all individual edges. Weighted corona Laplacian articles compute spectra/coherence for fixed weights, not solve this constrained optimization. The contribution is explicit full sunlet solution, not discovering SDP/concavity/Fourier eigenvalues.

## value

PASS

Under a natural two-orbit linear conductance-cost budget, the exact fastest-mixing network and its unique edge allocation quantify a meaningful resource tradeoff; n^-3 optimal gap and t~n^2 crossover are usable benchmark laws for graph design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
