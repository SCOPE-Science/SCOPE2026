---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

I checked the required compact-uniform continuity-corrected expansion by a separate derivation. Write h=c/sqrt(n), with c=d/sigma. The standardized one-step characteristic function has log expansion -t^2/2-i gamma t^3/6+O(t^4); maximal span gives a strict modulus gap away from zero in the fundamental inversion interval. Inverting at lattice sites and scaling frequency by sqrt(n) gives site masses h[phi(x)+gamma (x^3-3x) phi(x)/(6 sqrt(n))]+O(h/n), uniformly in x: the central Fourier remainder is bounded in L1 by O(n^-1) Gaussian times polynomial integrals, and the outer part decays exponentially. These estimates follow by Taylor expansion up to scaled frequency n^(1/12), Gaussian domination up to a small fixed original frequency, and then the modulus gap. Bounded summands make the omitted tails beyond a sufficiently large constant times sqrt(log n) negligible, and summing the local remainder over O(sqrt(n log n)) sites gives o(n^-1/2). Midpoint summation reaches x+h/2, and integrating the Hermite density correction gives (1-x^2)phi(x), with the record's sign. The same mass estimate gives positivity on fixed compacts. On such compacts Gaussian inversion and rounding on the skewness-shifted grid yield boundary differences o(h); O(1/h) cells imply vanishing discrepancy probability. Changing variable to z-A(z)/sqrt(n) gives a Jacobian tending uniformly to one there, so averaging over full grid periods yields an independent centered uniform rounding residual even with the n-dependent grid origin. Monotone coupling is optimal for each fixed power. Bobkov's Theorem 1.1 controls a higher coupling moment at the scaled rate, justifying removal of the compact cutoff. The quadratic constant and symmetric specialization follow by direct integration.

## originality

PASS

The supported distinction is the higher-order lattice Wasserstein constants and the joint limiting law of the normal coordinate and its scaled quantile-coupling displacement. The entire r=1 constant, including skew laws, is classical Esseen–Zolotarev, not merely the symmetric c/4 special case. I do not credit the r=1 formula, the continuity correction, or a lattice-valid optimal-order bound as new. The checked prior work on those quantities does not imply the all-order result or the joint law.

## value

PASS

A transport CLT rate alone does not tell how lattice spacing and asymmetry contribute at first order. The joint quantile law identifies an independent uniform error at the scale of one cell after accounting for skewness. In particular it gives the exact quadratic lattice-plus-skewness decomposition without a mixed term and determines higher costs that are not encoded by the known W1 constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
