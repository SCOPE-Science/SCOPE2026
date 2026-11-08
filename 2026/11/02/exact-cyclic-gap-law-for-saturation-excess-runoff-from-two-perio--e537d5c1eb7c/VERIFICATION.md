---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The N-step clipped recurrence is a contraction with factor at most r^N. At the two pulses, a=min(1,p+r^g b), b=min(1,p+r^(N-g) a), and g<=N-g forces a>=b. Three exhaustive saturation cases give exactly p0=(1-r^N)/(1+r^g), p1=1-r^(N-g) and the two nonzero maximum terms; check equality at thresholds. Since each positive candidate strictly decreases for consecutive permissible gaps, their max with zero decreases strictly wherever the later gap still overflows. Independent 2592 exact rational checks reconstruct fixed points and monotonicity. Arbitrary real values follow from the displayed inequalities, not sampling.

## originality

PASS

Prior hydrological papers consider stochastic storm arrivals, event-time distributions and catchment thresholds, not deterministic two-equal-pulse periodic clipped storage and exact total-outflow gap ordering. Explicit formulas not located by Resultary or keyword searches. An equivalent deterministic buffer/finite-dam smoothing theorem remains a historical priority risk.

## value

PASS

The exact event-specific overflow phases and sharp placement boundary for two fixed precipitation pulses explain how timing alone toggles excess runoff, including zero-runoff ties; a physically motivated idealized storage-control benchmark, not a field prediction or textbook parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
