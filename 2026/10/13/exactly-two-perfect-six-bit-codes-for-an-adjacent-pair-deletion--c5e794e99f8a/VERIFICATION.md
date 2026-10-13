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
# Reproducible checks and their limits

Execute `python3 verify_buckets.py` and `python3 verify_dp.py` in the extracted package directory. Each is standalone standard-library Python. Both were executed directly from the packaged source paths and succeeded before packaging, and then replayed from extracted embedded bytes.

`verify_buckets.py` enumerates all \(64\) input words, all five adjacent-pair deletion positions, all eight receiver words with equal even-indexed bits, all \(36\) eligible equality candidates, and every pairwise-disjoint choice from the eight canonical buckets. It finds exactly two size-eight codes and checks both linearity and the two displayed channel symmetries.

`verify_dp.py` independently reconstructs receiver bitmasks by integer arithmetic, then performs a complete exact-integer set-packing dynamic program on all \(2^{16}=65536\) receiver subsets, retaining the largest partial packing and its count. It finds maximum \(8\), count \(2\).

The upper bound is proved directly, rather than inferred from the programs. The equality census is exhaustive because the eight transversal buckets are necessary for every optimum and no branch is omitted. These are ordinary reproducible finite computations and a self-review; no independent audit or external certification has been performed. All scientific conclusions are restricted to binary length six and a burst of **exactly** two consecutive deletions.
