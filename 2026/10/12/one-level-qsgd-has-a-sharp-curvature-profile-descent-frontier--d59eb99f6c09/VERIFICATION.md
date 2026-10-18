---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For one-level QSGD, Q_i(g)=||g|| sign(g_i) B_i where B_i is Bernoulli(|g_i|/||g||). Thus E Q_i=g_i and E Q_i²=||g||||g_i||, including zero-coordinate cases. Expanding f(x−ηQ) exactly gives f−η||g||²+(η²/2)||g||∑ a_i|g_i|. Cauchy–Schwarz bounds ∑a_i|g_i| by ||a||₂||g||₂ and attains equality with |g_i| proportional a_i, i.e. all |x_i| equal. This proves iff 0<η<2/||a||₂ for strict universal one-step expected descent on a positive diagonal quadratic. For A=LI, h=ηL, maximal conditional ratio is 1−2h+√d h², minimized at h=1/√d; h=1 expands for d≥5. The source Bernoulli definition was checked in the full QSGD primary PDF, and the packaged bounded enumeration source inspected.

## originality

PASS

QSGD (Alistarh et al.) already provides unbiasedness and variance bounds and implies the general √d scaling, and generic compressed-gradient papers provide related conservative rates. The exact state-dependent diagonal curvature-profile threshold, equality direction, and one-step identity are the assessed additional statements. Fixed random-sketch matrix bounds do not immediately specialize to state-dependent Bernoulli probabilities.

## value

PASS

The exact per-coordinate curvature profile ||a||₂ rather than L√d distinguishes quantizer-induced stability from generic scalar variance bounds and identifies a sharp step threshold and worst-case dense direction. This directly informs a natural severe-quantization regime even though it is a restricted diagonal quadratic calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
