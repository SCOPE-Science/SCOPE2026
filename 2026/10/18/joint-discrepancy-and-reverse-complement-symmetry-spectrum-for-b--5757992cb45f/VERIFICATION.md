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

## Exact reproducibility

The result is a finite exhaustive theorem. Run both Python 3 files beside this document; neither has dependencies outside the standard library:

```
python3 verify_fsr.py
python3 verify_halfwords.py
```

The exhaustive feedback-register checker visits all 65,536 Boolean functions of four binary variables and tests each induced five-state shift register. Every order-five binary de Bruijn cycle is accepted exactly once, because its successor function is uniquely of the form \(f(x_0,t)=x_0\oplus g(t)\), and the initial state \(00000\) anchors rotation. It computes exact prefix-sum discrepancy, reverse-complement fixedness, and complement/reversal orbit cardinality. Expected output includes `FSM ALL 2048`, `FSM CR 64`, and `FSR_OK`.

The structurally separate half-word checker enumerates all 65,536 binary 16-bit words \(X\), forms \(X\,cr(X)\), checks uniqueness of every cyclic five-factor by direct integer encoding, and deduplicates cyclic rotations. Expected output includes `halfwords valid 128 unique rotations 64 hist {5: 16, 6: 16, 7: 24, 8: 8}` and `HALFWORDS_OK`.

This second method independently confirms the reverse-complement-fixed discrepancy counts but does not independently enumerate the unrestricted group orbits. It uses the classical CR normal form quoted as Chang--Wang Lemma 1.1. All arithmetic and coverage decisions are exact. The formulas do not extrapolate beyond binary order five.

No separate independent scholarly audit has been performed.
