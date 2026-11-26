---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Euler gives F=Σx_i∂_iF in characteristic two. No projective gradient zero means height four; the four homogeneous quadrics are then a regular sequence in the polynomial ring and the quotient has Hilbert series (1+t)^4. Conversely, full quintic image includes each x_i^5, which rules out any projective gradient zero. Thus the rank-56 test is geometric and works over the base field. With a separately written column-elimination implementation and variable swaps plus a shear generating GL4(F2), I regenerated all 141 nonzero-form orbits, the 36 smooth orbits and 322,560 smooth forms. The regenerated smooth bitmap and the representative/size keys agree exactly with the packaged data. For every orbit representative F I counted compatible G and used 15−popcount of the union of their nonzero-point masks; the weighted bins divide by six because F,G,F+G are the three nonzero forms and every pencil has six ordered bases. All 16 bins matched, totaling 5,002,905,600. A separate Walsh evaluation on the regenerated indicator yielded 30,017,433,600 ordered triples. Parity of cubic evaluations follows monomial by monomial since each leaves an unused variable; this independently excludes exactly fourteen common points. For fifteen points the Boolean reductions leave precisely the alternating pair terms, and the gradient is A times the coordinate-wise squares. I independently found 28 such smooth forms and 56 compatible pencils, one orbit with stabilizer 360. For each extremal pencil I checked the middle coefficients of each member's binary cubic restriction on all 35 rational lines; endpoints vanish already. The five contained lines in every case give each rational point exactly once, so they are pairwise skew.

## originality

PASS

The best-of-knowledge distinction is the complete exact census and full rational-base histogram of additive pencils, not the classification of individual F2 cubics or existence of smooth members in a pencil. The later indexed space-filling result has exact overlap on the b=15 slice and strengthens its geometry, but neither it nor any earlier inspected statement covers the full distribution.

## value

PASS

Lines wholly in the smooth parameter set are a natural exact finite instance of the finite-field smooth pencil problem. The rational common zero set is invariant under both coordinate changes and choice of basis and is a natural way to refine a total. The histogram quantifies the full spectrum rather than recomputing a known surface table: in particular the top two bins distinguish an impossible size from an attained extremal size with a skew-line spread and one symmetry type. This is usable benchmark data for additive incidence in smooth cubic forms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
