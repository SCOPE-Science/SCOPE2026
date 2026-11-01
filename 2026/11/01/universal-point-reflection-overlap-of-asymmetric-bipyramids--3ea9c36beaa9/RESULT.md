# Universal point-reflection overlap of asymmetric bipyramids

## Finding

**Theorem (shape-independent central-symmetry profile).** Fix an integer \(m\ge1\), a compact convex body \(B\subset\mathbb R^m\) with nonempty interior and \(B=-B\), a height \(h>0\), and \(0\le t\le1\). In \(\mathbb R^{m+1}\) form
\[
K_{B,h,t}=\operatorname{conv}\bigl((B\times\{0\})\cup\{(0,h),(0,-th)\}\bigr).
\]
For every convex body \(K\), define its maximal centrally symmetric volume ratio by
\[
\mathcal C(K)=\max_{z\in\mathbb R^{m+1}}
\frac{\operatorname{vol}_{m+1}(K\cap(2z-K))}{\operatorname{vol}_{m+1}(K)}.
\]
Set \(\alpha_m=2^{1/m}\) and \(D_m(t)=t+2\alpha_m-1\). Then
\[
\boxed{\mathcal C(K_{B,h,t})=2\left(\frac{1+t}{D_m(t)}\right)^m.}
\]
The maximizing reflection center is unique and equals
\[
\boxed{z_*=(0,\ldots,0,hc_*(t)),\qquad
c_*(t)=\frac{(1-t)(\alpha_m-1)}{D_m(t)}.}
\]
The ratio depends only on \(m\) and the two apex heights, not on the geometry of \(B\). It increases strictly with \(t\), and its exact attainable range is
\[
\boxed{\frac{2}{(2\alpha_m-1)^m}\le\mathcal C(K_{B,h,t})\le1.}
\]
The lower equality case is exactly the one-sided cone \(t=0\); the upper case is exactly the centrally symmetric double cone \(t=1\). Accordingly, an exact symmetry-ratio measurement identifies the apex-height ratio: with \(q=(\mathcal C(K_{B,h,t})/2)^{1/m}\),
\[
\boxed{t=\frac{(2\alpha_m-1)q-1}{1-q}.}
\]
For fixed \(m\), this inverse is Lipschitz on its entire attainable interval. In the high-dimensional limit at each fixed \(t\),
\[
\lim_{m\to\infty}\mathcal C(K_{B,h,t})=2^{(t-1)/(t+1)}.
\]

**Centroid comparison.** The centroid of \(K_{B,h,t}\) lies on the apex axis at normalized height \((1-t)/(m+2)\). Its displacement above the maximizing symmetry center is exactly
\[
\frac{1-t}{m+2}-c_*(t)
=\frac{(1-t)(t+m+1-m\alpha_m)}{(m+2)D_m(t)}\ge0.
\]
For \(t<1\), equality occurs only when \(m=1\) and \(t=0\). Thus, except for the triangular endpoint, the best symmetry center lies strictly closer to the equator than the centroid of an asymmetric bipyramid.

## Assumptions and scope

All volumes are ordinary Lebesgue volumes. The base \(B\) must be centrally symmetric about the common vertical projection of the apices, but need not be smooth, ellipsoidal, strictly convex, or polytopal. The equator is full dimensional within its hyperplane. Both parameters \(m\) and \(t\) are arbitrary in their stated ranges; the case \(t=0\) remains a full-dimensional cone. No claim is made for apices whose horizontal projections differ or for a base that is not centrally symmetric.

The ratio \(\mathcal C\) is the volume of the largest centrally symmetric convex subset divided by the body's volume. Indeed, if \(S\subseteq K\) is centrally symmetric about \(z\), then \(S\subseteq K\cap(2z-K)\), and the latter intersection is itself centrally symmetric about \(z\). The corresponding planar invariant is the Kovner–Besicovitch measure.

## Proof

