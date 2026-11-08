---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For each fixed odd k=2m+1>=5 and N iid arclength-uniform boundary points of a unit-circumradius regular k-gon, Lao (2010) Eq. (5.12), Thm. 5.3 supplies joint Exp(lambda=2/a=1/sin(pi/k)) corner gap limits and the correct 4k weighted-pair minimum under (N/k)(s_k-D_N), s_k=2cos(pi/(2k)). In source E-indexing, after reorienting the second m opposite pairs, the k coefficient-g=sin(pi/(2k)) edges form a perfect matching across 2k independent corner exponentials, other 3k edges coefficient b=sin(3pi/(2k)). Thus S_i=B_i+A_(i+m) are independent Gamma(2,lambda) and U_i=B_i/S_i iid Uniform[0,1] independent of S. Setting q=t/(2g), Y_k>t means all S_i>q plus b-weight inequalities. At S_i/q=1 these yield U_(i-m)+U_i<=2-r, U_i+U_(i+m)>=r, U_(i-m)-U_(i+m)<=1-r, r=g/b. Multiplication-by-m modulo k permutes coordinates (gcd(m,k)=1) into exactly P_k(r). For k>=5, 0<r<1/2 and [r,1-r]^k is inside the polytope. Given S_i>q, excess W_i=S_i-q has survival e^{-lambda w}(1+lambda(q+w))/(1+lambda q) -> e^{-lambda w}; joint tight convergence of W and independent U plus hyperplane-null boundaries yields uniform U on P_k(r), independent limiting Exp(lambda) W. Multiplying exact Gamma survival (1+lambda q)^k e^{-k lambda q} by limiting feasibility volume proves p_k(r)(lambda t/(2g))^k exp[-k lambda t/(2g)]. Lower endpoint P(Y_k<=t) arises from weighted edge sum events X_u+X_v<=t/(2c): the 4k-edge graph is a cycle of K_(2,2) bipartite blocks, triangle-free for k>=5, each vertex degree 4 and one g incident. Exactly 6k g,b and 6k b,b overlapping edge pairs; disjoint pairs and 3+-edge overlaps contribute O_k(t^4). Single-edge expansion lambda^2 q_c^2/2-lambda^3 q_c^3/3 and shared-pair volumes q_g q_b^2/2-q_b^3/6 and q_b^3/3 give alpha=k lambda^2(g^-2+3b^-2)/8, beta=k lambda^3(g^-3+6b^-3+9/(g b^2))/24. Independent numerical incidence for k=5,7,9,11,21,31 and 60k polytope equivalence trials k=5,7,9,11; independent SymPy expansion confirms cubic beta. Finite tests corroborate, not prove all k; analytic graph structure and dominated convergence do. Fixed k only; iterated limits, not simultaneous rate.

## originality

PASS

Best-of-knowledge the published 2010 thesis already proves the scalar weak-limit distribution by a 2k-dimensional exponential representation, so neither that limit nor a merely renamed min-law is new. The audited result makes an additional iterated rare-event conditioning on that law, identifies the explicit k-dimensional cyclic feasibility polytope and uniform marked corner splits independent of exponential residuals, and computes leading right-tail and cubic opposite-endpoint coefficients. These are nontrivial analytical deductions from known ingredients, not asserted as an independent new full scalar limit. Primary full-text comparison shows Lao Thm 5.3 and the k=3 Appendix D.2 do not state these odd-k>=5 conditioned marks, polytope, or expansion. The other inspected papers concern different observables/regions. Some formal implication is implicit in the stronger 2010 exponential-vector convergence; prior exposition under gamma-polytope terminology remains the principal originality risk.

## value

PASS

The odd regular polygon arclength-sample diameter is a natural classical extreme-distance problem with a known but highly dependent 4k-edge exponential-minimum limit. Conditioning on an unusually large deficit asks where all near-opposite corner pairs must be absent; the explicit k-dimensional cyclic polytope, its positive-volume shape and asymptotically independent exponential residuals are a nontrivial spatial large-deviation structure. It gives an exact geometric meaning to the right-tail prefactor and a correlation-sensitive t^3 coefficient at the small endpoint. This is mathematically useful as a canonical fixed-odd-k benchmark and not merely a numeric finite experiment or renamed limit. It does not claim the whole scalar distribution or a general fixed-k uniform asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
