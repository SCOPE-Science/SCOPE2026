---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-09-30.md",
      "INDEPENDENT_AUDIT_2026-09-30.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

An independent exact hitting-set formulation was built directly from the two sequence definitions. A separate MILP solver proved the six minima for each sequence through n=64 and reproduced the distinct-factor totals. For n=128,256,512,1024, exact substring grouping independently verified every committed greedy attractor set and all total distinct-factor counts, and reproduced the per-length lower bounds. For RS1024, the record's stronger disjoint-span lower bound 9 was independently reconstructed: nine exact factor occurrence-span unions are pairwise disjoint (length/start data included in the private computation), so nine attractor positions are necessary. These checks do not rely on the record's saved VERIFY log.

## originality

PASS

Schaeffer–Shallit establish the automatic-sequence dichotomy and give exact constants for other canonical words, but the primary abstract and targeted searches did not supply Rudin–Shapiro or regular-paperfolding prefix minima. Resultary and exact-phrase/parameter web searches returned the candidate as the only strong exact match. No source found implied these finite values or the displayed witnesses/bounds.

## value

PASS

These are two canonical binary 2-automatic sequences singled out by the surrounding string-attractor program. Exact small-prefix minima plus certified bounds to 1024 give a natural finite invariant profile that can guide or falsify conjectures about the known Theta(1)-versus-Theta(log n) dichotomy. The result is explicitly finite and does not overclaim the infinite classification, satisfying the allowed meaningful-finite-cutoff category.

The dated certificate retains the supplied scientific assessment, sources and limitations.
