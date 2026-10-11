---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Restricting the published four-collinear determinant to the baseline gives the exact bracket identity \((v_1-v_4)(v_2-v_3)[13][24]-(v_1-v_3)(v_2-v_4)[14][23]\), which on an affine chart is precisely equality of source and target cross ratios. Every diagonal projective transform therefore lies on the divisor; both its orbit closure and the irreducible divisor have dimension three, so they coincide. The affine equation is a quadratic form in the four target coordinates. Independent symbolic computation for distinct source coordinates gives Hessian rank three, kernel spanned by the common-shift vector, and every principal 3-by-3 minor equal to twice the nonzero Vandermonde. Hence the affine singular locus is exactly the diagonal and the normal quadratic form is nondegenerate. Simultaneous projective changes move any target quadruple into an affine chart, making the statement global. A rank-three quadratic is irreducible; the hypersurface is Cohen--Macaulay and its one-dimensional singular locus has codimension two in the threefold, so Serre's criterion gives normality. Because the defining equation is exactly quadratic transverse to the diagonal, the local analytic germ is \(A_1\).

## originality

PASS

Breiding--Duff--Gustafsson--Rydell--Shehu explicitly derive the four-collinear correction determinant and prove that the augmented collinear ideal is radical/defines the line multiview variety, but they do not identify the baseline restriction as a fixed-cross-ratio orbit closure or classify its singularities. Aluffi--Faber give a classical theory of PGL(2) orbit closures of unordered divisors on \(\mathbb P^1\), including boundary multiplicities and singularity criteria, but their ambient symmetric-power quotient changes the boundary singularities and does not state the ordered \((\mathbb P^1)^4\) divisor's small-diagonal transverse \(A_1\) structure. No inspected source mechanically implies the full audited claim.

## value

PASS

The correction determinant is a canonical exceptional feature of the four-collinear line-multiview problem. Identifying it intrinsically as a fixed-cross-ratio orbit closure and determining its exact singular locus, normality, and transverse node turns an elimination formula into geometric structure that supports subsequent birational analysis. This is a motivated local-geometry result rather than a cosmetic factorization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
