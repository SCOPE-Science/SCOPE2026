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

For all N>=1 the DCT-II modes are orthogonal, and for i<j the p^2 cosine second-moment identity follows by differentiating the Dirichlet kernel. Since d=j-i and s=i+j-1 have opposite parity, the N-1 terms cancel; cot^2(dπ/2N)-cot^2(sπ/2N)>0 follows by product of positive sines sin((i-1/2)π/N)sin((j-1/2)π/N). Thus Q_{ij} has sign (-1)^(j-i+1), giving floor((N-1)^2/4) negative unordered entries; analyticity implies N>=3 fails at small t; N<=2 explicit semigroup positive. Cauchy-Schwarz gives sufficient late positivity tπ²/L²>ln(N-1); direct spectral projectors for N=3 yield the exact unique cubic transition. Independently recomputed all 2925 offdiagonal entries for N=2..26, maximum abs difference 1.13e-12.

## originality

PASS

Best-of-knowledge PASS concerns the all-N alternating off-diagonal sign formula and sharp unconditional nodal positivity boundary for the DCT-II Neumann spectral generator, not the prior known DCT numerical method or qualitative counterexamples.

## value

PASS

Complete all-N sign classification for an exact widely used Neumann spectral discretization is meaningful because a full nodal maximum principle is a structural property for ALL initial nodal vectors. The exact first forbidden N and negativity census refine previously numerical violations and support method-selection/certification; the sharp N=3 recovery is secondary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
