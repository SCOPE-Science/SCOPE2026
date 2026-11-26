---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For invertible A and B the first two bilinear equations globally give y and x by their kernel lines over P1_z. Substituting in the third gives the homogeneous binary quadratic P; its derivative vanishes at a repeated zero in characteristic two exactly when its middle coefficient Q is zero, including the identically zero case. Expansion gives tr(AJB^TJCJ). Its coefficient of c0 is the irreducible 2×2 determinant a2b3+a3b2, which does not divide the coefficient of c1, so the linear polynomial in C is primitive and irreducible. The universal nontransverse incidence is irreducible: at a fixed base point three evaluations are independent and the six active derivatives freely specifiable; their sparse determinant is the irreducible binomial of disjoint triple products. This fibre description is locally trivial over the three P1s. The incidence image is closed by projectivity and meets the invertible open at F1=y+z, F2=x+z, F3=xy. Its intersection there agrees with V(Q), so the global reduced image equals V(Q). In the gradient, the trace pairing identifies sets of four derivatives with UV, VW and WU. If a matrix is invertible the other two vanish. Otherwise every rank is at most one and each intermediate line can be chosen between the incoming image and outgoing kernel. These choices yield the rank-three projective bundle of the record; generically the lines are recovered by the images of nonzero matrices, giving a rational inverse and dimension five. In its Segre class coefficient, the six ordered (2,1,0) exponent patterns contribute two each, the (1,1,1) pattern contributes two, and pure cubes vanish. Thus the degree is fourteen. Restricting to one nonzero block leaves its rank-one determinant quadric; the coordinate spaces are disjoint. The integral quadratic discriminant specializes to Q²; its primitivity can also be seen from the coefficient 1 on a2²b3²c0² in p1²−4p0p2.

## originality

PASS

Credit the global identification and exhaustion of the first reduced singular locus of the characteristic-two Nash discriminant, including how the components meet there. The older literature already gives the primitive sextic, the same factorized degree-fourteen family in characteristic zero, and the same three coordinate strata there. Neither the number fourteen for that family nor the existence of those coordinate loci deserves separate originality credit. The first reduced singular locus in characteristic two is a distinct assertion, not the characteristic-zero singular-locus table carried over by substitution.

## value

PASS

This identifies what replaces the first singular stratification of a well-studied discriminant after bad-characteristic reduction. The collapse of the defining sextic to a square would make a specialized sextic gradient uninformative; the reduced cubic has a substantially different first singular locus, with the surviving strata and their incidences specified. This gives geometric information beyond the elementary square factorization or the already recorded degree of one shared stratum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
