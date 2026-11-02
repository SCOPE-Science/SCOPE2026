---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The uniform random edge priorities coincide with rate-1/N independent exponential edge clocks. Directly counting eligible AB and BB edges yields the exact density-dependent chain with transitions (-1,-1) at AB/N and (0,-2) at B(B-1)/(2N), and limiting drift (-ab,-ab-b^2). The strictly positive first integral h(a,b)=a exp(-b/a) is conserved: its gradient (e^(-b/a)(1+b/a),-e^(-b/a)) has zero dot product with this drift; the fluid b tends to zero while a tends to r=alpha exp(-(1-alpha)/alpha). For fixed sufficiently late T, a(T)-b(T)>r/2; uniform fluid approximation gives A(T)-B(T)>rN/3 with high probability. Since A-B is nondecreasing at every deposition, cross-edges remain available whenever B>0, B is exhausted, and tau-T=O_p(log N) by comparison with a pure-death chain of rates >=(r/3)B. Thus terminal U=A(tau) with high probability, giving the law of large numbers and bounded expectation convergence. Taylor expansion on a>=r/3 gives the h-generator O(1/N), which integrated to tau gives o_p(N^-1/2). The martingale differences for AB and BB jumps are -e^(-b/a)(b/a)/N and +2e^(-b/a)/N, respectively. The scaled quadratic-variation density is Q=e^(-2b/a)(b^3/a+2b^2); each scaled jump is O(N^-1/2), giving Lindeberg. For t>=T, bracket density is <=C b; conditional expected integral of b is bounded by 3b(T)/r, so the martingale tail vanishes uniformly in the required sequential limits. The finite-horizon martingale CLT extends to the terminal state. With u=log(a/r), b=a u, du/dt=-b, integrating Q gives v=r integral_0^L e^(-u)(u^2+2u)du=r[4-(L+2)^2 exp(-L)]>0. Independently checked five finite complete-edge-order distributions, including 362880 orders for A=2,B=3, and a separate recursive count-chain law; checked finite exact/float moments at three N values and three alphas and symbolic h and bracket identities. These tests verify modeling and algebra only, not the general CLT.

## originality

PASS

Best-of-knowledge search across published mathematical findings and primary literature found no theorem implying the explicit terminal Gaussian jamming law for deterministic dense complete split graphs with both AB and BB edge reactions. Relevant foundational edge adsorption, general random greedy matching, random bipartite matching and parallel maximal matching address different graph regimes or observables. The inaccessible full Pippenger (1989) and Dyer–Frieze (1991) bodies, and unindexed reaction literature, remain explicitly material priority risks. A failed search is not a novelty proof.

## value

PASS

The complete split graph is a canonical deterministic dense inhomogeneous graph with a natural clique-plus-independent decomposition, not an arbitrary parameter slice. Greedy edge-dimer deposition on this graph is a natural irreversible kinetic process with a surprising positive jammed unmatched density despite the existence of perfect matchings. The explicit Gaussian fluctuation law and strictly positive computable variance capture the finite-size uncertainty of the entire matching, not just a mean or a standard special-function identity. Reaching a terminal stochastic state from a finite-time density-dependent CLT requires the substantive late-time separation, martingale drift and bracket-tail analysis supplied in the proof. This quantitative natural invariant is mathematically valuable even without Berry–Esseen or endpoint-uniform extensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
