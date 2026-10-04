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

The symbolic check is the proof in `RESULT.md`: unique core decomposition, exclusion of prime-power cores, fixed-support finiteness, the prior two-prime classification, and Landau's fixed-\(k\) almost-prime theorem.

The executable `verify_eperfect_layers.py` independently evaluates the exponential-divisor sum from the exponent divisors for every integer through \(500000\). It verifies that each detected e-perfect integer decomposes into a powerful e-perfect core and a coprime squarefree factor, and it checks the two-prime layer in that finite range.

Running `python verify_eperfect_layers.py` produced:

`VERIFY_OK bound=500000 eperfect=4345 decomposed=4345 omega2=[36] cores=4 base36_omega3=1639 layers=2:1,3:1642,4:2146,5:542,6:14`

The finite computation does not certify the infinite two-prime classification, the finiteness of powerful cores at fixed support size, Landau's theorem, or the asymptotic itself. Those are handled by the mathematical proof and cited literature.
