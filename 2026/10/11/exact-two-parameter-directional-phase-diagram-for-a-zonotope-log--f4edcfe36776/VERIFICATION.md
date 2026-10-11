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

The result is the exact two-parameter directional classification stated in `RESULT.md`. The accompanying source file `verify.py` is self-contained and requires Python 3 standard libraries only. Run `python verify.py` from this directory.

The verifier reconstructs the four generator lists explicitly, computes every order-four determinant as a signed 24-permutation sum in `fractions.Fraction`, and sums absolute determinants over all four-subsets. It uses a grid of 12 nonnegative rational values for each of two parameters, testing 144 pairs, including axes, transition chamber boundaries, and asymmetry cases. Every computed four-volume tuple agrees with the claimed piecewise-absolute-value expression, and every determinant-defined defect agrees with both the global expression and the applicable chamber expression. The expected exact terminal output is `VERIFY_OK 144 exact rational full determinant cases, including all chamber boundaries`.

The algebraic proof additionally lists the signed minor forms and their multiplicities. The continuous sign theorem is established analytically from those determinant identities, not from finite sampling. No exhaustive numerical search over real parameters, independent external review, or broader zonoid classification is claimed.
