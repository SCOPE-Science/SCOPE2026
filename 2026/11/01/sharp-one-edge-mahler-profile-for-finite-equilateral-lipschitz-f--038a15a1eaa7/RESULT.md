# Sharp one-edge Mahler profile for finite equilateral Lipschitz-free spaces

## Finding

Let \(N\geq3\) be an integer, and on the labeled set \(M_{N,r}=\{0,1,\ldots,N-1\}\) put
\[
d_r(1,2)=r,\qquad d_r(i,j)=1\quad(\{i,j\}\ne\{1,2\}),\qquad 0<r\leq1.
\]
Let \(\mathcal F(M_{N,r})\) be its real Lipschitz-free space, and put \(d=N-1\). In the coordinates of \(\operatorname{Lip}_0(M_{N,r})\cong\mathbb R^d\) obtained by fixing \(f(0)=0\), denote its dual unit ball by \(P_{N,r}\) and the free-space unit ball by \(Q_{N,r}=P_{N,r}^{\circ}\). Define
\[
B_N=\frac{2}{(N-1)!}\binom{2N-4}{N-2}.
\]
With coordinate Lebesgue volume in these dual bases, **both volumes are exact**:
\[
\operatorname{vol}_d(P_{N,r})=r\bigl(2(N-1)-(N-2)r\bigr),\qquad
\operatorname{vol}_d(Q_{N,r})=B_N\left(\frac1r+\frac{N-2}{N-1}\right).
\]
In particular, the affine-invariant Mahler volume product of this Banach-space unit ball is
\[
\boxed{\mathcal M_N(r)=B_N\left(2(N-1)+(N-2)r-\frac{(N-2)^2}{N-1}r^2\right).}
\]
For every \(N\ge4\), the function is strictly increasing up to the **unique** maximum at
\[
\boxed{r_N^*=\frac{N-1}{2(N-2)}\in(0,1)}
\]
and strictly decreasing thereafter. The maximum compared with the equilateral metric is
\[
\boxed{\frac{\mathcal M_N(r_N^*)}{\mathcal M_N(1)}=\frac{9(N-1)^2}{4N(2N-3)}>1.}
\]
Consequently, \(r_N^*\to1/2\), and the ratio tends to \(9/8\) as \(N\to\infty\). For \(N=3\), the unique maximum on \(0<r\le1\) occurs at \(r=1\).

## Assumptions and scope

All distances are positive, and the metric triangle inequalities hold for \(0<r\le1\). Let \(e_0=0\) and \(e_i\), \(1\le i\le N-1\), be the standard coordinate vectors in the primal space paired with \(f(0)=0\). The two polars are explicitly
\[
\begin{aligned}
P_{N,r}&=\{f: f(0)=0,\ \max_i f(i)-\min_i f(i)\le1,\ |f(1)-f(2)|\le r\},\\
Q_{N,r}&=\operatorname{conv}\left\{\pm\frac{e_i-e_j}{d_r(i,j)}:0\le i<j\le N-1\right\}.
\end{aligned}
\]
The first description uses the fact that all nonexceptional pairwise bounds equal \(1\). In fact the inequalities \(|f(i)-f(j)|\le1\) for all nonexceptional pairs together with \(|f(1)-f(2)|\le r\le1\) are equivalent to the range bound \(\max f-\min f\le1\) and the exceptional bound. The volume product is independent of the coordinate origin and of the chosen dual bases. **Only the shortening interval** is optimized; no assertion is made about a general weighted complete metric or the extension \(1<r\le2\).

## Proof

**1. Exact volume of the Lipschitz ball.** First consider \(P_{N,1}\). Partition its interior into chambers indexed by the \(N!\) strict total orderings of the \(N\) values \(f(0),\dots,f(N-1)\). In a fixed ordering, the \(N-1\) successive gaps \(g_j\) are nonnegative and have total at most \(1\). Once \(f(0)=0\) is imposed, the coordinate map from the gaps has determinant \(\pm1\), so each chamber is a simplex of volume \(1/(N-1)!\). In particular, \(\operatorname{vol}_d(P_{N,1})=N\).

