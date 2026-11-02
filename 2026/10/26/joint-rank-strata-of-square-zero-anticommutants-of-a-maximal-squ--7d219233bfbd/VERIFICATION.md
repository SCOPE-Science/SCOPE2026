---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For square-zero A of rank r in dimension 2r, choose A=[0,I;0,0]. Anticommutation gives B=[P,Y;0,-P]; B²=0 iff P²=0 and PY=YP even in characteristic 2. Let t=rankP and H=kerP/imP of dimension h=r-2t; projection on B image proves rankB=2t+rank(Y on H)=2t+u. Square-zero P ranks counted by choosing imP,kerP and an isomorphism; its centralizer dimension is c=(r-t)^2+t². The induced centralizer-to-End(H) map is onto with kernel c-h², giving count Gaussian[r,t] Gaussian[r-t,t]|GL_t| q^(c-h²) Gaussian[h,u] product_{i<u}(q^h-q^i). Smooth rank-u endomorphism strata fibred over rank-t square-zero orbit have dimension r²-(h-u)², irreducibility; top u=h strata closures give floor(r/2)+1 components. Independently enumerated all r=2,q=2 (P,Y) combinations and recovered exact rank stratification 1,9,6,12 including all 28 B. Boundaries t=0 and h=0 valid; prime powers supported algebraically, finite tests only prime q.

## originality

PASS

Paul Levy (2006) establishes equidimensional components of commuting square-zero pairs in characteristic two; this component count is antecedent and not novel. Chen–Wang anticommuting varieties give block normal forms, not demonstrably the fixed maximal-square-zero fiber with joint ranks of B,AB over all finite-field orders. Fine finite-field count via centralizer-to-homology and rank-u endomorphisms is the proposed addition. A plausible Ngai 2024 thesis could state equivalent rank strata and its full text was not obtained, so originality remains qualified.

## value

PASS

A full joint rank census is a natural arithmetic refinement of the geometry of square-zero anticommutants; conditional rankB-2t is exactly the rank law of an h-by-h random endomorphism. The exact stratification and dimensions are meaningful structural invariants beyond a known component count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
