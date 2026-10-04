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

The final claim is: Let \(n\ge 2\). For each \(r\in[1,\infty]\), let \(p_r=\|\cdot\|_r\) on \(\mathbb R^n\). Then \(p_r\) and \(p_s\) lie in the same intrinsic part of \(\mathcal N(\mathbb R^n)\) if and only if \(r=s\). For \(1<r<\infty\), the separating local triangular-defect asymptotic along \(e_1\) and \(e_1+t e_2\) is \(\Delta_{p_r}(e_1,e_1+t e_2)=((1-2^{1-r})/r)t^r+O(t^{2r})\). Consequently, for every \(n\ge 2\), the cone of equivalent norms on \(\mathbb R^n\) has continuum many intrinsic parts.

The decisive published input is the equivalence in arXiv:2609.28922v1, Theorem 4.6, between common intrinsic-part membership and two-sided uniform comparison of triangular defects. Corollary 4.7 gives equality of zero sets as a necessary condition.

For \(1<r<\infty\), direct symbolic expansion yields

\[
\Delta_{p_r}(e_1,e_1+t e_2)
=\frac{1-2^{1-r}}{r}t^r+O(t^{2r}),
\]

with a strictly positive coefficient. Thus distinct finite exponents give an asymptotic ratio tending to \(0\) in one direction, which is incompatible with uniform two-sided comparison. The coefficient specializes to \(1/4\) at \(r=2\) and \(7/32\) at \(r=4\), exactly matching Example 4.8 of the source.

At \(r=1\), the pair \(e_1,e_2\) has zero defect, while every \(r>1\) member has positive defect there. At \(r=\infty\), the pair \(e_1,e_1+e_2\) has zero defect, while every finite \(r>1\) member has positive defect by strict convexity. These checks cover all endpoint comparisons.

No finite computation, sampling argument, or numerical tolerance is used. The proof is exact. The literature search does not certify novelty; it only records that no covering statement was found among the inspected sources and semantic matches.
