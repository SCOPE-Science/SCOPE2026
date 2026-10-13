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

The proof was checked symbolically against the exact divisor-sum coefficient formula. In particular:

- for odd composite \\(n=pq\\) with \\(p\\) the least prime factor, the retained \\(d=p\\) contribution is \\(2p(p^2-1)(q^2-1)(p^2+pq-2)\\), whose minimum on \\(p,q\\ge3\\) is \\(6144\\);
- for \\(n=2m\\), the expanded formula for \\(h(2m)\\) was checked term-by-term and the analytic lower function \\(L\\) was differentiated exactly; its derivative is positive on \\([5,\\infty)\\) under \\(\\log x\\le x/3\\);
- for \\(4\\mid n\\), the exact functions \\(A_1,A_3,A_5,K\\) were re-evaluated, including \\(K(4)=-1\\) and \\(A_3(4)=71\\), and the sign of \\(u\\) was checked algebraically in the exceptional \\(t=4\\) and general \\(t\\ge8\\) ranges.

The bundled `verify_margin.py` reconstructs coefficients from divisor sums and checks every integer through \\(20000\\). Its expected replay output is recorded in `VERIFY_OUTPUT.txt`. This finite computation verifies normalization and catches boundary/algebra mistakes; it is not evidence for cases beyond the checked range and is not used in the infinite proof.
