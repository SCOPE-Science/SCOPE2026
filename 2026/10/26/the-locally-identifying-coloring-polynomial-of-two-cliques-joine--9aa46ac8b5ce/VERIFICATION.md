---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: derived the exact closed-neighborhood color sets P, Q and P∪{f(b_i)}, Q∪{f(a_i)} and verified every edge type. For 1<=t<n, shared colors lie only at unmatched positions; at t=1 prohibit n-1 shared colors because the cross matched endpoints then have equal neighborhood color sets. With t=n, at most one reused color with different indices; t=0 has true twins. Choosing paired shared colors and injective fresh colors yields each falling-factorial summand, including n=2,t=2 boundary. Independently checked 62 (n,t,k) instances against the ORIGINAL graph/neighborhood definition for n=2..4; not an infinite computational proof.

## originality

PASS

Qualified originality concerns the complete all-k polynomial and full partial-matching palette classification; the scalar chi_lid(K_n square K_2)=2n-1 for n>=3 is prior-covered and deliberately excluded as a new theorem.

## value

PASS

PASS: identifies a natural graph-polynomial invariant refining the known minimum color number for a canonical family interpolating disjoint cliques and a prism; its sharp t=1 and n=2,t=n effects are intrinsic structural transitions, not arbitrary slices. Full counting and color-orbit classification remain useful even where one endpoint scalar value is known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