**1. Reduction to axial centers.** Scale the last coordinate so that \(h=1\), and write \(v=\operatorname{vol}_m(B)>0\). For \(t>0\), the horizontal section at height \(y\) is \(f_t(y)B\), where
\[
f_t(y)=\begin{cases}
1+y/t,&-t\le y\le0,\\
1-y,&0\le y\le1,\\
0,&\text{otherwise.}
\end{cases}
\]
For \(t=0\), retain only the branch \(0\le y\le1\). The total volume is
\[
\operatorname{vol}_{m+1}(K_{B,1,t})=\frac{v(1+t)}{m+1}.
\]
Fix a putative center \(z=(u,c)\) with \(u\in\mathbb R^m\). Its reflected intersection has horizontal section
\[
f_t(y)B\ \cap\ \bigl(2u+f_t(2c-y)B\bigr).
\]
For any \(p,q\ge0\), the intersection of \(pB\) with a translate of \(qB\) has no larger volume than \(pB\cap qB\): write \(S_u=pB\cap(2u+qB)\). Central symmetry gives \(S_{-u}=-S_u\), and convexity gives \((S_u+S_{-u})/2\subseteq pB\cap qB\). The Brunn–Minkowski inequality therefore yields
\[
\operatorname{vol}_m(S_u)\le\operatorname{vol}_m(pB\cap qB).
\]
Integrating over \(y\) shows that at each fixed axial coordinate \(c\), the best horizontal choice is \(u=0\). If \(c\) is in the interior of the height interval and \(u\ne0\), the inequality is strict at \(y=c\): then both slices equal \(f_t(c)B\) with positive scale, whereas two nontrivially translated copies of the same bounded convex body cannot overlap in their entire volume. Continuity makes the integrated inequality strict. It suffices to maximize the one-dimensional profile
\[
H_t(c)=v\int_{\mathbb R}\min\{f_t(y),f_t(2c-y)\}^m\,dy.
\]
Centers outside the height interval have zero overlap.

**2. Exact axial overlap.** Assume first \(0<t<1\), and put \(c_0=(1-t)/2\). Symmetry about height \(c\), together with the piecewise affine slice radii, gives the following three exact expressions:
\[
\frac{(m+1)H_t(c)}{2v}=
\begin{cases}
(t+c)^{m+1}/t^m,&-t\le c\le0,\\
(1-c)^{m+1}-(1-t)\bigl(1-2c/(1-t)\bigr)^{m+1},&0\le c\le c_0,\\
(1-c)^{m+1},&c_0\le c\le1.
\end{cases}
\]
To verify the middle expression without any appeal to numerical integration, let \(y_*=-2ct/(1-t)\). On the lower half of the symmetric height pair, the smaller section radius is \(1+y/t\) for \(-t\le y\le y_*\), then \(1-2c+y\) for \(y_*\le y\le c\). Thus its volume is exactly
\[
H_t(c)=2v\left[\int_{-t}^{y_*}(1+y/t)^m\,dy+
\int_{y_*}^{c}(1-2c+y)^m\,dy\right],
\]
which simplifies to the displayed middle branch. The other two branches follow by integrating respectively the lower or upper linear cone profile over the symmetric half-interval. The pieces agree at \(c=0\) and \(c=c_0\).

