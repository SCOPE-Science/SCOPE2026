---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Multiplying consecutive matrices gives diagonal two-year products, with cohort logs N lambda+c S_N+d D_N and N lambda+c S_N-d D_N up to their constant initial-stage logs. Both stages start positive, so log-sum-exp differs from the maximum by a deterministic bounded term. For rho=1-2p, the centered innovations E_t-rho E_{t-1} have constant conditional variance 1-rho^2. Their ordinary and alternating sums give (1-rho)S_N and (1+rho)D_N up to bounded endpoints, and the conditional cross-variation normalized by N tends to zero because the signs alternate. Bounded increments verify the martingale CLT and give almost-sure sublinear sums and O(N^2) fourth moments. The one-year abundance multipliers are bounded above and away from zero, extending the growth exponent to all years. The even-time limit is c sqrt((1-p)/p) Z_1 plus |d| sqrt(p/(1-p)) |Z_2| for independent standard normals, with limiting first and second moments justified by uniform integrability. The folded summand's positive third centered moment for d nonzero is its scale cubed times sqrt(2/pi)(4/pi-1), proving non-Gaussianity; the d=0 point-mass case is Gaussian in the degenerate sense. Substitution t=p/(1-p) reduces variance minimization to c^2/t+(1-2/pi)d^2 t; balancing terms gives the unique stated p_* and minimum if both channels are nonzero, and the stated monotone or constant cases otherwise. No endpoint or finite-horizon optimality is entailed. Centering is by N lambda, not expectation. The frozen finite checks were inspected, not executed; correctness rests on the analytic proof.

## originality

PASS

The supported contribution is the explicit two-cohort second-order law and its moment and switching-rate consequences under symmetric Markov switching, not general stochastic growth theory or the observation that log-sum-exp approximates a maximum. The closest indexed Gaussian-maximum statement concerns three-stage life cycles with different Fourier modes and does not include the two-stage formula. Inspected primary results address positivity-based Gaussian limits, leading exponents of sparse products or mixing continuous-time phenotype switching, not the full parity-cohort claim. Remaining literature-access risks are explicit below.

## value

PASS

The same long-run exponent for every switching rate can hide both non-Gaussian risk and a positive square-root-time log-abundance correction. The explicit distinction between common and alternating cohort fluctuations gives a concrete mechanism and a unique variance-optimal switching rate in the nondegenerate case, with sharp degeneracies when one channel is absent. This is useful for understanding exactly which stochastic-growth conclusions fail without mixing of age composition. It is a scoped variance result for a density projection, not an extinction prediction or a claim of an optimum for all risk measures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
