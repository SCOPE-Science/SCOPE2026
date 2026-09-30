# The Euclidean Jung constant is the universal local Hausdorff–Gromov–Hausdorff constant — provenance-corrected presentation

## Status and provenance

The universal lower bound below is correct and is the substantive contribution of this record. One component of the original presentation, however, was already present in an earlier SCOPE record.

`2026/09/18/small-hole-gromov-hausdorff-cubic-asymptotic--a0d57fbb476f`,
first committed at 2026-09-18T13:52:44Z, already proves
\[
d_{\mathrm{GH}}(M\setminus B_r(a),M)
=
c_n r+O(r^3),
\qquad
c_n=\sqrt{\frac{n+1}{2n}}.
\]
The present record was first committed at 2026-09-19T01:53:04Z. Accordingly, the deleted-ball cubic asymptotic is treated here as prior SCOPE input, not as a new contribution.

The new claim retained here is the scale-sensitive lower bound for **every** sufficiently dense compact subset and the resulting universal local infimum.

## Theorem

Let \((M,g)\) be a closed connected Riemannian \(n\)-manifold, \(n\ge2\), and put
\[
c_n=\sqrt{\frac{n+1}{2n}},\qquad
h(A)=d_{\mathrm H}(A,M).
\]
There exist \(C_M<\infty\) and \(h_0>0\) such that every compact \(A\subset M\) with \(0<h(A)<h_0\) satisfies
\[
\boxed{
d_{\mathrm{GH}}(A,M)\ge c_n h(A)-C_M h(A)^3.
}
\]

More precisely, with
\[
\kappa_+=\max\{0,\sup_M\sec_g\},
\]
define
\[
\alpha_n(q)=
\begin{cases}
c_n,&q=0,\\[3pt]
c_n\,
\dfrac{\sin\!\left(\frac{\pi}{2}\sqrt{\frac{q}{q+1}}\right)}
{\frac{\pi}{2}\sqrt{\frac{q}{q+1}}},&q>0.
\end{cases}
\]
For any fixed
\[
0<\delta<\frac{\pi}{4(c_n+1)},
\]
after decreasing \(h_0\) if necessary,
\[
\boxed{
\frac{d_{\mathrm{GH}}(A,M)}{h(A)}
\ge
\alpha_n\!\left(\frac{\kappa_+h(A)^2}{\delta^2}\right).
}
\]

If
\[
\mathcal C_M(h)=
\inf\left\{
\frac{d_{\mathrm{GH}}(A,M)}{d_{\mathrm H}(A,M)}:
A\subset M\text{ compact},\ d_{\mathrm H}(A,M)=h
\right\},
\]
then the earlier deleted-ball asymptotic supplies the matching upper family, and therefore
\[
\boxed{
\mathcal C_M(h)=c_n+O_M(h^2),
\qquad
\lim_{h\downarrow0}\mathcal C_M(h)=c_n.
}
\]

## Proof of the universal lower bound

Adams--Frick--Majhi--McBride prove that for a closed Riemannian \(n\)-manifold with sectional curvature bounded above by \(q\ge0\),
\[
d_{\mathrm{GH}}(X,M)
\ge
\min\left\{
\alpha_n(q)d_{\mathrm H}(X,M),
\frac{\alpha_n(q)\tau}{2\alpha_n(q)+2}
\right\},
\]
with the corresponding convexity-radius/curvature cutoff \(\tau\).

Let \(h=d_{\mathrm H}(A,M)>0\) and rescale
\[
g_h=\lambda^2g,\qquad \lambda=\frac{\delta}{h}.
\]
Then
\[
d_{\mathrm H}^{g_h}(A,M)=\delta,\qquad
d_{\mathrm{GH}}^{g_h}(A,M)=\lambda d_{\mathrm{GH}}^g(A,M),
\]
the upper curvature bound becomes
\[
q_h=\frac{\kappa_+h^2}{\delta^2},
\]
and the convexity radius is multiplied by \(\lambda\).

If \(\kappa_+>0\), the second branch of the cited minimum tends to
\[
\frac{c_n(\pi/2)}{2c_n+2},
\]
whereas the first branch tends to \(c_n\delta\). The chosen inequality
\[
\delta<\frac{\pi}{4(c_n+1)}
\]
makes the first branch strictly smaller for all sufficiently small \(h\). Thus
\[
\lambda d_{\mathrm{GH}}^g(A,M)\ge\alpha_n(q_h)\delta,
\]
or
\[
\frac{d_{\mathrm{GH}}^g(A,M)}h
\ge
\alpha_n(q_h).
\]
For \(\kappa_+=0\) the same conclusion holds with \(q_h=0\).

Since
\[
\alpha_n(q)=c_n\left(1-\frac{\pi^2}{24}q+O(q^2)\right),
\]
the displayed cubic lower error follows uniformly for small \(h\).

## Sharpness and relation to the earlier SCOPE record

The earlier record
`small-hole-gromov-hausdorff-cubic-asymptotic--a0d57fbb476f`
combines Schott's optimal Euclidean correspondence, quadratic normal-coordinate distortion, and the same curvature-vanishing rescaling to prove
\[
d_{\mathrm{GH}}(M\setminus B_r(a),M)=c_nr+O(r^3),
\qquad
d_{\mathrm H}(M\setminus B_r(a),M)=r.
\]
That prior SCOPE theorem supplies
\[
\mathcal C_M(h)\le c_n+O(h^2),
\]
while the universal lower bound above supplies the reverse inequality. Hence the local infimum converges to \(c_n\) on every closed manifold, independently of the sign of curvature.

## Scientific value

The record's distinct value is the quantifier upgrade from one asymptotically extremizing deleted-ball family to **all** sufficiently dense compact subsets. It identifies the effective curvature parameter as \(\kappa h^2\) and proves a universal infinitesimal converse constant. The deleted-ball cubic estimate is retained only as prior sharpness input.

## Limitations

The optimal coefficient of the \(h^2\) correction to the ratio is not identified. No classification of all asymptotically extremizing subsets is given. The theorem is restricted to smooth closed Riemannian manifolds of dimension at least two.

## References

1. H. Adams, F. Frick, S. Majhi, N. McBride, *Hausdorff vs Gromov–Hausdorff Distances*, Discrete & Computational Geometry 75 (2026), 1217--1246; arXiv:2309.16648.
2. P. Schott, *A converse bound for dGH vs. dH for Euclidean space and Riemannian manifolds*, arXiv:2609.12625 (2026).
3. SCOPE record `2026/09/18/small-hole-gromov-hausdorff-cubic-asymptotic--a0d57fbb476f`, first committed 2026-09-18T13:52:44Z.
