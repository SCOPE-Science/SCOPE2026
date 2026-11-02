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

# Verification and reproducibility

Execute `python3 verify.py` from the directory containing this file and the checker. No third-party packages or external data are required.

The checker enumerates \(2^{16}=65536\) Boolean feedback truth tables. A register is retained precisely when its all-zero state has a full orbit of length \(32\). A separate Euler-circuit traversal of the order-four de Bruijn graph forces the unique all-zero five-bit edge first, enumerates all admissible used-edge paths, and verifies set equality with the feedback cycles. These are distinct exhaustive constructions.

The first discrepancy calculation takes the range of signed prefix sums. The other examines all cyclic substrings of lengths \(1\) through \(32\) at all \(32\) starting positions. Expected exact output:

```
feedback_maps=65536 canonical_cycles=2048
euler_circuits=2048 exactly_matching_cycles=True
discrepancy_histogram= {5: 224, 6: 688, 7: 912, 8: 224}
mean_discrepancy=839/128
cycle_list_sha256= e8b5746482780303fec542789b123a2d51a892f460137bb9f8a96c85fec30421
VERIFY_OK
```

The two exhaustive encodings establish a finite exact answer at order five. They are not a proof of any general formula in higher orders. No independent audit or human scientific validation is represented by these computations.
