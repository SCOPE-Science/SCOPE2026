---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The Higgins balanced-weighting criterion is translated to six exact Hall inequalities d_i>=ceil(q/3), a_i<=floor(q/3); counting incidences produces the sharp residue-wise lower bounds. Equality cases exhaust singleton-only (q=0 mod3), one triple or two distinct doubles (q=1 mod3), and two distinct doubles (q=2 mod3). Multinomial label counts include q=1 separately. Independent multiset enumeration of all seven nonempty support types for q=1..7 reproduces both minima and multiplicities; finite data corroborate rather than prove arbitrary q.

## originality

PASS

Best-of-knowledge original fixed-three-row extremal and enumerative classification; Higgins gives only balanced-support feasibility, not the optimized edge count or all equality multiplicities. Search did not find a dominating incidence-matrix classification, but inaccessible paper-level comparisons and old tabulations remain real risks.

## value

PASS

A natural first nontrivial fixed-row extremal problem after a newly established matching criterion; exact complete equality structures and labeled multiplicities are useful for testing Rees-band matching examples, not merely a restatement of Hall feasibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
