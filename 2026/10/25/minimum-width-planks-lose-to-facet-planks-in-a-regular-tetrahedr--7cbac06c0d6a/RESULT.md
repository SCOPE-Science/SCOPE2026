# Minimum-width planks lose to facet planks in a regular tetrahedron: an exact crossover

## Finding
Consider the regular tetrahedron
\[
T=\operatorname{conv}\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}\subset\mathbb R^3.
\]
Its minimum Euclidean width is \(w(T)=2\), and the only minimum-width unoriented normals are the three coordinate axes. For \(0<W<2\), let \(G(W)\) be the maximum fraction of the volume of \(T\) captured by a plank of width \(W\) whose normal is a minimum-width normal, and let \(F(W)\) be the analogous maximum over normals perpendicular to a triangular facet. Then
\[
G(W)=\frac{3W}{4}-\frac{W^3}{16},\qquad
F(W)=1-\left(1-\frac{\sqrt3W}{4}\right)^3.
\]
They cross **exactly once** in \(0<W<2\), at
\[
W_*=8\sqrt3-12=1.856406460551\ldots.
\]
For every \(0<W<W_*\), \(F(W)>G(W)\). Consequently **no minimum-width normal can maximize the volume captured by one plank** in that interval: a facet-parallel plank of the same width is strictly better than every plank of minimum-width orientation, even when those planks are optimally translated. For \(W_*<W<2\), the comparison of these two symmetry-orbits reverses, but no assertion is made that either orbit is globally optimal among all directions. In particular, this is not a determination of the optimal partial-plank covering of a tetrahedron by arbitrary families.

## Assumptions and scope
A plank of Euclidean width \(W\) is the region between two parallel planes distance \(W\) apart. Its normal may be reversed without changing the plank. The optimization in \(G\) and \(F\) allows arbitrary translations of each plank along its normal. Fractions are relative to the ordinary three-dimensional volume of the nondegenerate tetrahedron \(T\), whose volume equals \(8/3\). The formulas hold exactly for every real \(0<W<2\). The facet-normal projection has height \(4/\sqrt3>2\), so the facet-adjacent width-\(W\) plank exists over this entire range.

## Proof
Write the four listed vertices as \(v_1,\ldots,v_4\). For a unit normal \(u\), put \(t_i=\langle v_i,u\rangle\). Direct calculation gives \(\sum_i t_i=0\) and \(\sum_i t_i^2=4\). Thus the variance of these four numbers is one. The elementary range--variance inequality gives
\[
1\le\frac{(\max_i t_i-\min_i t_i)^2}{4},
\]
so every directional width is at least two. Equality requires every \(t_i\) to be an endpoint of an interval of length two and both endpoints to occur equally often: the four projected vertices must have values \(+1,+1,-1,-1\), in some order. Each partition of the four vertices into two pairs determines, up to sign, one of \(e_1,e_2,e_3\). These coordinate directions indeed have width two; hence the minimum width is exactly two and the described list of normals is complete.

To calculate the captured volumes without any slicing approximation, choose a uniformly distributed point \(X\) of \(T\). Its barycentric coordinates \((\lambda_1,\ldots,\lambda_4)\) have the uniform Dirichlet law \(\operatorname{Dirichlet}(1,1,1,1)\). In the coordinate direction \(e_3\), two vertices have height \(+1\) and the other two have height \(-1\). If \(S\) is the sum of the two positive-height barycentric coordinates, then \(S\sim\operatorname{Beta}(2,2)\) and the height is \(Z=2S-1\). Its exact probability density on \([-1,1]\) is
\[
f_Z(z)=\frac34(1-z^2).
\]
This density is even and strictly decreases with \(|z|\). Sliding a width-\(W\) window toward zero strictly increases its captured probability until centered, so every maximizing coordinate-normal plank is centered. Integration gives
\[
G(W)=\int_{-W/2}^{W/2}\frac34(1-z^2)\,dz
=\frac{3W}{4}-\frac{W^3}{16}.
\]
Symmetry covers all three minimum-width axes.

