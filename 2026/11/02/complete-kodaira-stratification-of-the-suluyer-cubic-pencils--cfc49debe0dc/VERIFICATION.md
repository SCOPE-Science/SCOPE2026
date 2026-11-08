---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The defining plane cubic is birational to binary quartic w²=(A+tB)(A(x²+y²)+tB(x²-xy+y²)), A=x-ay and B=x-y. Recomputing invariant I,J yields Δ∝(a-1)²t²(t+1)²(t+a)²Q_a(t) with deg(Q)=4; independently factored Q discriminant 512(a-1)^4(a²-a+1)(71a²-196a+71)^3 and evaluated I,J,Q local orders at all seven exceptional parameter loci. The Tate–Kodaira characteristic-zero table, including additive III (1,2,3) and II (1,1,2), determines fiber types. The discriminant at infinity contributes order 2, total Euler 12. Resolving nine basepoints counting the infinitely near one at a²-a+1=0 produces a relatively minimal rational elliptic surface with section, and Shioda–Tate rank = 8−sum(m_v−1) yields the five listed ranks. A separate exact SymPy calculation matched all exceptional valuations and generic factorization.

## originality

PASS

Suluyer’s fully accessible 2024 thesis (section 4.3, Theorem 4.3.1 and Example 4.3.2), now materially read, defines precisely this family and computes only a=2 non-special singular curves; the 2026 journal version similarly treats the four conic-line members. Thus the family and the special a=2 case are prior, not new. The generic uniform discriminant, all collision loci, extra infinitely-near I2 type and MW ranks are distinct mathematical results not supplied by the inspected thesis chapters or journal example. Resultary similar elliptic surface hits concerned other families. Historical equivalence under elliptic-surface isomorphisms remains a risk.

## value

PASS

A natural published family of cubic pencils lacked complete singular-fiber classification outside the singled-out member. Providing the full parameter stratification, additive/multiplicative collision distinction and Mordell–Weil rank changes describes central invariants of the associated rational elliptic surfaces, including the exceptional base-scheme tangency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
