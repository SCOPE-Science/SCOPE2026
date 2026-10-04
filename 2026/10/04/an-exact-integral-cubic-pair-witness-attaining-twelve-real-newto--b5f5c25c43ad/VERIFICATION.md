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

The verifier reconstructs the two integer cubics exactly and forms
\[
\gamma_1=\partial_xF_1\,F_2-\partial_xF_2\,F_1,
\qquad
\gamma_2=\partial_yF_1\,F_2-\partial_yF_2\,F_1.
\]

It performs the following exact checks over \(\mathbf Q\):

- each generator cubic is smooth in the affine chart, and its leading binary cubic is squarefree at infinity;
- the projective pencil has no singular point on the line at infinity;
- the base resultant has degree \(9\), is squarefree, and has exactly \(9\) real roots;
- the base ideal is in shape position and its Jacobian determinant never vanishes on the base locus;
- the critical resultant has degree \(21\), is squarefree, and has exactly \(21\) real roots;
- exact division by the base resultant gives a squarefree degree-\(12\) quotient with exactly \(12\) real roots;
- the Hessian determinant of the corresponding pencil member is nonzero at every quotient root;
- eliminating the pencil parameter gives a squarefree degree-\(12\) polynomial with exactly \(12\) real roots.

The real-root counts are exact polynomial root counts. Together with shape position and squarefreeness, they prove the asserted cardinalities and exclude hidden nonreal solutions in the relevant zero-dimensional schemes.

The saved replay ends in `VERIFY_OK`.
