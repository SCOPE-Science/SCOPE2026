---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Verified exact supporting-line distances r_A=y,r_B=(h+hx-y)/sqrt(1+h²),r_C=(h-hx-y)/sqrt(1+h²). Convexity minimizes apex defect at x=0 and F(y) globally at y*=(L-1)/sqrt(2L-1), giving h<=sqrt(3). For a base vertex the convex two-focus G_h has tangent point (x*,0); its inward y derivative is strictly positive when t=h/L<=1/2, while exact polynomial identity -(2t-1)(4t³-4t+1) establishes nonnegative boundary deficit. For 1/sqrt(3)<h<=1 the same x* makes G_h<0; for 1<=h<sqrt(3) centroid deficit is negative; for h>sqrt(3) apex fails. Rotational symmetry at h=sqrt(3) proves the isolated equilateral case. The cyclic implication follows termwise by reciprocals only where its denominators are positive. This is an all-h proof, not numerical extrapolation.

## originality

PASS

The original Liu 2015 Conjecture 1 is cyclic and does not state three simultaneous termwise conditions or their sharp disconnected isosceles shape classification. The close published symmetric weight theorem proves PA+PB+PC >= lambda(r_a+r_b)+2r_c with optimized lambda(h) and Liu Conjecture 2, a different sum. Its exact proof and assumptions were read. No stronger claim was found that implies these three individual comparisons. Best-of-knowledge PASS with residual unindexed weighted-inequality risk.

## value

PASS

The three termwise inequalities are a genuinely motivated mechanism for a published unproved cyclic inequality. The exact if-and-only-if shape classification isolates a full extreme-angle branch and a disconnected equilateral point, and explicitly bounds the region on which that stronger proof method can work. The restriction to method failure (not cyclic-conjecture failure) is essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