The first branch is strictly increasing and the third is strictly decreasing in the interior. In the middle branch,
\[
H_t'(c)=2v\left[2\bigl(1-2c/(1-t)\bigr)^m-(1-c)^m\right].
\]
The ratio \(\bigl(1-2c/(1-t)\bigr)/(1-c)\) decreases strictly from \(1\) to \(0\) on \([0,c_0]\). Hence \(H_t'\) changes sign exactly once, at the unique solution of
\[
1-c=\alpha_m\bigl(1-2c/(1-t)\bigr),
\quad\text{namely}\quad
c=c_*(t)=\frac{(1-t)(\alpha_m-1)}{D_m(t)}.
\]
This is the unique axial maximum. The matching identities
\[
1-c_*=\frac{\alpha_m(1+t)}{D_m(t)},\qquad
1-\frac{2c_*}{1-t}=\frac{1+t}{D_m(t)}
\]
give
\[
H_t(c_*)=\frac{2v}{m+1}\frac{(1+t)^{m+1}}{D_m(t)^m}.
\]
Dividing by the total volume proves the claimed formula and location for \(0<t<1\). The preceding transverse strictness proves global uniqueness.

For \(t=0\), direct integration over the single cone yields the same middle expression with \(t=0\) for \(0\le c\le1/2\), followed by the decreasing upper branch; its maximizer is \(c_*(0)\). For \(t=1\), the body is centrally symmetric, and its unique maximizing center is the origin, agreeing with \(c_*(1)=0\) and \(\mathcal C=1\). These endpoint arguments avoid divisions by zero in the three-branch formula.

**3. Monotonicity, reconstruction, limits, and centroid.** Logarithmic differentiation gives, for all \(0\le t\le1\),
\[
\frac{d}{dt}\log\mathcal C(K_{B,h,t})
=\frac{2m(\alpha_m-1)}{(1+t)D_m(t)}>0.
\]
This proves the exact range, its equality cases, and a positive minimum derivative on the compact parameter interval. Rearranging the equality \(q=(1+t)/D_m(t)\) gives the stated inverse, which is Lipschitz by the derivative bound. Since \(\alpha_m=1+(\log2)/m+O(m^{-2})\), taking logarithms yields the high-dimensional limit.

The axial centroid follows by integrating \(y f_t(y)^m\) over the two cones, obtaining \(h(1-t)/(m+2)\). Subtracting \(hc_*(t)\) proves the displacement formula. Finally, \(2^{1/m}\le1+1/m\), with equality exactly at \(m=1\), follows from \((1+1/m)^m\ge2\); the latter is strict for \(m>1\) by the binomial theorem. This proves all centroid comparison cases.

## Verification

The included `verify_bicone.py` uses only the Python standard library. It independently computes 570 exact rational one-dimensional reflection-overlap integrals by subdividing each pair of piecewise-linear radii at its crossing points, agreeing exactly with every stated branch for dimensions \(m=1,\ldots,6\). Separately it integrates genuine \((m+1)\)-dimensional overlap sections for cubical equators, including axial and transverse perturbations, for \(m=1,\ldots,5\). It also tests the inverse formula at endpoint and interior samples. Executing `python verify_bicone.py` prints `ALL_CHECKS_PASSED`. The proof above, rather than these finite checks, establishes the universal statements for all dimensions and every centrally symmetric base.

## Relationship to prior work

Stein's 1956 theorem already proves uniqueness of the maximal reflection center for *every* convex body; only its **explicit location for this family** is claimed here. Stein also establishes the symmetry ratio of simplices, which includes the triangular \(m=1,t=0\) endpoint. Chakerian and Stein (1965) study the same general central-symmetry volume invariant and dimension-dependent lower bounds. The later work of Huang, Slomka, Tkocz and Vritsiou (first public version November 30, 2018) studies maximal overlaps with reflected translates in connection with Hadwiger's covering problem; it does not give this shape-independent bicone profile. Goenka, Moore, Sun and White (2023) discuss the central measure as context while investigating a different invariant, axial symmetry. Chan and Hair (2025) give a general planar overlap algorithm, not an all-dimensional symbolic formula. The contribution here is the unrestricted centrally symmetric equator, both apex heights, exact dimension-dependent ratio, explicit maximizing location, invertible profile, and limiting behavior. Classical universal uniqueness and triangular facts are not presented as new.

## Limitations

Historical priority remains provisional: although relevant primary works and records were compared, unindexed or specialized older treatments of bipyramids may contain equivalent formulas. The theorem assumes exactly symmetric equators and vertically aligned apices, and does not identify a general body's symmetry center. Exact population geometric volumes, not noisy measurements, underlie the inverse statement. Lipschitz inversion is dimensionwise; no dimension-uniform inverse condition number is asserted. The high-dimensional statement holds for each fixed \(t\), and does not characterize regimes in which \(t\) varies with dimension.

## References

1. S. K. Stein, *The Symmetry Function in a Convex Body*, Pacific Journal of Mathematics **6** (1956), 145–148. https://doi.org/10.2140/pjm.1956.6.145.
2. G. D. Chakerian and S. K. Stein, *On Measures of Symmetry of Convex Bodies*, Canadian Journal of Mathematics **17** (1965), 497–504. https://doi.org/10.4153/CJM-1965-049-3.
3. H. Huang, B. A. Slomka, T. Tkocz and B.-H. Vritsiou, *Improved bounds for Hadwiger's covering problem via thin-shell estimates*, first public arXiv version dated November 30, 2018, https://arxiv.org/abs/1811.12548.
4. R. Goenka, K. Moore, W. R. Sun and E. P. White, *On Axial Symmetry in Convex Bodies*, first public arXiv version dated September 22, 2023, https://arxiv.org/abs/2309.12597.
5. T. M. Chan and I. M. Hair, *A Linear Time Algorithm for the Maximum Overlap of Two Convex Polygons Under Translation*, SoCG 2025, https://doi.org/10.4230/LIPIcs.SoCG.2025.31.
