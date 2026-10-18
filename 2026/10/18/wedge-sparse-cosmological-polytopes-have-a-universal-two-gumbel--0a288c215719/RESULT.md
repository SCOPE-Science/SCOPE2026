# Wedge-sparse cosmological polytopes have a universal two-Gumbel directional-width law

## Finding

Consider any sequence of connected **simple** undirected graphs \(G\) with \(m=|E(G)|\to\infty\), \(n=|V(G)|\), and its canonical cosmological polytope \(P_G\) in the standard-coordinate Euclidean realization. Put
\[
\Omega(G)=\sum_{v\in V(G)}\binom{\deg_G(v)}2,\qquad d=n+m-1,\qquad N=3m,\qquad L=\log N,
\]
and define
\[
 a_N=\sqrt3\left(\sqrt{2L}-\frac{\log L+\log(4\pi)}{2\sqrt{2L}}\right),\qquad b_N=\frac{\sqrt3}{\sqrt{2L}}.
\]
For a Haar-uniform unit vector \(U\) in the direction space of the affine hull, let \(W_G(U)\) be the intrinsic Euclidean width of \(P_G\) in direction \(U\).

**Theorem (wedge-sparsity universality).** If
\[
\Omega(G)=o\bigl(m^{3/2}(\log m)^{1/4}\bigr),
\]
then
\[
\boxed{\ \frac{\sqrt d\,W_G(U)-2a_N}{b_N}\ \Longrightarrow\ \mathcal G_1+\mathcal G_2\ },
\]
where \(\mathcal G_1,\mathcal G_2\) are independent standard Gumbel variables with distribution \(\Pr(\mathcal G_i\le t)=\exp(-e^{-t})\).

More precisely, for any fixed real \(x,y\), the numbers of Gaussian vertex scores above \(a_N+b_Nx\) and below \(-a_N-b_Ny\) converge jointly to **independent** Poisson variables with means \(e^{-x}\) and \(e^{-y}\). Their comparison to independent Poisson counts admits an error bounded, up to a constant depending on \(x,y\), by
\[
\frac{N+\Omega(G)}{N^2}+\frac{N+\Omega(G)}{N^{3/2}(\log N)^{1/4}}.
\]
The additional error in replacing the exact Poisson means by \(e^{-x}\) and \(e^{-y}\) is \(O((\log\log N)^2/\log N)\).

If in addition the graph degrees are **uniformly bounded**, the normalized-width convergence holds in second moment, and hence
\[
\sqrt d\,\mathbb E W_G(U)=2a_N+2\gamma b_N+o(b_N),
\qquad d\,\operatorname{Var}(W_G(U))\sim \frac{\pi^2}{2\log(3m)},
\]
where \(\gamma\) is Euler's constant. The moment conclusions are **not asserted** for all wedge-sparse graph sequences.

The wedge hypothesis includes every bounded-degree graph sequence and also every simple graph sequence with \(m\ge c n^2\) for a fixed \(c>0\), including complete graphs. A star has \(\Omega(G)=\binom m2\) and is not covered by the theorem. The stated sufficient condition is not claimed to be necessary or sharp.

## Assumptions and scope

The standard-coordinate cosmological polytope for a simple graph without isolated vertices is the convex hull, over edges \(e=\{u,v\}\), of the three points
\[
 p_{e,0}=e_u+e_v-e_e,\quad p_{e,1}=e_u-e_v+e_e,\quad p_{e,2}=-e_u+e_v+e_e
\]
in \(\mathbb R^{n+m}\), where \(e_u\) and \(e_e\) are orthonormal coordinates indexed by vertices and edges. Every listed point has coordinate sum one. For any edge, the pairwise midpoints of its three displayed points are exactly \(e_u\), \(e_v\), and \(e_e\). Because the graph has no isolated vertices, these midpoints supply every standard coordinate basis vector, proving that \(P_G\) affinely spans the sum-one hyperplane. Its intrinsic dimension is \(d=n+m-1\). All directions and distances in this statement use the inherited standard Euclidean inner product; arbitrary affine changes of coordinates do not preserve the theorem.

For all sufficiently large \(m\), \(m\ge1\) and \(N\ge3\), so the normalizers are well-defined. The graph sequence may be deterministic or chosen arbitrarily at each size; no degree regularity or fixed graph family is required beyond the displayed wedge condition.

## Proof

**1. Exact Euclidean Gaussian score geometry.** Let \(g=(X_v,Y_e)\) have independent standard normal coordinates. Define \(Z_{e,j}=\langle g,p_{e,j}\rangle\). Each of the \(N=3m\) variables is centered normal with variance \(3\). Within any one edge, the three unordered distinct score pairs have covariance \(-1\). For two distinct graph edges that are disjoint, all nine pairs have covariance zero and the corresponding triples are independent. For two edges meeting at one vertex, precisely five of the nine pairs have covariance \(+1\), and four have covariance \(-1\). In particular, all correlations between distinct scores have absolute value at most \(1/3\). The number of unordered edge pairs sharing a vertex is exactly \(\Omega(G)\); hence the score-dependency graph has \(O(N+\Omega(G))\) adjacent index pairs. These are identities, not probabilistic approximations.

