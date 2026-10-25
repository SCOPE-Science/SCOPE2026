# A compound-Poisson angular width defect for critical-rank assignment polytopes

## Finding
For each integer \(N\geq3\), let \(1\leq k_N<N\), let \(H_N\) be the hypersimplex of binary \(N\)-by-\(N\) matrices containing exactly \(k_N\) ones, and let \(M_N\subset H_N\) be the convex hull of such matrices with at most one one in each row and each column. Both are considered in their common affine hyperplane with the Frobenius metric. For a unit vector \(u\) parallel to this hyperplane, define the directional width \(W_P(u)=\max_{x\in P}\langle u,x\rangle-\min_{x\in P}\langle u,x\rangle\). Let \(U_N\) be uniform on the intrinsic unit sphere, put \(d_N=N^2-1\), and define \(t_N=\Phi^{-1}(1-k_N/N^2)\), where \(\Phi\) is the standard-normal distribution function.

If \(k_N/\sqrt N\to c\in(0,\infty)\), then
\[
t_N\sqrt{d_N}\bigl(W_{H_N}(U_N)-W_{M_N}(U_N)\bigr)\ \Longrightarrow\ \sum_{j=1}^{J} E_j,\qquad J\sim\operatorname{Poisson}(2c^2),\quad E_j\overset{\mathrm{iid}}\sim\operatorname{Exp}(2),\]
where the jumps are independent of the Poisson count and \(\operatorname{Exp}(2)\) has rate two. More strongly, the similarly normalized positive and negative support-function losses converge jointly to **independent** compound-Poisson variables, each with intensity \(c^2\) and rate-two exponential jumps. The limiting width-loss law has an atom \(e^{-2c^2}\) at zero, mean \(c^2\), and variance \(c^2\).

For every finite \(N\) and \(1\leq k\leq N\), the one-sided spherical probability of equality of the two support functions is exactly
\[
\mathbb P\{h_{M_{N,k}}(U)=h_{H_{N,k}}(U)\}
=\frac{(N)_{\underline k}^2}{(N^2)_{\underline k}},
\]
where \((a)_{\underline k}=a(a-1)\cdots(a-k+1)\). The two-sided equality event obeys the sharp threshold
\[
\mathbb P\{W_{M_{N,k_N}}(U_N)=W_{H_{N,k_N}}(U_N)\}\longrightarrow
\begin{cases}1,&k_N/\sqrt N\to0,\\ e^{-2c^2},&k_N/\sqrt N\to c\in(0,\infty),\\0,&k_N/\sqrt N\to\infty,\end{cases}
\]
for integer sequences \(1\leq k_N<N\). The zero-atom assertion is established through collision events, not inferred merely from weak convergence at a discontinuity.

## Assumptions and scope
The underlying polytope \(M_{N,k}\) consists of incidence matrices of size-\(k\) matchings of the complete bipartite graph on two parts of size \(N\). The ambient coordinate space is \(\mathbb R^{N\times N}\); the common direction space is \(L_N=\{u:\sum_{i,j}u_{ij}=0\}\) of dimension \(d_N\). The normalized Euclidean spherical measure on \(L_N\), not the ambient full-sphere measure nor an unnormalized Gaussian law, is used. All widths are intrinsic Frobenius-Euclidean widths. The principal limit assumes \(c>0\); the edge regimes in the equality probability include all ranks allowed above. No limit for the positive nonzero defect in the supercritical regime is asserted.

## Proof
**1. Gaussian representation and the exact equality event.** Let \(G=(G_{ij})\) have independent standard-normal entries, and let \(\widetilde G\) be its orthogonal projection onto \(L_N\). Then \(\widetilde G/\|\widetilde G\|_F\) has the prescribed spherical law. Since every vertex of either polytope has coordinate sum \(k\), subtracting the mean of \(G\) changes both support values by the same scalar, and hence does not change their difference. Write \(G_{(1)}>\cdots>G_{(N^2)}\) for decreasingly ordered entries, and let \(A_N(G)\) be the maximum weight of a size-\(k\) nonattacking selection. The positive Gaussian loss is
\[
D_N^+(G)=\sum_{r=1}^kG_{(r)}-A_N(G)\geq0,
\]
and the negative loss is \(D_N^-(G)=D_N^+(-G)\). Thus the spherical width loss is \((D_N^++D_N^-)/\|\widetilde G\|_F\).

