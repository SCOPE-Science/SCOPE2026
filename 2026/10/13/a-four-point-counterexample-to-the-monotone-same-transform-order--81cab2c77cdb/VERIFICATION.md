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

The finding is proved by exact finite counting followed by algebraic identities.

For three iid uniform draws from \(\{1,2,3,4\}\), the joint count of \((L,U)=(i,j)\) is \(1\) on the diagonal and \(6(j-i)\) above it. This yields row counts \((37,19,7,1)\) and column counts \((1,7,19,37)\).

For \(g_a=(0,a,1-a,1)\), the exact variance and covariance are
\[
\operatorname{Var}(g_a(L))=\operatorname{Var}(g_a(U))=\frac{95a^2-68a+28}{256},
\]
\[
\operatorname{Cov}(g_a(L),g_a(U))=\frac{-7a^2+4a+4}{256}.
\]
Subtracting the ordinary correlation \(41/143\) gives the exact factorization
\[
\frac{-96(3a-1)(17a-6)}{143(95a^2-68a+28)}.
\]
The denominator is everywhere positive, so the strict-improvement interval is exactly \(1/3<a<6/17\).

`verify.py` independently enumerates all \(64\) ordered triples at the rational witness \(a=7/20\), checks the exact positive gap, and checks the polynomial identities for the comparison and derivative using rational arithmetic. The optimizer \(a_*=6-4\sqrt2\) is established analytically from the derivative sign; no floating-point computation is needed for the proof.

Limits: the verification certifies the stated family and counterexample. It does not attempt to compute the full supremum defining \(R_4''(1,3:3)\) or \(R_4'(1,3:3)\).
