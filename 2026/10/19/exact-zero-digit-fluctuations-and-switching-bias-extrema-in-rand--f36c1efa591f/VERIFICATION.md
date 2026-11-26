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

At alpha=1 the four quarter-branches of each map send uniform measure bijectively onto a half-interval. This preserves conditional uniformity given any sequence of branches, and yields the marked transition weights. From the left half the nonzero weights to left and right are 1/2 and p/2, and the zero weight q/2 stays left; the right row is the reflected version with p and q swapped. The stationary row (q,p) and the stated eigenvalues follow. With B=diag(q/2,p/2) and P=M_p(1), the joint moment at lag k inserts B P^(k−1) B. The nonstationary projection contributes the factor 2^(−(k−1)) times the stationary variance of the two entries of B, namely h(1−4h)/4. At p=1/2 the next-zero conditional probability is 1/4 for any hidden-half distribution, giving IID digits; at any other interior p the lag-one covariance is positive. Summing covariances gives the finite variance, including N=1, and optimizing its asymptotic coefficient over 0<h≤1/4 gives the asserted minimum and maxima. The positive tilted matrix has an isolated simple Perron eigenvalue: the spectral prefactor tends to one in the centered t/sqrt(N) expansion, giving the CLT with variance Gamma. The limiting log-mgf is differentiable on the full real line and the normalized counts have compact support, yielding the full LDP. The eigenvalue limits at z→0 and after division by z at z→∞ give the two finite endpoint rates; equivalently the all-nonzero and all-zero events use M_p(0) and B respectively. These conclusions are annealed and stationary, not claims for a quenched or nonstationary law. The frozen finite verification was read as evidence, not executed or used to prove the limit statements.

## originality

PASS

The starting stationary density, maps and marginal digit frequency are prior. The supported distinct claim is the explicit marked law at the random endpoint and its joint fluctuations, including the non-balanced variance maximizers. The bounded comparison did not establish equivalent coverage of those results.

## value

PASS

The endpoint of the published signed-expansion model is a natural tractable case. The exact two-state law determines finite-sample zero-digit counts, and exposes a difference between mean-frequency analysis and variability: the fair switch has IID digits and minimizes asymptotic variance, while two biased switches maximize it. The explicit rare-event rates and the variance extrema are concrete information about the expansion statistics, not merely a general CLT citation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
