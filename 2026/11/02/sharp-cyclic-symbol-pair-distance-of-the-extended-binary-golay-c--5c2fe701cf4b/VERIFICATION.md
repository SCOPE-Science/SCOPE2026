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

# Reproducibility of the optimized Golay pair-distance bound

Execute `python VERIFY.py` using Python 3.8 or later. The standalone program has no dependencies, network access, mutable inputs, or external data files.

It generates the 4096 parity-extended words of the degree-eleven binary cyclic generator; checks codeword uniqueness and Hamming enumerator; tests all 42504 five-element coordinate subsets for exact Steiner uniqueness; counts all induced edges of all 759 octads in the explicit coordinate order; and measures the entire pair-weight enumerator by direct adjacent-pair inspection.

Expected terminal final line: `VERIFY_OK`. Prior to that line it prints the Hamming enumerator, octad internal-edge counts, complete pair-weight enumerator, and optimum 12. The upper bound for arbitrary coordinate permutations follows from the fully tested five-design property, since every order includes a five-consecutive-coordinate subset and thus an octad containing its four edges. No enumeration of all 24! orders is needed or claimed.

The enumeration is exhaustive for this finite, explicitly defined code and its octads. It makes no claim about other Golay realizations without the appropriate coordinate relabeling, other lengths, or independent outside review.
