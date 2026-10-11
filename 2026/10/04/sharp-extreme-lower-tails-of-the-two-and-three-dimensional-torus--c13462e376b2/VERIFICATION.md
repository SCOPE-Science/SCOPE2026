---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Starting from the centered-exponential spectral series, the cumulant generating function of Y_d=-L_d is K_d(s)=sum_{[k]}(s a_k-log(1+s a_k)), a_k=1/(2 pi^2 |k|^2). In d=3, the lattice Riemann sum gives K_3(s)~A s^(3/2), A=1/(3 sqrt(2) pi); the radial integral follows by differentiating J(a), and the Legendre constant 4/(27 A^2)=8 pi^2/3 was independently recomputed. In d=2, Abel summation with N(r)=pi r^2+O(r) gives K_2'(s)~(4 pi)^(-1) log s and K_2''(s)=O(s^-1). Chernoff upper bounds and exponential tilting, with variance negligible at the saddle scale, give matching lower bounds. The monotone inversion to lower quantiles is valid. No finite-sample tail claim is inferred from weak convergence.

## originality

PASS

Feng–Mordant identify the limiting laws and variance asymptotics but their accessible primary abstract does not state extreme lower-tail or lower-quantile constants. Wang–Zhao prove a broader second-Wiener-chaos/partition-function framework and sharp large-parameter growth in certain kernel settings, but only their abstract was accessible here; it does not expose the flat-torus constants or show that their hypotheses mechanically yield the submitted probability constants. The full-text public fetches for both recent arXiv papers failed, and the single authorized institutional fallback for Wang–Zhao returned worker unavailable/request invalid; no retry or bypass was attempted. This access limitation is retained as a material residual risk rather than treated as negative evidence.

## value

PASS

The extreme-tail constants are natural invariants of newly identified statistical limit laws and reveal a genuine dimension transition: double-exponential behavior in d=2 versus cubic stretched-exponential behavior in d=3. The lower-quantile formulas are useful for understanding rare low matching costs while the theorem carefully avoids unsupported finite-sample extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
