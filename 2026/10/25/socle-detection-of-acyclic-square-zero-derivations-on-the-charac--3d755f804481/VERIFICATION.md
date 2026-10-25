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
# Verification of the socle-rank classification

The supplied independent-from-formula implementation `check.py` constructs each finite-field derivation by choosing its two generator images. It computes \(D(xy)\), tests the two generator equations for \(D^2=0\), and computes rank of the resulting \(4\)-by-\(4\) action directly. An alternate calculation enumerates normalized projective covectors \([v]\), all nonzero vectors orthogonal to them, constructs the corresponding derivations and ranks, and compares with the closed counts.

Actual `python3 check.py` output:

```
exhaustive 2 {0: 1, 1: 9, 2: 12} OK
exhaustive 4 {0: 1, 1: 75, 2: 240} OK
matrix_parameterization 2 {1: 9, 2: 12} OK
matrix_parameterization 4 {1: 75, 2: 240} OK
matrix_parameterization 8 {1: 567, 2: 4032} OK
matrix_parameterization 16 {1: 4335, 2: 65280} OK
SQUARE_ZERO_DERIVATION_RANK_OK
```

The exhaustive calculations cover exactly the finite fields \(\mathbb F_2\) and \(\mathbb F_4\), not all fields. The parametrized checks also cover \(\mathbb F_8\) and \(\mathbb F_{16}\). The infinite theorem follows instead from the coordinate square identity and complete rank-one matrix parametrization in the written proof. No computer proof assistant or external certification is asserted. The script is self-contained and uses the standard Python runtime only. Independent audit status remains not performed.
