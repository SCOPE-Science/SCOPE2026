# Quantitative one-positive-chamber stability for minimal regular-simplex slices

## Result

Let
\[
T_{n-1}=\operatorname{conv}(e_1,\ldots,e_n)\subset\mathbb R^n,\qquad n\ge 3,
\]
and, for a unit vector \(a\perp(1,\ldots,1)\), write
\[
V(a)=\operatorname{Vol}_{n-2}(T_{n-1}\cap a^\perp).
\]
Fix the facet-parallel minimizing normal
\[
a_*=(A,-B,\ldots,-B),\qquad
A=\sqrt{\frac{n-1}{n}},\quad
B=\frac1{\sqrt{n(n-1)}}.
\]
Its section volume is
\[
V_{\min}=\frac{\sqrt n}{(n-2)!}
\left(\frac{n-1}{n}\right)^{n-\frac32}.
\]

Consider the closed sign chamber
\[
\mathcal C=\{a=(x,-y_2,\ldots,-y_n):
x>0,\ y_j\ge0,\ \sum_{j=2}^n y_j=x,\ \|a\|_2=1\}.
\]
Then every \(a\in\mathcal C\) satisfies the quantitative estimate
\[
\boxed{\quad
\frac{V(a)}{V_{\min}}
\ge \frac1{\langle a,a_*\rangle}
=\sec\theta
=\frac1{1-\frac12\|a-a_*\|_2^2},
\quad}
\]
where \(\theta=\arccos\langle a,a_*\rangle\). Equality holds only at \(a=a_*\).

Equivalently, if \(r_j=y_j/x\), so that \(\sum r_j=1\), and
\[
\delta_r=\sum_{j=2}^n\left(r_j-\frac1{n-1}\right)^2,
\]
then
\[
\frac{V(a)}{V_{\min}}
\ge
\sqrt{1+\frac{n-1}{n}\,\delta_r}.
\]
In particular,
\[
V(a)-V_{\min}\ge V_{\min}(\sec\theta-1)
\ge \frac12V_{\min}\theta^2.
\]

Moreover the facet-parallel minimum is nondegenerate, and the full Riemannian Hessian of \(V\) on
\[
S^{n-2}=\{a:\|a\|_2=1,\ \sum a_j=0\}
\]
at \(a_*\) is isotropic:
\[
\boxed{\qquad
\operatorname{Hess}_{a_*}V
=
\frac{2n-1}{n}\,V_{\min}\,g.
\qquad}
\]
Thus the Hessian has the single eigenvalue
\[
\frac{2n-1}{n}V_{\min}
\]
with multiplicity \(n-2\).

## Proof of the chamber estimate

Ambrus and Gárgyán use the standard exponential representation
\[
V(a)=\frac{\sqrt n}{(n-2)!}\sigma(a),
\]
where \(\sigma(a)\) is the density at zero of
\[
\sum_{j=1}^n a_jX_j
\]
for independent rate-one exponential random variables \(X_j\).

For \(a=(x,-y_2,\ldots,-y_n)\in\mathcal C\), set \(r_j=y_j/x\). Then \(r_j\ge0\) and \(\sum r_j=1\). Conditioning on \(Y=\sum_{j=2}^ny_jX_j\) gives the exact formula
\[
\sigma(a)
=
\frac1x\mathbb E e^{-Y/x}
=
\frac1x\prod_{j=2}^n\frac1{1+r_j}.
\]
At \(a_*\), all \(r_j=1/(n-1)\), hence
\[
\sigma(a_*)
=
\frac1A\left(\frac{n-1}{n}\right)^{n-1}.
\]
By AM-GM,
\[
\prod_{j=2}^n(1+r_j)
\le
\left(\frac{n}{n-1}\right)^{n-1},
\]
and therefore
\[
\frac{\sigma(a)}{\sigma(a_*)}\ge\frac A x.
\]
Since
\[
\langle a,a_*\rangle
=xA+B\sum_{j=2}^ny_j
=x(A+B)=\frac xA,
\]
this proves
\[
\frac{V(a)}{V_{\min}}\ge\frac1{\langle a,a_*\rangle}.
\]
Equality in AM-GM forces all \(r_j=1/(n-1)\); together with \(\|a\|=1\), this forces \(a=a_*\).

