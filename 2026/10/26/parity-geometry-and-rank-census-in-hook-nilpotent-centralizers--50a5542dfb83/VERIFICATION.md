---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For every field k and n≥3 fix N=J_n(0)⊕J_1(0). Viewing module R⊕k with R=k[t]/t^n, an N-centralizing endomorphism is X(f,u)=(af+b t^{n−1}u,c f(0)+d u). X²=0 forces d=a(0)=0 and a²+bc t^{n−1}=0 mod t^n. If n=2h, valuation forces a∈t^h R, so bc=0 and the reduced locus is A^h×V(bc), two transversal affine (h+1)-spaces singular along A^h. If n=2h+1, a∈t^h R and a_h²+bc=0, giving A^h×V(bc+z²), irreducible quadric cone dimension h+2 with singular A^h even in characteristic two (partials b,c,2z and on-locus equation). For nonzero a with ord_t a=v≤n−2, matrix rank n−v; at v=n−1 rank one. Count leading a_v and higher coefficients with bc=0 or bc=−a_h². This yields rank coefficient rank0 1; rank1 (q−1)(2q+1); rank r=2..floor(n/2) (q−1)(2q−1)q^{r−1}, plus odd terminal (q−1)²q^{(n−1)/2}. Totals (2q−1)q^{n/2} even, q^{(n+3)/2} odd, and acyclic X-complexes only n odd of rank (n+1)/2. Independently assembled matrices and Gaussian-eliminated all q^{n+3} coordinate tuples for q∈{2,3}, n=3,4,5, matching full rank distributions. Arithmetic proof works for all q/fields; enumeration is corroborative only.

## originality

PASS

The centralizer module coordinates and commuting nilpotent conjugacy/orbit frameworks are established. Britnell–Wildon 2010 classifies which nilpotent similarity types can commute; Hua 2023 treats indecomposable commuting nilpotent pairs up to simultaneous conjugacy. Neither inspected primary theorem tabulates the entire *labeled* square-zero fiber for fixed hook (n,1) by ordinary rank or describes its characteristic-uniform reduced singular geometry. The claim includes a whole odd/even family, not a single tiny matrix. A general Hall-polynomial/quiver variety formula might imply the counts and is retained as a genuine priority risk, but no explicit dominating formula was identified.

## value

PASS

Square-zero centralizing endomorphisms are natural differentials on a fixed nilpotent module. The parity switch from two components to irreducible singular quadric, complete finite-field rank generating function, and exact acyclic-complex count give a structural and arithmetic classification useful for representation varieties and homological constructions. It is not arbitrary table recomputation or mere correctness of code.

The dated certificate retains the supplied scientific assessment, sources and limitations.
