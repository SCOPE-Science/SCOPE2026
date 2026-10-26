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

# Verification of the finite classification

Run `python3 verify.py` from this directory. The verifier uses only the Python standard library and recreates `classification.json` exactly. The expected transcript is embedded as `verification_output.txt`.

It constructs the complete rank-three Hintikka signature for each of the 56 sorted triples of chain lengths two through seven, verifies 25 distinct signatures, checks 36 exact six/seven coordinate replacements, computes each class's smallest product cardinality and confirms the sharp maximum of 150. It also compares two logically equivalent but independently implemented extension enumerators (coordinate four-bit-intersection states versus full enumeration of all third-move vertices) on twelve cases and checks five additional boundary examples of side length eight.

The proof of the infinite reduction is mathematical: an ordinary three-round game on a finite chain identifies all lengths at least seven, and three coordinate strategies can be played in parallel on a Cartesian product. The finite code is exhaustive only on the expressly finite canonical domain. Neither this code nor its transcript amounts to an external or independent scientific audit, and no claim is made about larger signatures or more than three prime factors.
