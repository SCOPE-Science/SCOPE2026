---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS: On the dense nonsingular 2x2 minor chart, unique recurrence a_{j+2}=Sa_{j+1}-Pa_j yields field C(A,B,S,P). Fixing A=a0,B=a1,C=a3 gives P=(BS^2-C)/(AS+B), so function field is C(A,B,C)(S). Only possible finite pole is -B/A. Delta=A^2*C-B^3 nonzero generically forces the degree n-4 at infinity. For t=n-1, highest P power has coefficient (-1)^m A when t=2m and (-1)^m(B+mAS) when t=2m+1; evaluated at S=-B/A nonzero for m>=2, giving floor(t/2) pole. Degree is sum of pole orders, generic separability in characteristic 0. Independent symbolic recurrence with rational A,B,C verified n=5..11. Proof covers all n, not extrapolated.

## originality

PASS

Best-of-knowledge novelty rests on a precise target mathematical statement not established or implied by inspected stronger primary results. Existing identical primitives, partial tables, scalar invariants and adjacent object classes are credited; an inaccessible or unindexed equivalent theorem remains a documented risk.

## value

PASS

PASS: Generic completion count for a natural minimally determined sparse Hankel pattern measures algebraic reconstruction ambiguity. Exact all-n degree and two pole orders resolve the alternating six-entry computed table in published work, improve a general bound for infinitely many n and provide geometric mechanism; not a merely renamed finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
