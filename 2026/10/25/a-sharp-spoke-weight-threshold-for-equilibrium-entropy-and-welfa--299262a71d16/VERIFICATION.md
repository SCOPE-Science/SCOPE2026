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

The proof in `RESULT.md` establishes the universal statement for all integers \(m\ge3\) and real parameters \(\lambda>0\) by direct payoff comparisons, a cyclic gap decomposition, transfer-matrix traces, and a deterministic cut-improvement argument. The separate code supplies a finite exact-arithmetic check and does not constitute an infinite proof.

With Python 3 standard library, execute:

```
python3 verify.py
```

This enumerates both hub actions and all \(2^m\) rim configurations for \(3\le m\le14\), at each of the six rational weights \(1/2,1,199/100,2,201/100,5\), verifying Nash and strict Nash tests by direct per-player payoff evaluation, all refined equilibrium counts, the weighted-cut optimum, the equilibrium welfare levels, and the price-of-anarchy numerator and denominator. It verifies the enumerator sequences through \(m=299\) using exact integers. A successful execution reports `PASS 72 wheel/weight cases; 393120 full profiles`, with two further `PASS` messages. These calculations do not cover all real weights or all \(m\); the proof handles those quantifiers.

No independent audit or externally assessed validation has been performed. Related general graphical-game literature establishes existence and potential-game principles but does not, on the inspected primary sections, imply the exact spoke-weighted wheel classification. An equivalent statement in less-visible Ising or local-cut literature remains possible.
