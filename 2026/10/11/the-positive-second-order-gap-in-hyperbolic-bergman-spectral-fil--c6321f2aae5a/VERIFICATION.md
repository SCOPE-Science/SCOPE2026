---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS. Exact weighted-ball monomial decomposition gives radial T=|z|^2 distributed Beta(k+d,b), b=alpha+1; shell multiplicity binomial(k+d-1,d-1). Strict stochastic monotonicity orders eigenvalues. Scaling W=(k+d)(1-T) and domination of all logarithmic moments gives E log W=psi(b)+O(1/k), with exact log identity arctanh sqrt(T)=(log(k+d))/2+log(1+sqrt(T))-(log W)/2. Tail moments justify the two-term expansion for every p>0 including 0<p<1. Shell-weight log distribution contributes -1/d and partial-shell error is negligible; independently expanding arsinh filling and subtracting yields p/(2d)^p[log Gamma(b+d)/Gamma(b)-d psi(b)]. Strict Jensen psi(b)<log b plus Gamma(b+d)/Gamma(b)>=b^d proves positivity. Independent coefficient calculations for (d,alpha,p)=(1,0,1),(2,0,1),(2,1.5,2),(3,-.5,.5), and inspection of finite-N quadrature diagnostics, corroborate but do not prove asymptotic.

## originality

PASS

PASS, best-of-knowledge and with explicit high-relevance access risk. Alvarez–Camper–Mitkovski, Orthogonality, Spectral Filling, and Uncertainty, arXiv:2610.02484, establishes exact filling lower bound I_N and the leading asymptotic, whereas the assessed result is the NEW explicit strictly positive coefficient at scale N(log N)^(p-1) from a Beta-to-gamma boundary layer and shell-count correction. Resultary searches for equivalent coefficient, beta/digamma and nonradial aliases found only assigned finding and unrelated Bergman results; general radial Toeplitz diagonalizations by Grudsky et al. and Bauer et al. are not themselves this second-order defect. Full Alvarez paper unavailable despite arXiv and OA mirror attempts; authorized institutional request returned VPN disconnected, so an implicit corollary or appendix remains a genuine priority risk and no whole-document NOT_COVERING claim is made.

## value

PASS

PASS. The sharp second-order difference between spectral accumulation and hyperbolic-volume filling is a natural quantitative invariant of a known inequality, not mere diagonalization or a chosen arbitrary parameter. A positive exact coefficient for all complex dimensions, weights alpha>-1 and fractional p>0 distinguishes an asymptotically strict gap hidden by leading order and may guide precise Toeplitz spectral estimates. Bounded-fixed-parameter regime stated honestly; no inflated claim of a semiclassical or nonradial theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
