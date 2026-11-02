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

The precise domain is integer \(19\le n\le128\) and binary words with four \(1\)'s. The main enumerator visits each increasing four-tuple once. An exact decomposition counts separate zero-, two-, and four-one distinct Abelian square strings, with set-union treatment where two adjacent one-pairs have the same interior zero-gap. The complete table is in `abelian_four_optimized_n128.txt`.

The independent direct-substring C++ program reaches length \(50\) and stores each qualifying contiguous bitstring once; its complete table agrees with the exact-decomposition enumerator. The third Python program reconstructs all substrings for \(n\le18\). The deterministic family verifier tests every specified optimizer and checks equality with the exhaustive minimum and count. To reproduce, follow the compile/execute commands in RESULT.md.

**Limit:** The result is computationally exhaustive only for the stated finite range. Neither finite experiments nor cross-checks prove the optimizer classification at arbitrarily large lengths. The external audit channel remains unperformed.
