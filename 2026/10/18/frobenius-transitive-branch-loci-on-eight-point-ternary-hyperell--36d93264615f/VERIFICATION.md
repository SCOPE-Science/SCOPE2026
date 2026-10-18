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

The proof is mathematical and independent of the finite checks. To repeat computational corroboration, execute `python3 COUNT.py` and `python3 CHARACTER_CHECK.py` using Python 3 standard library. Each program prints and asserts its own exact comparisons. `COUNT.py` exhaustively enumerates monic ternary polynomials congruent to one modulo \(T^3-T\) in degrees \(4,6,8,10,12\), checks irreducibility using polynomial gcd and Frobenius powering, and compares the counts with the closed formula; it also checks arithmetic formula positivity through degree forty-two. `CHARACTER_CHECK.py` constructs explicit finite fields at degrees six and eight, counts three simultaneous square-character constraints, and independently filters exact-degree roots. Finite checks do not constitute proof of the all-genus statement; the proof in `RESULT.md` does.

The complete-curve rational-point count uses the three split finite fibres and two split points above infinity. The geometric smoothness follows from irreducibility over the perfect field. Neither program establishes independent external audit.
