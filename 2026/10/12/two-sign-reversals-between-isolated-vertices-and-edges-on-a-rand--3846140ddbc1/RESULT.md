# Two sign reversals between isolated vertices and edges on a random geometric circle

## Finding

Take \(n\ge2\) independent uniform points on a circle of circumference one. Connect two points if their shorter circular distance is at most \(r\), for \(0<r<1/2\). Let \(I_n\) be the number of isolated vertices (degree zero), and let \(E_n\) be the number of edges. Write \(L=1-2r\) and
\[
q_r=1-\left(\max\left\{1-\frac rL,0\right\}\right)^2.
\]
Their exact finite-sample covariance is
\[
\operatorname{Cov}(I_n,E_n)=\frac{n(n-1)}2L^{n-1}\left[(n-2)(q_r-2r)-4r\right]. \tag{1}
\]
Equivalently, with no discontinuity at \(r=1/3\),
\[
\operatorname{Cov}(I_n,E_n)=
\begin{cases}
\displaystyle \frac{n(n-1)}2L^{n-3}r\left[-4+(3n+10)r-8nr^2\right],&0<r\le1/3,\\[5pt]
\displaystyle \frac{n(n-1)}2L^{n-1}\left[(n-2)L-4r\right],&1/3\le r<1/2.
\end{cases} \tag{2}
\]
There is a sharp **minimal sample size and complete sign phase diagram**:

* For \(2\le n\le5\), this covariance is strictly negative throughout \(0<r<1/2\).
* For \(n=6\), it is strictly positive exactly when \(1/4<r<1/3\), zero at those two endpoints, and strictly negative elsewhere in \((0,1/2)\).
* For each \(n\ge7\), let
\[
 r_{\mathrm{low}}(n)=\frac{3n+10-\sqrt{9n^2-68n+100}}{16n},\qquad
 r_{\mathrm{high}}(n)=\frac{n-2}{2n}.
\]
Then \(0<r_{\mathrm{low}}(n)<1/3<r_{\mathrm{high}}(n)<1/2\). The covariance is positive **exactly** for \(r_{\mathrm{low}}(n)<r<r_{\mathrm{high}}(n)\), zero at the two endpoints, and negative elsewhere in \((0,1/2)\).

The two thresholds satisfy
\[
 n\,r_{\mathrm{low}}(n)\longrightarrow\frac43,
 \qquad r_{\mathrm{high}}(n)=\frac12-\frac1n.
\]
More quantitatively, for every fixed \(c>0\), the thermodynamic regime \(r=c/n\) obeys
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(I_n,E_n)}{n}
=e^{-2c}\left(\frac{3c^2}{2}-2c\right). \tag{3}
\]
This limiting covariance density changes sign at the exact geometric threshold \(c=4/3\). At the degenerate endpoints \(r=0\) and \(r\ge1/2\) the graph is deterministic and the covariance is zero. For \(n=1\), it is also zero.

## Assumptions and scope

The locations are independent, identically distributed uniform points on the **periodic unit circle**, not the unit interval with free boundaries. Edges are determined by the hard geometric cutoff, not independently sampled conditional on a soft connection probability. Continuous sampling makes distance-equality conventions irrelevant almost surely. All formulae concern the ordinary unnormalized counts \(I_n\) and \(E_n\), not their Pearson correlation, an edge-density-normalized statistic, or a Poisson number of vertices.

## Proof

**1. One-vertex isolation law.** Fix a labelled point, rotate it to the origin, and let \(A\) denote its isolation event. The forbidden neighbourhood is an arc of length \(2r\), so its complement is a single arc of length \(L=1-2r\). Independence of the other \(n-1\) point locations gives \(\Pr(A)=L^{n-1}\). Conditional on \(A\), all other locations remain independent and uniform on that complement arc.

**2. Conditional edge probability.** Parametrize the complement arc linearly by \([0,L]\). If two points in this arc have coordinate separation \(d\le L\), their alternative wrap-around route has length \(1-d\ge1-L=2r>r\). Thus they are adjacent exactly when their linear separation is at most \(r\). For two independent uniform coordinates on \([0,L]\), the area of the two corner triangles with separation exceeding \(r\) is \(\max(L-r,0)^2\), giving
\[
 \Pr(\text{edge between two other vertices}\mid A)
 =1-\frac{\max(L-r,0)^2}{L^2}=q_r.
\]
Unconditionally, a specified edge is present with probability \(2r\).

**3. Covariance by symmetry and conditional expectation.** Since an isolated vertex is incident to no edges,
\[
 \mathbb E[E_n\mid A]={n-1\choose2}q_r,
 \qquad \mathbb E[E_n]={n\choose2}2r.
\]
Writing \(I_n\) as the sum of the \(n\) isolation indicators and using exchangeability yields
\[
\begin{aligned}
\operatorname{Cov}(I_n,E_n)
&=n\,\Pr(A)\bigl(\mathbb E[E_n\mid A]-\mathbb E[E_n]\bigr)\\
&=nL^{n-1}\left[{n-1\choose2}(q_r-2r)-(n-1)2r\right],
\end{aligned}
\]
which is (1). If \(r\le L\), equivalently \(r\le1/3\), elementary cancellation gives
\[
 q_r-2r=\frac{r^2(3-8r)}{(1-2r)^2}.
\]
If \(r\ge L\), the conditional pair probability is one and \(q_r-2r=L\). Substitution proves (2), including agreement at \(r=1/3\).