If the ranks of the distinguished labels \(1,2\) differ by \(s\), then their absolute potential difference is the sum of exactly \(s\) successive gaps. The slack variable \(1-\sum_jg_j\), together with the \(N-1\) gaps, is uniformly distributed on the standard \(N\)-coordinate simplex; hence this sum has the beta distribution with integer parameters \((s,N-s)\). Its distribution function is
\[
I_r(s,N-s)=\sum_{j=s}^{N-1}\binom{N-1}{j}r^j(1-r)^{N-1-j}.
\]
There are \(2(N-s)(N-2)!\) orderings with that rank gap. Therefore the *unnormalized* volume remaining after imposing \(|f(1)-f(2)|\le r\) is
\[
V_N(r)=\frac{2}{N-1}\sum_{s=1}^{N-1}(N-s)I_r(s,N-s).
\]
Differentiating the integer-beta polynomials, and setting \(j=s-1\), gives
\[
\begin{aligned}
V_N'(r)&=2\sum_{j=0}^{N-2}(N-1-j)\binom{N-2}{j}
 r^j(1-r)^{N-2-j}\\
&=2\bigl((N-1)-(N-2)r\bigr).
\end{aligned}
\]
The last identity is the zeroth and first moment identity of the binomial distribution. Since \(V_N(0)=0\), integration yields
\[
V_N(r)=2(N-1)r-(N-2)r^2.
\]
This argument includes \(r=1\) by continuity and uses ordinary \(d\)-dimensional Lebesgue volume, not a probability-normalized volume.

**2. Facet pyramids of the root polytope.** Put \(R_N=Q_{N,1}\), the type-\(A_{N-1}\) root polytope. Its facets are indexed by nonempty proper subsets \(S\subset\{0,\dots,N-1\}\). The facet corresponding to \(S\) is
\[
F_S=\operatorname{conv}\{e_i-e_j:i\in S,\ j\notin S\},
\]
exposed by the potential \(\mathbf1_S\) modulo constants. If \(|S|=k\), it is affinely a product \(\Delta_{k-1}\times\Delta_{N-k-1}\). Its staircase triangulation has \(\binom{N-2}{k-1}\) top-dimensional simplices. Coning each simplex to the origin gives a simplex whose other \(N-1\) vertices are a reduced signed incidence basis of a spanning tree, hence have determinant of absolute value \(1\). Thus
\[
\operatorname{vol}_d\bigl(\operatorname{conv}(0,F_S)\bigr)
=\frac{1}{(N-1)!}\binom{N-2}{k-1}.
\]
The facet cones partition \(R_N\) up to boundaries. Summation and Vandermonde's identity give
\[
\operatorname{vol}_d(R_N)
=\frac{1}{(N-1)!}\sum_{k=1}^{N-1}\binom Nk\binom{N-2}{k-1}
=\frac{1}{(N-1)!}\binom{2N-2}{N-1}.
\]

**3. Stretching exactly one antipodal root pair.** For \(0<r<1\), \(Q_{N,r}\) arises from \(R_N\) by adjoining the two points \(\pm(e_1-e_2)/r\). The positive point lies beyond precisely those facets \(F_S\) with \(1\in S\) and \(2\notin S\); on each such facet its exposing functional takes value \(1/r>1\), and on all other facets it takes a value at most \(1\). The added region is the disjoint-interior union of the pyramids from that point to these visible facets. The height ratio over the corresponding origin-cone is exactly \(1/r-1\).

There are \(\binom{N-2}{k-1}\) visible facets of size \(k\). Accordingly the added volume at the positive tip is
\[
\frac{1/r-1}{(N-1)!}\sum_{k=1}^{N-1}\binom{N-2}{k-1}^{\!2}
=\frac{1/r-1}{(N-1)!}\binom{2N-4}{N-2}.
\]
The negative tip adds the same amount. The two added caps have disjoint interiors: the positive visible faces and tip lie in the halfspace where the coordinate functional \(x\mapsto x_1-x_2\) is nonnegative, while the negative cap lies in the opposite halfspace. (For a base-point convention \(e_0=0\), this functional is well defined.) The convex hull of \(R_N\) and both tips is the union of the two one-tip hulls, because the segment between the tips contains the origin. Consequently no hidden mixed-volume term appears.

