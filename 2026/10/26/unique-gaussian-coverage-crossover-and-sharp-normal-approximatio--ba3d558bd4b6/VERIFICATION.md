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

Accumulating Brownian increments over backwards Poisson spacings gives conditional variances 2D E_j/r weighted by a^(2j). Their sum is finite almost surely and gives a stationary law via the process on a two-sided time axis; synchronously coupled initial states contract by a^N_t, giving uniqueness. The stated rescaling leaves the independent unit-normal mixture with V=sum_j (1−q)q^j E_j. Its mean is one, variance s_a, and fourth centered moment is 3s_a²+6 sum_j w_j^4, since independent unit exponentials have fourth cumulant 6. The density ratio at squared radius 2y is strictly convex in y, finite and continuous by domination on bounded y intervals by e^y V^(-1/2), with finite inverse half-moment from the first exponential. Strict Jensen makes its value >1 at zero; positive mixing mass on a compact interval above 1 makes it tend to infinity. Equal integrated density mass forces a strict dip below 1. This gives precisely +,−,+ for the density difference on the positive half-line. Its integral from zero is positive at the first turning radius and negative at the second because its remaining tail integral is strictly positive; hence there is exactly one positive coverage zero. In the expansion, differentiating the variance-scaled Gaussian twice gives H4(x)phi(x)/4, and the third derivative has L1 norm bounded by C v^(-3). For V≥1/2 the L1 Taylor remainder is O(E|V−1|³)=O(s_a^(3/2)), because sum w_j^4≤s_a². For V<1/2 the Gaussian and its Taylor surrogate are uniformly bounded in L1; the printed exponential lower-tail estimate follows from log E exp(−t(V−1))≤t²s_a/2 at t=1/(2w_0), and even the fourth-moment Markov bound there gives O(s_a²). Integrating H4 phi yields −H3 phi. Its absolute maximum is attained at the smaller positive critical radius u or its reflection: the squared comparison of the two absolute values is exp(2 sqrt(6))>(3+sqrt(6))/(3−sqrt(6))=5+2 sqrt(6), true already from the quadratic lower Taylor polynomial of exp. Summing the signed density integrals across the two Hermite roots gives the stated TV constant with the factor 1/2 convention. Independent high-precision quadrature and direct CDF evaluation (python /workspace/review_checks.py, check 2) reproduce 0.17503751880186475, 0.06882347993760242 and 0.91673548333644960. The uniform CDF remainder and the simple positive root of −H3 phi yield the claimed crossover localization and O(s_a^(1/2)) error. This limit is a→1, not r→0; the uniqueness proof applies to all 0<a<1 without using numerical inversion.

## originality

PASS

The checked sources already give the stationary sum, normalization and qualitative Gaussian limit; the literature also contains an asymptotic Gaussian error statement and related central-crossing theorems for different laws. In the material checked, none gives the all-contraction crossing for the reset law together with the rigorously uniform density/CDF expansions and sharp metric coefficients. The Gaussian variance-mixture argument is general in form, so priority for its crossing mechanism alone is not asserted. The supported distinct mathematical content is the reset-law calibration and sharp metric expansions, not the product representation or Gaussian limit.

## value

PASS

For a canonical non-Gaussian stationary model, the unique coverage switch gives the direction of calibration error at every radius for every allowed contraction, not merely a near-Gaussian heuristic. Its weak-reset threshold and sharp TV and uniform CDF errors quantify what the known weak limit does not supply. This gives a usable calibration result without extrapolation to drift or other reset processes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
