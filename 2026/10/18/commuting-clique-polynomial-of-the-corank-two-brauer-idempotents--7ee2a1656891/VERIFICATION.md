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

Run `python3 verify_brauer_clique.py` with Python 3 and its standard library. The program contains independently implemented perfect-matching enumeration, three-row diagram multiplication using union--find, rank evaluation, candidate generation, the complete five-label commutation census, and a disjoint-support clique enumeration.

The output includes `FULL_IDEMPOTENTS 2 1`, `FULL_IDEMPOTENTS 3 9`, `FULL_IDEMPOTENTS 4 30`, `FULL_IDEMPOTENTS 5 70`, and `ALL_B5_COMMUTATION_PAIRS 2415 PASS`. It also compares all clique polynomials for degrees two through eight with the formula. Completion yields `VERIFY_OK_BRAUER_CORANK_TWO_CLIQUES`.

The abstract support-reduction proof shows that every possibly noncommuting pair in arbitrary degree embeds as a multiplication pair using at most five nonvertical labels. The verifier covers *every* such five-label configuration; a finite data sample without that reduction would not prove the global claim. Unrelated-rank products, higher-rank classifications, and independent mathematical validation are not covered.
