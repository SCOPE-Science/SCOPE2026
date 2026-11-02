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

The starting density formula is explicitly credited to Britton et al.: mu_{n,t}=E[g_{min(T_n,t)}], pi_n=E[g_{T_n}], with T_n Gamma(shape n, rate r) and g_v Gaussian of variance 2Dv. After scaling to U_n= r T_n/n, the difference is E[1_{U_n>c}(g_c-g_{U_n})]. Dividing by the positive g_c leaves a strictly decreasing function of |x|, since for U_n>c the ratio g_{U_n}/g_c is strictly increasing in x^2; at zero the difference is positive and as |x| grows negative, proving exactly one positive crossing. Gamma LLN gives L1 convergence of variance mixtures to normal densities and the explicit theta<1 TV formula, while Gamma Chernoff controls theta>1. In the n+s sqrt(n) critical window, Gamma CLT and bounded second moments give sqrt(n) E(U_n-c)_+ -> phi(s)-s(1-Phi(s)); uniform L1 Taylor control of Gaussian variance derivatives yields limiting signed density -[...]*g_1' and TV coefficient (1/2)||g_1'||_1=phi(1). Independent finite numerical Gamma-mixture quadrature found the unique crossings and profile convergence at n=4,16,64, supporting but not replacing these limits.

## originality

PASS

Britton et al. (2026) provide the exact Gamma-mixture transient formula and local accumulation-time results, which are correctly credited. Their accessible abstract emphasizes propagation of local relaxation and heterogeneity; it does not itself assert this global tagged-marginal total-variation profile or critical Gaussian coefficient. The full plausible preprint could not be inspected by open/OA paths and authorized institutional access was blocked by disconnected VPN, so this is a qualified best-of-knowledge PASS and meaningful priority risk, not a claim that the whole source lacks the result.

## value

PASS

The model has published stationary and transient tagged-particle distributions but the global total-variation approach is a natural strong distributional relaxation statistic not equivalent to local accumulation time. The theorem distinguishes a non-cutoff macroscopic profile from a vanishing Gaussian critical layer with exact coefficient, a useful refinement for a canonical nested reset chain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
