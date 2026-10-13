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

For the weighted projective presentation \(\mathbf P(1^{n+1},m)\), the source theorem has degree \(d=rm\) and weight sum \(W=n+1+m\). The asserted numerical condition
\[
(r-1)m>n+1
\]
is exactly \(d>W\), and the stated gcd condition is exactly \(\gcd(d,W)=1\).

Quasismoothness is checked directly from the affine cone equation \(f=z^r-F(x)\). A critical point satisfies \(rz^{r-1}=0\), hence \(z=0\), and simultaneously \(\partial_iF=0\) for every \(i\). On \(f=0\) this also gives \(F=0\). Away from the origin this would be a singular point of the projective branch hypersurface, excluded by hypothesis.

The classification of graded coordinate changes is forced by the weights. Since \(m\ge2\), every degree-one coordinate is a linear combination of the \(x_i\), so \(x\mapsto Lx\). The unique weight-\(m\) coordinate may change as \(z\mapsto az+h_m(x)\), with \(a\ne0\). In
\[
(az+h_m)^r-G(Lx)=c(z^r-F),
\]
the \(z^{r-1}\)-coefficient is \(ra^{r-1}h_m\). Characteristic zero implies \(h_m=0\); then the \(z^r\)-coefficient gives \(c=a^r\) and the constant term gives \(G(Lx)=a^rF(x)\).

No computational experiment is needed for this universal proof. The nonstandard input is Theorem 1.7 of arXiv:2610.00130v1. The closest same-source branch-recovery calculation is its Fano double-cover Corollary 1.5, while the general-type section does not state a cyclic-cover corollary.
