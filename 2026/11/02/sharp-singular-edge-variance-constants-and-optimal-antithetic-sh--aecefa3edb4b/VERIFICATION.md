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

Unbiasedness is by exact cell integration. For fixed m the first summand is asymptotic to g(0)m^(α−1)u^(−α); all other terms are bounded as u tends to zero. Positivity gives the same divergent-moment lower bound for any coupling, with logarithmic divergence at qα=1. Below this threshold the sum is controlled by the two marginal moments. In the pure-power scaled error H_m, consecutive differences are O(m^(−1−α)) uniformly in the shift, so the remainder to the limit is O(m^(−α)) and H_α is square integrable for α<1/2. The g−g(0) component has integrable derivative and variation error O(m^−1). Direct cellwise Fourier integration gives the stated gamma coefficients and zero mean; Parseval gives C_α, and reflection takes real parts, multiplying that norm by sin²(πα/2). The strict countermonotone claim can be proved by integrating the intersection lower bound P(U<a,V<b)>=(a+b−1)_+ for superlevel sets of the decreasing profile (shift it by a constant if needed). Attainment forces equality at all interior a,b by continuity of the copula and strict continuous monotonicity; this determines the reflected coupling. This applies to Q_m when f is strictly decreasing, with variance finite. The difference in scaled second moments from replacing each marginal by the limiting profile tends to zero uniformly in the coupling by Cauchy–Schwarz, so coupling infima converge to the same optimum. It neither asserts uniqueness at infinite variance nor requires monotonicity for the limiting gain. Independent numerical integration of finite-grid squared errors (`python3 /workspace/branches/independent_replay.py 5`) gave reflected coefficient ratios within 0.0004 of one for α=0.18,0.33, g=1 or 1+2x² at m=1024. The uncorrected single-grid coefficients converge more slowly; an endpoint-corrected numerical check is only diagnostic, not the basis for the limit.

## originality

PASS

The antithetic lattice construction, the rearrangement principle and the Hurwitz Fourier expansion are prior; the supported distinct result is the sharp endpoint-singular variance coefficient and reflection gain as an optimum over all prescribed-marginal couplings, stable for the stated multipliers. The closest shifted-lattice paper uses the equivalent pairing and gives an unbounded-tail warning, but the inspected passages do not establish that singular L² limit or the optimal coefficient.

## value

PASS

At equal work for two global shifts, 2 sin²(πα/2) quantifies how much reflection gains and proves that no other coupling improves the leading coefficient for these multipliers. The complementary impossibility of curing infinite variance by dependence alone identifies when a different estimator, rather than a different pairing, is necessary. Both conclusions are practically interpretable for the singular shifted rule and not a trivial comparison of two simulations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