Because \(a\) and \(a_*\) are unit vectors,
\[
\langle a,a_*\rangle
=1-\frac12\|a-a_*\|^2=\cos\theta.
\]
Also
\[
x^{-2}=1+\sum r_j^2
=\frac n{n-1}+\delta_r,
\]
so
\[
\left(\frac A x\right)^2
=1+\frac{n-1}{n}\delta_r.
\]
The displayed equivalent forms follow.

## Exact Hessian

The tangent space at \(a_*\) is
\[
T_{a_*}S^{n-2}
=
\{v=(0,v_2,\ldots,v_n):\sum_{j=2}^nv_j=0\}.
\]
Take a unit tangent vector \(v\) and the unit-speed geodesic
\[
a(t)=a_*\cos t+v\sin t.
\]
For small \(t\), this remains in the same open sign chamber. Put
\[
D=A+B=\sqrt{\frac n{n-1}}.
\]
Using the exact chamber formula above,
\[
\log\sigma(a(t))
=
(n-2)\log(A\cos t)
-\sum_{j=2}^n
\log(D\cos t-v_j\sin t).
\]
The first derivative at \(t=0\) vanishes because \(\sum v_j=0\). The second derivative is
\[
-(n-2)+(n-1)+\frac{\sum v_j^2}{D^2}
=
1+\frac{n-1}{n}
=
\frac{2n-1}{n}.
\]
Since \((\log\sigma)'(0)=0\),
\[
\frac{d^2}{dt^2}V(a(t))\Big|_{t=0}
=
\frac{2n-1}{n}V_{\min}.
\]
This is independent of the unit tangent direction \(v\), proving the Hessian formula.

## Relation to prior work

Ambrus and Gárgyán proved in 2026 that facet-parallel central sections are the global minimizers of the regular simplex. Their paper also notes a sign gap in the proof of Dirksen's 2017 balancing proposition, on which an earlier partial verification relied.

Dirksen's work had stated a qualitative minimum result in the chamber with one coordinate of one sign and all remaining coordinates of the opposite sign. The argument above gives a direct proof in that chamber that does not use the affected balancing step, and strengthens the qualitative statement to an explicit angular and coordinate-imbalance deficit. It also determines the complete second variation at the facet-parallel minimizer.

The 2025 stability theorem of Myroshnychenko, Tang, Tatarko and Tkocz concerns the opposite extremal problem: stability of Webb's maximal-volume central sections. It does not give a minimum-side deficit or the Hessian computed here.

## Limitations

The explicit deficit above is proved only in a one-positive-coordinate chamber (and, by permutation and sign, its symmetric copies). It is not a global quantitative stability theorem for all central hyperplanes. The Hessian statement is local. In particular, this result does not quantify how the section volume grows away from the full finite set of facet-parallel minimizers through regions where the normal has two or more positive and two or more negative coordinates.

The motivating global-minimum preprint is very recent, so unindexed parallel work remains a residual originality risk.

## References

1. G. Ambrus and B. Gárgyán, *Minimal central slices of the regular simplex*, arXiv:2609.12714 (2026), https://arxiv.org/abs/2609.12714.
2. H. Dirksen, *Sections of the regular simplex – Volume formulas and estimates*, Math. Nachr. 290 (2017), 2567–2584, https://doi.org/10.1002/mana.201600109.
3. S. Myroshnychenko, C. Tang, K. Tatarko and T. Tkocz, *Stability of Simplex Slicing*, Discrete Comput. Geom. 76 (2026), 491–507, https://doi.org/10.1007/s00454-025-00758-x.
