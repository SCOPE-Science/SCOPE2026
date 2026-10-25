# Rare-diameter corner profiles and cyclic feasibility polytopes of odd regular polygons

## Finding
Fix an odd integer \(k=2m+1\ge5\). Let \(N\) points be independently sampled uniformly in arclength on the boundary of the regular \(k\)-gon of circumradius one, and let \(D_N\) be their largest Euclidean pairwise distance. Put \(s_k=2\cos(\pi/(2k))\) and \(Y_{k,N}=(N/k)(s_k-D_N)\). Let \(Y_k\) be the known weak limit described in Lao's Theorem 5.3. Define
\[
 g=\sin(\pi/(2k)),\quad b=\sin(3\pi/(2k)),\quad \lambda=1/\sin(\pi/k),\quad r=g/b.
\]
Let \(A_i,B_i\), \(i\in\mathbb Z/k\mathbb Z\), be independent exponential variables of rate \(\lambda\), representing the two normalized closest-to-vertex distances in their respective directed edge sectors. The limit \(Y_k\) is twice the minimum over the following \(4k\) expressions:
\[
 b(A_i+A_{i+m}),\quad b(A_i+B_{i+m}),\quad g(B_i+A_{i+m}),\quad b(B_i+B_{i+m}),\qquad i\in\mathbb Z/k\mathbb Z.
\]
Write \(S_i=B_i+A_{i+m}\) and \(U_i=B_i/S_i\). For \(j\in\mathbb Z/k\mathbb Z\), set \(V_j=U_{jm}\). The cyclic feasibility polytope is
\[
 P_k(r)=\left\{v\in[0,1]^k:\ r\le v_j+v_{j+1}\le2-r,\quad v_{j-1}-v_{j+1}\le1-r\ (j\bmod k)\right\}.
\]
It has positive volume \(p_k(r)=\operatorname{vol}_k(P_k(r))\). As \(t\to\infty\), conditional on \(Y_k>t\), the joint law of the marked corner-split vector \(V\) and the excess vector \((S_i-t/(2g))_{i=0}^{k-1}\) converges to **independent** components: \(V\) is uniformly distributed on \(P_k(r)\), and the \(k\) excesses are independent exponential random variables of rate \(\lambda\). Equivalently this is an iterated \(N\to\infty\), then \(t\to\infty\), conditional law for the finite-sample corner gaps; no joint finite-\(N\) rate is asserted.

The associated sharp upper tail is
\[
\Pr(Y_k>t)\sim p_k(r)\left(\frac{\lambda t}{2g}\right)^k\exp\left(-\frac{k\lambda t}{2g}\right).
\]
The opposite endpoint has an explicit first correlation correction:
\[
\Pr(Y_k\le t)=\alpha_k t^2-\beta_k t^3+O_k(t^4),
\]
where
\[
\alpha_k=\frac{k\lambda^2}{8}\left(g^{-2}+3b^{-2}\right),\quad
\beta_k=\frac{k\lambda^3}{24}\left(g^{-3}+6b^{-3}+\frac9{gb^2}\right).
\]
These formulas describe one common marked extreme-distance law, not a separately claimed solution to the full distribution function.

## Assumptions and scope
The polygon has an odd fixed number of sides at least five, points are sampled on its boundary (not in its interior), and the sampling measure is normalized arclength. Limits occur first as the point count \(N\to\infty\) at fixed diameter-deficit threshold and only afterward as the threshold tends to infinity. Small-threshold expansions concern the already-established weak limit \(Y_k\). Exponential rates refer to this explicitly stated normalization; indices are cyclic, and the full boundary contains no point atoms. The coefficient \(p_k(r)\) is specified as an exact finite-dimensional polytope volume, not evaluated in elementary closed form.

## Proof
**Source reduction.** Lao (2010), Section 5.2, equation (5.12) and Theorem 5.3, proves convergence of the \(2k\) corner minima (scaled by \(N/(2k)\)) jointly to independent \(\mathrm{Exp}(\lambda)\) variables and identifies the limit diameter as the minimum of the \(4k\) linear forms displayed above. Thus no reproof of the original scalar weak limit is claimed. Its four linear forms arise from Taylor expansions at the \(k\) longest-diagonal vertex pairs.

**Marked large-deficit reduction.** The \(k\) exceptional-weight terms \(g(B_i+A_{i+m})\) use each of the \(2k\) independent exponentials exactly once. Consequently the \(S_i\) are independent \(\mathrm{Gamma}(2,\lambda)\) sums, while the \(U_i\) are independent uniform random variables on \([0,1]\) and independent of all \(S_i\). Put \(q=t/(2g)\). Necessarily \(S_i>q\) for every \(i\). Conversely, given all these \(k\) inequalities, the remaining \(3k\) large-weight inequalities are exact linear conditions on \(U\) and \(S/q\).

