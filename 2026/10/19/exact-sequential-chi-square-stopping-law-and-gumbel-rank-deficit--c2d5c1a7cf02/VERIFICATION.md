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

Conditional on the history at residual rank m, an orthogonal change of coordinates turns the fresh projected block into bm independent N(0,1/b) entries. Hence its squared Frobenius norm times b is chi-square with bm degrees of freedom, irrespective of basis orientation and prior failures. A failed test has full block rank almost surely for m>=b; rank zero terminates surely. Multiplying conditional failures and then the final success yields the claimed all-grid law, including q_n=0 if it occurs at small n. With q=q_n, j=m-q, and s=sqrt(b/(2q)), Stirling expansion of the standardized gamma density gives relative normal-tail accuracy uniformly for 0<=j<=C sqrt(q log q): choose the density truncation constant sufficiently large that the discarded Chernoff tail is smaller than the smallest normal tail in that range. Also chi-square stochastic ordering in m and the Chernoff bound at C sqrt(q log q) make the far-rank sum o(1) for C sufficiently large. The standardized mesh bs=b^(3/2)/sqrt(2q) makes the relevant hazard sum asymptotic to sqrt(2q)/b^(3/2) times the integrated normal tail at z=β+x/β. That tail is asymptotic to φ(z)/z²; requiring the leading hazard at β to be 1 gives exactly β²+4 log β=log(q/(π b³)). The hazard tends to e^(-x), its largest term tends to zero, and the no-success product limits to exp(-e^(-x)), with the stated cutoff and sign. The rank shortfall law then follows by tightness; bounded last-block deletion changes the Gumbel-scaled rank by at most bβs=o(1), not preserving the finite distribution. Independent replay: python3 /workspace/branches/independent_checks.py 5; 8,000 actual Gaussian QR stopping trajectories for n=12,b=3,q=6 agree with the exact PMF within test tolerance, and bounded incomplete-gamma products at b=1,4,16 show the predicted direction of finite-size convergence. The analytic hazard argument, not the latter comparison, establishes the limit.

## originality

PASS

The raw Gaussian estimator and blocked inspection are antecedents. Qualitative false acceptance and the leading one-block deficit scale are expressly not claimed as new in the original. The supported distinct result is the exact all-grid absolute-threshold stopping law combined with fixed-width, second-order Gumbel asymptotics and the corresponding explicit centering. No verified equivalent or stronger claim covering this law was identified.

## value

PASS

On an exact flat-spectrum benchmark, the rule uses individually unbiased estimates but stops outside tolerance with probability tending to one. The complete finite law quantifies that risk across block widths, and the Gumbel centering gives a second-order rank calibration beyond the already known leading-scale failure. Showing that bounded last-block pruning cannot reverse the effect addresses the practical algorithmic distinction. This is a benchmark for sequential inspection, not a claim that identity matrices are compressible or that relative norm errors are large.

The dated certificate retains the supplied scientific assessment, sources and limitations.
