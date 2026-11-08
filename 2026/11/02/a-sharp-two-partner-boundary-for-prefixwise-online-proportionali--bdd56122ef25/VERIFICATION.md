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

The online rule sends an item eligible to pair e={u,v} to the endpoint with smaller pair-specific cumulative load (singletons forced). Induction gives -B_{v,e}<=Q_{u,e}-Q_{v,e}<=B_{u,e} after EVERY arrival even with arbitrary positive real weights. For any agent i, exact identity L_i-P_i=1/2 sum_{e incident i}(Q_{i,e}-Q_{other,e}). At most 2 DISTINCT partner pairs implies simultaneous -b_i^-<=L_i-P_i<=b_i^+ for all prefixes, good and chore versions, regardless of repeated edges or horizon. Adaptive knockout on eight agents with seven unit pair-jobs forms a degree-3 tree and forces winner load3, proportional share3/2, failure after removing one unit. The inspected verifier checks integer finite examples; induction proves all positive real weights.

## originality

PASS

The eligibility-aware share and unrestricted-online approximation lower bounds were already published by Biburger/Megow/Shahkarami (2026), so these are not novelty. The positive bounded-distinct-partner-degree-2 simultaneous all-prefix weighted algorithm is the new constrained guarantee; existing offline graphical orientation results are not equivalent to irrevocable online prefixes.

## value

PASS

Maximum distinct partner degree is a natural sparseness/interaction restriction in restricted-assignment scheduling. A deterministic pair-local greedy rule that simultaneously attains exact two-sided Prop1 for arbitrary weights and prefixes, together with a matching degree-3 obstruction, gives a sharp structural boundary rather than a marginal improvement in a toy instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
