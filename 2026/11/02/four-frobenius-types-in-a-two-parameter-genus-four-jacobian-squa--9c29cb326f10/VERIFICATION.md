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

# Verification notes

`verify_bruin_kulkarni.py` is a standalone Python 3 checker using only the standard library. Execute it from its directory with `python3 verify_bruin_kulkarni.py`. It uses polynomial arithmetic over prime fields to compute \(\gcd(F(X),X^{p^d}-X)\) for \(d=1,2,4\). From these gcd degrees it independently obtains the number of Frobenius cycles of lengths \(1,2,4\), verifies the ten roots split by degree four, and compares them with the character-based classification for each admissible parameter. It also checks the degree-ten polynomial directly at every field element and confirms the exact frequency counts.

The completed exhaustive prime-field runs were:

- \(q=3\): \(3\) coefficient pairs, frequencies \((0,0,0,3)\).
- \(q=5\): \(13\) coefficient pairs, frequencies \((0,0,4,9)\).
- \(q=7\): \(31\) coefficient pairs, frequencies \((0,4,9,18)\).
- \(q=11\): \(91\) coefficient pairs, frequencies \((1,14,31,45)\).
- \(q=13\): \(133\) coefficient pairs, frequencies \((1,18,51,63)\).
- \(q=17\): \(241\) coefficient pairs, frequencies \((3,36,94,108)\).
- \(q=19\): \(307\) coefficient pairs, frequencies \((6,52,114,135)\).
- \(q=23\): \(463\) coefficient pairs, frequencies \((10,80,175,198)\).

The checker additionally verified the cardinalities of Frobenius-invariant even-subset classes modulo complement in all eight cycle configurations. Independent direct coefficient and rational-root enumeration in the quadratic extensions \(\mathbb F_9\) and \(\mathbb F_{25}\) checked respectively \(57\) and \(553\) smooth pairs, with frequencies \((0,6,21,30)\) and \((10,90,219,234)\). All tests passed, ending in `BRUIN_KULKARNI_PRIME_POWER_AND_TWO_TORSION_PASS`.

These finite checks do not prove the theorem for untested finite fields; the universal proof is in `RESULT.md`. The literature-comparison limitations and the scientific reasoning for correctness, originality, and value are in `REVIEW.md` and `AUDIT.json`. No independent audit has been performed.
