---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

A word in {p,m,u,v} defines a Munn interval and terminal vertex; p/m move one edge, u/v inspect one adjacent edge at cost one and leave the vertex unchanged. If a,b>0, left-first shortest exposure costs 2a+b-1 (using a left probe), right-first costs a+2b-1. Equality has precisely two words for each minimizing route; when a=b both contribute four. Boundary classes have the two monotone/probe representatives; D-width n needs n newly exposed edges and its shortest sweeps have 1,4,8 words in widths 0,1,at least 2. Summing cases gives the two displayed rational R series. Explicit one-counter inequalities prove R DCFL; its intersection with m^+vp^+ is nonregular by distinguishable prefixes. D templates are regular. Independent enumeration verified every R-class length and multiplicity for min length <=6; actual verifier separately checks longer prefixes through n=9.

## originality

PASS

The highly relevant 2026 paper proves monogenic Green-geodesic language complexity on the original two-direction generator metric, and its section 9 was read. The present alphabet adjoining cost-one idempotent probes changes exact optimal route lengths, word templates and enumerators, none contained in that source. Direct Resultary and title/alias searches did not surface an equivalent four-letter enumeration, with residual risks recorded.

## value

PASS

Adding the two naturally distinguished nonidentity idempotents of the free inverse monoid alters geodesic geometry; classifying every optimal representative and deriving closed rational growth series provides reusable exact information for a natural generating set and distinguishes regular from nonregular Green languages.

The dated certificate retains the supplied scientific assessment, sources and limitations.
