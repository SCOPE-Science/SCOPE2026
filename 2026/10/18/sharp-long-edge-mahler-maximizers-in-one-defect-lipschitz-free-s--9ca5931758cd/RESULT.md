# Sharp long-edge Mahler maximizers in one-defect Lipschitz-free spaces

## Finding

For an integer \(d\ge 2\), let \(M_{d,t}\) consist of \(d+1\) points with all pairwise distances equal to \(1\), except one unordered pair \(\{a,b\}\) at distance \(t\in[1,2]\). Let \(P_{d,t}\) be the unit ball of the real Lipschitz-free Banach space \(\mathcal F(M_{d,t})\), represented in evaluation/molecule coordinates relative to any basepoint, and let \(Q_{d,t}=P_{d,t}^{\circ}\) be its polar, the dual Lipschitz unit ball. Set \(C_d=\binom{2d}{d}\). Their exact coordinate volumes are

\[
\operatorname{vol}_d(P_{d,t})=\frac{C_d-2^d(1-t^{-1})}{d!},\qquad
\operatorname{vol}_d(Q_{d,t})=d+1+\frac2d\bigl[1-(2-t)^d\bigr].
\]

Consequently the affine-invariant Mahler product equals

\[
\mathcal P_d(t)=\frac{\bigl[C_d-2^d(1-t^{-1})\bigr]\bigl[d+1+\frac2d(1-(2-t)^d)\bigr]}{d!}.
\]

For \(d=2\), \(\mathcal P_2(t)=(t+2)(4-t)\), which is strictly decreasing for \(1<t\le2\). In contrast, for **every integer \(d\ge3\)**, the product is strictly increasing up to a **unique maximizer** \(t_d\in(1,2)\), and strictly decreasing thereafter. In particular the equilateral member \(t=1\) is a strict endpoint local minimum along the long-edge deformation. Put \(a_d=C_d-2^d\), \(b_d=2^d\), and

\[
F_d(t)=2(2-t)^{d-1}\bigl(a_dt^2+b_dt\bigr)
-b_d\left[d+1+\frac2d\bigl(1-(2-t)^d\bigr)\right].
\]

The maximizer is characterized by the single equation \(F_d(t_d)=0\) on \((1,2)\). Moreover

\[
\lim_{d\to\infty}t_d=\frac32,\qquad
\frac{\mathcal P_d(t_d)}{\mathcal P_d(1)}
=1+\frac{2}{d(d+1)}+o(d^{-2}).
\]

This is an extremal theorem *within this one-exceptional-distance family*, not a statement that these metric spaces maximize the product among all metrics on the same number of points.

## Assumptions and scope

The field is real. The range \(1\le t\le2\) is exactly the long-edge metric interval; at \(t=2\) a triangle inequality becomes an equality, while for \(t<2\) all triangle inequalities are strict. Write \(e_0=0\) and \(e_1,\dots,e_d\) for the coordinate unit vectors corresponding to non-basepoint evaluations. The molecules are \((e_i-e_j)/d(i,j)\); their convex hull is \(P_{d,t}\). The polar is determined by inequalities \(|f_i-f_j|\le d(i,j)\), with \(f_0=0\). The displayed volumes use the mutually dual anchored coordinate Lebesgue measures, so their product is independent of the chosen basepoint.

## Proof

**Step 1: The equilateral reference volume.** For the equilateral metric, a vector \(x=(x_1,\ldots,x_d)\) represents a signed mass with mass \(-\sum_i x_i\) at the basepoint. Its transportation norm is \(\max\{\sum_i(x_i)_+,\sum_i(-x_i)_+\}\). In a coordinate orthant with \(k\) positive entries, the unit-ball region is the product of standard simplices of dimensions \(k\) and \(d-k\), hence has volume \(1/[k!(d-k)!]\). Summing the \(\binom dk\) orthants and invoking Vandermonde's identity yields

\[
\operatorname{vol}_d(P_{d,1})=
\sum_{k=0}^d\frac{\binom dk}{k!(d-k)!}
=\frac1{d!}\sum_{k=0}^d\binom dk^2
=\frac{C_d}{d!}.
\]

