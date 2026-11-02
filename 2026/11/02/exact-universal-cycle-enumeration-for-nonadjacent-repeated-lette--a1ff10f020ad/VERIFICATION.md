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

# Reproducible checks

Run `python verify.py` from this extracted directory. The standalone Python 3 program needs no third-party packages, internet, or external input.

It builds every \(abac\), \(abca\), and \(abcb\) word on an alphabet of size \(q=3,4,5,6\), constructs the permitted length-three overlap graph, computes the proposed exact count and directed spanning-tree cofactors, and generates literal cyclic witnesses. Its independent fraction-free determinant computation covers \(q=3,4,5\). A direct rooted exhaustive Euler-tour enumeration for \(q=3\) returns \(12\). Every witness is checked by generating all wraparound length-four factors, testing that the factors are distinct, and comparing them with the complete specified language. The program outputs `VERIFY_OK` if all tests pass.

The formulas for arbitrary alphabet sizes are proved mathematically in RESULT.md; these finitely many checks cannot certify the all-\(q\) statement by themselves. No independent external audit or formal proof is represented.