**2. Simultaneous upper and lower extremes.** Write \(u_N(t)=a_N+b_Nt\). Elementary normal-tail asymptotics give
\[
 N\Pr(Z_{e,j}>u_N(t))=N\overline\Phi\bigl(u_N(t)/\sqrt3\bigr)\longrightarrow e^{-t}.
\]
We record a quantitative joint-tail bound. If \((A,B)\) are standard jointly Gaussian with \(|\rho|\le1/3\), a change of variables \(A=z+s,B=z+t\) in the bivariate density, \(s,t\ge0\), gives for \(z\ge1\)
\[
\Pr(A>z,B>z)\le \frac{C}{z^2}\exp\left(-\frac{z^2}{1+\rho}\right)
\le\frac{C}{z^2}e^{-3z^2/4}.
\]
Indeed, after translation to \((z,z)\), the density has a nonnegative quadratic remainder and a linear factor \(\exp[-z(s+t)/(1+\rho)]\); integrating this factor over the positive quadrant gives the reciprocal square. With \(z=\min(u_N(x),u_N(y))/\sqrt3\), this bound is
\[
 O_{x,y}\bigl(N^{-3/2}(\log N)^{-1/4}\bigr)
\]
for all pairs of nonidentical dependent signed scores, including upper/lower mixed pairs. Opposite signs of the **same** score cannot exceed positive upper/lower thresholds simultaneously.

Index the upper-threshold events and lower-threshold events by a signed copy of the score indices. Each event has probability \(O_{x,y}(N^{-1})\). Two events are independent whenever their underlying graph edges are disjoint. There are \(O(N+\Omega(G))\) neighboring ordered event pairs. The local-dependence Poisson process approximation, or equivalently the usual two-color factorial-moment argument, thus has the standard errors
\[
 b_1=O_{x,y}\left(\frac{N+\Omega(G)}{N^2}\right),\qquad
 b_2=O_{x,y}\left(\frac{N+\Omega(G)}{N^{3/2}(\log N)^{1/4}}\right),\qquad b_3=0.
\]
The assumed wedge growth makes both errors vanish. The two marked upper/lower exceedance counts therefore converge jointly to independent Poisson variables with the stated means. The no-exceedance events imply
\[
\left(\frac{\max_{e,j}Z_{e,j}-a_N}{b_N},\ \frac{-\min_{e,j}Z_{e,j}-a_N}{b_N}\right)
\Longrightarrow(\mathcal G_1,\mathcal G_2)
\]
with independent coordinates.

**3. Intrinsic spherical normalization.** Let \(H=\{t\in\mathbb R^{n+m}:\sum t_i=0\}\), \(g_H\) be the orthogonal projection of \(g\) onto \(H\), and \(R=\|g_H\|\). Because all polytope vertices have coordinate sum one, replacing \(g\) by \(g_H\) subtracts the same scalar from every vertex score. Consequently, with \(U=g_H/R\),
\[
 W_G(U)=\frac{\max Z_{e,j}-\min Z_{e,j}}R.
\]
Here \(R\) has the \(\chi_d\) distribution, \(U\) is Haar-uniform on the unit sphere in \(H\), and \(\sqrt d/R-1=O_{\Pr}(d^{-1/2})\). The Gaussian score range is \(O_{\Pr}(\sqrt{\log N})\); dividing the resulting radial error by \(b_N\asymp(\log N)^{-1/2}\) gives \(O_{\Pr}(\log N/\sqrt d)=o_{\Pr}(1)\), since \(d\ge m\). Slutsky's theorem proves the displayed two-Gumbel width law.

**4. Second-moment refinement for bounded degree.** Suppose \(\deg_G(v)\le D\) for an absolute constant \(D\). A greedy matching selects at least \(m/(2D-1)\) pairwise disjoint graph edges. One score from each selected edge is independent and has distribution \(N(0,3)\). For the normalized maximum \(T_N=(\max Z_{e,j}-a_N)/b_N\), a union bound gives uniformly exponential upper tails. The matching and standard one-dimensional normal-tail bounds give uniformly doubly-exponential lower tails for \(0\le t\le \log N\), exponentially small probabilities throughout \(\log N<t\le2\log N\), and a further Gaussian-square decay beyond \(2\log N\). The same estimates hold for the normalized negative minimum. They give uniform integrability of every fixed power of these normalized extrema, so their first two moments converge to those of the independent Gumbel pair.

