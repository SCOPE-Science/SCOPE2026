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

The infinite theorem is verified by the proof in `RESULT.md`; the finite computation below is an independent stress test, not a replacement for that proof.

`verify_mu3_cyclic.py` uses integer arithmetic only. It builds \(\Phi_N\) recursively, reduces powers exactly modulo \(\Phi_N\), and tests vanishing of each candidate \(3\times3\) Fourier determinant as an exact cyclotomic identity. For every \(3\le N\le36\), it exhausts normalized supports \(\{0,a,b\}\), handles row-equivalent frequency classes, and checks every nondegenerate two-zero kernel. The packaged replay produced:

```
checked N=3..36
normalized_supports=7140
nondegenerate_pair_kernels=168000
exact_cyclotomic_determinant_tests=4950750
VERIFY_OK
```

The computation verifies only the stated finite range. The proof covers all \(N\ge3\). No numerical tolerance is used in the finite checker.
