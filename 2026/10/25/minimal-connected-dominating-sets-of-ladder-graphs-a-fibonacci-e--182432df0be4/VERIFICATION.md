---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For a two-row ladder every connected vertex subset occupies a column interval; domination forces endpoints at first/second and last/penultimate columns. If an endpoint column is occupied it must begin TT or DD, whereas an omitted endpoint needs adjacent B; analogous right rules. Interior double columns B are indispensable only if neighboring singleton runs lie in opposite rows, so all internal B occur in TBD or DBT, and unseparated singleton columns share a row. Conversely those words dominate, connect, and every deletion destroys domination or connectivity. Connected domination is upward closed, making single-deletion tests equivalent to inclusion-minimality. Decomposing disjoint singleton runs and switching B columns yields bivariate GF 2V+(2BV^2+4xBV+2x^2B^2U)/(1-BU)+x^2B+x^2B^2+2x^2y^2, U=xy/(1-xy), V=x^2y^2/(1-xy), B=xy^2. y=1 gives (4x^2-x^3-x^6)/(1-x-x^2), so a2=4,a3=3,a4=7 and a_n=2F_n for n>=5. Independent vertex-subset enumeration n=2..8 exactly verified counts 4,3,7,10,16,26,42 and corresponding size profiles; this does not replace all-n proof.

## originality

PASS

Best-of-knowledge PASS, qualified: exact inclusion-minimal connected dominating sets and graded Fibonacci generating function not implied by literature enumerating all connected sets, ordinary minimal domination, or generic enumeration algorithms.

## value

PASS

Natural full antichain of minimal connected domination on an infinite bounded-width ladder family has complete structural language and bivariate cardinality profile; a stable twice-Fibonacci total emerges from nontrivial local row-switch constraints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