For the spherical correction, \(\mathbb E|\sqrt d/R-1|^4=O(d^{-2})\) and \(\mathbb E(\max Z-\min Z)^4=O((\log N)^2)\). Cauchy–Schwarz shows that the squared \(b_N\)-normalized radius error has expectation \(O((\log N)^2/d)=o(1)\). Therefore the normalized spherical width converges in second moment. Using \(\mathbb E\mathcal G_i=\gamma\) and \(\operatorname{Var}(\mathcal G_i)=\pi^2/6\) proves the asserted mean and variance formulas.

**5. Graph-class consequences.** If the degree bound is \(D\), then \(\Omega(G)\le m(D-1)\), proving the bounded-degree assertion. More generally, if \(m\ge c n^2\), then \(\Omega(G)\le n\binom{n-1}2=O(n^3)=O(m^{3/2})\), which is strictly smaller than the required \(o(m^{3/2}(\log m)^{1/4})\) scale. This includes the complete graphs and dense irregular graph sequences. For a star, \(\Omega(G)=\binom m2\), which violates the sufficient condition; the theorem makes no inference about the star law.

## Verification

A separate deterministic checker, `verification.py`, constructs each embedded coordinate vertex directly and compares Gaussian-direction widths with the exact score-range identity. It verifies all pairwise covariance cases, including the five-positive/four-negative covariance split for pairs of incident edges, and checks finite examples from paths, cycles, branching trees, an irregular graph, and a complete graph. On a seeded run it passed 231 constructed vertices and 840 direct score/width tests. Additional seeded diagnostics sampled path and cycle sizes \(m=160,600\) and complete-graph sizes \(m=120,595\); the diagnostics are finite-size illustrations, not proofs of the asymptotic law. Convergence may be particularly slow for dense graphs because the displayed Poisson dependency error may decay only logarithmically. The proof, not the simulations, covers arbitrarily large graphs.

To reproduce, use Python 3 with NumPy and run `python verification.py` from a directory containing the supplied standalone file. A successful run prints `VERIFY_OK`.

## Relationship to prior work

Arkani-Hamed, Benincasa and Postnikov introduced the underlying cosmological-polytope construction. Kühne and Monin gave its graph-indexed coordinate realization and combinatorial face structure; Benjes, Ferry and Schröter analyzed good triangulations and Ehrhart/Tutte aspects. Those constructions and results are not new here. Kabluchko, Litvak and Zaporozhets established Gaussian width formulas and two-independent-Gumbel asymptotics for regular simplices, as well as related results for cubes and crosspolytopes; **the distribution type itself is not claimed as new**. Arratia, Goldstein and Gordon established general local-dependence Poisson approximation and treated maxima of Gaussian sequences; **the probabilistic approximation technique is not claimed as new**.

The specific statement proved here concerns the standard Euclidean geometry of *cosmological* graph polytopes, its exact three-score covariance incidence structure, the graph-wedge sufficient condition (including all dense simple graphs), and the bounded-degree width-moment consequences. The listed primary polytope and Gaussian-extreme results do not state these graph-indexed geometric consequences. A general Gaussian-array theorem can supply a major proof ingredient once this polytope-specific reduction is established; the result should not be read as inventing a new extreme-value method.

## Limitations

This is a sufficient wedge condition, not a necessary-and-sufficient classification or a sharp universality threshold. The asymptotic moment formulas require uniformly bounded degree; they are not proved for dense graphs merely from the wedge hypothesis. The rate displayed applies to the Gaussian marked exceedance process at fixed thresholds, not directly to the entire centered width distribution. The theorem uses the inherited Euclidean metric and simple connected graphs; no assertion is made for parallel-edge multigraphs, arbitrary metrics, or isolated-vertex versions. Finite numerical diagnostics are not a substitute for the analytic limit proof. Literature equivalence under an alternate Gaussian-array or stochastic-geometry formulation remains a residual bibliographic risk. Independent mathematical validation has not been performed.

## References

1. N. Arkani-Hamed, P. Benincasa, and A. Postnikov, *Cosmological polytopes and the wavefunction of the universe*, arXiv:1709.02813 (2017).
2. L. Kühne and L. Monin, *Faces of Cosmological Polytopes*, arXiv:2209.08069, first posted 2022-09-16; *Ann. Inst. Henri Poincaré D*, DOI 10.4171/AIHPD/192.
3. A. Benjes, K. Ferry, and B. Schröter, *Good Triangulations of Cosmological Polytopes*, arXiv:2503.13393 (2025).
4. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479; *J. Math. Sci.* 225 (2017), 770–787, DOI 10.1007/s10958-017-3492-3.
5. R. Arratia, L. Goldstein, and L. Gordon, *Poisson approximation and the Chen–Stein method*, *Statistical Science* 5 (1990), 403–424, DOI 10.1214/ss/1177012015.
