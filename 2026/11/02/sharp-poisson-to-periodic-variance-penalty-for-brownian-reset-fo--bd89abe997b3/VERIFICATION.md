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

In the stationary renewal construction the interval at a random observation time is length-biased and its age is uniform conditional on its length. For lag s≥0, only same-interval Brownian increments contribute; conditional covariance is 2Da at age a with a+s<L. Integrating gives C_L(s)=(D/m)E[(L−s)_+²], and symmetry gives negative lags. The finite second moment bounds that covariance, permits the L¹ kernel's mean-square convolution and its variance integral, and makes the convex-order comparison valid for nonnegative kernels. For the exponential kernel the two-sided integral reduces to μ^{−1}∫₀^∞e^{−μs}C_L(s)ds; integrating over s≤L gives the stated clock functional. Its bracket has second derivative 2(1−e^{−μL})>0, so Jensen is strict away from the point mass. The proposed two-point law preserves m and sends the second moment to infinity while the remaining terms in the bracket have bounded expectations. The periodic random-phase and equal-mean exponential laws give the two stated variances. Independently, writing H=2/R and integrating (1+z)∫₀¹e^{−zu}(1−u)²du by parts gives H=1−∫₀¹e^{−zu}(1−u²)du. Its derivative is ∫₀¹u(1−u²)e^{−zu}du>0 and H tends to 1/3 and 1 by dominated convergence, giving the strict 6-to-2 ratio. An exact phase check uses g(a)=2a−3+4e^{−a}−e^{−2a}: averaging the within-cycle variance yields Dμ^{−3}[∫₀^z g(a)da+g(z)/2]/z, equal to the claimed V_per, not the epoch variance.

## originality

PASS

Credit is limited to the explicit strict sharp Poisson-to-periodic variance ratio at stationary random times and matched mean. The covariance mechanism, stationary filtering and basic convexity are prior or direct consequences. A distinct catalogue record has the exact clock functional and deterministic minimizer but the inspected passages do not settle the ratio. The closest primary treatment of the same harmonic dynamics gives a periodic epoch statistic and a separately normalized Poisson statistic, not the same comparison.

## value

PASS

The ratio quantifies a physically motivated choice of clock for the same mean reset effort and unchanged harmonic response. It distinguishes the variance penalty when many resets fit within a relaxation time from that when resets are sparse, gives exact limiting penalties and orders the entire interpolation. Those conclusions cannot be obtained from merely knowing that the deterministic clock minimizes variance at any one relaxation rate. The random-time rather than epoch requirement matters to using these values as stationary observables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
