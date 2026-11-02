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
Run `python3 verify.py` using Python 3.9 or later. It will independently construct Apéry sets by Dijkstra's shortest-path method on residues modulo the multiplicity, then calculate the same semigroups by dynamic-programming membership. The Frobenius numbers and symmetry are checked by an exact genus count. For every qualifying input, a direct pseudo-Frobenius gap test is compared with the proposed one- or two-generator candidate filter, with separate testing when the Frobenius number is divisible by three.

A completed run returned:

```
VERIFY_OK symmetric_inputs=1122 residue_classes=0:182,1:383,2:557 sharp_families=22 independent_apery_dp=yes
```

The census uses multiplicities four through nine with at most four listed generators and additional generators in the next fourteen positions, and 22 further parameterized sharpness cases. There is no probabilistic arithmetic and no timeouts in the reported successful run. The census is finite; the proof in `RESULT.md` establishes the universal statement.