It follows that
\[
\operatorname{vol}_d(Q_{N,r})
=\frac{\binom{2N-2}{N-1}+2(1/r-1)\binom{2N-4}{N-2}}{(N-1)!}
=B_N\left(\frac1r+\frac{N-2}{N-1}\right).
\]

**4. The optimizer.** Multiplying the polar volumes gives the stated quadratic polynomial. Its derivative is
\[
\mathcal M_N'(r)=B_N(N-2)\left(1-\frac{2(N-2)}{N-1}r\right),
\]
with strictly negative second derivative for \(N\ge3\). For \(N=3\), the unique stationary point is \(r=1\). For \(N\ge4\), it lies at \(r_N^*\in(0,1)\), and is the unique maximum. Substitution gives
\[
\mathcal M_N(r_N^*)=\frac94(N-1)B_N,
\qquad
\mathcal M_N(1)=\frac{N}{(N-1)!}\binom{2N-2}{N-1},
\]
whose ratio and limits are exactly those in the finding.

## Verification

The standalone `volume_checker.py` independently evaluates the order-chamber/beta-binomial sums and the root-facet/Vandermonde sums using exact rational arithmetic, without substituting the closed volume formulas during the summations. It checks \(3\le N\le40\) at six rational shortening lengths, and checks the maximizing point and ratio for \(4\le N\le40\). With NumPy and SciPy it also constructs both actual polytopes by independent halfspace-intersection and convex-hull algorithms and checks their volumes at \(N=3,4,5,6,7\) and three parameter values. The executed check printed:

`CHECK_OK exact_volume_identities=567 independently_computed_convex_hull_volumes=30 parameter_N=3..40`

The finite checks are diagnostic only; the all-parameter result is established by the chamber integration and facet-pyramid proof.

## Relationship to prior work

Alexander, Fradelizi, García-Lirola, and Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces* (arXiv:1911.10642, first public 2019-11-24), introduced and studied this Banach-space Mahler product, evaluated the undeformed equilateral benchmark in their §5.2, and showed that for at least four metric points the equilateral metric is not a global maximum. Their Lemma 5.4 also contains the general visible-facet cap-volume principle, which is used here with an explicitly evaluated facet count. Their findings do not provide the exact one-edge polar volumes, the unique shortening optimizer, or the limiting enhancement \(9/8\). The present formula quantitatively refines **that particular** nonmaximality phenomenon, without claiming a global optimizer over all finite metrics.

Gordon and Petrov, *Combinatorics of the Lipschitz polytope* (arXiv:1608.06848), relate the face structure to root-polytope triangulations, but not the one-edge Mahler-volume profile. Çelik, Jamneshan, Montúfar, Sturmfels, and Venturello, *Wasserstein Distance to Independence Models* (arXiv:2003.06725), treat polyhedral Wasserstein norms and describe discrete-metric Lipschitz polytopes, not a varying single distance and its volume product. A published study of equilateral metrics with independently shortened disjoint pairs determines **facet counts and extremal potentials**, not the volumes or the optimizer of their Mahler product. These comparisons distinguish implication and object, rather than relying on differences in titles.

## Limitations

The optimizing statement is **only** among \(0<r\le1\) in the given one-edge shortening family, and the formula does not determine volume products for two or more independently shortened pairs. No general Mahler minimum/maximum theorem is asserted. The limiting value as \(r\downarrow0\) concerns a degenerating metric and is not included in the parameter domain. Earlier equivalences phrased solely in root-polytope deformation language remain a possible priority risk; no claim of exhaustive literature coverage or independent external validation is made.

## References

1. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first public 2019-11-24), https://arxiv.org/abs/1911.10642.
2. J. Gordon and F. Petrov, *Combinatorics of the Lipschitz polytope*, arXiv:1608.06848 (first public 2016-08-24), https://arxiv.org/abs/1608.06848.
3. T. Ö. Çelik, A. Jamneshan, G. Montúfar, B. Sturmfels, L. Venturello, *Wasserstein Distance to Independence Models*, arXiv:2003.06725 (first public 2020-03-15), https://arxiv.org/abs/2003.06725.
4. *Facet enumeration for equilateral metrics with independently shortened pairs*, published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-facet-enumeration-for-equilateral-metrics-with-independently-sho--3bd6d7048744.
