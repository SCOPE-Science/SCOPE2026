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

# Reproduction and limits

Run the two standalone programs in this directory:

```sh
python3 verify_formula.py
python3 verify_extensions.py
```

The first program exhausts all \(42\) admissible ordered pairs in \(\mathbb F_9\), derives all three quotient traces, checks the complete five-row distribution, and compares the resulting rational-point counts with the original genus-three curve. The separate `spectrum_21.csv` certificate lists the \(21\) unordered pairs exhaustively with their exact traces.

The second program models the base field independently and enumerates points of every curve over \(\mathbb F_9\), \(\mathbb F_{81}\), and \(\mathbb F_{729}\), checking the predicted power sums and hence the zeta numerator. Its extension constructions assert the field-defining polynomials are irreducible. Both programs completed successfully in the recorded computation.

The analytic justification of the zeta factorization is the explicit quotient-involution argument in `RESULT.md`. The computations are exact finite exhaustions; they do not prove any claim about arbitrary finite fields or abstract isomorphism classes. No independent external validation has been performed.
