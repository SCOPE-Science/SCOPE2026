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

# Reproduction and limitations

Run all three Python-standard-library programs alongside this document:

```
python verify_matrix.py
python verify_orbits.py
python verify_polynomial.py
```

All program outputs for this reviewed submission appear in `verification_output.txt`. The matrix program tests grid lengths \(7\), \(15\), and \(31\) using actual binary adjacency rows, tests exact corner moments, null-feedback extinction, eventual rank, and fixed-point dimensions. The orbit program constructs an independent site-by-site update routine, isolates the full seven-dimensional recurrent subspace on the \(3\times7\) example, and checks all \(127\) nonzero states return for the first time at step \(127\). The polynomial program supplies complete finite-field Rabin tests for degrees \(7\) and \(31\), and verifies the two Mersenne primality assertions by complete trial division.

These computations do not enumerate all \(2^{93}\) grid states or simulate a \(2^{31}-1\)-step orbit. Those universal conclusions follow from the exact determinant, Fitting-decomposition and irreducibility arguments in `RESULT.md`, together with the finite arithmetic certificates. No external independent audit is represented.