**4. All signs and the first sample size.** Every prefactor in (2) is positive for the stated open range. On \(0<r\le1/3\), the sign is that of
\[
 P_n(r)=-4+(3n+10)r-8nr^2.
\]
For \(n=2\), this is \(-4(1-2r)^2<0\). For \(n=3,4,5\), its discriminant \(9n^2-68n+100\) is negative and its leading coefficient is negative, so it is everywhere strictly negative. For \(n=6\), \(P_6(r)=-4(3r-1)(4r-1)\), giving the claimed first positive interval. For every \(n\ge7\), \(P_n(0)=-4\), \(P_n(1/3)=(n-6)/9>0\), and \(P_n\) is strictly concave. It therefore has exactly one zero within \((0,1/3)\), given by the smaller quadratic root \(r_{\mathrm{low}}(n)\), and is positive from that root through \(1/3\). On \(1/3\le r<1/2\), the sign is that of the strictly decreasing linear function \((n-2)-2nr\). This function is nonpositive there for \(n\le6\); for \(n\ge7\) it has a unique zero at \(r_{\mathrm{high}}(n)\), and is positive to its left. The two branches join continuously. This proves the complete sign diagram and both zero classifications.

**5. Scaling.** The smaller positive root of \(P_n\) obeys \(nr_{\mathrm{low}}(n)\to4/3\), either by expansion of the displayed quadratic formula or by dividing \(P_n(c/n)\) by its fixed-order terms. When \(r=c/n\) for fixed \(c>0\), one has \(L^{n-3}\to e^{-2c}\) and \(P_n(c/n)\to3c-4\). Divide the first case of (2) by \(n\) to obtain (3). The second threshold formula is exact.

## Verification

The accompanying independent-entrypoint script `check_circle.py` uses exact rational arithmetic to compare (1) and (2) for a grid of sample sizes and radii, checks the sign phase diagram on additional rational grids, and checks its three exact boundary zeros. It executes \(15{,}252\) such rational tests. Separately, five seeded Monte Carlo experiments compute isolation and edge counts **directly from point coordinates**, without using the conditional-edge proof, and compare empirical covariances with (1). Run `python3 check_circle.py` with Python 3 and NumPy; the expected final line is `ALL_CHECKS_PASS`. Monte Carlo tolerance is deliberately conservative; only the analytic argument proves the infinite-parameter assertion.

## Relationship to prior work

Penrose and Peres (2010, arXiv:1006.3523) develop local central limit theorems for random geometric graph subgraph and component counts, explicitly including edges and isolated points, but their theorems do not state a finite-sample joint covariance phase diagram. Penrose (2015, arXiv:1507.07132) studies Poisson approximation for isolated vertices and for the number of edges in an inhomogeneous random graph, not the mixed hard-circle covariance. Doku-Amponsah (2016, DOI:10.1186/s40064-016-2718-z) studies a joint large-deviation principle for empirical degree and edge measures in a geometric model, rather than exact finite conditional pair probabilities. Wilsher, Dettmann and Ganesh (2022, arXiv:2202.08044) study a Poisson-input soft geometric graph on a circle and a marginal isolation-count limit; their stated assumptions exclude the hard geometric cutoff used here.

The qualitative contrast with an Erdős–Rényi graph having the **same edge marginal** \(p=2r\) is sharp: independence of nonincident edges after conditioning on isolation gives
\[
 \operatorname{Cov}(I_n^{\mathrm{ER}},E_n^{\mathrm{ER}})
 =-2n(n-1)r(1-2r)^{n-1}<0.
\]
Here the conditioned geometric points are compressed into a complementary arc, which creates the competing positive term and permits two sign reversals. This is a statement about the present model only, not a general theorem about all spatial graphs.

## Limitations

This is a one-dimensional periodic, hard-cutoff, fixed-sample-size result. The sign phenomenon need not persist for an interval with boundary, a Poisson vertex count, an arbitrary soft connection kernel, or higher-dimensional geometry. The limiting covariance density does not describe correlation coefficients and does not by itself assert a joint central limit theorem. The displayed moment identity follows from elementary conditioning; the claimed contribution is its complete, sharp two-transition classification and thermodynamic sign law. General moment/Palm methods or historical material not fully accessible may imply the finite identity indirectly; exhaustive historical priority is not asserted.

## References

1. M. D. Penrose and Y. Peres, *Local central limit theorems in stochastic geometry*, first publicly available 2010-06-17, arXiv:1006.3523v1, https://arxiv.org/abs/1006.3523v1 .
2. M. D. Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, first publicly available 2015-07-25, arXiv:1507.07132v1, https://arxiv.org/abs/1507.07132v1 .
3. K. Doku-Amponsah, *Joint large deviation result for empirical measures of the coloured random geometric graphs*, 2016-07-20, https://doi.org/10.1186/s40064-016-2718-z .
4. M. Wilsher, C. P. Dettmann and A. J. Ganesh, *The Distribution of the Number of Isolated Nodes in the 1-Dimensional Soft Random Geometric Graph*, first publicly available 2022-02-16, arXiv:2202.08044v1, https://arxiv.org/abs/2202.08044v1 .
5. M. D. Penrose, *Random Geometric Graphs*, Oxford University Press, 2003, https://doi.org/10.1093/acprof:oso/9780198506263.001.0001 .
