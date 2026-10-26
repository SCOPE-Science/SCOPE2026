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
# Verification record

The separate `verify.py` script uses only the Python standard library. Run `python3 verify.py` in the extracted directory. It tests the exact integer identity \(\kappa_1(P_k)=\sum_{j=0}^k c_jF_j\), where \(\prod_{i=1}^k(p_i+r)=\sum_j c_jr^j\) and \(F_j\) are ordered Bell numbers, against the defining divisor recursion for \(1\le k\le10\). It also records approximate positions and values of the maximizer of the finite prime-product logarithm at five prime cutoffs. These calculations were executed successfully in the working environment. There is no claim that finite tests verify the asymptotic limit.

The unrestricted argument in `RESULT.md` rests on effective prime-number-theorem estimates, including the weighted prime-summation kernel evaluations, the concavity/saddle argument, and the summation tail bound. No external or independent mathematical audit has been performed.
