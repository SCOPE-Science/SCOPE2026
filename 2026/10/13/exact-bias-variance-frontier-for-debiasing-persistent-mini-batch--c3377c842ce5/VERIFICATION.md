---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Condition on one fixed gradient population g_i, persistent R of size r, fresh S uniformly without replacement from complementary M=N-r, with s>=1, B=r+s<N. Inclusion probabilities yield E||gbar_S-b||²=(M-s)V/[s(M-1)]. The two estimators are U=(1-q)a+q gbar_S and C=(1-p)a+p gbar_S, where q=s/B, p=M/N, D=p-q>0. Their bias and variance follow by shared centered noise, giving Var(C)/Var(U)=(p/q)² if V>0. For G_t=(1-t)U+tC, MSE=(1-t)²D²||a-b||²+(q+tD)² sigma². Differentiation yields the constrained oracle t*, with t*<1 for sigma²>0, and full-correction/no-correction threshold Delta²>(p+q)sigma²/D. The 50% overlap expression reduces to (2-B/N)². Independent exact-rational subset enumeration for five populations corroborated, but the unrestricted statement uses finite-population algebra.

## originality

PASS

Lapucci–Pucci Section 5.1.1 analyzes the biased persistent estimator, proves a fully unbiased correction in Proposition 5.1, and reports its practical degradation in Remark 2. It does not compute the conditional variance inflation, shrinkage interpolation MSE, or oracle partial correction. Classical Horvitz–Thompson sampling yields ingredient inclusion probabilities, but not the source-specific optimized frontier as a finished mathematical statement. Generic shrinkage equivalence is a residual risk.

## value

PASS

The exact conditional bias-variance frontier quantitatively explains why the source deliberately uses persistent batches yet cautions that its fully unbiased correction degrades performance. It gives a mathematically meaningful oracle tradeoff and exact variance inflation at half overlap, while acknowledging an implementability gap and no full optimization guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
