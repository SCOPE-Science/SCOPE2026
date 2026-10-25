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

Execute `python3 verify.py` using Python 3.10 or later. The standalone script has no nonstandard dependencies. Its first algorithm reduces the weighted face-poset filtration exactly over \(\mathbb F_2\) for both roots and all \(3\le n\le8\). The second constructs every chain of the filtered order complex independently and repeats exact persistence reduction for all \(3\le n\le5\). Both compare complete interval multisets to the stated formulas, including homological degree, both endpoints and multiplicity.

The expected successful terminal markers are `VERIFY_OK` and `DIRECT_ORDER_VERIFY_OK`. The direct order-complex checker enumerates \(12,74,540\) chains at \(n=3,4,5\), respectively, for either root type. The binary calculations are tests of the formulas, not all-field or all-size proofs. The all-field claim follows from the displayed integral sphere-skeleton and cone decompositions in `RESULT.md`, and the exact persistence statement follows from the literal filtration identifications and inclusion maps.

Independent scientific review or audit has not been performed.
