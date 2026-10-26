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

The reproducible `verify.py` uses only Python 3 standard-library exact fractions and integer combinatorics. Execute `python3 verify.py`. It checks the norm against exact parity-conditioned binomial averages in each dimension 3 through 200, the unrestricted full-cube norm, relative parity factors and all adjacent difference identities. It also constructs every code vertex and every kernel row in dimensions 3 through 10, checks all Gram entries of the character family, and constructs sign inputs reaching the row sums.

Expected direct output:

`VERIFY_OK finite_n=3..200 exact_binomial_checks=791 direct_dimensions=3..10 direct_rows=1020 Gram_entries=492`

These are finitely many tests, not an exhaustive infinite proof. The all-dimensional proof is the explicit alternating-binomial identity and the exact kernel derivation given in `RESULT.md`. Independent audit has not been performed.
