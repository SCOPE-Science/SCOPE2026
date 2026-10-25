---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For n>=4 periodic two-leg square ladder with degree-three sites and the exact two-end vacancy Kob–Andersen hop rule, each quadruple (a,b,c,d) passes a local Boolean test iff its central rung and two following leg edges disallow enabled hopping. Independently rebuilt the 64 triple-rung transfer states, counted 108 allowed weighted transitions and identified a single 29-state primitive recurrent class. Independently constructed its exact symbolic characteristic polynomial, verifying x^16 F(x,z)G(x,z) with given octic/quintic, and separately brute-enumerated all rung words n=4..8 and full particle-size distribution with totals 54,129,319,837,2150. The exact trace/log determinant identity yields all-n polynomial Z_n; Perron-Frobenius, Rouché bound on quintic, Descartes root uniqueness for octic x>2 and analytic perturbation prove asymptotic entropy log(2.605506658540588...) per rung and density 0.736222013311... per site. These are all-n analytic consequences of the verified transfer identity.

## originality

PASS

Best-of-knowledge statement-level comparison: This is a finite-width natural-model calculation not mechanically read off an unrelated general kinetic constraint statement.

## value

PASS

The complete weighted jammed-state polynomial for a natural exactly solvable width-two kinetic-constraint model simultaneously yields rigorous all-volume counts, Perron entropy and typical particle density. Exact finite-width solvability is useful as a benchmark for kinetic jamming studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
