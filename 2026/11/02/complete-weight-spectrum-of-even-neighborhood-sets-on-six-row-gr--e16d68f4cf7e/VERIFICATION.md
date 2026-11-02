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

The standalone `verify.py` uses only the Python standard library. Run `python3 verify.py` with these files placed together.

The recorded replay produced:

```text
EXHAUSTIVE_64_INITIAL_COLUMNS_OK
INDEPENDENT_GF2_MATRIX_ELIMINATION_OK 54
COLUMN_RECURRENCE_AND_DIRECT_PARITY_OK 144
VERIFY_OK
```

The verifier checks all \(64\) first-column vectors in the \(6\times8\) base board. It then builds the original closed-neighborhood matrix independently, row-reduces it over \(\mathbb F_2\), enumerates every resulting nullspace vector, and compares the exact Hamming spectrum for lengths \(1\) through \(54\). A separate recurrence method checks lengths \(1\) through \(144\) and validates the original parity equations for every generated word.

These are finite verification ranges, not a substitute for the infinite proof. The all-length result is deduced from the explicitly displayed characteristic polynomial, invertible residue classes, matrix recurrence, and exhaustive 64-entry base classification in `RESULT.md`. No external certification or independent mathematical audit is claimed.
