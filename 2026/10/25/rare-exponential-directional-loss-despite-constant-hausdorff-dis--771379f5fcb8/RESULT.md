# Rare exponential directional loss despite constant Hausdorff distance in crown-graph root polytopes

## Finding
For every integer \(n\ge3\), put \(P_n=\Delta_{n-1}\times\Delta_{n-1}\subset\mathbb R^{2n}\) and
\[
Q_n=\operatorname{conv}\{(e_i,e_j):1\le i,j\le n,\ i\ne j\}.
\]
This is the bipartite root polytope of the crown graph, in a sign-reversed but isometric realization. The product and crown polytope satisfy
\[
\frac{\operatorname{vol}_{2n-2}(Q_n)}{\operatorname{vol}_{2n-2}(P_n)}=1-\frac{n}{\binom{2n-2}{n-1}},\qquad
 d_H(P_n,Q_n)=\sqrt{\frac{n}{2(n-1)}}.
\]
Let \(U_n\) be a uniform unit vector in their common intrinsic direction space, and let \(\Delta_n=w_{P_n}(U_n)-w_{Q_n}(U_n)\) be the difference of their Euclidean widths. For the normal quantile \(b_n=\Phi^{-1}(1-1/n)\),
\[
\Pr(\Delta_n>0)=\frac2n-\frac{1}{n(n-1)},\qquad
\mathcal L\bigl(b_n\sqrt{2n}\,\Delta_n\mid\Delta_n>0\bigr)\Longrightarrow\operatorname{Exp}(2).
\]
The positive gap has mean and variance asymptotics
\[
\mathbb E\Delta_n\sim\frac{1}{n b_n\sqrt{2n}},\qquad
\operatorname{Var}(\Delta_n)\sim\frac{1}{2n^2b_n^2}.
\]
Thus a deletion of only \(n\) product vertices produces an exponentially small *relative volume* loss, a nonvanishing worst-case Euclidean Hausdorff distance, and a random-width loss supported on a set of spherical directions of probability asymptotic to \(2/n\). Conditionally on that rare event its sharp scale is \((n\log n)^{-1/2}\), with an exponential limit.

## Assumptions and scope
Use the standard simplex \(\Delta_{n-1}=\{p\in\mathbb R^n:p_i\ge0,\sum_i p_i=1\}\). All volume and distance quantities use the intrinsic Euclidean metric inherited from the fixed affine subspace \(\sum_i p_i=\sum_i q_i=1\), dimension \(2n-2\). Spherical width means \(w_K(u)=h_K(u)+h_K(-u)\), where \(h_K(u)=\max_{z\in K}\langle u,z\rangle\). The exponential law \(\operatorname{Exp}(2)\) has rate two and mean one half. All limits are along integer \(n\to\infty\); quantile \(b_n\) is positive for \(n\ge3\).

## Proof
**1. Exact description and volume.** The transportation-table coupling criterion for the bipartite graph with all diagonal cells forbidden gives
\[
Q_n=\{(p,q)\in\Delta_{n-1}^2:p_i+q_i\le1\ \text{for each }i\}.
\]
Indeed for a singleton row set \(\{i\}\), its allowed neighboring columns are all except \(i\), giving \(p_i\le1-q_i\); for any row set of cardinality at least two, the neighboring set is all columns and the required Hall inequality is automatic. Conversely a feasible coupling decomposes into edge tables, realizing \((p,q)\) as a convex combination of \((e_i,e_j)\) with \(i\ne j\).

A uniform point in \(P_n\) has independent uniform-simplex coordinates \(p,q\). For each fixed \(i\), their marginals \(p_i,q_i\) are independent \(\operatorname{Beta}(1,n-1)\), so
\[
\Pr(p_i+q_i>1)=(n-1)\int_0^1(1-x)^{n-2}x^{n-1}\,dx=\binom{2n-2}{n-1}^{-1}.
\]
The events \(p_i+q_i>1\) are pairwise disjoint (two strict violations would make \(\sum_i(p_i+q_i)>2\)). Summing them gives the exact volume ratio. Stirling's formula yields a relative volume deficit \(n\sqrt{\pi(n-1)}\,4^{-(n-1)}(1+O(1/n))\).

**2. Hausdorff distance.** As \(Q_n\subset P_n\), the convex distance-to-\(Q_n\) function on \(P_n\) achieves its maximum at a vertex. Its surviving off-diagonal vertices have distance zero. At a removed vertex \((e_i,e_i)\), let \(a=p_i\), \(b=q_i\) for a candidate \((p,q)\in Q_n\). We have \(a+b\le1\) and, by Cauchy–Schwarz,
\[
\|(p,q)-(e_i,e_i)\|_2^2\ge\frac n{n-1}\bigl[(1-a)^2+(1-b)^2\bigr]\ge\frac n{2(n-1)}.
\]
Equality is attained by the equal-weight convex combination of \((e_i,e_j)\) and \((e_j,e_i)\) over all \(j\ne i\). This proves the exact distance.

