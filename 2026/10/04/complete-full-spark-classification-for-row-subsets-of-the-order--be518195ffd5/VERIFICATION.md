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
The finite proof certificate is `verify_z14_fullspark.py`. It enumerates every uniformly distributed subset of \(\mathbb Z_{14}\), reduces them to affine representatives and complementary classes, checks every maximal minor of the low-cardinality representatives using two exact finite-field reductions, and proves the four exceptional witnesses by exact reduction modulo \(\Phi_{14}\). The script confirms the complete size-by-size census and ends with `VERIFY_OK`.

A nonzero finite-field reduction is used only as a one-way certificate of nonvanishing over \(\mathbb C\); a modular zero is never used to infer complex singularity. The four singular representatives are certified separately by exact cyclotomic divisibility. No claim beyond Fourier order \(14\) is certified.
