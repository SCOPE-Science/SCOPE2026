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

The companion `verify_partition_pell.py` uses only Python standard-library exact integer arithmetic. Run:

```sh
python3 verify_partition_pell.py
```

It checks 684 values of the closed quadratic partition formula directly by summing restricted partitions. It computes fundamental Pell units using a continued-fraction recurrence for 87 distinct nonsquare-product parameter pairs with \(3\le a<b\le16\), searches modular orders of the associated integer matrices, and verifies integral-positive recovery, norm invariance, and partition-polynomial equality. It independently checks \(P_3(42)=P_4(48)=169\) by direct enumeration.

Expected output:

```text
VERIFY_OK section_checks=684 pell_pairs=87
```

The unrestricted theorem rests on the exact partition summation, classical Pell existence, the finite-order property of determinant-one matrices modulo \(2ab\), growth of the positive matrix orbit, and an elementary count of square-product parameters. The finite tests do not prove general Pell existence, general modular finiteness, or the infinite solution claim; these are treated in the written proof.
