---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

With exact unpivoted QR, first block direction q1=(X,epsilon Y)/sqrt(X^2+epsilon^2Y^2) for independent real Gaussians X,Y (X=0 null event). Put s=epsilon^2Y^2/(X^2+epsilon^2Y^2); row energy squares are 1-(1-epsilon^2)s and epsilon^2+(1-epsilon^2)s, summing 1+epsilon^2. Algorithm 3.2 discards a smaller row iff its squared energy is <tau^2 on exact-zero residual. With u=(tau^2-epsilon^2)/(1-epsilon^2), and 0<u<1/2 for epsilon<(2c^2-1)^-1/2, both retained exactly when u<=s<=1-u (ties probability zero). Ratio Y/X is standard Cauchy, giving the difference of two arctangent probabilities. Limit as epsilon->0 is (2/pi) arctan(1/sqrt(c^2-1)). Eckart--Young singular values 1,epsilon show optimal residual epsilon<tau for rank1, while rank0 fails tau<||A||. Actual Frobenius look-ahead at first test rejects with probability at most 1-e^(-c^2 epsilon^2); with a complete rank-two block the next residual is zero and conditional probability differs from the unconditional Cauchy law by at most this rejection probability. Numerically evaluated exact formula at c=sqrt2,epsilon=0.005: 0.499976126 vs limiting 0.5; this is corroboration only. The publisher code explicitly sorts row norms and discards until strict test fails.

## originality

PASS

The primary Smith--Do--Chen method and row-energy greedy pruning are prior. Its algorithms/paper do not derive an exact Cauchy law or a constant nonminimal-rank probability for a natural singular-value-separated family. General QB/SVD rank theory gives optimum rank but not probability of this particular ordered QR pruning choice.

## value

PASS

Motivated exact diagnosis of the efficiency criterion introduced for a current adaptive matrix-free algorithm: a natural rank-two spectrum and Gaussian sketch have a limiting one-half chance of returning two rows despite rank-one optimality. The finite exact distribution, limiting threshold law and controlled look-ahead make a nontrivial reproducible boundary to a claimed near-minimal-rank property; routine singular-value optimality alone does not yield this sensitivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