As \(q\to\infty\), the conditional excesses \(W_i=S_i-q\) converge independently to \(\mathrm{Exp}(\lambda)\): their survival probability equals \(e^{-\lambda w}[1+\lambda(q+w)]/[1+\lambda q]\). In particular \(S_i/q\to1\) in probability. At \(S_i=q\), the other three inequalities for longest-diagonal pair \(i,i+m\) become
\[
 U_{i-m}+U_i\le2-r,\quad U_i+U_{i+m}\ge r,\quad U_{i-m}-U_{i+m}\le1-r.
\]
Since \(\gcd(m,k)=1\), the coordinate reordering \(V_j=U_{jm}\) turns these into precisely the defining inequalities for \(P_k(r)\). Every constraint-boundary hyperplane has zero measure under the joint uniform marks; dominated convergence therefore yields the joint conditional limit with uniform \(P_k(r)\)-marks and independently exponential excesses. The cube \([r,1-r]^k\) lies inside \(P_k(r)\), and \(0<r<1/2\), proving \(p_k(r)>0\). Since \(\Pr(S_i>q)=e^{-\lambda q}(1+\lambda q)\), multiplication by the limiting feasibility probability gives the sharp upper-tail asymptotic.

**Small-deficit correction.** Let \(E_e\) be the event that one of the \(4k\) weighted two-exponential sums is at most \(t/2\). The associated graph on the \(2k\) corner variables has \(k\) edges of weight \(g\), \(3k\) of weight \(b\), degree four at every vertex, and no triangles for \(k\ge5\). A single edge of weight \(c\) has probability \(\lambda^2q_c^2/2-\lambda^3q_c^3/3+O(t^4)\) with \(q_c=t/(2c)\). Two disjoint-edge events intersect in order \(t^4\). A pair of edges sharing one exponential has leading intersection volume \(q_\mathrm{small}^2q_\mathrm{large}/2-q_\mathrm{small}^3/6\), times \(\lambda^3\). There are exactly \(6k\) shared \(g,b\) pairs and \(6k\) shared \(b,b\) pairs. As the edge graph is triangle-free, any intersection of three distinct edge events forces at least four independent exponentials to be \(O(t)\), so all such triple intersections are \(O_k(t^4)\). Finite inclusion-exclusion, with \(q_b<q_g\), gives the stated \(\alpha_k\) and \(\beta_k\). The remainder is uniform for each fixed \(k\).

## Verification
The accompanying standard-library Python program checks the exact edge incidence for odd \(k=5,7,9,11,13,17,21\), with no triangles and the specified shared-edge multiplicities. It additionally verifies \(17{,}500\) exact algebraic-constraint equivalences at zero excess, and compares Monte Carlo estimates of both endpoint formulas for \(k=5,7\). These checks are finite diagnostics only; the mathematical proof establishes all fixed odd \(k\ge5\).

## Relationship to prior work
The complete weak-limit representation used as a starting theorem is **already due to Wei Lao (2010), Theorem 5.3**; it is explicitly not claimed as new. The contribution here is the two-scale, joint **conditional corner geometry**, its cyclic feasible polytope and conditional independence, plus sharp upper- and lower-endpoint coefficients extracted from the dependent exponential representation. Koroleva and Nikitin (2013) treat U-max statistics for random polygon perimeters and areas, not these conditional sample-diameter corner variables. Related random boundary-hull Hausdorff asymptotics describe a different statistic. The scalar asymptotics here logically follow from Lao's stronger implicit full scalar limit representation after additional calculation; they are not evidence of a new general scalar limit theorem.

## Limitations
No elementary closed form is asserted for \(p_k(r)\), and no uniform estimates as \(k\to\infty\) or joint \(N,t\) limit are proved. The use of the 2010 source's underlying joint corner convergence is essential. Identical marked conditional laws may have appeared under exponential-graph or polytope terminology elsewhere; historical-priority confirmation requires independent specialist review. The earliest day-verified publisher listing used in metadata is 2010-12-20, but the scholarly 2010 source lacks a confirmed initial online release day; that date is not asserted to be its first digital availability.

## References
1. Wei Lao, *Some Weak Limit Laws for the Diameter of Random Point Sets in Bounded Regions*, KIT Scientific Publishing (2010), Section 5.2, equation (5.12), Theorem 5.3, DOI: 10.5445/KSP/1000019800, https://publikationen.bibliothek.kit.edu/1000019800/105664897 .
2. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360v1 (first posted 2013-01-07), https://arxiv.org/abs/1301.1360 .
