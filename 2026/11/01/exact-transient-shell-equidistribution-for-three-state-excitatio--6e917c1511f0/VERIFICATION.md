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

The independent external audit has not been performed. The mathematical claim is proved in `RESULT.md` by an exhaustive finite original-support transition table; for each initial support, the number of labelled assignments is a closed onto-function count. No finite-size experiment is used to infer the all-size result.

Run `python3 verify_book.py` with a standard Python 3 interpreter. The program verifies every cell of the 126-entry reduced transition table, the exact source-support weighting formulas and their summed census for positive page counts through twelve, and a separately implemented explicit-neighborhood evolution of **every** labelled coloring for each page count from one through eight, or 88,560 configurations per model. It compares the exact \((T,P)\) values, confirms that the two three-cycle state sets coincide, and tests equality of their next-state transitions.

The actual replay produced the final sentinel `BOOK_CCA_GHM_VERIFY_OK`; the complete short output is in `verification_output.txt`. The reduced original-support lemma, full 63-class tables per model and algebraic weighting, not this finite microscopic replay alone, justify the unlimited-parameter statement.

The old 1995 cyclic-automata paper's complete text was not available for novelty inspection; no certification of uniqueness or independent mathematical assessment is asserted.
