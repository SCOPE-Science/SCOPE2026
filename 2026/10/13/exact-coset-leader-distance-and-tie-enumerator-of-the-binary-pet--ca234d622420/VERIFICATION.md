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

# Finite exact verification

Execute `python3 verify.py` using a standard Python 3 interpreter. The checker prints `VERIFY_OK` only after all asserts pass; it requires no third-party libraries.

The code enumerates each of the 32768 binary edge patterns and verifies that their vertex parity syndromes lie in the 512 even vertex subsets. It computes each syndrome’s minimum error weight and tie count. Independently, breadth-first search of the syndrome graph verifies each shortest distance and its number of shortest ordered paths, using the identity \(P(t)=d(t)!m(t)\). The 120 natural graph automorphisms are applied to all syndrome masks to generate 18 disjoint orbits; their table is compared entry-by-entry. The zero-syndrome weight histogram and the all-ones syndrome’s six leaders are checked separately.

The computation is exhaustive only for the defined ten-vertex graph; it does not prove anything for other graphs and does not constitute independent validation by another party. Arithmetic is exact integer and bitwise arithmetic.
