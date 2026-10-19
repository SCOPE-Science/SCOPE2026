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
# Reproduction and proof limits

Run `python3 verify.py` using standard Python 3 with no external dependencies. The script prints a line beginning `VERIFY_OK` on success and stops with an assertion on a mismatch.

The script enumerates the 194 arrows of the five-generator subset quiver, their 100 length-two paths, and the twenty intermediate-subset blocks. It checks the five-in/one-out and one-in/five-out patterns, pairwise disjointness of the 120 contributing arrows, the 74 remaining annihilator arrows, and the absence of cross-block length-two products. It exhaustively enumerates all noncentral commuting tuples for the rectangular five-by-one factor for parameters (field size, arity) \((2,1),(2,2),(2,3),(3,1),(3,2)\). It checks the 0/1/5 commutator-image rank distribution for field sizes \(2,3,5\), its class-number and weighted-count identities, and the global possible conjugacy-class size exponent set.

Finite enumeration does **not** establish the classification over arbitrary fields or for unbounded tuple length. Those conclusions follow from the path-algebra theorem and the explicit support-block and bilinear-commutator arguments in RESULT.md. The program does not independently reconstruct the full monoid-to-path algebra isomorphism; that is an established cited theorem. The verification does not constitute an independent mathematical audit.
