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

# Reproduction

Execute `python3 verify_jaccard.py` with the supplied `census_n_le_6.csv` in the same directory. The program computes the complete rational census table from inclusion–exclusion and independently enumerates all labeled sample pairs; the two implementations agree at all 135 sample-size/profile cells for census sizes one through six. It reproduces 29 integer-partition profiles, with a single strict decrease for \((1,5)\) between sizes two and three.

It also checks the analytic singleton/dominant family at the listed finite parameter values and separately enumerates all feasible ordered disjoint pairs through the specified small sizes. These tests confirm the code calculations only; the unrestricted formulas and the disjoint-protocol gap are established by the algebraic argument in the main result. No experiment is used to establish a claim about all integer population sizes.

The first-publication date for the cited 2002 autosimilarity study is stated by its publisher. The technical full text of that study was not accessible for complete statement-by-statement novelty comparison, and independent validation has not been performed.
