---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Hübener et al. §II Lemma 1 applies to the nonzero symmetric complex multilinear form for n≥4 and forces proportional local factors at every maximum, not merely the existence of a symmetric maximizer. For any interior latitude both Dicke amplitudes are nonzero, and the phase of their ratio is (n−2)φ up to sign. The only optimal phases modulo 2π are 2πj/(n−2). The two poles have zero overlap. With x=(1+tanh t)/2, the phase-maximized squared overlap is n·2^(1−n) cosh²(at)/coshⁿ(t), a=(n−2)/2. For a>1 the logarithmic derivative of tanh(at)/tanh t is negative by sinh(2at)>a sinh(2t), so the ratio strictly decreases from a to 1 on t>0. Comparing with n/(n−2) proves no positive root for n=5 and exactly one for n≥6, with the indicated change from increasing to decreasing. For n=4 the log-overlap derivative is −2 tanh t. This gives the complete latitude and phase counts. At n=6, z=tanh t gives z²=1/3, cosh(2t)=2 and cosh⁶t=27/8, hence 2/9. On x≤1/2 the contribution squared of the minority Dicke term is at most 2^(−n), using x(1−x)≤1/4, while the dominant term is bounded by its value at x=1/n; symmetry and testing x=1/n give the same limiting lower and upper bound 1/(2e). The inspected verifier was not executed; its finite grids do not establish this optimizer classification.

## originality

PASS

Pass is for the uniform all-n classification and limit. The scalar optimization framework and the individual n=4,5,6,7 cases must not be counted as novel: the four-qubit state is locally equivalent to GHZ, and Aulbach–Markham–Murao treat the same tri-, square-, and pentagonal dipyramid states. Those examples already show the observed switch from equatorial rays to two circles at six qubits; they do not prove the two-latitude branch persists at every larger n or the limit. The same-day Resultary hit uses the same state but a different observable. No inspected statement covers the uniform branch theorem.

## value

PASS

An all-dimension solution for a natural symmetric entangled family turns known small-dimensional configurations into a sharp global branch theorem. The uniqueness of the latitude, full phase-resolved count at every n and limiting overlap give information beyond observing the transition in low dimension or reporting numerical stationary points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
