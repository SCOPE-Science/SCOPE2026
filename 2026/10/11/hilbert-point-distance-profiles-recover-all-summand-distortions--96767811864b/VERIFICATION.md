---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

The published Grundbacher–Kobos formula f(p)=||(d_i)||_{2p/|p-2|} is substituted with p_r=2r/(r-2), yielding exactly S(r)=f(p_r)^r=sum_i d_i^r for all r>2. A finite ordered exponential sum has D1=lim S(r)^(1/r), m1=lim S(r)/D1^r, and subtracting m1 D1^r inductively identifies all remaining distances and multiplicities. For p=2±h, r=4/h±2, so the lower levels are O(e^{-c/h}); division by r gives cusp derivatives ±D log m/4 when maximum multiplicity m>=2 and C-infinity flatness at p2 for m=1. Source checker was read; finite sampling is illustrative, not the proof. The exact-data hypothesis is indispensable.

## originality

PASS

Grundbacher–Kobos already gives the complete forward profile, so the inverse result is a mathematical consequence of a known stronger forward formula, not a new Banach–Mazur distance computation. Nonetheless no source inspected gives the injectivity/inversion of the Hilbert germ or its cusp/flatness stratification as a result, and a finite-exponential identification argument is required. This modest inverse statement is treated as a distinct conclusion rather than an independent reproof of the formula; high residual risk of being considered a routine corollary.

## value

PASS

The exact local germ has the unexpectedly global ability to recover EVERY component distortion level, and the nonsmoothness order discriminates the number of worst components. This is a natural inverse-identifiability result for finite sum geometry, though ill conditioned and not a stable algorithm; the combined explicit recovery and singularity statement is more useful than an isolated power-mean limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
