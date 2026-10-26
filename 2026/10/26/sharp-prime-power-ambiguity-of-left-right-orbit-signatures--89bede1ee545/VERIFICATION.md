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

# Reproducibility

Run `python3 verify.py` with a standard Python 3 interpreter. The standalone script explicitly computes the full left-right sign matrix for the digit-reversal cycle and all invertible powers for prime powers of sizes \(4\), \(8\), \(16\), \(9\), \(27\), and \(25\). It also enumerates every distinct cyclic permutation on \(4\), \(8\), and \(9\) ordered labels and verifies that the number of indistinguishable generating powers never exceeds the sharp bound, with equality attained. Expected output ends in `PASS`.

The computation is exact-integer, uses no random seeds and has no external dependencies. Its finite scope is not an exhaustive test for arbitrary prime powers. The written proof, specifically the second-smallest-point congruence and digit-reversal leading-differing-digit lemma, establishes the complete theorem independently of the checker.
