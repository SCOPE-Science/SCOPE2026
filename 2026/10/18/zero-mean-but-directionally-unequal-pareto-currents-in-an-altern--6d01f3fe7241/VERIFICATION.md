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

With rate one per undirected bond, the discrete heat equation gives rho_0(t)-rho_1(t)=p_t(0)=exp(-2t)I_0(2t), by convolution with the step and telescoping. That density difference is the mean instantaneous current. Integrating the Bessel recurrence gives m(t)=t exp(-2t)(I_0(2t)+I_1(2t)) and m(t)~sqrt(t/pi). Net current equals occupation of the initially empty half-line: only the central bond can add mass from outside, and its finite-time clock rings are finite. Particle-hole exchange gives the opposite signed law from the other preparation. For distinct sites the product evolution minus the evolving density product is the two-particle exclusion generator applied to the covariance, with extra forcing -(rho_i-rho_{i+1})^2 at adjacency (the two blocked jump terms). Initial covariances vanish, so the positive semigroup/Duhamel formula gives nonpositive covariance. The finite-sum moment bound passes to the full initially empty half-line by monotone convergence for the first and second moments, yielding Var(J_0(t))<=m(t). Stationary renewal reward over a complete plus/minus pair has age weight Psi_s(t)dt/M, M=mu_++mu_-, and gives the integral mean and positive absolute first moment bound for alpha_s>3/2. A positive tail gets contributions only from the plus phase and vice versa. At age t=y^2 u the reset-free scaled current converges in probability to sqrt(u/pi); above any fixed positive u cutoff, the survival kernel is integrable in u and the limit is the indicator u>pi. Below age epsilon y^2, use E[J_0^2]<=m^2+m=O(t) for t>=1 and boundedness on fixed intervals. The discarded contribution is O(y^-2)+O(epsilon^(2-alpha_s) y^(-2(alpha_s-1))), negligible after scaling and letting epsilon decrease to zero. Integrating the limit from pi gives exactly b_s^alpha_s pi^(1-alpha_s)/(M(alpha_s-1)); both exponents are between 1 and 2, so the second moment diverges. Finally F_alpha(b)=E[H(bU)], with H'=m>0 and U standard Pareto, is continuous by local domination with U^(3/2), strictly increasing from zero to infinity. This proves unique cancellation. Independent unbounded-tail quadrature with z=(b/t)^(alpha-3/2) reproduced b_-=1.479346536529261 and coefficients 0.11547182752349883 and 0.15032611782075804; replay with python3 /workspace/checks/1_pareto_calibration.py (mpmath). This numerical comparison is not interval certification, and the infinite theorem replays from the analytic proof. The uploaded finite-state and proxy checker was inspected, not run.

## originality

PASS

The single-step Pareto renewal law, its stationary mean integral, separate moment thresholds, reset-free asymptotics, and the two-configuration zero-current idea are prior. The supported distinct content is the sharply normalized unequal directional tails for a stationary alternating two-clock system, with exact and unique cancellation of the within-cycle mean. The nearest single-step paper actually gives a survival integral and numerical stationary distribution, not the exact tail limit in its inspected distribution section. A general age-mixture identity enables the argument but does not evaluate either sharp tail.

## value

PASS

The dichotomous-reset literature motivates separating mean balance from equilibrium; the power-law literature motivates asking which moments and tails remain observable at stationary time. Here the mean can be tuned to zero without making the directional current tails even comparable in order of decay. The exact coefficients and unique cutoff make that distinction quantitative for a canonical interacting lattice transport process, rather than a proxy example for independent walkers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
