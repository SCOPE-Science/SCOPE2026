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

# Verification record

The proof applies to all integers \(n\ge3\) and all real \(p\in(0,1)\). It uses a harmonic birth-and-death scale on the integer lift, a two-boundary characterization of the last-visited label, and finite-interval gambler's ruin with two applications of the strong Markov property. No large-sample approximation is needed.

The standalone `verify.py` requires Python 3.10+ and uses only its standard library. Execute `python3 verify.py`. The recorded execution yielded `VERIFIED 20580 exact rational checks`.

One group of checks compares the explicit formulas against a separate exact scale-function hitting calculation for sizes \(3\) through \(64\), across five rational biases. A second group independently computes absorption probabilities of the original cyclic, time-dependent walk using rational Gaussian elimination over visited masks, positions, and phase, for sizes \(3\) through \(7\), across four rational biases. Both groups also test probability normalization or positivity. The finite checks support the proof; they do not certify infinitely many cases or establish novelty. External independent mathematical audit has not been performed.
