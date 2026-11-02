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

## Reproduction

Run `sh reproduce.sh` in the extracted package directory, with a C++17 compiler and Python 3. The C++ program reconstructs rank-four zero-tuple types using full equality, sort and incidence atoms for ordered quadruples; it checks orders 2, 3, 4, 5 and 7. The Python program implements the same mathematical extension-type definition independently with nested immutable sets and a separately coded field \(\mathbb F_4\), checking orders 2, 3 and 4. The atlas program checks all enhanced diagrams for selected tuples of lengths zero through three in orders four and five and compares both the sets of diagrams and all permitted final extension profiles.

Expected deterministic outputs appear in `computed_types.txt`, `independent_output.txt` and `atlas_output.txt`. Program output does not prove the infinite claim; see the full incidence-axiom back-and-forth proof in `RESULT.md`.

## Scope and limits

The types include repeated selections, both unary sorts, equality, and both orientations of the incidence predicate (only the point-to-line direction can be true). The computational checks use coordinate planes. The mathematical proof uses only affine-plane axioms, and therefore covers arbitrary finite affine planes. Historical priority remains incompletely verified. No independent audit is claimed.
