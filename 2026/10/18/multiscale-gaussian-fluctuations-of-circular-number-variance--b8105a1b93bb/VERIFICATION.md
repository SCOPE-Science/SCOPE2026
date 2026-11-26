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

Expanding the integrated square gives a deterministic diagonal term Ns(1-s) and twice the sum of centered overlap kernels over unordered pairs. Conditioning eliminates all distinct-pair covariances, including pairs sharing an index. For folded lengths 0<=u<=v<=1/2 the integral of the product of the uncentered overlaps is 2 times the integral of (u-x)(v-x) from 0 to u, namely u^2v-u^3/3; centering subtracts u^2v^2. Multiplying by 2N(N-1) gives (1), with the complement symmetry exact and N=1 or zero folded length deterministic. The periodic bridge Fourier modes give common independent Exp(1) energies with summable weights. On shrinking scales the maximum normalized coefficient is O(sqrt(delta)), the variance of each finite combination has the stated limit, and the sum of its third moments tends to zero; the fourth increment moment is O(|t-r|^4), proving tightness. The limiting Gaussian covariance is that of twice integrated Brownian motion. The uniform bridge coupling error divided by delta^(3/2) is O_P(eta/delta+eta^2/delta^(3/2)) since the supremum bridge energy is O_P(delta); the assumed eta=O_P(log N/sqrt N)=o_P(delta) makes both terms vanish. This proves the process limit for fixed R under exactly the stated condition. Independently checked 225 rational mixed overlaps by exact piecewise-quadratic integration (python3 /workspace/check_frozen_math.py); frozen verification and checker inspected, not executed.

## originality

PASS

The expectation, short-window exact finite-sample diagonal variance, bridge model and fixed-window laws are existing results. In particular the frozen literature discussion understates the prior diagonal overlap: Aistleitner–Hörmann–Manskova give the exact finite-N variance in §6, equation (17), not only the Lemma 4 bridge variance. The supported distinct claims are the explicit off-diagonal finite-N formula and the centered shrinking-window C([0,R]) limit at the stated coupling scale. Neither a fixed-scale series law nor a uniform first-order almost-sure law implies a multiscale centered Gaussian functional limit without the new triangular-array and tightness steps.

## value

PASS

Repeated measurements of the number variance on a common sample are dependent. The mixed covariance makes that dependence explicit at finite N; the integrated-Brownian limit quantifies it uniformly across shrinking scales and specifies fluctuation geometry unavailable from one-window laws. This is a natural stochastic-process question, with a precise sufficient regime rather than an unsupported optimality claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
