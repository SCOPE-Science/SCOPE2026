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

The mathematical proof in `RESULT.md` is valid for every integer \(k\ge1\), with no unverified infinite-case computational assumption.

To reproduce the independent finite calculations, run `python3 checker.py` with Python 3.8 or later, requiring only the standard library. Compare its complete output against `checker_output.txt`; it ends in `VERIFICATION_OK`.

The checker exhaustively enumerates all possible residual fingerprints for successor-dyadic shifts \(c=2^k+1\) for each \(k=1,\ldots,8\). It uses the exact finite quotient decomposition of the infinite Thue–Morse word into low-order residues and all four possible adjacent high-order Thue–Morse bit pairs. It separately checks the disjoint even/odd partitions and their respective Fibonacci cardinalities. Additional finite tests compare residual-function signatures with carry-offset fingerprints for shifts 1 through 40 across 70 prefix values each.

Finite checks are not relied upon to certify the proof for unbounded \(k\), nor do they establish literature originality. The mathematics was reviewed against the stated definitions, boundary cases and original sources. Independent scientific audit has not been performed.
