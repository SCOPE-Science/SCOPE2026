---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Writing z(w)=cw+d/w with 0<r=d/c<1 gives deck h(r/w)=h(w). Unimodularity of rational h on unit circle gives h(w)h*(1/w)=1 as a rational identity. Reflect and combine deck involution to force dilation h(v)=h(r²v). Any rational Laurent expansion around 0 then has only exponent zero because r² is not a root of unity; hence h constant unimodular. For polynomials, H=Q/P handles P≠0; P=0 forces Q=0 by infinitely many zeros. For degree≤n, |P(z(e^{it}))|² is a Laurent polynomial of order≤2n; a nonzero intensity difference has at most 4n distinct points on S¹. The ellipse parameter is injective, so 4n+1 samples force full equality. Reciprocal linear polynomials disprove the circle case. Checked identities and CHECK.py’s exact Laurent arithmetic; numerical samples are supplementary, not an infinite proof.

## originality

PASS

Rigidity of rational unimodular functions on a single noncircular ellipse and corresponding universal all-degree labelled sampling contrast with prior multi-line/multi-circle holomorphic phase retrieval. Lemniscate intersection theorems are closest broader framework but were not shown to imply the specific single-ellipse rigidity.

## value

PASS

The geometric distinction between a circular curve with an exact reciprocal ambiguity and any arbitrarily slightly eccentric ellipse with global polynomial phase rigidity is mathematically natural and strong; its universal finite sampling theorem supplies an explicit useful sufficient measurement size, without claiming optimality or stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
