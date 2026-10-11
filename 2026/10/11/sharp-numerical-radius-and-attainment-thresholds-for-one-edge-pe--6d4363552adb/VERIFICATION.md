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
# Verification of the numerical-radius thresholds

The proof is analytic, valid for arbitrary positive real \(p\) between one and infinity and over real or complex scalars. Its critical identities were verified by direct algebra:

1. For the forward shift, the Young tail deficit is at least \((p-1)u_2^p/p\), and the two-variable optimizer satisfies \(u_1/u_2=p^{-1/p}\).
2. For the backward shift, the deficit is at least \(u_2^p/p\), and the optimizer satisfies \((u_1/u_2)^p=(p-1)/p\).
3. For geometric-tail vectors \(u_1=a\), \(u_n=s^{n-2}\) with \(n\ge2\), the exact defects are \(ta-a^p-(1-s^{p-1})/(1-s^p)\) and \(ta^{p-1}-a^p-(1-s)/(1-s^p)\), respectively.
4. The weak-convergence argument uses \(1<p<\infty\) essentially to extract a weakly convergent subsequence. The tail sum is no greater than the tail \(\ell_p\) mass, which forces a maximizing weak limit to have unit norm when the radius exceeds one.

Numerical substitution for exponents \(5/4,3/2,2,3,4,10\) checks that finite geometric-tail defects at the boundary are negative and tend to zero from below. This finite test is not used as the proof. The claimed threshold, nonattainment and supercritical attainment follow entirely from the analytic inequalities. No external independent audit or formal certification is represented.
