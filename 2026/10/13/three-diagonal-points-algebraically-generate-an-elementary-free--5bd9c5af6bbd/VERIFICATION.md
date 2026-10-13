---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The primary-source check used Hyttinen–Paolini, arXiv:1811.03351. Proposition 7.1 is the decisive input: for a generating quadrangle \(a,b,c,d\) of \(\pi^4\), it defines the three diagonal points \(e,f,g\), exhibits an automorphism fixing \(e,f,g\) but moving each generator, and proves that all four generators are algebraic over \(e,f,g\). The same paper proves that \(\pi^4\) sits elementarily in the free-plane chain and identifies algebraic closure with its \(\operatorname{cl}^*\) construction.

The new equality is then a formal closure consequence. Since \(a,b,c,d\in\operatorname{acl}(e,f,g)\) and \(\pi^4=\langle a,b,c,d\rangle\) under the definable join/meet terms, every element of \(\pi^4\) is algebraic over \(e,f,g\). Conversely, no algebraic element over parameters in an elementary submodel can lie outside that submodel, because a finite definable solution set has the same exact cardinality in the submodel and the ambient model.

The accompanying script `verify_complete_quadrilateral.py` checks the complete-quadrilateral incidence pattern, the closed-over-three degree condition used by the source, the absence of forbidden double intersections among displayed lines, and the parameter-fixing involution. It returns `VERIFY_OK 37 exact finite assertions`.

No independent audit has yet been performed.