**Step 2: The two changed pyramids.** For the remaining coordinate computations, choose the basepoint to be one of the core vertices outside the exceptional pair; changes of basepoint act by unimodular transformations. Let \(K\) be the convex hull of all unit-distance molecules except those associated with the distinguished pair \(\{a,b\}\), and set \(v=e_a-e_b\). The deleted-edge graph is the complete graph on \(d+1\) vertices with one edge removed. A vertex of \(K^\circ\) has \(d\) independent tight difference constraints supported on a spanning tree, and hence takes integer values modulo the basepoint because all remaining edge lengths equal \(1\). Every core point \(c\notin\{a,b\}\) connects \(a\) to \(b\) by two unit edges, so \(|f_a-f_b|\le2\). If \(f_a-f_b=2\), the tight inequalities force \(f_a=1+f_c\), \(f_b=-1+f_c\), and the values of all core points coincide; there is exactly one such anchored potential. The case \(f_a-f_b=-2\) is its negative. Thus only two opposite supporting facets of \(K\) are exposed beyond the threshold \(\pm(f_a-f_b)=1\).

For the positive facet, the unique supporting potential is \(f^*\) with \(f^*_a=1\), \(f^*_b=-1\), and \(f^*_c=0\) for every other point. The facet is

\[
F_+=\operatorname{conv}\{e_a-e_c,\ e_c-e_b:\ c\notin\{a,b\}\}
=\frac v2+\operatorname{conv}\{\pm h_c:c\notin\{a,b\}\},
\quad h_c=\frac{e_a+e_b}{2}-e_c.
\]

The \(d-1\) vectors \(h_c\) are independent and \(|\det(h_{c_1},\ldots,h_{c_{d-1}},v)|=1\), regardless of which point is anchored. Indeed, if a core point is anchored the change to the basis consisting of the pair difference, the anchored-core mean, and differences of other core vertices is unimodular; if an endpoint is anchored the same determinant follows by an integral change of anchoring. The facet is therefore an affine cross-polytope, and adjoining the apex \(v/t\) adds one pyramid of volume

\[
\frac{2^{d-1}}{d!}\left(\frac1t-\frac12\right).
\]

Both opposite facets contribute, and there are no other new visible facets. At \(t=1\) the original root polytope consists of \(K\) plus precisely these two pyramids. Replacing their apices by \(\pm v/t\) thus subtracts exactly \(2^d(1-t^{-1})/d!\) from the equilateral volume. The argument also applies at \(t=2\) by continuity, when the apices lie on the supporting hyperplanes.

**Step 3: Exact polar volume.** Choose the basepoint at a core vertex. For \(d\ge3\), the \(r=d-1\) core vertices (including the basepoint) have range \(R\in[0,1]\). In their \(r-1\) free coordinates, the measure of configurations whose range does not exceed \(s\in[0,1]\) is \(r s^{r-1}\); differentiation gives \(r(r-1)R^{r-2}\,dR\). For a fixed core configuration of range \(R\), the two exceptional values \(f_a,f_b\) lie in a common interval of length \(L=2-R\). Restricting their difference to \(|f_a-f_b|\le t\) leaves area

\[
L^2-(L-t)_+^2.
\]

The uncut area integral is

\[
r(r-1)\int_0^1R^{r-2}(2-R)^2\,dR=d+1+\frac2d.
\]

Writing \(x=2-t\in[0,1]\), the removed area is the beta integral

\[
r(r-1)\int_0^xR^{r-2}(x-R)^2\,dR
=\frac2d x^d,
\]

proving the polar-volume formula. For \(d=2\), the sole core point is the basepoint and the polar is simply \(\{(u,v)\in[-1,1]^2:|u-v|\le t\}\), with area \(4-(2-t)^2\), the same formula.

**Step 4: Uniqueness of the maximizer.** Put \(a=C_d-2^d>0\), \(b=2^d\), \(x=2-t\), \(g(t)=at^2+bt\), and \(B(t)=d+1+\frac2d(1-x^d)\). Direct differentiation yields

\[
d!\,t^2\mathcal P_d'(t)=F_d(t)=2x^{d-1}g(t)-bB(t).
\]

If \(d\ge3\), then for \(1\le t<2\), \(xg'(t)\le2g(t)\) and

\[
F_d'(t)=2x^{d-2}\bigl[xg'(t)-(d-1)g(t)\bigr]-2b x^{d-1}<0.
\]