Because the entries have a continuous exchangeable law, their decreasing index ordering is a uniformly random permutation of the \(N^2\) grid cells, independent of the ordered values. The positive loss vanishes exactly when the top \(k\) cells form a matching. Counting size-\(k\) nonattacking subsets gives \(\binom Nk^2 k!\); dividing by \(\binom{N^2}k\) proves the exact one-sided formula.

**2. Rare ranked collisions.** Assume \(k/\sqrt N\to c>0\). For every ranked pair \(1\leq a<b\leq k\), mark the point \((a/k,b/k)\) whenever the two associated grid cells lie in one common row or column. The resulting point process on \(\{0<u<v<1\}\) converges to a Poisson point process of intensity \(2c^2\,du\,dv\). To see this, couple the first \(k\) uniformly distinct cells to \(k\) independent uniformly sampled cells. The probability of a repeated complete cell under the latter experiment is at most \(\binom k2/N^2=o(1)\). In the independent experiment, a given pair collides in a row or column with probability \(2/N+O(N^{-2})\). For factorial moments on disjoint rank regions, families of pair events using disjoint rank labels contribute the product intensities. Events using a connected component of three or more rank labels contribute \(O(k^vN^{-(v-1)})=o(1)\) when that component has \(v\geq3\), by exposing the component along a spanning tree. Consequently the limiting factorial moment measures are Poisson. In particular the number \(C_N\) of collisions is tight and converges to \(\operatorname{Poisson}(c^2)\); with probability tending to one no two collision pairs share a ranked cell.

**3. Gaussian scores at moving ranks.** The positive number \(t_N\) is chosen by \(N^2\overline\Phi(t_N)=k\). For every fixed \(x\), Gaussian tail asymptotics give
\[
\frac{\overline\Phi(t_N+x/t_N)}{\overline\Phi(t_N)}\longrightarrow e^{-x}.
\]
The number of scores above the displayed threshold has mean asymptotic to \(ke^{-x}\) and relative fluctuations tending to zero. Monotonicity and a finite-grid argument therefore give, for every \(\delta>0\) and each fixed integer \(B\geq0\),
\[
\sup_{\delta k\leq r\leq k+B}
\left|t_N(G_{(r)}-t_N)-\log(k/r)\right|\xrightarrow{\mathbb P}0.
\]
In particular \(t_N(G_{(k)}-G_{(k+B)})\to0\) in probability. Ranked collisions with their larger rank below \(\delta k\) have expected count \(O(\delta^2)\), so their contribution can be removed by first fixing \(\delta\) and then decreasing it to zero.

**4. A two-sided optimization sandwich.** On the event that the collision pairs are disjoint, denote their ranked endpoints by \((a_j,b_j)\) with \(a_j<b_j\), \(1\leq j\leq C_N\). Every matching must omit at least one member of each pair, and all replacement scores are at most \(G_{(k)}\). Therefore
\[
D_N^+(G)\geq\sum_{j=1}^{C_N}\bigl(G_{(b_j)}-G_{(k)}\bigr).
\]
Delete the weaker ranked member \(b_j\) from each pair. The retained \(k-C_N\) cells form a matching. With probability tending to one, the next \(C_N\) ranked cells, whose number is tight, have no row or column conflict with this matching or with one another (their collision probability is \(O_{\mathbb P}(C_Nk/N+C_N^2/N)=o_{\mathbb P}(1)\)). Adding these cells constructs a size-\(k\) matching and yields
\[
D_N^+(G)\leq\sum_{j=1}^{C_N}\bigl(G_{(b_j)}-G_{(k+C_N)}\bigr).
\]
After multiplication by \(t_N\), the gap between the two bounds vanishes in probability. The marked collision limit and the moving-rank score approximation now give
\[
t_ND_N^+(G)\Longrightarrow\sum_{(u,v)\in\mathcal P}-\log v,
\]
where \(\mathcal P\) has intensity \(2c^2du\,dv\) on \(0<u<v<1\). Its count is Poisson with mean \(c^2\); conditional on a point, \(v\) has density \(2v\), so \(-\log v\) has the rate-two exponential distribution.

