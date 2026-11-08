---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The independent proof reconstruction starts from the correlated Gaussian orthant integral at a=-Phi^{-1}(u),b=-Phi^{-1}(v). With b/a->1, positive derivative coefficients gamma_1,gamma_2 yield a uniform relative error O(a^-2+b^-2) after exponential rescaling. Mills-ratio subtraction for t=log(u/v)=O(log log(1/u)) gives Q(a,b)-Q(a,a)~2t/(1+rho); the ratio is K_rho*L^{-alpha}*exp(alpha*t)*(1+o(1)), uniformly on bounded logarithmic wedges. The conditional Gaussian h_u(t)=Phi((Phi^{-1}(u)-rho Phi^{-1}(t))/sqrt(1-rho^2)) strictly decreases with t; thus G(u,v)/v decreases from 1 to the diagonal comparison and gives a unique crossing, not just two test signs. Independent Gauss-orthant 1D quadrature at rho=.3,.5,.7 and u=10^-10 brackets c_rho by c_rho/4 and 4c_rho. Finite quadrature is corroboration only. Endpoints rho=0,1 and multi-parameter uniformity are excluded.

## originality

PASS

Best-of-knowledge novelty lies in the uniquely located Gaussian/symmetric Marshall–Olkin moving-ray crossover, not generic Gaussian tail asymptotics or local stochastic order. Read the accessible primary Li–Joe HTML exposition and compared the precise direction regimes to Siburg–Strothmann and Furman; no stronger statement carrying this calibrated moving logarithmic boundary was established. Fixed-ray asymptotics cannot simply be substituted into v/u=1/log(1/u); older moderate-deviation lemmas could give the result implicitly.

## value

PASS

The theorem gives a sharp, natural counterexample to neighborhood copula dominance even for matched diagonal tail power and quantifies the boundary by a universal exponent and model-dependent coefficient. Conditional threshold uniqueness and a uniform moving-direction expansion are mathematically motivated beyond a numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
