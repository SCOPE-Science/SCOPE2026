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

A nonzero real traceless symmetric matrix has both signs, and diagonalization with scaling/sign and interchange of axes gives diag(1,-a,-(1-a)), 0<=a<=1/2. In a frame with last vector n, the n-normal restriction determinant is its last principal cofactor, hence s n_x^2-(1-a)n_y^2-a n_z^2 with s=a(1-a). A nondegenerate indefinite binary form gives four circle zeros and a definite one gives none. The exceptional normals have measure zero also at a=0 (there the determinant is -n_y^2). The nodal set is rectifiable: it is smooth on S^2 for nonsingular A, and two great circles in the singular case. The normalized Crofton factor pi gives 2pi for a great circle intersected twice. The uniform polar coordinate n_x then yields L/(4pi) as the average of sqrt(U/(U+s)) with U=(1-a)cos^2(phi)+a sin^2(phi). At a=0 this equals 1 almost everywhere, and it is everywhere strictly less than 1 for positive a. For the lower bound, the two shifted U values sum to one and have product k; the paired p,q satisfy p^2+q^2=(2k+s)/(k+s+s^2), pq=sqrt(k/(k+s+s^2)). The deficits for p^2+q^2>=4/3 and pq>=2/3 reduce respectively to 2k-s-4s^2 and 5k-4s(1+s). Substitution of d=1-2a and v=cos(2phi) gives the printed two factorizations: both bracket factors are at least 1-d^2>0 for 0<a<1/2, making the inequalities strict unless d=0. Averaging the pair gives the exact lower endpoint, with a=0 handled separately. Thus the extrema are exactly the double-eigenvalue and zero-eigenvalue classes, respectively. This is analytic; the frozen eight-point numerical output is consistency evidence only.

## originality

PASS

The deterministic lower theorem and its equality classification are distinct to the best of the inspected evidence. Gichev had proposed the zonal length as a possible sharp lower bound, so the candidate itself is not new. The general upper bound and its sectoral attainment are prior and are not credited as the contribution. The frozen elementary calculation pins down both equality cases in degree two.

## value

PASS

This resolves the zonal-minimum candidate and identifies all minimizers in the first degree where the length is nonconstant across real harmonics. It is a geometric invariant of a canonical eigenspace, motivated by the previously posed sharp lower-bound question. The proof yields a useful spectrum-to-length formula and establishes strict optimality without needing a monotonicity assumption. It neither solves the higher-degree problem nor needs to in order to settle this nontrivial case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
