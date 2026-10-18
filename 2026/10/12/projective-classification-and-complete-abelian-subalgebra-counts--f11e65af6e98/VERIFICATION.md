---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Use the actual Saha–Towers multiplication table e1e2=e4,e1e3=e5,e2e3=e6,e1e6=e7,e2e5=−e7,e3e4=e7 and anti-commutativity to identify A=V⊕Λ²V⊕Λ³V (dim 7), with product (v,a,c)(w,b,d)=(0,v∧w,v∧b−w∧a). An abelian subspace with nonzero V projection has that projection contained in a single line L=Kv because v∧w=0. For x=v+a+c with v nonzero, the centralizer consists of V components λv and Λ² components λa+v∧V, with unrestricted Λ³V, yielding a four-dimensional abelian subalgebra C(x). The ideal M=Λ²V⊕Λ³V is also maximal abelian and self-centralizing; every abelian H outside M belongs to a unique C(x), and its choice depends on one section over each L of Hom(L,Λ²(V/L)), a one-dimensional line bundle O(2) over P². Distinct C at same L meet in dimension3; different L meet in dimension2. For q odd, there are q(q²+q+1) of these plus M. Counting d-subspaces in M and then uniquely in each other maximal gives N_d=[4 d]_q+q(q²+q+1)([4 d]_q−[3 d]_q), 0<=d<=7. Over F3, independent RREF enumeration of 99,463 two-dimensional subspaces found exactly 4,693 abelian ones, agreeing with the formula; the all-field result is established by wedge relations, not the finite check. The source's Example4.6 sign convention was rechecked in its full arXiv manuscript page6.

## originality

PASS

Saha–Towers (2020) explicitly gives the seven-dimensional class-three CB algebra and its multiplication table; these are prior and not novel. Their paper proves broad properties of centralizers as ideals but does not supply the projective line-bundle classification of all maximal abelian subalgebras, intersection geometry, or full subalgebra-count polynomial. A 2018 Saffarnia–Moghaddam–Rostamyari paper on centralizer counts in Lie algebras is a plausible comparison for characteristic three but its full text remained inaccessible; its available abstract does not assert this exact all-characteristic algebra and Gaussian distribution. An inaccessible plausible article is expressly recorded as originality risk rather than treated as automatic failure.

## value

PASS

This is a complete natural classification/count for the smallest nontrivial class-three example motivating a broad CB-algebra classification. It determines the entire abelian-subalgebra lattice profile over every odd finite field and its incidence strata. The geometric O(2) parametrization and finite-field distribution give structural understanding not implicit in merely knowing the multiplication table. Dimension-four extremal/complete counts are exact natural invariants, not arbitrary computation or an unsupported number sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
