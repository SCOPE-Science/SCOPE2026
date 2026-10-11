# Sharp radial-retraction Lipschitz profile of the real Lorentz-predual octagonal planes
## Finding
For every \(0<w<1\), let \(X_w=(\mathbb R^2,N_w)\) be the real Banach plane with
\[
N_w(u,v)=\max\!\left\{|u|,|v|,\frac{|u|+|v|}{1+w}\right\}.
\]
For \(r>0\), define its radial retraction onto the closed radius-\(r\) ball by
\[
R_{w,r}(x)=\frac{x}{\max\{1,N_w(x)/r\}}.
\]
Then the *optimal global Lipschitz constant* in the norm \(N_w\), independent of \(r>0\), is
\[
\operatorname{Lip}(R_{w,r})=k(X_w)
=\max\left\{1+w^2,\frac{2(1+w^2)}{(1+w)^2}\right\}
=\begin{cases}
\dfrac{2(1+w^2)}{(1+w)^2},&0<w\le\sqrt2-1,\\[3pt]
1+w^2,&\sqrt2-1\le w<1.
\end{cases}
\]
The profile has exactly one minimizer, \(w=\sqrt2-1\), the regular-octagonal member, where
\[
\min_{0<w<1}k(X_w)=4-2\sqrt2.
\]
Thus the universal radial bound \(2\) improves strictly for every \(0<w<1\), while the constant tends to \(2\) at both endpoints. Sharpness on each branch is witnessed by exterior derivatives approaching one of the two kinds of octagonal vertices, with common extremal input direction \((-w,1)\).

## Assumptions and scope
All spaces and vectors are real. Fix \(0<w<1\), write \(a=1+w\), and let \(B_w=\{x:N_w(x)\le1\}\). Its eight vertices, counted with signs and coordinate exchange, are
\[
(\pm1,\pm w),\qquad(\pm w,\pm1).
\]
All these sign combinations are independent. The radial map \(R_{w,r}\) is defined on the entire plane, equals the identity on the radius-\(r\) ball, and takes values in that ball. By \(R_{w,r}(x)=rR_{w,1}(x/r)\), its Lipschitz constant is independent of \(r>0\). Thus set \(r=1\) and write \(R_w\).

## Proof
**1. Global-to-local reduction.** The norm is the maximum of finitely many linear functionals (the signed coordinate functionals and signed diagonal functionals). If \(N_w(x)>1\) and one functional \(f\) is uniquely active, then \(N_w(x)=f(x)\) in an open neighborhood and
\[
DR_w(x)h=\frac1{N_w(x)}\left[h-R_w(x)f(h)\right].
\]
Writing \(z=R_w(x)\in\partial B_w\), the local derivative has operator norm
\[
\|DR_w(x)\|_{N_w\to N_w}
=\frac{\|I-z\otimes f\|_{N_w\to N_w}}{N_w(x)}
\le\|I-z\otimes f\|_{N_w\to N_w}.
\]
The map is the identity inside the unit ball, with local Lipschitz constant \(1\). If a polygonal edge \(E_f=\{z\in B_w:f(z)=1\}\) corresponds to the functional \(f\), then
\[
\|I-z\otimes f\|_{N_w\to N_w}
\]
is convex in \(z\), since an operator norm is convex in its operator and the operator here depends affinely on \(z\). Therefore its maximum on the edge is attained at an endpoint. Symmetry under coordinate swaps and independent signs reduces all edge endpoints to \(z=(1,w)\) with either the vertical support functional \(f_V(u,v)=u\) or the diagonal support functional \(f_D(u,v)=(u+v)/a\).

The derivative estimates give a *global* estimate. Indeed, on a generic line segment connecting any two points, \(R_w\) is continuously differentiable on finitely many subsegments separated by crossings with \(\partial B_w\) and finitely many facet-cone boundaries. Integrating the derivative on these subsegments bounds the total output displacement by the largest derivative bound times the input displacement. Nonsmooth or nongeneric segments are limits of generic ones, and continuity extends the bound. Consequently,
\[
\operatorname{Lip}(R_w)\le
\max\left\{1,\|I-z\otimes f_V\|,\|I-z\otimes f_D\|\right\},
\qquad z=(1,w).
\]

Conversely, approach \(z=(1,w)\) through the relative interiors of either incident facet, then approach that unit point from the exterior. At each such point the derivative exists with norm arbitrarily close to the corresponding endpoint operator norm. Any global Lipschitz constant must dominate every derivative norm. Thus the preceding inequality is equality.

**2. Exact facet operators.** Let \(h=(u,v)\) and \(z=(1,w)\). For the vertical facet,
\[
(I-z\otimes f_V)h=(0,v-wu),
\]
so
\[
\|I-z\otimes f_V\|=\sup_{h\in B_w}|v-wu|.
\]
The maximum of an absolute linear functional on \(B_w\) occurs at a vertex. Direct evaluation at the eight vertices gives
\[
\sup_{h\in B_w}|v-wu|
=\max\{1+w^2,2w,1-w^2,0\}=1+w^2;
\]
the final equality follows from \((1-w)^2\ge0\). The maximizing input \(h=(-w,1)\) is a unit-ball vertex.

For the diagonal facet, direct cancellation gives
\[
(I-z\otimes f_D)h
=\frac{wu-v}{a}(1,-1).
\]
As \(N_w(1,-1)=2/a\) for \(0<w<1\),
\[
\|I-z\otimes f_D\|
=\frac{2}{a^2}\sup_{h\in B_w}|v-wu|
=\frac{2(1+w^2)}{(1+w)^2}.
\]
The same unit input \(h=(-w,1)\) maximizes the latter operator norm.

