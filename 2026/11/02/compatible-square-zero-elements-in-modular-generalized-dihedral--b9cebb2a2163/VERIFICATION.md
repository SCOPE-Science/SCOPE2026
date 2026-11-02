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

# Reproduction and scope

Run `python verify_group_ring.py` then `python verify_compatible_differentials.py` with Python 3 and only its standard library. Both files are included in this finding and use genuine multiplication in the specified finite group algebra. The second script reconstructs the six binary and extension-field configurations, enumerates all square-zero elements directly (with the binary squaring map used to find the unique radical coefficient), calculates original noncommutative products, verifies compatible pairs are mutually annihilating, and independently checks the entire multivariate rank histogram against coefficient multiplication. It checks binary compatible triples for kernels \(C_3\) and \(C_5\). `verification_output.txt` captures the replayed results.

The six exhaustive compatible-pair checks cover \(H=C_3,C_5,C_7,C_3\times C_3,C_9\) over \(\mathbb F_2\) and \(H=C_3\) over \(\mathbb F_4\). All predicted pair totals and rank-vector histograms passed. The binary run reconstructs the original group basis and multiplication and has no dependency on the published Wedderburn classification. The quaternary run uses explicit extension-field arithmetic. The earlier univariate checker additionally validates every source matrix for seven cases.

The independent audit has not been performed. Neither these small-field enumerations nor matching program outputs constitute an infinite proof or independent historical-priority certification. The general proof is in `RESULT.md`.
