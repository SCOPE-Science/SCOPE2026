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
For
\[
R_K=\sum_{x=0}^{K}p_X(x)F_Y(x-1),
\]
the exact omitted part is
\[
R-R_K=\sum_{x=K+1}^{\infty}p_X(x)F_Y(x-1).
\]
Since \(F_Y\) is nondecreasing,
\[
F_Y(K)\le F_Y(x-1)\le1
\]
throughout the omitted range. Summing gives
\[
F_Y(K)\Pr(X>K)\le R-R_K\le\Pr(X>K).
\]

The checker reconstructs the DAPW survival and PMF from the published formulas. For Scenario 4 and \(K=4041\), it verifies
\[
R_K-R_{K-1}<10^{-6},
\]
while independently calculating \(\Pr(X>K)>0.00416\) and the certified lower remainder bound above \(0.0041\).

The direct large-cutoff summation in the checker is only a consistency replay. The certificate itself is exact and does not rely on finite enumeration or on an assumption that the last summand controls the remaining tail.