Both operator norms are at least \(1\). Combining the exact lower and upper bounds proves
\[
\operatorname{Lip}(R_w)=\max\left\{1+w^2,\frac{2(1+w^2)}{(1+w)^2}\right\}.
\]

**3. Parameter transition.** The diagonal value is larger precisely when
\[
\frac{2}{(1+w)^2}\ge1
\quad\Longleftrightarrow\quad
0<w\le\sqrt2-1.
\]
The diagonal branch \(2(1+w^2)/(1+w)^2\) has derivative \(4(w-1)/(1+w)^3<0\) on \((0,1)\). The vertical branch \(1+w^2\) has derivative \(2w>0\). Hence their maximum has a unique minimum at the crossing, with value \(1+(\sqrt2-1)^2=4-2\sqrt2\). Each branch is strictly less than \(2\) away from its endpoint limit. This completes the proof.

## Verification
For the exact vertex calculation, the possible values of \(|v-wu|\) on the eight vertices are \(0\), \(1-w^2\), \(2w\), and \(1+w^2\). No numerical sampling or discretization is used to establish the operator norm. The global-to-local derivative reduction is valid for all real input pairs by integrating on line segments, so the proof concerns the global Lipschitz constant rather than merely a directional or local bound.

For independent computational spot checks, rational test values \(w=1/10,1/5,1/3,1/2,7/10,9/10\) were evaluated using exact rational arithmetic by enumerating all unit-ball vertices for both operators. Each calculation agreed with the two stated rational formulas. These finite checks corroborate but do not replace the continuous analytic proof.

The number at the unique minimizer is \(4-2\sqrt2\approx1.17157287525381\). The limiting constants as \(w\downarrow0\) (the \(\ell_1^2\) endpoint) and \(w\uparrow1\) (the \(\ell_\infty^2\) endpoint) are \(2\), matching the classical sharp universal bound.

## Relationship to prior work
De Figueiredo and Karlovitz (1967) and Thele (1974) established general radial-projection geometry; Thele's constant is the Lipschitz constant of the radial retraction and can be expressed through Birkhoff--James orthogonality. Șerb (1999) identifies it with the zero-parameter limit of the rectangular modulus. Rieffel (arXiv preprint first posted 2005) proves the universal radial-retraction bound \(k(X)\le2\) and equality on many spaces of continuous functions, noting \(k(H)=1\) for Hilbert spaces. None of the inspected complete texts gives the exact weighted octagonal profile stated here.

Christianson, Handina and Wierman (2022) use this same radial Lipschitz constant in a quantitative convex-body/function-chasing bound. Their full paper gives general theorems and does not evaluate it for the present octagonal family; the exact calculation therefore supplies a concrete, sharp norm-dependent factor for those bounds.

A separate published determination of the Euclidean Banach--Mazur distance of this octagonal family has a squared expression matching the formula proved here. That determination concerns optimal *linear* Euclidean distortion, not the sharp Lipschitz norm of this particular *nonlinear* radial retraction; neither its statement nor the standard general radial estimates supplies the required reverse sharpness for the radial map. A separate Gao-constant computation for the dual weighted Lorentz plane also yields numerically reciprocal branch expressions; it is a different invariant, and no general inverse-identity is presumed here.

## Limitations
The theorem evaluates the canonical radial retraction, not the *smallest possible* Lipschitz constant over all retractions onto the unit ball. The latter optimization is a different problem. The result applies to the real two-dimensional weighted family and does not assert an arbitrary-dimensional formula or characterize all finite pairs approaching sharpness.

The full historical articles by Thele (1974), De Figueiredo--Karlovitz (1967), and Kapoor--Mathur (1983) were not obtainable as readable original texts through the checked public routes; the accessible primary expositions of their general results were inspected instead. These historical access limitations leave a residual bibliographic possibility of earlier equivalent calculations for this particular family. The exact first-public-date field uses the verified day-level arXiv submission of the main motivating radial-retraction exposition; historical citations with year-only dating are not assigned fabricated dates.

## References
1. M. A. Rieffel, “Lipschitz extension constants equal projection constants,” arXiv:math/0508097v1, first posted 2005-08-04 (subsequent complete text arXiv:math/0508097v5), MSC 46B20 and 26A16, Section 8, Proposition 8.1.
2. I. Șerb, “Rectangular modulus, Birkhoff orthogonality and characterizations of inner product spaces,” *Commentationes Mathematicae Universitatis Carolinae* 40 (1999), 107–119, public full text https://dml.cz/dmlcz/119066, especially Theorem 6.
3. N. Christianson, T. Handina and A. Wierman, “Chasing Convex Bodies and Functions with Black-Box Advice,” *Proceedings of Machine Learning Research* 178 (2022), complete open-access paper https://proceedings.mlr.press/v178/christianson22a/christianson22a.pdf, Section 4.1 and Appendix C.
4. R. L. Thele, “Some results on the radial projection in Banach spaces,” *Proceedings of the American Mathematical Society* 42 (1974), 483–486, DOI 10.1090/S0002-9939-1974-0328550-1 (the full original was not accessible in the checked routes).
5. D. G. De Figueiredo and L. A. Karlovitz, “On the radial projection in normed spaces,” *Bulletin of the American Mathematical Society* 73 (1967), 364–368, DOI 10.1090/S0002-9904-1967-11753-1 (the full original was not accessible in the checked routes).
