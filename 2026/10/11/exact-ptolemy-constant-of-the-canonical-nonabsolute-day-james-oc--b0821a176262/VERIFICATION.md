---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Independently reconstructed the exact real norm from its 3-piece psi, including continuity at t=1/8 and 1/2, the opposite-sign ell_infinity branch and agreement on coordinate axes. The unit sphere is the 8-vertex centrally symmetric convex polygon with right-half boundary (0,-1),(1,-1),(1,1/7),(2/3,2/3),(0,1). The quadratic q(a,b)=a²+(10/13)ab+b² is positive definite (eigenvalues 1 +/- 5/13). On the four independent edges, exact rational stationary minima are (144/169,144/169,72/65,64/65), at parameters (5/13,7/13,3/10,4/5). Vertex values (1,16/13,720/637,16/13,1) yield exact global m=144/169, M=16/13 by convexity and central symmetry. Thus sqrt(m)N<=sqrt(q)<=sqrt(M)N for every vector and Hilbert Ptolemy gives the global bound C_Pt<=M/m=13/9. The explicitly admissible pairwise-distinct nonzero triple x=(-2/3,-2/3), y=(3/2,-3/2), z=(5/6,-13/6) has six norms (N(x),N(y),N(z),N(x-y),N(x-z),N(z-y))=(1,3/2,13/6,13/6,3/2,1), so its Ptolemy ratio equals (13/6)²/((3/2)²+1)=13/9. Independent exact Fraction arithmetic verified all edge minima, vertex values and witness norms. The continuous universal assertion is proved analytically, not by finite sampling or checker output alone.

## originality

PASS

The exact real two-dimensional nonabsolute Day--James octagon from Nilsrakoo--Saejung 2006 is natural and documented, but the inspected defining paper establishes James-type properties, not a Ptolemy constant. Zuo 2012 and 2018 give Ptolemy theorems for absolute normalized planes, a class explicitly excluding this canonical octagon. A materially inspected earlier published finding establishes the same octagon’s exact squared Euclidean Banach--Mazur distance 13/9 and even the identical optimal quadratic q, so the sharp Ptolemy upper bound is already implied and receives NO originality credit. That affine-distortion result neither states nor logically forces that the Ptolemy constant attains the upper bound. A distinct triple gives the necessary lower bound by exact norm calculation. Other inspected Ptolemy cases concern distinct polygonal or classical Day--James norms; the midpoint symmetric-absolute equality theorem also excludes this nonabsolute octagon. No covering primary theorem or table was identified after searches of aliases and equations. Best-of-knowledge PASS applies narrowly to the exact Ptolemy equality and explicit witness, not to the previously established Euclidean comparison. Historical-priority and unread-source risks are retained.

## value

PASS

The Ptolemy constant is a natural affine-invariant measure of Hilbert/Ptolemaic four-point geometry. The norm is the specific canonical nonabsolute generalized Day--James octagon used by Nilsrakoo--Saejung to demonstrate that this class genuinely exceeds normalized absolute norms. Its exact four-point invariant was not implied by its previously computed Banach--Mazur distortion: proving equality of metric and linear-distortion bounds requires a sharp saturating quadrilateral configuration. The exact 13/9 value and rational attaining triple therefore provide a substantive reproducible benchmark at a natural boundary of existing absolute-norm Ptolemy theories. The contribution is one motivated exact planar case, not a general generalized Day--James classification; an independently useful precise fact need not produce a paper-sized downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
