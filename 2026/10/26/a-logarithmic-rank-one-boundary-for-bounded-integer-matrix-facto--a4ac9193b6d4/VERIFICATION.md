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

# Verification of the bounded rank-one matrix-factorization count

Run `python verify.py` with Python 3 (standard library only). The program directly enumerates all admissible integer matrices \(B\) and separately counts admissible rows of \(A\), independently of the primitive-vector decomposition. It compares the resulting exact pair counts at heights \(T=1,2,3,4,5,6\) with the formula \(2S(T)-C(T)\). It also enumerates the primitive sup-norm shells for all \(h=1,\ldots,40\) and compares them with \(8\varphi(h)\).

Observed output:

`VERIFY_OK heights=1..6 direct_AB_counts=6 primitive_shells=40 integer_exact=PASS finite_only=YES`

The six full pair counts are \(100,404,996,1844,3076,4500\). All arithmetic is integral and exact. The exact-to-asymptotic transition uses the proved uniform Bézout fiber bound and Euler-totient sum, not an extrapolation from these finite computations. No independent audit was performed.
