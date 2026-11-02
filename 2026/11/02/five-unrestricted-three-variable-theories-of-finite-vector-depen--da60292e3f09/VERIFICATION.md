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

# Verification and scope

The proof is the explicit all-parameter two-anchor extension table and the three-pebble invariant in `RESULT.md`, not the finite output files.

The script `support_check.py` enumerates every ordered pair and every possible third vector for each of seven specified finite vector spaces. It groups pairs by their equality/zero/parallel/independent status, asserts that each status has one common extension support within a structure, and asserts agreement of that support across the structures in a common field-size bin. The field of order four is represented using a polynomial quotient over the binary field.

The independently written `count_check.py` evaluates all third-vector possibilities for canonical anchor pairs (and all distinct nonunit scalar ratios) and asserts equality with the symbolic extension-count formulas. The output files `support_output.txt` and `count_output.txt` were obtained by executing the delivered source scripts.

Reproduction: `python support_check.py` and `python count_check.py`, with Python 3 and no nonstandard dependencies. These checks confirm the sample and formula implementations, not logical equivalence for every dimension and field without the written algebraic argument. Full primary-article historical-priority checking was not possible for Pierce (2009); this is an access limitation, not a substitute for science.
