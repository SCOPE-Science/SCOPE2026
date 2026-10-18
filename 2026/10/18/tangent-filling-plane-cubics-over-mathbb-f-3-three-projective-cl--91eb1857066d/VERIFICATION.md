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
# Verification instructions and scope

Execute `python verify.py` with Python at least 3.10 and `sympy==1.14.0`. The verifier enumerates all \(13\), \(364\), and \(29524\) projective coefficient vectors of degrees \(1\), \(2\), and \(3\) respectively. It constructs all \(13\) projective rational points, evaluates every polynomial and the derivatives at each point, counts tangent-line incidences, and asserts exactly \(3744\) cubic coverings and no smaller-degree covering.

Its separate orbit phase constructs the actions of standard generators of \(\operatorname{PGL}_3(\mathbb F_3)\), confirms orbit sizes \(936\), \(1872\), and \(936\), their disjointness, and exhaustive coverage of the enumerated coverings. Gröbner bases of the three representatives' projective Jacobian systems on each affine chart verify smoothness over the algebraic closure. The body of `RESULT.md` supplies a direct hand-checkable smoothness proof as well.

No random selection, external computational dataset, or timeout-as-proof is used. The finite enumeration is exhaustive over this particular field; it is not a classification in general characteristic or field size. The independent audit remains unperformed.
