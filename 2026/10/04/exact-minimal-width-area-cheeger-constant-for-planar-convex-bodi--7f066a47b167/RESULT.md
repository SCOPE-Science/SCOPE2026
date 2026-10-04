# Exact minimal-width–area Cheeger constant for planar convex bodies

## Finding

Let \(\Omega\subset\mathbb R^2\) be a planar convex body, meaning a compact convex set with nonempty interior, and let \(D(\Omega)\) be its Euclidean diameter. For every bounded measurable set \(X\subseteq\Omega\) of positive area define the directional width
\[
w_u(X)=
\sup_{x\in X}\langle x,u\rangle-
\inf_{x\in X}\langle x,u\rangle,
\qquad u\in S^1,
\]
and its minimal width
\[
\omega(X)=\min_{u\in S^1}w_u(X).
\]
Then
\[
\boxed{
\inf_{\substack{X\subseteq\Omega\\A(X)>0}}
\frac{\omega(X)}{A(X)}
=
\frac{1}{D(\Omega)}
}.
\]

The infimum is not attained by any positive-area admissible set.

Moreover, every diameter segment generates an explicit minimizing mechanism. If \(p,q\in\Omega\) satisfy
\[
|p-q|=D(\Omega),
\]
choose any point \(r\in\operatorname{int}\Omega\) not on the line through \(p,q\), and let \(h>0\) be the perpendicular distance from \(r\) to that line. For \(0<t<h\), take the portion of \(\Omega\) lying between the diameter line and the parallel line at distance \(t\) on the side containing \(r\). These convex slices satisfy
\[
\frac{\omega(X_t)}{A(X_t)}
\le
\frac{1}{D(\Omega)\left(1-\frac{t}{2h}\right)},
\]
so their ratios converge to \(1/D(\Omega)\).

## Assumptions and scope

No convexity is imposed on the admissible set \(X\). The width of an arbitrary bounded set is defined through its directional projection lengths as above; passing to the closed convex hull does not change any directional width.

The result addresses the Cheeger-type variant proposed in the literature in which the perimeter numerator is replaced by minimal width. It shows that, unlike the ordinary planar Cheeger problem, this variant has no positive-area minimizer for any planar convex body: the optimal value is controlled only by the ambient diameter and is approached by degenerating thin slices.

## Proof

Let \(X\subseteq\Omega\) be measurable with \(A(X)>0\), and let
\[
K=\overline{\operatorname{conv}}(X).
\]
Directional extrema are unchanged by taking the closed convex hull, hence
\[
\omega(K)=\omega(X).
\]
Also,
\[
A(X)\le A(K).
\]

Choose \(u\in S^1\) for which
\[
w_u(K)=\omega(K),
\]
and let \(v\) be a unit vector perpendicular to \(u\). The body \(K\) lies in the orthogonal bounding rectangle whose side lengths are \(w_u(K)\) and \(w_v(K)\). Therefore
\[
A(K)\le w_u(K)w_v(K).
\]
Since every directional width is bounded by the Euclidean diameter,
\[
w_v(K)\le D(K)\le D(\Omega).
\]
Consequently,
\[
A(X)\le A(K)\le\omega(X)D(\Omega),
\]
and hence
\[
\frac{\omega(X)}{A(X)}
\ge
\frac1{D(\Omega)}.
\]
This proves the universal lower bound.

To prove sharpness, choose a diameter pair \(p,q\in\Omega\), so
\[
|p-q|=D(\Omega)=D.
\]
Let \(L\) be the line through \(p,q\). Because \(\Omega\) has nonempty interior, choose \(r\in\operatorname{int}\Omega\setminus L\). Let \(u\) be the unit normal to \(L\) pointing toward \(r\), and let
\[
h=\operatorname{dist}(r,L)>0.
\]
After translating the \(u\)-coordinate so that \(L\) is at level \(0\), define
\[
X_t=
\Omega\cap\{x:0\le\langle x,u\rangle\le t\},
\qquad 0<t<h.
\]

The triangle
\[
T=\operatorname{conv}\{p,q,r\}
\]
lies in \(\Omega\). Its section parallel to \(pq\) at normal height \(s\in[0,h]\) has length
\[
D\left(1-\frac{s}{h}\right).
\]
Therefore
\[
A(X_t)
\ge
\int_0^t
D\left(1-\frac{s}{h}\right)\,ds
=
Dt\left(1-\frac{t}{2h}\right).
\]
On the other hand, \(X_t\) lies in a strip of width \(t\), so
\[
\omega(X_t)\le t.
\]
Thus
\[
\frac{\omega(X_t)}{A(X_t)}
\le
\frac{1}{D\left(1-\frac{t}{2h}\right)}.
\]
Letting \(t\downarrow0\) gives the reverse inequality for the infimum and hence the exact value.

