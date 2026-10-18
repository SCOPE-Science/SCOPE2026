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

# Verification

`CHECK.py` independently enumerates all possible physical ordered read vectors from each source and each of the permitted deletion positions; the graph and inverse-ambiguity histogram are generated from those readouts, not from the theoretical formulas.

The checker compares physical confusability with the unit-transfer adjacency criterion, confirms unique parents for each inconsistent output, confirms that each consistent output has as many parents as its shortened word has constant runs, tests the complete multiplicity histogram, tests the exact edge sums and the adapter-independent closed edge count when length is at least three, and checks the total distinct received vectors.

The executed checker output (`CHECK.out`) records successful tests for every boundary pair in each of these ranges: alphabet size 2, lengths 1 through 9; alphabet size 3, lengths 1 through 6; alphabet size 4, lengths 1 through 5; alphabet size 5, lengths 1 through 4. This is 270 fully enumerated combinations. The proof in `RESULT.md` establishes the unrestricted integer-parameter theorem and handles short cases separately; finite testing alone does not prove it.

No independent scientific audit or validation has been performed. The full content of the directly relevant Chee–Vu 2020 article was unavailable; only its abstract and downstream accounts could be compared.
