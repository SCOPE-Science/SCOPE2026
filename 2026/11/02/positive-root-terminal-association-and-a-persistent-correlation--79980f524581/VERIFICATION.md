---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact verification and scope

Run `python3 verify.py` with Python 3 and no third-party packages. The script enumerates all \((n-1)^{n-1}\) vectors of relevant attachment choices for each \(n=3,4,5,6,7\), constructs the actual rooted forests and computes raw sums, pair indicators and exact rational moments. Its output from the packaged version was:

```
n=3: enumerated=4, E(C)=3/2, E(L)=7/4, Cov(C,L)=1/8, Var(L)=3/16
n=4: enumerated=27, E(C)=2, E(L)=65/27, Cov(C,L)=2/9, Var(L)=230/729
n=5: enumerated=256, E(C)=5/2, E(L)=781/256, Cov(C,L)=159/512, Var(L)=27735/65536
n=6: enumerated=3125, E(C)=3, E(L)=11529/3125, Cov(C,L)=1236/3125, Var(L)=5135284/9765625
n=7: enumerated=46656, E(C)=7/2, E(L)=201811/46656, Cov(C,L)=1655/3456, Var(L)=1363543895/2176782336
PASS: 425 independent exact-rational identities; 50068 exhaustively enumerated configurations.
```

All computations use Python's `fractions.Fraction`, and the tree construction is independent of the derived identities. Assertions include the full root–terminal cross-covariance kernel and the joint probabilities of terminal events, not just the aggregate formula; upper-quadrant association is also checked for every nonconstant integer threshold in the tested sizes. The general covariance identity is proved through the independent-choice factorization and finite geometric derivatives in `RESULT.md`. The nonnegative-covariance assertion for all monotone transforms follows analytically from Bernoulli product-measure association, and the limiting constant follows from uniformly controlled Riemann sums. **No finite enumeration is claimed to establish these infinite-parameter facts.**

Scientific limitations: the model must be stationary and use uniformly chosen ordered pairs of distinct vertices; terminal means zero children, including isolated roots. No bivariate CLT and no full joint distribution are claimed. Independent audit or independent validation has not been performed.
