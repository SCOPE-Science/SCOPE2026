---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For f=x^s u nonzero (u a unit in A=Fq[x]/x^p), g=uh, the bracket is u^2 x^(s-1)(xh' -s h) for s>=1. The coefficient condition (i-s)a_i=0 for 0<=i<=p-s leaves s-1 free high coefficients, plus the i=s coefficient iff 2s<=p; for s=0 the derivative kernel consists only of constants. Thus dimension is 1 at s=0, s for 1<=s<=m, s-1 for m<s<=p-1, m=(p-1)/2; zero f has centralizer dimension p. Valuation s has exactly (q-1)q^(p-s-1) rational elements. Combining strata gives exact histogram, sum=q^p and sum_f q^dimC=q^(p-2)(q^3+m(q^2-1)), so cd=(q^3+m(q^2-1))/q^(p+2). An independently written modular row-reduction of ad(f) exhaustively verified all F5^5=3125 elements, histogram {1:3000,2:120,3:4,5:1} and 21625 commuting ordered pairs. Infinite-field-extension validity is symbolic from the coefficient equation, not from finite tests. Scope p>3 prime, q=p^e, same standard truncated-polynomial derivation algebra.

## originality

PASS

Premet and Chang establish regularity/invariant geometry of Witt algebras, and Yao–Chang 2018 treats the *same* one-variable W1 commuting variety and its irreducible components. Their published abstract and accessible page do not state the all-element finite-field centralizer multiplicity or rational commuting-pair formula; however full article could not be read and it may contain dimension-by-valuation lemmas. The full finite-field spectrum/commutativity-degree is assessed best-of-knowledge original relative to the accessible texts, explicitly excluding geometric irreducible-component results and any prior known centralizer method. A decisive prior implication by a hidden centralizer table would undermine originality; that material risk is retained.

## value

PASS

The exact rational-point distribution of Lie-centralizer sizes and closed commuting probability for W1 over every finite extension field is a natural nontrivial all-element invariant; it refines regular-element criteria and geometric commuting-variety component dimensions, and gives exact frequencies rather than a few example centralizers. It has mathematical use as a benchmark for finite modular Lie-algebra commuting statistics. Significance does not rely merely on successful code checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
