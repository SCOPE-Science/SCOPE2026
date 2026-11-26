---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reconstructed the three replacements by the squared-distance midpoint formula d(k,mid(i,j))=(d(k,i)+d(k,j))/2−d(i,j)/4, where d denotes squared distance. Acting on labels by the stated cycle sends the final 03, 01, 02 entries to 01, 02, 03 respectively and returns D/4 with parameters (−3x/2−y,x). The return preserves Q, has determinant 1 and trace −3/2, which cannot be the rational algebraic-integer sum of two roots of unity. In the Gram basis of edge vectors v1,v2+v3,v2−v3 from vertex 0, writing s=x+y and t=x−y gives diagonal entries 23+4s,2+2s,10 and off-diagonals 6+9s/2,t/2,t. Its determinant divided by 4 is 25−35Q/4; the original first two leading minors are positive on Q≤2 by the dual norm estimates. The two intermediate winners are tied at squared lengths 20 and 10; the other three variable entries stay below these lengths using |x|,|y|<2. Thus only s≥−3/4 remains, and Q=(7s²+t²)/2 gives cutoff 63/32 with unique negative contact. The orbit visits the open violating arc at every higher level if an infinite admissible branch is hypothesized, without requiring physicality of the whole higher ellipse. On Q≤2 the arc fraction is arctan(sqrt((q−q_c)/q_c))/π above threshold, proving the frequency and onset; its endpoints have zero angular measure. Midpoint replacement preserves nondegeneracy, compact phase images give compact shape sets, and the two fixed squared lengths 20 force the scale factor to be one at marked returns; finite relabelings cannot eliminate infinitely many distinct normalized parameters. The determinant minimum 995/128 and diameter-squared maximum 26 are simultaneous at (3/8,3/8), proving the sharp marked volume bound.

## originality

PASS

The exact marked return, affine ellipse, and irrational dynamics are prior. The supported increment is the sharp entire-family cutoff, its all-phase obstruction and formal angular frequency/onset, and the sharp marked-boundary normalized-volume bound. These are not in the inspected proof on the sample ellipse or supplied by convexity of pattern cells.

## value

PASS

For a prescribed nonperiodic refinement mechanism, the maximum invariant set by quadratic level is a natural robustness question. The cutoff decides legality simultaneously for every phase, rules out all infinite repetitions above it, and quantifies near-boundary failure and guaranteed block-boundary shape quality. It is an exact range of the known mechanism rather than another arbitrarily small legal example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