**3. Exact Gaussian support defect.** Let \(G_1,\dots,G_n,H_1,\dots,H_n\) be independent standard normal variables. Write \(\bar G,\bar H\) for their sample means and
\[
R_n=\biggl[\sum_i(G_i-\bar G)^2+\sum_i(H_i-\bar H)^2\biggr]^{1/2}.
\]
Then \(U_n=((G_i-\bar G)_i,(H_i-\bar H)_i)/R_n\) is uniform on the unit sphere in the intrinsic direction space, and \(R_n^2\sim\chi^2_{2n-2}\). Let \(I_+\) be the event that the maximizing index of \(G\) equals that of \(H\), and \(I_-\) the analogous event for the minimizing indices. If \(A_n^+\) and \(B_n^+\) denote the respective upper gaps between the largest and second-largest observations, and \(A_n^-\), \(B_n^-\) the lower gaps, direct maximization over allowed off-diagonal indices shows exactly that
\[
\Delta_n=\frac{\mathbf1_{I_+}\min(A_n^+,B_n^+)+\mathbf1_{I_-}\min(A_n^-,B_n^-)}{R_n}.
\]
Each index-rank permutation is independent of its ordered Gaussian sample, so the indicator events are independent of all ordered gaps and \(R_n\). Uniform independent permutations give \(\Pr(I_+)=\Pr(I_-)=1/n\) and \(\Pr(I_+\cap I_-)=1/[n(n-1)]\). Positivity is almost sure whenever either event occurs, establishing its stated exact probability.

**4. Rare-event limit and moments.** The standard normal upper order statistics satisfy
\[
b_n A_n^+\Longrightarrow\operatorname{Exp}(1),\qquad
b_n B_n^+\Longrightarrow\operatorname{Exp}(1)
\]
independently, and identically for lower gaps. One direct proof conditions on the second-largest value \(s\): the survival function of the top gap at \(t\) is \(\overline\Phi(s+t)/\overline\Phi(s)\). The second-largest is \(b_n(1+o_P(1))\), and the Gaussian tail ratio with \(t=z/b_n\) tends to \(e^{-z}\). The two independent upper gaps have minimum limit \(\operatorname{Exp}(2)\). The independent spherical normalization obeys \(R_n/\sqrt{2n}\to1\) in probability. Conditioned on a positive loss, the probability of the simultaneous upper and lower index coincidence is \(1/(2n-3)\to0\), and the two single-coincidence cases are symmetric. This gives the conditional distribution.

For the claimed mean and variance one also needs convergence of the first two (in fact all fixed positive) moments of normalized gaps, not just weak convergence. Gaussian increasing hazard rates imply, conditional on second-largest \(s\ge b_n/2\), that \(\Pr(b_n A_n^+>z\mid s)\le e^{-z/2}\). The complementary event has superpolynomially small probability in \(n\); Cauchy–Schwarz and polynomial Gaussian-maximum moments control its contribution. This proves uniform integrability of the squared scaled gap. Chi-square negative moments give the same for \(\sqrt{2n}/R_n\), which is asymptotically one in every fixed \(L^p\). Consequently, with \(D_n=\min(A_n^+,B_n^+)\),
\[
\mathbb E\bigl[b_n\sqrt{2n}\,D_n/R_n\bigr]\to\tfrac12,\qquad
\mathbb E\bigl[(b_n\sqrt{2n}\,D_n/R_n)^2\bigr]\to\tfrac12.
\]
The exact independent-event decomposition then yields the displayed mean and second-moment asymptotics. The contribution of simultaneous upper and lower coincidences is lower-order by Cauchy–Schwarz, and \((\mathbb E\Delta_n)^2\) is smaller than \(\mathbb E\Delta_n^2\) by a factor of order \(1/n\). Therefore the variance has the claimed equivalent.

## Verification
Run `python checks/check_crown.py` with NumPy and SciPy. The script independently constructs all product/crown vertices, checks intrinsic convex-hull volumes in dimensions \(n=3,4,5\), numerically minimizes distances from the deleted vertices to the crown hull, and checks the exact Gaussian width-defect identity against direct vertex maximization in 1,500 independently sampled directions. Its additional Monte Carlo diagnostics inspect the positivity probability and conditional scaling for \(n=20,50,100\). All assertions passed. Finite calculations are corroboration, not a proof of the asymptotic law; the proof above handles all \(n\ge3\).

## Relationship to prior work
Almousa–Dochtermann–Smith study root polytopes of arbitrary bipartite subgraphs of a complete bipartite graph as subpolytopes of products of simplices, and analyze their triangulations, tropical-type ideals, and toric edge rings [1]. Ohsugi–Tsuchiya study graph PQ-type adjacency polytopes and derive normalized volumes and Ehrhart invariants for join graphs [2]. A PQ-type adjacency polytope should not be confused with the crown root polytope, which excludes its diagonal product vertices. These sources provide the combinatorial-geometric setting but do not state the conditional spherical-width loss law or the three-way metric separation proved here. Gaussian extreme-spacing asymptotics are standard probabilistic inputs and are not claimed as new in isolation.

## Limitations
The result uses the standard intrinsic Euclidean embedding; arbitrary affine transformations do not preserve the Hausdorff or width formulas. No asymptotic law is asserted when the forbidden edges are not a perfect matching. Novelty was evaluated against inspected primary literature and relevant indexed findings, but an unindexed equivalent probabilistic or convex-geometric formulation remains possible. The result has not undergone independent mathematical validation.

## References
[1] A. Almousa, A. Dochtermann, B. Smith, *Root polytopes, tropical types, and toric edge ideals*, arXiv:2209.09851 (initial public submission 2022-09-20), https://arxiv.org/pdf/2209.09851.

[2] H. Ohsugi, A. Tsuchiya, *PQ-type adjacency polytopes of join graphs*, arXiv:2103.15045 (initial public submission 2021-03-28), https://arxiv.org/abs/2103.15045.
