# Sharp positional stability for aligned plank coverage of a Euclidean ball

## Finding

Let \(d\ge2\), let \(B^d\subset\mathbb R^d\) be the Euclidean unit ball, and let a finite or countable family of parallel planks have total width \(W\in(0,2)\). Choose their common unit normal as the first coordinate direction. Denote the union of their normal-coordinate traces inside \([-1,1]\) by \(E\). **Assume there is no lost normal-coordinate width:** \(|E|=W\).

Write
\[
a=W/2,\quad E_*=[-a,a],\quad
\delta=\tfrac12|E\triangle E_*|,\quad
f_d(t)=(1-t^2)^{(d-1)/2}.
\]
Then \(0\le\delta\le\min\{W,2-W\}\), and the exact **sharp positional deficit** is
\[
\boxed{
\operatorname{vol}_d(B^d\cap\{x:x_1\in E_*\})
-\operatorname{vol}_d\!\left(B^d\cap\bigcup_iP_i\right)
\ge
2\kappa_{d-1}
\left[
\int_{a-\delta/2}^{a}f_d(t)\,dt-
\int_a^{a+\delta/2}f_d(t)\,dt
\right].}
\tag{1}
\]
Here \(\kappa_{d-1}\) is the volume of the Euclidean unit \((d-1)\)-ball. The right-hand side is strictly positive for \(\delta>0\). For every \(d,W,\delta\) in the stated ranges, equality in (1) is realized by a union of three parallel planks with normal-coordinate traces
\[
\boxed{
[-a-\delta/2,-a]\ \cup\
[-a+\delta/2,a-\delta/2]\ \cup\
[a,a+\delta/2].}
\tag{2}
\]
More precisely, equality forces (2) up to null sets when \(\delta>0\). Thus (1) is the optimal possible deficit function of the symmetric-difference distance \(\delta\), not merely a small-error estimate.

The unquantified centered-plank volume optimum is recalled below solely as **prior-established background**; it is not claimed as new.

## Definitions, scope, and prior baseline

A plank is a region between two parallel hyperplanes; the width is their Euclidean separation. A common unit normal \(u\) permits a rotation to \(u=e_1\), making the \(i\)-th plank the set \(\alpha_i\le x_1\le\beta_i\). Set
\[
E=\left(\bigcup_i[\alpha_i,\beta_i]\right)\cap[-1,1],\qquad
W=\sum_i(\beta_i-\alpha_i).
\]
Countable subadditivity gives \(|E|\le W\). The hypothesis \(|E|=W\) requires that no positive width is lost to overlap or to the outside of the ball's coordinate diameter. It does not require that \(E\) be connected.

Bakaev and Polyanskii, *Optimal Partial Plank Coverings*, arXiv:2607.27483v1 (29 July 2026), Theorem 10 and its uniqueness discussion, already resolve the centered-plank optimum for arbitrary finite plank directions, hence in particular for the aligned direction class. In aligned coordinates this optimum has the elementary slice form
\[
V_{d,*}(W)=\kappa_{d-1}\int_{-W/2}^{W/2}f_d(t)\,dt
=\kappa_d I_{W^2/4}\!\left(\tfrac12,\tfrac{d+1}{2}\right).
\tag{3}
\]
Neither (3) nor the statement that the centered plank maximizes covered volume is offered as an original theorem. Formula (1), conditioned on the full utilized width and prescribing the geometric displacement \(\delta\), is the precise new mathematical claim assessed here.

This result does **not** provide a stability inequality for nonparallel planks; it does not handle overlapping or out-of-ball width losses, and it makes no claim about stability of the full theorem of Bakaev and Polyanskii.

## Proof

By exact Euclidean slicing, at height \(t\in[-1,1]\) the ball section is a \((d-1)\)-ball of radius \(\sqrt{1-t^2}\), so
\[
\operatorname{vol}_d(B^d\cap\{x:x_1\in F\})
=\kappa_{d-1}\int_F f_d(t)\,dt
\tag{4}
\]
for every measurable \(F\subset[-1,1]\). In particular, the covered-volume deficit for \(E\) is
\[
\frac{D(E)}{\kappa_{d-1}}
=\int_{E_*\setminus E}f_d(t)\,dt
-\int_{E\setminus E_*}f_d(t)\,dt.
\tag{5}
\]
Since \(|E|=|E_*|=W\), both \(A=E_*\setminus E\) and \(C=E\setminus E_*\) have measure exactly \(\delta\). The available interior measure is \(W\), while the available exterior measure in \([-1,1]\) is \(2-W\); consequently \(\delta\le\min\{W,2-W\}\).

