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
# Verification

The exact domain is \(n\ge2\), \(0\le\alpha<1\), and \(\theta>-\alpha\) for the standard Pitman–Yor exchangeable partition.

The critical proof steps are:

1. At time two, \(1\sim2\) gives one block and \(1\not\sim2\) gives two blocks, with probabilities \((1-\alpha)/(\theta+1)\) and \((\theta+\alpha)/(\theta+1)\).
2. Expected block count obeys the affine recursion \(u_{m+1}=(1+\alpha/(\theta+m))u_m+\theta/(\theta+m)\).
3. Subtracting the two conditional recursions yields the exact gap \(R_n\).
4. Exchangeability makes the covariance with every unordered pair indicator identical, so averaging those indicators gives pair homozygosity without another approximation.
5. Sample homozygosity satisfies \(\widehat H_n=1/n+(n-1)Q_n/n\).

`checker.py` enumerates all set partitions through \(n=8\) for five rational parameter pairs and verifies total probability, pair-homozygosity mean, the covariance formula, the conditional gap, and the sample-homozygosity conversion using exact rational arithmetic. It also replays the conditional-gap recurrence through \(n=500\).

Finite enumeration is supplementary. The all-\(n\) claim is established by the symbolic recurrence and exchangeability proof.
