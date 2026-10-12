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

# Reproducible checks

Run `python3 verify.py` with Python 3. No nonstandard packages or network access are required. The script uses exact `fractions.Fraction` arithmetic and exhaustive finite Cartesian products, so no floating-point tolerance is involved.

The successful execution reported: `PASS: 4368 exact finite row/valuation cases; 12 rational increasing-prefix checks; no infinite inference from enumeration`.

The finite tests confirm attainment on finite weighted rows for a four-value grid and the specified finite prefixes of non-attainment examples. They do **not** establish any assertion quantified over arbitrary infinite frames, all real weights, or all modal formulas. Those claims follow only from the four-part analytic proof in `RESULT.md`. The infinite counterexamples are explicit positive sequences, not based on extrapolating a finite failure.

In the symbolic argument, the key calculations are the Gödel residuum at strictly smaller positive atomic values, and the fact that a strictly positive diamond supremum is controlled by finitely many successors above half that supremum. The assumptions include a nonempty world set, unrestricted atomic truth assignments, and ordinary choice for extracting countable sequences from infinite sets. No external validation has been performed.