**5. The two tails and the sphere.** Jointly, the top \(k\) and bottom \(k\) grid-cell lists are uniformly ordered disjoint lists, independent of the score order statistics. They can be coupled to two independent lists of \(k\) iid uniform grid cells with failure probability \(O(k^2/N^2)=o(1)\). The upper- and lower-tail marked collision processes hence converge to independent Poisson processes. The score approximations in step 3 hold for both tails, so the two scaled losses converge jointly to independent compound-Poisson variables of intensity \(c^2\) and rate-two jumps. Finally, \(\|\widetilde G\|_F/\sqrt{N^2-1}\to1\) in probability. Slutsky's lemma establishes the width limit, whose count parameter is the sum of the two independent intensities.

**6. Exact zero-loss crossover.** Gaussian scores are distinct almost surely. Thus the width loss vanishes exactly when both top and bottom \(k\)-cell selections are matchings. The two collision counts converge jointly to independent \(\operatorname{Poisson}(c^2)\) variables, giving probability \(e^{-2c^2}\) of no collision. If \(k=o(\sqrt N)\), the expected number of top-or-bottom colliding pairs tends to zero and the probability tends to one. If \(k/\sqrt N\to\infty\), the one-sided exact counting probability tends to zero: taking logarithms of the falling-factorial ratio gives an upper bound \(-k(k-1)/N+O(1)\) for \(k\leq N\). The width-equality probability is at most this one-sided probability.

## Verification
The included `check.py` uses exact combinatorial search against an independent assignment optimizer in small dimensions, plus a check of the collision-repair sandwich and seeded finite-rank simulations. Its numerical experiments do not prove the infinite-dimensional Poisson or Gaussian-quantile assertions. They directly check the finite formulas and the stated optimization inequalities; `CHECKS.txt` records observed values. Run with `python check.py` in an environment with NumPy and SciPy installed. All reproducibility files are included in this package.

## Relationship to prior work
Gill and Linusson studied the face structure and graph diameter of fixed-cardinality assignment polytopes. Torres established normality of the broader bipartite \(k\)-matching polytopes and recalled their linear descriptions. Those results establish the geometric objects but do not identify random spherical width losses. Classical random assignment work of Coppersmith–Sorkin and Alm–Sorkin concerns minimum costs under exponential weights and in particular exact expectations, not the Gaussian critical-rank width-loss distribution relative to a hypersimplex. The present geometric quantity is the **difference** between two width functionals on the same randomly oriented direction; neither the absolute matching optimum nor the usual assignment-value expectation is claimed as new.

## Limitations
The result concerns complete balanced bipartite graphs and standard Frobenius geometry, with independent Gaussian coefficients used solely as the equivalent spherical representation. No universal non-Gaussian-tail extension, convergence rate, or supercritical nonzero-loss scaling is proved. The convergence in distribution does not assert convergence of all moments, and numerical simulations alone cannot establish it. While the checked literature did not yield a covering theorem, equivalent formulations in unindexed probabilistic matching and extreme-value work remain possible. Independent external mathematical audit has not been performed.

## References
1. Juan Camilo Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910v1 (first publicly submitted 2023-06-20), https://arxiv.org/abs/2306.11910.
2. Jonna Gill and Svante Linusson, *The k-assignment polytope*, Discrete Optimization 6 (2009), 148–161, doi:10.1016/j.disopt.2008.10.003. Open postprint: https://liu.diva-portal.org/smash/get/diva2:210918/FULLTEXT01.pdf.
3. Don Coppersmith and Gregory B. Sorkin, *Constructive bounds and exact expectations for the random assignment problem*, Random Structures & Algorithms 15 (1999), 113–144, doi:10.1002/(SICI)1098-2418(199909)15:2<113::AID-RSA1>3.0.CO;2-S.
4. Sven Erick Alm and Gregory B. Sorkin, *Exact expectations and distributions for the random assignment problem*, Combinatorics, Probability and Computing 11 (2002), 217–248, doi:10.1017/S0963548302005114.
