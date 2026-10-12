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

Run `python verify.py` with Python 3 and no external packages. The program constructs every labelled order of sizes one through three, every upset, every local neighbourhood family and every ordered list of upsets as scope and witnesses of arity at most the carrier size. It evaluates the instantial box clause directly and independently computes the proposed minimal-frontier core. It checks that the direct semantic equivalence classes agree exactly with core equality and that their number equals the product of antichain counts in the frontier fibres.

Observed outputs include `VERIFY_OK: exhaustive full ordered-witness semantic comparison {1: (1, 4), 2: (3, 32), 3: (19, 928)}`. The script also checks chain and discrete formulas for sizes one through four; explicit star examples with zero through three minima; and lower-bound witness-arity examples for discrete sets of sizes one through four. These are finite tests rather than certification of the general finite-order theorem, which follows from the symbolic frontier-dominance and reconstruction lemmas in RESULT.md.

All source citations are bibliographic. Independent audit has not been performed. The main preprint's full PDF was not available, and no unread material is certified as non-overlapping.
