---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Partial fractions and Fourier transform give four geometric-series terms for the Zak kernel B(z,r); elimination in the upper/lower torus halves and factored boundary cases yield exactly three zeros (0,0),(1/2,0),(0,1/2). Zak-Parseval reduces the lower frame bound to min(|Zg(x,omega)|²+|Zg(x,omega-delta)|²), which is zero only when the two zeros share x at delta=1/2. At this offset the spatial and frequency linear Taylor directions are orthogonal; local minimization of c0 u²+ch(u-1)² yields c0*ch/(c0+ch), while compactness/nondegeneracy control global minimizers. Independently calculated the exact c0/ch coefficient numerically (0.269312334496...) and optimized actual two-coset symbol near delta=.5 for epsilon=.01,.003,.001; all checks passed. Full infinite frame claim rests on algebraic zero classification and compactness, not sampled grid.

## originality

PASS

The directly relevant Ghosh preprint studies this very same window for rectangular lattice Gabor frames. Its public abstract and indexed content concern rational rectangular densities; a two-frequency-coset union at general irrational or non-half rational offset is not a single rectangular lattice. The known parity-based nonframe obstruction could explain the half-shift failure but neither sufficiency at every other offset nor a sharp lower-bound coefficient. Crucially, Ghosh full text could not be obtained from arXiv/OA and authorized institutional access was blocked, so priority of the Zak-zero calculation and possible general-frame corollaries remains materially unverified. This supports qualified best-knowledge PASS, not an assertion that the unread source is noncovering.

## value

PASS

The exact two-coset frame/nonframe frontier and the sharp quadratic instability constant for a natural rational odd window quantify robust sampling beyond the single-lattice frame set. The nonframe at the half shift is an analytically motivated boundary, rather than a numerical isolated failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
