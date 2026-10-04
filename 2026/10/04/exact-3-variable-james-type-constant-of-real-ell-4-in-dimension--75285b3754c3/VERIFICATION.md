---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The mathematical check is analytic.

1. Normalize the scalar quotient by \(a^4+b^4+c^4=1\). The constraint is compact and smooth.
2. Euler homogeneity applied to the Lagrange equations gives a positive multiplier at a maximizing nonconstant triple. For an all-distinct stationary triple, subtracting those equations then forces \(a+b+c=0\); expansion gives quotient \(9\).
3. A repeated coordinate equal to zero gives quotient \(2\). Otherwise scaling reduces the quotient to \(f(t)=2(1-t)^4/(2+t^4)\), and direct differentiation gives \(f'(t)=8(t-1)^3(t^3+2)/(t^4+2)^2\). Its global maximum is attained at \(t=-\sqrt[3]{2}\) and equals \((1+\sqrt[3]{2})^3\), which is strictly larger than \(9\).
4. Summing the sharp scalar inequality over coordinates proves the infinite-dimensional upper bound without truncation or enumeration.
5. The three cyclic vectors in the proof are unit vectors and have all three pairwise distances exactly \((1+\sqrt[3]{2})^{3/4}\).

No computational experiment is needed for the proof. The remaining limitation is bibliographic rather than mathematical: differently named older three-point packing results may exist, although the recorded equivalence and exact-value searches did not find one.
