---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The minimal automaton has state residues and delta(r,d)=br+d mod m, every state accessible and separately observed. A repeated state with distinct incoming digits at positions i<j yields positive prefix-value difference multiple of m but not b, bounded by b^L-b; thus m<=b^L-b. Conversely with K=b^(L-1)-1 and m<=bK one may write m=cK+t for c in {0,...,b-1}, t in [0,K]; the word with first digit c and length-(L-1) tail for t repeats residue at its last prefix but changes incoming digit because b does not divide m. If b divides m no distinct digit collision exists. Allouche--Yao published shortest-inhomogeneous-path theorem then gives opacity, and interval counting of nonmultiples b yields (b-1)^2 b^(L-2), including L=2 and m=1. The witness proves the unbounded statement, not bounded checking alone.

## originality

PASS

The final claim was independently compared at statement/implication level against the identified closest original publications and targeted semantic finding searches. Specific prior components are credited and the remaining claimed addition is identified. Residual priority/access risks remain and this is best-of-knowledge, not universal certification. Exact radix–period opacity and level spectrum for residue clocks.

## value

PASS

The residue clock is the canonical maximally informative m-periodic automatic sequence. The result supplies the complete two-parameter b,m transparent/nontransparent classification, sharp shortest-collision depth, and exact infinite level multiplicities, natural quantitative consequences of a general opacity algorithm not previously evaluated in these parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