The strict inequality is needed only on \([1,2)\), since continuity extends strict monotonicity to the endpoint. The endpoint signs are \(F_d(1)=2C_d-2^d(d+1)>0\) and \(F_d(2)=-b[d+1+2/d]<0\). The inequality at \(t=1\) holds for every \(d\ge3\): it is immediate at \(d=3\), and induction follows from \(C_{d+1}/C_d=2(2d+1)/(d+1)>2(d+2)/(d+1)\) for \(d\ge2\). Therefore there is exactly one zero and one strict interior maximum. For \(d=2\), direct simplification gives \((t+2)(4-t)\), as stated.

**Step 5: Asymptotic location and gain.** The stationarity equation at \(t_d\) reads

\[
(2-t_d)^{d-1}=\frac{2^dB(t_d)}{2[(C_d-2^d)t_d^2+2^dt_d]}.
\]

Since \(1<t_d<2\), the numerator is of order \(2^d d\) and the denominator is of order \(C_d\), uniformly in \(t_d\). As \(C_d\sim4^d/\sqrt{\pi d}\), the right-hand side is \(\Theta(d^{3/2}2^{-d})\). Taking \((d-1)\)-st roots yields \(2-t_d\to1/2\). Finally \(2^d/C_d=O(\sqrt d\,2^{-d})\) and \((2-t_d)^d\to0\); inserting these into the two exact volume factors gives

\[
\frac{\mathcal P_d(t_d)}{\mathcal P_d(1)}
=\bigl[1+O(\sqrt d\,2^{-d})\bigr]
\left[1+\frac{2}{d(d+1)}\bigl(1-(2-t_d)^d\bigr)\right]
=1+\frac2{d(d+1)}+o(d^{-2}).
\]

## Verification

The accompanying separate exact-arithmetic checker, `verify_single_long_edge.py`, reconstructs both primal and polar convex hulls from their defining molecules and Lipschitz inequalities. It obtains combinatorial hull triangulations numerically but integrates every simplex by exact rational determinants, after rationally reconstructing each dual vertex. It verifies both volume identities and their product for \(d\in\{2,3,4,5\}\) and \(t\in\{1,5/4,3/2,2\}\), 16 distinct configurations. Run with `OPENBLAS_NUM_THREADS=1 python verify_single_long_edge.py`; the expected terminal line is `EXACT_ONE_DEFECT_VOLUME_CHECKS_PASS 16 cases`. The infinite-dimensional statement rests on the analytic proof above, not on the finite computation.

## Relationship to prior work

Aliaga's characterization of extreme points of real Lipschitz-free balls over proper metric spaces supplies the canonical finite-metric molecule framework [1]; the present quantitative formula is not contained in that characterization. Alexander, Fradelizi, García-Lirola and Zvavitch study the Mahler product in these spaces and evaluate the equilateral case, while proving qualitative restrictions on globally maximizing metrics [2]. Their statements do not directly imply the exact dependence on a single exceptional distance, the unique family-wise optimizer, or its limiting location. Gordon and Petrov analyze the combinatorics of generic Lipschitz polytopes [3], not this non-generic one-edge volume deformation. Alanazi's dissertation tabulates volume products for unweighted graph metrics on three, four, and five vertices [4]; these discrete metric examples do not determine the continuous all-dimensional deformation or its asymptotic optimizer. Prior calculations of a different four-point metric with **two** exceptional pairs and of the **shortened-edge** range concern distinct parameter families; those neither imply the displayed long-edge formulas nor the \(d\ge3\) optimizer.

## Limitations

The theorem is confined to one exceptional distance and real scalars. The volume coordinates are anchored and mutually dual; separately reported volume factors are not Euclidean zero-sum volumes unless the corresponding Jacobian is inserted. The proof does not settle global Mahler extremizers among all finite metrics. Finite checks do not certify all dimensions. The bibliographic comparison cannot exclude an unindexed identical formula or equivalent one-edge computation under different terminology. Independent scientific validation has not been performed.

## References

[1] R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219 (first public 2021-02-01), especially Theorem 1 and its finite-metric specialization. Primary MSC2020: 46B20.

[2] M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first public 2019-11-24), particularly the volume-product and equilateral sections.

[3] J. Gordon and F. Petrov, *Combinatorics of the Lipschitz polytope*, arXiv:1608.06848 (2016), especially the generic root-polytope triangulation discussion.

[4] N. M. Alanazi, *On the Volume Product of the Unit Balls of Lipschitz-Free Spaces*, M.S. thesis, Kent State University (2024), Chapters 2.1--2.3, OhioLINK accession kent1729688666198301.
