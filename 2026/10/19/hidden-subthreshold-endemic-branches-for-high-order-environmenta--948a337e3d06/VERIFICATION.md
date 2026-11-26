---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For I>0 the stationary V and S equations solve uniquely with V/S=sigma/(epsilon I+eta+mu+alpha_2 g(qI)), q=varphi/omega. The return term in the susceptible denominator is strictly less than sigma, so that denominator is positive. All other coordinates reconstruct positively and only the exposed balance remains. With h=alpha^[-1/(n-1)] and I=hy, the apparent singularity alpha g(qI)/I cancels and the extended equation at h=0 is S_0 q^n y^(n-1)/kappa-K(1-R_c), strictly increasing at its positive root. With t=1/alpha and I away from zero the equation extends smoothly with limit Lambda/I-K, whose derivative at Lambda/K is nonzero. Both implicit-function arguments therefore give roots for every sufficiently large alpha; their limits separate them. As a separate check, adding the stationary S,E,V balances gives K I=Lambda-mu S-(p eta+mu)V, confirming the large-root limit is approached from below. At the disease-free state g'(0)=0. The infected (E,I) and uninfected (S,V) blocks have negative traces and positive determinants xi K(1-R_c) and mu(sigma+eta+mu)+p eta sigma; the other eigenvalues are -mu and -omega. The exact rational witness was independently reconstructed. Its Q has signs (-,+,+,-) at (1/20,1/10,1/3,1) and a positive denominator. The numerator Sturm variations are 3 at 0 and 1 at positive infinity, giving exactly two positive roots, one in each interval. It gives R_c=5/42, sqrt(37)/4 and 2/3 as stated.

## originality

PASS

The supported distinct claim is the pair of subthreshold endemic branches, at the two explicit singular scales, in this six-compartment model with fixed baseline parameters, n>=3 and every sufficiently large alpha. The closest same-model papers establish local bifurcation direction or supercritical persistence, not that combination. Analogous indexed conclusions change the dynamical model or the threshold regime. A relevant abstract leaves a real but unresolved priority risk, not evidence of equivalent coverage.

## value

PASS

This model-specific result identifies a concrete limitation of relying on the disease-free invasion threshold or the local transcritical direction to rule out other equilibria. It proves persistence of two separate equilibrium branches as a parameter varies, distinguishes their scales quantitatively, and supplies a certified finite witness. It is not a claim about two attracting endemic states, public-health forecasts, or feasibility of the high-strength regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