The density \(f_d\) is even and strictly decreases as \(|t|\) increases from \(0\) to \(1\). Among all measurable subsets \(A\subset[-a,a]\) of measure \(\delta\), its integral is therefore **minimized** by selecting points with the largest \(|t|\), namely
\[
A_*=[-a,-a+\delta/2]\cup[a-\delta/2,a].
\tag{6}
\]
Indeed, exchange of any positive-measure portion of \(A\) closer to the origin with an equal-measure portion of its complement farther from the origin can only reduce the integral; strict radial monotonicity gives uniqueness up to null sets. This is the elementary layer-cake (bathtub) rearrangement principle.

Similarly, among all measurable \(C\subset[-1,-a)\cup(a,1]\) of measure \(\delta\), the integral of \(f_d\) is **maximized** by its two immediately adjacent exterior layers,
\[
C_*=[-a-\delta/2,-a]\cup[a,a+\delta/2].
\tag{7}
\]
Substituting the extremal integrals of (6) and (7) into (5) gives exactly (1). The domain restrictions ensure all four layers lie in \([-1,1]\). Taking \(E=(E_*\setminus A_*)\cup C_*\) yields the union (2), has measure \(W\), and achieves equality simultaneously in both exchanges. These three intervals are genuine plank traces, so the lower bound is sharp **within the actual family of parallel planks**, not merely for abstract measurable sets.

If \(\delta>0\), every interior point of the removed layers has \(|t|<\) the corresponding exterior-layer point (up to endpoints), and \(f_d\) is strictly decreasing in \(|t|\). Thus the deficit is positive and the layer-exchange equality pattern is unique modulo null sets. The case \(\delta=0\) gives \(D(E)=0\), as required.

## Why this precise fact matters

The classical and now settled ball plank optimum specifies the maximizing covered volume but does not quantify how much covered volume must be forfeited when an *aligned*, full-utilization configuration fails to occupy the optimal centered trace. Formula (1) supplies the exact answer as a function of a natural \(L^1\)-symmetric-difference distance, including all dimensions and all finite displacements. It distinguishes geometric misplacement from the additional, separate phenomena of overlap, width wasted outside the ball, and changes of plank direction. It also gives explicit sharp configurations, not only an inequality with unspecified constants.

## Verification and limitations

Equation (4) follows from Fubini and the ball cross-section formula; (5)--(7) prove the global bound and sharpness without recourse to numerical experiments. The original accompanying `verify.py` provides diagnostic slice and boundary-layer integral tests in dimensions \(2\)–\(10\), but finite tests do not prove the all-dimensional theorem. A further direct independent numerical equality check may corroborate (1), without changing its proof.

The sharp profile is an instance of the general one-dimensional bathtub rearrangement method specialized to the geometric plank parameter. Its originality is therefore **best-of-knowledge**: an identical sharp positional form may be present in classical quantitative rearrangement literature. The 2026 full partial-covering theorem covers the baseline optimizer but does not, in its inspected statement and proof, prescribe the exact symmetric-difference deficit (1). The related Bakaev–Yehudayoff plank *covering* stability problem imposes a different annular/full-coverage condition and does not state (1).

## References

1. E. Bakaev and A. Polyanskii, *Optimal Partial Plank Coverings*, arXiv:2607.27483v1, first posted 29 July 2026, Theorem 10 and the uniqueness discussion; https://arxiv.org/html/2607.27483 .
2. K. Bezdek, A. Deza and Y. Ye, *Selected Open Problems in Discrete Geometry and Optimization*, Fields Institute Communications 69 (2013), 321–336, doi:10.1007/978-3-319-00200-2_18.
3. E. Bakaev and A. Yehudayoff, *Volume stability of plank covers*, arXiv:2609.30409v2 (8 October 2026). Its covering-stability geometry is distinct from the aligned partial-volume displacement profile above.
