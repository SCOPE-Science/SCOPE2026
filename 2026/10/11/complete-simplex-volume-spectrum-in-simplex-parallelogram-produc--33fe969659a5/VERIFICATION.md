---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

All quantifiers checked for integer n≥1, arbitrary nondegenerate affine n-simplex and parallelogram, all unordered N+2-vertex subsets and all full-dimensional contained simplices. After selecting one row per simplex-vertex layer the barycentric block is an identity and exactly two surplus rows remain, yielding a 2×2 determinant of corner differences; missing a layer forces zero. The only nonzero-support occupancy patterns are a triple layer plus N−1 singles (each of four possible triples determinant 1), or two doubled layers plus N−2 singles. Among six unoriented square-segment types, 36 ordered pairs partition into 10 zero (parallel), 24 unit (eight perpendicular edge–edge and sixteen edge–diagonal), and two determinant-two (the complementary diagonal pair). Thus H1=N4^N+12N(N−1)4^(N−2), H2=N(N−1)4^(N−2), H0=binom(4N,N+2)−H1−H2. Homogeneous-coordinate determinant equals (n+2)! volume for standard simplex×unit square, while product volume is 1/n!, giving j/((n+1)(n+2)). The maximum of |det| is separately convex in each arbitrary simplex vertex, so sequential extremal replacement proves no nonvertex simplex exceeds determinant 2. Existence at n=1 uses distinct doubled layers and diagonal pairs. Product affine transformations transfer ratios and vertex-supported equality cases. Independent full subset enumeration by planar occupancy and cross products for n=1..4 gave (H0,H1,H2)=(12,56,2),(288,480,24),(4488,3328,192),(55760,20480,1280). Independently constructed ordinary homogeneous matrices with exact SymPy Bareiss determinants for n=1..3 and obtained identical counts. All-n conclusion rests on the algebraic proof, not finite checks. No classification of nonvertex equality cases is claimed; the volume-only triangulation lower bound is nonoptimal and not claimed novel.

## originality

PASS

Qualified best-of-knowledge PASS for the all-n complete three-class vertex-volume histogram and exact affine-invariant contained-simplex maximum. Seacrest–Su 2017/2018 Sections 3 and 7 provide normalized class vocabulary, the n=2 maximal class 2, and the exact 24 class-two simplices. These statements cover the n=2 specialization, and the n=1 cube is classical. The inspected full original text does not state, tabulate, or mathematically imply without substantial additional enumeration the all-n formulas H0/H1/H2 for Delta_n times two segments. Ardila–Billey Sections 7–8 cover combinatorics of triangulations of a product of TWO simplices, not all vertex-supported potentially nonunimodular simplices of this THREE-factor product. Three actual Resultary semantic searches found an identical indexed copy of this very assigned record, excluded as independent priority evidence; other returned SCOPE records address different polytope problems. All-dimensional proof is elementary but is not a routine parameter substitution of the inspected prior n=2 theorem. No claim of exhaustive historical priority.

## value

PASS

The product of an arbitrary simplex and a parallelogram is a canonical infinite 3-factor simplotope family, with dimension growing and an existing literature on normalized volume classes and triangulations. An exact full histogram of nonzero and zero full-dimensional vertex-subset determinants, plus sharp equality classification and the unrestricted maximal contained-simplex volume fraction, is a motivated natural geometric invariant useful for class-based covering/triangulation lower bounds and exact benchmark families. It goes beyond a single precomputed n=2 entry, gives complete closed formulas for every n and controls arbitrary inscribed simplices. The recurrence-free proof is short but not merely parameter substitution of a prior all-dimensional formula; no unproved general consequence or optimal triangulation size is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
