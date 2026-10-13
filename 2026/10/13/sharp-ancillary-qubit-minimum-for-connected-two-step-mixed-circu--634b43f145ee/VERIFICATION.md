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

The proof in RESULT.md is an all-orders proof over the binary field. The accompanying standalone checker constructs the full symmetric adjacency bit matrix for every admissible connected step pair at even orders \(6,8,\ldots,72\). Direct Gaussian elimination is independent of its polynomial nullity function: the script compares those computed ranks, checks the lower bound for every pair, and checks the proposed sharp witness at every order. To reproduce, extract `artifacts/verify.py` and run `python3 artifacts/verify.py`. Expected stdout:

`VERIFY_OK n=6..72_even connected_step_pairs=21152 exact_GF2_rank_and_cyclic_kernel_agree=true minimum_and_witness=true`

The script uses only the Python standard library. Finite enumeration is not a certificate for arbitrary order; the repeated-root argument, divisor bounds, and sharpness construction provide the proof. Ordinary real/complex adjacency nullity is not the invariant computed by this checker. Independent audit has not been performed.
