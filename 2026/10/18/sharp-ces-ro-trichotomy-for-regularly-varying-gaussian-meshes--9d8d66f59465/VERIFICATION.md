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

Reconstructed the entire RESULT.md theorem under source admissibility d_1<=1/8, d_{n+1}<=d_n/(1+64d_n^2), positive l2-not-l1 increments, and additional regular variation index -alpha (1/2<alpha<=1) with an existing extended limit a=lim n*d_n. The source Proposition 6.2 fixes <x_i,x_j>=rho_i*rho_j*exp(-(t_i-t_j)^2), rho_i=exp(-sum_{k<i}d_k^2), so rho_infty=exp(-sum d_k^2)>0. For nd_n->infinity, i d_i->infinity and 1/d_i=o(i): a Gaussian local Riemann sum gives d_i sum_{j>=1} exp(-(t_i-t_j)^2)->sqrt(pi). For j>2i the omitted tail is <=C i exp(-c(i d_i)^2), whose product with d_i tends to zero, and all nearer tails are uniformly controlled by monotonicity and regular variation. For i in any interior proportional window the finite n row has the same asymptotic. Karamata yields sum_{i<=n}1/d_i ~ n/((1+alpha)d_n), giving the exact coefficient sqrt(pi)/(1+alpha). Weighted Cesaro convergence replaces rho_i*rho_j by rho_infty^2 without altering this scale. If a<infinity, necessarily alpha=1: proportional-window step sums converge to a log(s/t) and bounded two-dimensional Riemann sums, including the omitted small-index region, give rho_infty^2*F(a), with F(a)=int_0^infty exp(-a^2u^2-u)du. F(0)=1; strict decrease and aF(a)->sqrt(pi)/2 follow from the integral. For c*n^-alpha, c<=1/16, the mesh recurrence follows from n^alpha*((n+1)^alpha-n^alpha)>=alpha*2^(alpha-1)>=1/(2sqrt(2))>64c^2, so rho_infty=exp(-c^2*zeta(2alpha)) and the claimed power rate is valid. One subtle normalization checked: Gaussian kernel is exp(-(s-t)^2), not a kernel with a hidden 1/2 in the exponent. The theorem is only for the constructed orbit, not all firmly nonexpansive operators.

## originality

PASS

Qualified best-of-knowledge priority, after comparing actual mathematical statements. The directly relevant 2026-06-30 Bauschke–Tung v2 source, Theorem 7.6, proves strong convergence under nd_n->infinity through the explicit nonsharp inequality sum_{i,j<=n}exp(-(t_i-t_j)^2)<=n(1+sqrt(pi))/d_n (its equation 74), and Example 7.7 proves qualitative convergence for d_n=1/(16n^(3/4)). It does not present the sharp asymptotic coefficient sqrt(pi)/(1+alpha) or the a=0 finite-density boundary. The previously published Resultary harmonic finding proves exactly rho_infty^2*F(delta) for d_n=delta/n, and expressly limits its domain to that one mesh. The harmonic result is an acknowledged special case, not claimed as new. Neither a source upper bound nor a fixed-harmonic exact calculation implies a sharp asymptotic for all regularly varying admissible meshes; a new uniform local Gaussian-row argument plus Karamata summation supplies the missing content. Searches for Gaussian-kernel localization and nonlinear mean-ergodic aliases did not establish a dominating result. These searches are not an exhaustive historical priority proof.

## value

PASS

The source paper established a qualitatively new nonlinear mean-ergodic obstruction and showed that one power-law mesh converges strongly, without the sharp rate. The audited theorem supplies a motivated and precise quantitative invariant of that particular constructed orbit: the natural density n*d_n controls a phase split; in the fast-mesh regime the exact constant sqrt(pi)/(1+alpha) and polynomial decay exponent distinguish different RV indices; at finite density an explicit Gaussian-logarithmic crossover F(a) includes the previously unquantified a=0 boundary. This is an exact and useful classification of convergence behavior of a specified nonlinear example, not a mere substitution into an existing constant or a generic assertion for all nonexpansive maps. It can serve as a sharp test case for quantitative ergodic and kernel-localization analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
