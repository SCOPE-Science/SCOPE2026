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

Independently reconstructed Sun telescoping identity S_n(X)=n^2 sum_{j<n}B_nj^2 X^j/(2j+1). For n=p^a, p odd, only denominator j=(n-1)/2 reaches p^a; B is a p-adic unit, yielding coefficientwise mod p^{a+1} congruence. At x=pu, normalized polynomial F_{p,a}(u) is 1 mod p for p>=5 and 1+u mod 3 for p=3; Hensel and unit difference quotient give unique 3-adic zero and exact valuation/root counts. Fixed-divisor argument uses S_n(0)=n^2 and S_n(1) with valuation a; dyadic denominators are odd. Independent direct/closed coefficient and residue-class counts were checked at (p,a)=(3,1),(3,2),(5,1),(7,1).

## originality

PASS

Sun 2011 supplies EXACT sum coefficient identity (1.5) and congruences but no seen complete p^a-index integral p-adic root-count/Hensel classification. Guo-Zeng/Pan concern divisibility. The new zero-locus assertion logically requires valuation analysis not implied by divisibility alone. Resultary semantic queries of published records performed with two tailored queries; no exact dominating result located, and this is not proof of priority. The listed primary sources were compared on mathematical implications; inaccessible relevant text retained as risk.

## value

PASS

Prime-power Apéry polynomial sums are natural arithmetic objects with studied divisibility. The exact p-adic zero classification, especially 3-adic uniqueness vs all p>=5 absence and complete modular root numbers, yields a concrete local arithmetic invariant not supplied by the source coefficient formula alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
