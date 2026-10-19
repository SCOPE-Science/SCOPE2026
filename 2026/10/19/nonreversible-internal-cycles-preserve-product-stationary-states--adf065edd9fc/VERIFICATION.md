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

Run `python3 verify.py` in the directory containing the seven public files. This self-contained program uses `fractions.Fraction` and enumerates finite labelled-ring states. It independently constructs every hop and blocked-particle color transition of the Markov generator; tests all master equations against the proposed weights, including normalizer \(LZ_{M,V}/M\); and computes direct net pair-color currents against the exact coefficient formula.

Successful execution gives 32 exact rational generator cases and 5,004 checked weighted state balances. The three cyclic rate selections include forward and reverse biases, and a separate noncirculant color generator tests global balance without pairwise balance. The special three-site, two-particle example and invariance under bias reversal are checked exactly. These finite comparisons do not prove the full-size theorem or establish novelty. The general proof is given in RESULT.md; neither independent audit nor independent validation has been performed.
