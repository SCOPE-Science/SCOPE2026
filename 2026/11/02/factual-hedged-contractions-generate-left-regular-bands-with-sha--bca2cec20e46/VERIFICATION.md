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

# Verification of factual-contraction composition identities

The derivation in `RESULT.md` establishes the general statements for every finite nonempty carrier. The standalone Python program `checker.py` implements the factual row update directly on bitmask subsets. It computes the generated transformation monoids by breadth-first closure, rather than assuming the identities under test.

Run `python3 checker.py` with Python 3.9 or later. On the tested carriers of orders one, two and three, it checks the two proposed left-regular-band identities for every ordered pair of monoid elements, and recomputes the monoid after suppressing each nonidentity canonical generator. The unrestricted monoid counts are 2, 7 and 97, with generating ranks 1, 3 and 7. The corresponding serial counts are 1, 4 and 45, with generating ranks 0, 2 and 6. The checker verifies that the hub/private-marker construction has exactly the number of distinct transformations predicted by free injective words for one through five generators, in both unrestricted and serial versions. It also exhaustively compares the row update with its original propositional falsity-set definition on all three-world rows.

The verified execution returns the marker `ALL_CHECKS_OK`. The tests are finite consistency checks; the arbitrary-carrier rank formulas and exact equational theory depend on the explicit symbolic arguments rather than any computational extrapolation.
