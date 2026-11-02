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

Run `python checker.py` with Python 3 and NumPy. The script constructs the finite radial Toeplitz matrices independently of the angular basis; compares exact conjugated entries to the claimed blocks in 907 rational configurations; verifies the finite Hilbert--Schmidt formula; and checks three full finite singular-value spectra numerically. The executed output was:

```text
EXACT PASS 4 2 1/4 dimension 21 block-inner-products 441 HS-square 75/16
EXACT PASS 4 2 1/5 dimension 21 block-inner-products 441 HS-square 2853/625
EXACT PASS 4 1 1/3 dimension 5 block-inner-products 25 HS-square 29/9
NUMERIC PASS 2 5 1/4 dimension 63 max-spectrum-error 2.220446049250313e-16
NUMERIC PASS 2 5 1/2 dimension 63 max-spectrum-error 3.3306690738754696e-16
NUMERIC PASS 4 3 1/5 dimension 85 max-spectrum-error 4.440892098500626e-16
TOTAL_EXACT_BLOCK_ENTRIES 907
PASS
```

The unrestricted unitary decomposition, convergence and pole statements are proved analytically in RESULT.md. Finite sections do not by themselves certify infinite-dimensional claims, and the comparison to the inaccessible complete 2023 journal version is not settled independently.
