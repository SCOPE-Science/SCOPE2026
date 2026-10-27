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

# Reproducibility and scope

Run `python3 verify.py` using Python 3 and the standard library. It enumerates all points of a four-dimensional symplectic projective space over the three-element field, computes nonorthogonality, enumerates every clique by a strictly increasing vertex-index recursion, verifies that there are 2,880 seven-cliques and no eight-cliques, and finds exactly 864 seven-cliques avoiding the specified isotropic line. An independent direct matrix-commutator test checks all 496 distinct pairs in an explicit 32-member subset of the group. The exact exponent identity for the number of maximum group subsets is checked. These finite checks prove the enumerative ternary subproblem by exhaustive search; the general-field structural decomposition is established algebraically in RESULT.md.

The prior symplectic seven-clique census also appears in Lansdown, *Designs in finite geometry*, Chapter 4 Table 4.1. No independent external audit has been performed.
