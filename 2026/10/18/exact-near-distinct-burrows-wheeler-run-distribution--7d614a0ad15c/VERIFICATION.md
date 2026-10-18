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

The theorem covers every integer \(q\ge2\) and every choice of repeated letter \(c\) in the ordered \(q\)-symbol alphabet. Its proof partitions necklaces according to whether the two copies of \(c\) are cyclically adjacent, counts neighboring successor pairs, and subtracts from the primitive fixed-content total. The key finite checks are independent of the symbolic counting argument.

Run `python3 check.py` from this package directory. The program generates every multiset permutation for alphabet sizes \(2\) through \(7\), quotients by cyclic rotation using canonical representatives, constructs and sorts all rotations to compute the BWT, and independently verifies the one-cycle LF condition. For each duplicated symbol it compares the observed run histogram with the exact formula. Its expected successful transcript is in `check-output.txt`.

No code result proves the formula for larger alphabets; that is supplied by the direct counting proof in RESULT.md. No outside computation, external certificate, or independent audit is represented as completed.
