---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For arbitrary fixed finite nonnegative lags and positive current populations, logistic and forced linear comparisons give positivity/global boundedness. For beta<d, y'≤beta*y(t-tau1)-d*y and beta<d give exponential comparison, then z decays exponentially. At beta=d, P=y+d∫_(t-tau1)^t y satisfies the exact dissipation P'=-d*m*y(t-tau1)^2/(x(t-tau1)+m*y(t-tau1))-theta*y*z/(v+p*y+q*z)≤0. The bounded denominator yields ∫y²<∞, and bounded derivative yields y→0, hence z exponential. Under r>b+alpha/m, lower logistic comparison bounds x away from zero and gives x→X=(r-b)/a. Writing h=-P', y'=d(y_del-y)-h, positivity bounds y_del≤e^(D*tau1)y≤e^(D*tau1)P, so h≤C(P²+zP). Q=1/P satisfies Q'≤C+C*z*Q; z integrable gives Q=O(t), yielding P≥c/(1+t), slow variation under bounded translations, and z/P→0. Normalized translates y(t_n+s)/P(t_n) converge subsequentially to bounded entire solutions Y'=d(Y(s-tau1)-Y), Y+d∫Y=1. Fourier symbol i*xi+d(1-e^(-i*xi*tau1)) has only real zero xi=0; bounded entire Y is constant 1/(1+d*tau1). Hence -P'/P²→d*m/[X*(1+d*tau1)²], and t*y→X*(1+d*tau1)/(d*m), including tau1=0. Independent exact SymPy algebra verified the dissipation, quadratic delay normal coefficient, and rational beta>d stable-equilibrium Jacobian (trace -11/8, determinant 17/16, remaining eigenvalue -1/2). Computation does not replace the global analytic argument.

## originality

PASS

Closest full primary source Wang–Shao–Chai 2023 has the identical equations, but its strict local criterion beta<d and neutral characteristic root at beta=d do not imply global equality extinction or the uniform t^-1 coefficient. Fresh Resultary searches, direct reading of two related published SCOPE results, and full primary Tian–Xu 2011 comparison found no stronger theorem that mathematically covers the same claim. The exact Resultary match is the assessed record and is excluded as independent priority evidence. Some plausible two-species full texts remain inaccessible; they are documented as risks rather than automatic rejection. The mathematical novelty conclusion is best-of-knowledge, not historical priority certification.

## value

PASS

The beta=d surface is a natural nonhyperbolic spectral threshold in a published three-species delay model; strict local stability fails to determine nonlinear global extinction or relaxation. The theorem supplies a structurally new nonnegative lag-compensated mass, closes the endpoint globally for all positive histories and finite fixed delays, obtains an exact positive leading amplitude depending linearly on gestation time, and exhibits an attracting positive-predator equilibrium for beta>d showing sharpness of the parameter-uniform extinction bound. These are motivated analytical dynamics facts with interpretable boundary behavior, not just a standard norm estimate, finite simulation or known equilibrium table. It does not claim stochastic/spatial/time-varying delay cases or classify all beta>d.

The dated certificate retains the supplied scientific assessment, sources and limitations.
