---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Condition on all Poisson clocks, leaving the Gaussian integrators independent. Stochastic Fubini on each reset interval turns the integrated response into a Brownian integral with deterministic kernel ∫_u^b h_j(-t) dt. The terms' variances add, including the independent Gaussian response, giving the positive squared-integral sum. Exponential integrability of the deterministic filter in time and the stationary Laplace bath moments give every finite output moment by Minkowski and justify passage from truncation. The decisive strictness argument works for signed filters: choose an interval where a nonzero response has constant strict sign; expose the entire clock outside a short middle interval and require its neighboring reset points, which are then fixed, to lie in that sign interval. With positive conditional probabilities there are no middle resets, or one near an interior point. The difference of squared-integral terms on the affected interval is ∫[Q²+2Q∫_u^c h_j(-t)dt]du over its part before the insertion; both terms are nonnegative and Q² is strictly positive. All exterior contributions are unchanged. Thus that bath variance is random; independence prevents cancellation. Analyticity on the last reset interval also gives positive conditional variance almost surely for any nonzero response. Consequently the density is symmetric and strictly decreasing for positive arguments (finite there, since each Gaussian density at a fixed x≠0 has a uniform upper bound in the variance), and the positive characteristic function is a Laplace transform of variance in squared frequency. Gaussian conditional moments and strict Jensen give all the asserted even inequalities and κ4=3 Var(V); when all transfers vanish only the independent Gaussian part remains. OU covariance matching is exact at all stationary lags by independence and linear filtering. For the fixed-end chain, the energy estimate excludes unstable modes and excludes imaginary modes because zero boundary velocities force all coordinates of a nonzero-frequency mode to vanish by nearest-neighbor recursion; zero frequency is excluded by positive stiffness. The positive real-frequency inverse of the irreducible diagonally dominant tridiagonal matrix is entrywise positive, hence no site has a zero transfer from either wall. As an independent scalar check, stationarity of Y^i X^j gives (ai+r 1_{j>0})M_ij=iM_{i-1,j+1}+Dj(j-1)M_{i,j-2}. With a=r=D=1 this yields M_02=2, M_04=24, M_11=M_20=1, M_13=15, M_22=32/3 and M_31=M_40=8, giving κ4=5; eliminating the same moments symbolically gives the claimed general scalar formula. The uploaded verify.py was read, not executed; the recurrence is a special case, not the network proof.

## originality

PASS

Credit strict variance nondegeneracy and the exact Gaussian/no-transfer criterion over arbitrary signed stable linear readouts, with the resulting shape and moment hierarchy. Do not credit covariance matching, classical mixture theory, or the already known scalar moments in isolation. The closest chain entry essentially duplicates the specific finite-chain fourth-cumulant conclusion; the full-network criterion, not priority for that corollary, supports this pass.

## value

PASS

The criterion identifies exactly which linear projections can distinguish covariance-matched reservoirs despite identical full two-time correlations. It both rules out cancellation among independent visible baths and upgrades a fourth-order diagnostic to an all-order one, with the chain illustrating why positive finite-size kurtosis persists under additional Gaussian heating.

The dated certificate retains the supplied scientific assessment, sources and limitations.
