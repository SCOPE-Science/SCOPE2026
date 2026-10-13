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

Li--Li's local model gives
\[
R_d=
\bigoplus_{m\ge0}
H^0\!\left(
\mathbf P^1,
\operatorname{Sym}^m(
\mathcal O_{\mathbf P^1}(1)\oplus
\mathcal O_{\mathbf P^1}(d))
\right).
\]
For \(m\ge0\),
\[
\operatorname{Sym}^m(
\mathcal O(1)\oplus\mathcal O(d))
=
\bigoplus_{b=0}^{m}
\mathcal O(m-b+bd).
\]
Every summand has nonnegative degree, hence
\[
\begin{aligned}
\dim (R_d)_m
&=
\sum_{b=0}^{m}(m-b+bd+1)\\
&=
(m+1)^2+\frac{(d-1)m(m+1)}{2}\\
&=
\frac{d+1}{2}m^2+\frac{d+3}{2}m+1.
\end{aligned}
\]
The leading coefficient is \((d+1)/2\). A standard graded ring of dimension \(3\) has leading Hilbert-polynomial coefficient \(e/2!\), so
\[
e(R_d)=d+1.
\]

The source identifies the completed local contraction ring with the completion of this graded local ring. Hilbert--Samuel multiplicity is invariant under completion, giving
\[
\operatorname{mult}_{y_i}(Y_i)=d_i+1.
\]

The same source independently establishes
\[
\operatorname{edim}_{y_i}(Y_i)=d_i+3
\]
and chooses the integers \(d_i\) strictly increasing. Therefore
\[
\operatorname{mult}_{y_i}(Y_i)=\operatorname{edim}_{y_i}(Y_i)-2
\]
and these multiplicities are unbounded.

No numerical experiment is used. The only general commutative-algebra inputs are the standard relation between Hilbert-polynomial leading coefficient and multiplicity for a standard graded ring, and invariance of Hilbert--Samuel multiplicity under completion.