It remains to prove nonattainment. Suppose that some positive-area \(X\subseteq\Omega\) satisfies
\[
\frac{\omega(X)}{A(X)}=\frac1D.
\]
With \(K=\overline{\operatorname{conv}}(X)\) and a minimizing width direction \(u\) as above, the chain
\[
A(X)\le A(K)\le \omega(K)w_v(K)\le\omega(X)D=A(X)
\]
forces equality throughout. In particular,
\[
w_v(K)=D
\]
and \(K\) has the full area of its orthogonal bounding rectangle of side lengths \(\omega(K)\) and \(D\). A proper compact convex subset of a rectangle has strictly smaller area, so \(K\) must equal that rectangle.

Because \(A(X)>0\), one has \(\omega(K)>0\). The rectangle \(K\) therefore has Euclidean diameter
\[
\sqrt{D^2+\omega(K)^2}>D,
\]
contradicting
\[
D(K)\le D(\Omega)=D.
\]
Hence the infimum is never attained.

## Verification

The argument is exact and does not rely on finite enumeration or numerical optimization.

The lower bound uses only three elementary facts: convexification preserves directional widths; a planar convex set has area at most the area of any orthogonal bounding rectangle; and every directional width is at most the Euclidean diameter.

The upper bound is witnessed inside the explicit triangle \(\operatorname{conv}\{p,q,r\}\). Integrating its linear section profile gives
\[
Dt\left(1-\frac{t}{2h}\right),
\]
which supplies a quantitative minimizing sequence.

The nonattainment argument checks the equality conditions in the same bounding chain. No computational certificate or unproved asymptotic step is used.

## Relationship to prior work

Cañete explicitly proposed a Cheeger-type problem in which the perimeter numerator is replaced by other classical geometric magnitudes. In Remark 11, minimal width, circumradius, and inradius are named, with the objective of minimizing
\[
\frac{F(X)}{A(X)}
\]
over subsets \(X\) of a fixed planar convex body. The paper states that no related reference was found there. The present theorem gives a complete answer for the minimal-width choice \(F=\omega\): the value is the reciprocal ambient diameter, and there is never a positive-area minimizer.

Ftouhi, Masiello, and Paoli later studied sharp inequalities involving the ordinary perimeter-based Cheeger constant together with area, minimal width, diameter, circumradius, and other global functionals. Their variable is the ambient convex body and their Cheeger constant remains the classical perimeter-over-area infimum. Their full text defines minimal width and develops diagrams such as \((\omega,h,D)\), but it does not replace perimeter by minimal width in the subset functional and therefore does not imply the theorem above.

Targeted searches for “minimum width area Cheeger,” “minimal width divided by area,” “width-area Cheeger,” reciprocal-diameter formulations, thin-strip minimizing sequences, and Problem A23 terminology did not locate an equivalent theorem.

## Limitations

The theorem is planar. The same bounding-box idea gives a lower bound in higher dimensions, but the numerator has homogeneity one while volume has higher homogeneity, so the exact formulation and degenerating geometry are different and are not claimed here.

The admissible class allows arbitrary measurable positive-area subsets. The theorem does not impose additional constraints such as fixed topology, prescribed inradius, connected complement, or a lower bound on area. Under such constraints an attained optimization problem may reappear.

The originality search was targeted rather than exhaustive. The 2021 source itself reported no related reference for this replacement-functional question, but older literature may formulate an equivalent fact under different terminology.

## References

A. Cañete, “Cheeger Sets for Rotationally Symmetric Planar Convex Bodies,” Results in Mathematics 77 (2022), article 9, published online 2021-11-06, DOI 10.1007/s00025-021-01539-7.

I. Ftouhi, A. L. Masiello, and G. Paoli, “Sharp inequalities involving the Cheeger constant of planar convex sets,” arXiv:2206.13158, first submitted 2022-06-27; ESAIM: Control, Optimisation and Calculus of Variations 30 (2024), article 23.

H. T. Croft, K. J. Falconer, and R. K. Guy, Unsolved Problems in Geometry, Springer, 1991, Problem A23, as cited by Cañete.