For the facet normal \(u=(1,1,1)/\sqrt3\), one vertex has height \(\sqrt3\) and three have height \(-1/\sqrt3\). If \(U\) is the barycentric coordinate at the unique upper vertex, then \(U\sim\operatorname{Beta}(1,3)\) and the projected height is \((-1+4U)/\sqrt3\). Its normalized height \(U\in[0,1]\) has density \(3(1-U)^2\), strictly decreasing. A width-\(W\) plank therefore captures the greatest volume when it abuts the triangular facet at the bottom. The entire projected height is \(H=4/\sqrt3\), so
\[
F(W)=\int_0^{W/H}3(1-s)^2\,ds=1-(1-W/H)^3
=1-\left(1-\frac{\sqrt3W}{4}\right)^3.
\]
All four facet-normal orbits have the same profile by tetrahedral symmetry.

Subtracting and factoring in the exact quadratic field \(\mathbb Q(\sqrt3)\) yields
\[
F(W)-G(W)
=\frac{(4+3\sqrt3)W}{64}
\bigl(W-(8\sqrt3-12)\bigr)
\left(W-\frac{20\sqrt3-12}{11}\right).
\]
The first positive root satisfies \(0<8\sqrt3-12<2\), while the second satisfies \((20\sqrt3-12)/11>2\). Consequently the product is positive for \(0<W<W_*\), zero at \(W_*\), and negative for \(W_*<W<2\). This gives the exact crossover and, because \(G\) already optimizes every minimum-width direction and its translation, proves their global disqualification for every width below \(W_*\). It does not compare either profile with generic oblique normals or multiple-plank families.

## Verification
A standalone exact-symbolic checker, `verify.py`, independently constructs the one-dimensional densities from the beta laws, integrates over optimizing intervals, verifies the factorization, checks both root positions using exact inequalities, and checks that the explicit vertex matrix has frame operator \(4I\). It also checks the limiting normalized volume and several rational test widths. Run `python verify.py` with Python 3 and SymPy installed. The stated theorem follows analytically from the preceding derivations; symbolic calculations provide a replayable check, not a replacement for the quantifiers and optimization argument.

## Relationship to prior work
Bakaev and Polyanskii introduce optimal partial-plank volume covering, prove one-plank optimality for every planar convex body, and prove higher-dimensional simplex cases when a facet altitude equals the minimum width. Their regular-simplex discussion observes that the facet-altitude condition fails for regular simplices of dimension at least three; it does not determine the one-plank volume profiles compared here. A separate published result on the exact Minkowski-subtraction core for simplices identifies minimum-width complementary-face directions, including the pair--pair axes of a regular tetrahedron, but expressly does **not** infer which single plank captures the most volume. Likewise, a published minimum-width formula for pyramids does not compare these directional captured-volume profiles. Thus none of those statements implies that a facet-normal plank strictly dominates every minimum-width-normal plank for a nontrivial, exactly identified interval.

## Limitations
This is an exact comparison between two natural finite symmetry orbits of plank normals and an obstruction to restricting the global search to minimum-width directions. It does **not** identify the best oblique direction, prove a global one-plank optimum, or resolve optimality among arbitrary plank families in three dimensions. No independent audit has been performed. Unindexed older literature about simplex splines or tetrahedral slicing might contain equivalent formulas or their immediate consequence, although no matching statement was found in the checked sources.

## References
1. E. Bakaev and A. Polyanskii, *Optimal partial plank coverings*, arXiv:2607.27483v1, first posted 29 July 2026; especially the simplex discussion and general partial-volume problem.
2. *Bang's homothetic core is exact for every simplex*, published mathematical finding, 11 October 2026, identifier `2026/10/11/SCOPE-bang-s-homothetic-core-is-exact-for-every-simplex--b077f6e663a4`.
3. *Exact minimum-width formula for convex pyramids and a partial-plank consequence*, published mathematical finding, 4 October 2026, identifier `2026/10/4/SCOPE-exact-minimum-width-formula-for-convex-pyramids-and-a-partial-pl--5011fb3c7815`.
