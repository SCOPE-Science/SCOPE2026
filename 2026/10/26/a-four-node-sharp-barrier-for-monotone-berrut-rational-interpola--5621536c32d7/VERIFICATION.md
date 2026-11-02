---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

In a cell nx=m+t, 0<t<1, write central weight sum u=t^−1+(1−t)^−1 and alternating left/right tails a,b, with 0≤a≤(1+t)^−1, 0≤b≤(2−t)^−1. The normalized barycentric denominator D=u−a−b>5/2 has no pole. Every monotone sample decomposes into nonnegative step jumps, and normalized suffix responses H_k satisfy −b/D≤H_k≤1+a/D by alternating partial/suffix bounds. The sharp local range defect equals max(a,b)/D. Monotonicity in both tails reduces every grid to the envelope F(t), equal to t(t−1)(t−2)/[2(t²−t+1)] for 0<t≤1/2, symmetric under t↦1−t. F has one interior maximizer t*=0.4404585133... since its derivative numerator t^4−2t^3+4t²−6t+2 crosses zero exactly once. The polynomial resultant gives the unique positive algebraic defect; n=3 with one-tail terms attains both signs via complementary step data. Independently checked 680 exact (n,cell,rational t) cases and the symbolic derivative/resultant.

## originality

PASS

Berrut 1988 introduced the exact original alternating barycentric interpolant. Bos–De Marchi–Hormann 2011 proved logarithmic growth of its unrestricted Lebesgue constant; a universal sharp range defect restricted to monotone step data is a different norm and is not implied by a logarithmic unrestricted bound. Nguyen–Cuyt–Salazar Celis 2011 develop comonotone/coconvex interpolation with designed rational weights, not the assessed fixed weights in inspected accessible descriptions. Published Resultary exact four-point range defects concern degree-one Floater–Hormann, cubic Lagrange, Catmull–Rom and Akima operators, which have different weights/bases. An inaccessible original Berrut full text and unexamined comonotone article remain possible priority sources.

## value

PASS

This theorem is the all-n sharp shape defect of the canonical simple pole-free barycentric rational interpolant under the natural monotone-data cone, with a finite four-node universal extremizer despite growing unrestricted Lebesgue constants. The exact algebraic constant is a motivated, independent numerical invariant of a standard approximation operator, useful for quantitative shape-preserving error control.

The dated certificate retains the supplied scientific assessment, sources and limitations.
