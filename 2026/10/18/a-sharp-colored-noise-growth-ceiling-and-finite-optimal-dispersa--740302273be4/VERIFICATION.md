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

Subtracting the log equations gives Ẋ=H−M sinh X, with stationary variance 2λD for the OU difference. On a common forcing path all solutions contract at rate M, and the pullback from zero is Cauchy with stationary bound |X(t)|≤∫_{−∞}^t e^{−M(t−s)}|H(s)|ds. Jensen against the normalized exponential kernel gives finite exponential moments, locally uniform in M>0. The pullback is a stationary ergodic factor of H; contraction transfers the long-time log-total growth to arbitrary positive initial abundances. Direct differentiation gives g=(1/2)E[H tanh(X/2)], including the zero mean environmental average. Applying stationarity to log cosh(X/2) gives g=(M/2)E[cosh X−1]; X cannot be identically zero under nondegenerate forcing. At M=0 both uncoupled log growth rates, and thus the log growth rate of their sum, converge to r. For the critical Gaussian identity I independently condition the past as H(−u)=e^(−λu)H(0)+Z(u), with the residual path Z independent of H(0). Scalar Gaussian integration by parts, first with finite past, differentiates X(0) in H(0) by integrating the input e^(−λu) against exp(−M∫_{−u}^0 cosh X). This proves the stated response formula, including its λD/2 prefactor; e^(−(M+λ)u) dominates passage to infinite past. The sech² factor is strictly below 1 with positive probability, proving the strict global cap. The stationary cosh moment gives E sinh²X≤2λD/M². Since cosh X−1≤sinh²X/2, the response converges to the linear one at fixed M as D→0, and on times u=v/M at fixed D as M→∞, yielding both coefficients by dominated convergence. Stationarity of X², XH and cosh X gives λM E[X sinh X]+M² E[sinh²X]=2λD. It implies the small-M split bound at any R, and taking first M→0 and then R→∞ proves the endpoint. For continuity at positive M, couple the two stationary pullbacks on one H; the difference has a restoring rate at least min(M,M') and source bounded by |M−M'|·|sinh X_{M'}|. The uniform local moments yield L¹ continuity of X and hence continuity of the bounded tanh response paired with the integrable H. Strict positivity and the two vanishing endpoints give an attained finite positive maximum, not uniqueness. The frozen simulation was inspected, not run; its seeded finite-time checks cannot certify the strict bound or limiting statements.

## originality

PASS

The exact model, the basic stationary growth identity and the numerical observation of a finite colored-noise optimum are prior. The surviving contribution is the exact response identity and strict ceiling at all positive parameters, its sharp weak-noise and fast-migration coefficients, and the quantitative slow-migration estimate proving rigorous attainment. No inspected source supplies or mechanically implies that package.

## value

PASS

The model and question are independently motivated by an existing numerical finite-optimum observation. The strict ceiling gives usable parameter-dependent control without a white-noise or weak-noise replacement, the two sharp limits identify its accuracy, and the small-migration bound makes the qualitative finite optimum rigorous without claiming uniqueness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
