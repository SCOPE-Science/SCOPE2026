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

For p prime, p∤m, r>=1 and P=p^r, write k=bP+t. Independently derived v_p(C(mP,bP+t))=r-v_p(t)+h_b for 1<=t<P, and boundary value g_b. From v_p(N(n,k))=v_p(C(n,k))+v_p(C(n,k+1))-r, the interior equals r-v_p(t(t+1))+2h_b, while two boundary entries yield u^{g_b+h_b}+u^{g_{b+1}+h_b}. Exact p-adic shell counts are (p-2)p^{r-1} for valuation zero and 2(p-1)p^{r-d-1} for valuation d (1<=d<r); hence the stated histogram and rational bivariate GF by geometric series. Coupling T mod p^r to Haar-uniform Z∈Z_p excludes exactly T=0,p^r-1, total probability 2p^-r, giving the shifted geometric law with the same total-variation bound. Independently enumerated 92 exact Narayana rows for several p,m,r and checked the formal rational GF. Infinite assertions rely on digit/coupling proof, not enumeration.

## originality

PASS

Best-of-knowledge originality from distinct actual primary statements and implications: Checked indexing change explicitly to avoid false novelty from k-shift; known individual carry formulas are supporting lemmas rather than a published full-row distribution. The exact m=1 stratum may follow known prime-power valuation theory and is credited. General fixed m with p∤m creates h_b-dependent shifted mixture absent from those statements. Classical inputs plus nontrivial uniform block and shell decomposition yield this quantitative theorem, not an automatic renaming of a known table.

## value

PASS

The entire p-adic valuation distribution in a natural combinatorial row family becomes a finite formula and rational bivariate GF, with a quantitative shifted-geometric limit including the nontrivial dependence on m. Such exact divisibility data can be used for prime-power congruences and random Narayana statistic calculations, beyond yes/no divisibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
