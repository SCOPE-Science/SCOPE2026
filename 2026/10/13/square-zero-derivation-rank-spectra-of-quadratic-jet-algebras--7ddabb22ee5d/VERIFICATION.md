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

A derivation kills 1 and its generator images have no constants: differentiating x_i²x_j=0 for i!=j forces the constant coefficient of D(x_j) zero even in p=2,3. Write D on V⊕Sym²V as block [[P,0],[Q,S(P)]]. For odd p, D²(x_j²) quadratic component 2(Px_j)² forces P=0, Q unrestricted. In p=2, D² is a derivation and generator equation is P²=0 and S(P)Q+QP=0. A rank-r square-zero P comprises r doublets and t=d-2r singletons; induced S(P) has h=r(d-r) doublets and s=r+binom(t+1,2) singletons. Chain maps contribute q^(d h+r s) free parameters and arbitrary s×t homology map of rank k, full D rank r+h+k. This proves all strata and maxima. Independent exhaustive actual derivation matrices at d=2: q=2 spectrum 1+21T+66T²; q=3 spectrum 1+104T+624T². The all-d extension-field result is symbolic, not inferred from tests.

## originality

PASS

The direct complete operator-rank distribution for the nonreduced total-degree-3 jet algebra, including characteristic-two differential homology blocks, differs from general Hasse–Schmidt integrability and regular-derivation results in separate p-power truncated algebras. The different use of "square-zero derivation" for elementwise identity was disambiguated. No equivalent prior spectrum identified in searches; qualified, not certified novelty.

## value

PASS

A natural exact moduli/count invariant for nilpotent Leibniz operators with a characteristic-two rank jump and homology-dimension distribution, for every d and finite q. Substantial structural block calculation beyond a field-matrix rank table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
