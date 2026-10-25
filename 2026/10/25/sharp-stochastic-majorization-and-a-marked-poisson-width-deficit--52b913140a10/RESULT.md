# Sharp stochastic majorization and a marked-Poisson width-deficit law for multipartite root polytopes

## Finding

For a fixed integer \(r\ge3\) and integers \(n_1,\ldots,n_r\ge1\), let \(N=\sum_{c=1}^r n_c\ge r\), and let \(G_{\mathbf n}=K_{n_1,\ldots,n_r}\) be the complete multipartite graph. In the **standard induced Euclidean metric** on the hyperplane \(H_N=\{x\in\mathbb R^N:\sum_i x_i=0\}\), define
\[
P_{\mathbf n}=\operatorname{conv}\{\pm(e_i-e_j):\{i,j\}\in E(G_{\mathbf n})\},\qquad
P_{\rm all}=\operatorname{conv}\{\pm(e_i-e_j):i\ne j\}.
\]
Write \(w_P(u)=h_P(u)+h_P(-u)\) for directional width and let \(U_N\) be Haar-uniform on the unit sphere of \(H_N\). Define the nonnegative width loss \(L_{\mathbf n}=w_{P_{\rm all}}(U_N)-w_{P_{\mathbf n}}(U_N)\).

**Finite-dimensional theorem (exact conditional law and stochastic order).** Let \(g_1,\ldots,g_N\) be independent standard normal variables with distinct values; put \(M=\max_i g_i\), \(m=\min_i g_i\), and, for \(s\ge0\),
\[
K_s(g)=\#\{i:g_i\ge M-s\ \text{or}\ g_i\le m+s\}.
\]
For a uniformly random placement of the prescribed part labels among the ranked coordinates, the unnormalized Gaussian support loss \(D_{\mathbf n}(g)=h_{P_{\rm all}}(g)-h_{P_{\mathbf n}}(g)\) satisfies, conditionally on the unordered values of \(g\),
\[
\boxed{\Pr\{D_{\mathbf n}(g)>s\mid\{g_1,\ldots,g_N\}\}
=\frac{\sum_{c=1}^r(n_c)_{K_s(g)}}{(N)_{K_s(g)}}.}
\]
Here \((a)_k=a(a-1)\cdots(a-k+1)\), with \((a)_k=0\) when \(k>a\). This identity also determines the spherical-loss law by replacing \(s\) by \(t\|g-\bar g\mathbf1\|_2/2\), because \(L_{\mathbf n}=2D_{\mathbf n}(g)/\|g-\bar g\mathbf1\|_2\).

For fixed \(N\) and \(r\), an outward unit transfer from a part of size \(q\ge2\) into another of size \(p\ge q\) **strictly increases** the unnormalized Gaussian width loss in first-order stochastic order at every finite threshold \(s\ge0\); it also increases the spherical width loss in stochastic order and strictly increases its expectation. Consequently, for \(N\ge r\), the multipartite Euclidean mean width is maximized uniquely (up to relabeling parts) by the most balanced positive integer profile, and minimized uniquely by \((N-r+1,1,\ldots,1)\). Coincident profiles when \(N=r\) or \(N=r+1\) are understood. Exactly,
\[
\Pr\{L_{\mathbf n}>0\}=\frac{\sum_c n_c(n_c-1)}{N(N-1)}.
\]

**Asymptotic theorem (all fixed numbers of parts \(r\ge3\)).** Suppose \(N\to\infty\), \(n_c/N\to\alpha_c\in(0,1)\) for every \(c\), and \(\sum_c\alpha_c=1\). Put \(a_N=\sqrt{2\log N}\), and \(Z_N=a_N\sqrt{N-1}\,L_{\mathbf n}/2\). Then \(Z_N\) converges in distribution, and in first moment, to a nonnegative random variable \(Z_{\boldsymbol\alpha}\) with the explicit survival function, for all \(t\ge0\),
\[
\boxed{\Pr\{Z_{\boldsymbol\alpha}>t\}
=\sum_{c=1}^r\frac{\alpha_c^2}{[\alpha_c+(1-\alpha_c)e^t]^2}.}
\]
The law has an atom of mass \(1-\sum_c\alpha_c^2\) at zero. In particular, the **exact sharp mean-width correction** is
\[
\boxed{\lim_{N\to\infty}\frac{a_N\sqrt{N-1}}2
\bigl(\mathbb E w_{P_{\rm all}}(U_N)-\mathbb E w_{P_{\mathbf n}}(U_N)\bigr)
=-1-\sum_{c=1}^r\log(1-\alpha_c).}
\]
The entire limiting loss distribution is strictly ordered under any nontrivial majorization of \(\boldsymbol\alpha\): its survival function increases at every \(t\ge0\). In particular, the balanced point \(\alpha_c=1/r\) uniquely minimizes the limiting loss, with expected value \(r\log(r/(r-1))-1\). These assertions concern the width **deficit**, not the (oppositely ordered) width of the polytope itself.

## Assumptions and scope

The finite result requires \(r\ge3\), positive integer part sizes and \(N\ge r\). Gaussian coordinates are independent, continuous and exchangeable; zero-probability ties are excluded. The stochastic comparison is for a fixed \(N,r\) and two positive-integer part profiles ordered by majorization. Spherical widths use the Euclidean structure inherited from \(\mathbb R^N\), not a lattice-normalized or coordinate-dropped Euclidean norm. The asymptotic result requires fixed \(r\) and **all** limiting proportions strictly positive. No claim of the same asymptotic coefficient is made when a part has vanishing proportion or when \(r\) grows.

## Proof

**1. Support function and the cap identity.** Since \(P_{\rm all}\) and \(P_{\mathbf n}\) are centrally symmetric, for every vector \(g\in\mathbb R^N\),
\[
h_{P_{\rm all}}(g)=M-m,\qquad
h_{P_{\mathbf n}}(g)=\max_{i,j\text{ in distinct parts}}(g_i-g_j).
\]
Both expressions ignore constant translations of all coordinates. If the global maximum and minimum lie in different parts the loss is zero. If both lie in part \(c\), write \(M_{\neg c}\) and \(m_{\neg c}\) for the maximum and minimum outside that part. Every admissible cross-part difference is bounded by at least one of \(M-m_{\neg c}\) and \(M_{\neg c}-m\), and both are admissible. Thus
\[
D_{\mathbf n}(g)=\min\{M-M_{\neg c},m_{\neg c}-m\}
\quad\text{if both extrema are in }c,
\]
and it is zero otherwise. Hence \(D_{\mathbf n}(g)>s\) holds **if and only if** all coordinate indices in the union of the two extreme caps \(\{g_i\ge M-s\}\cup\{g_i\le m+s\}\) have one common part label. Since the labels of the ordered independent continuous observations are a uniform permutation of their fixed multiset, the probability that a specific set of \(k\) ranks shares part \(c\) is \((n_c)_k/(N)_k\). Summing over the disjoint alternatives \(c\) proves the conditional formula, including thresholds where the caps overlap. When \(s=0\), the caps contain exactly the distinct minimum and maximum and \(K_0=2\), yielding the stated strict-event probability.

**2. Finite majorization and equality.** For integers \(p\ge q\ge2\), any \(k\ge2\) obeys
\[
\bigl[(p+1)_k+(q-1)_k\bigr]-\bigl[(p)_k+(q)_k\bigr]
=k!\left[\binom p{k-1}-\binom{q-1}{k-1}\right]\ge0,
\]
using zero binomial coefficients outside their range. At \(k=2\) the difference is \(2(p-q+1)>0\). All other part sizes are unchanged, so conditioning on the unordered Gaussian values proves the stochastic order for every threshold. For each fixed \(s<\infty\), the event \(K_s=2\) has positive Gaussian probability (put two values far apart and the remaining values well between them), proving strictness of the unnormalized order. For spherical directions, condition instead on the unordered values and put \(s=t\|g-\bar g\mathbf1\|_2/2\), which is still invariant under rank permutations. The order persists and is strict on a nonempty interval of positive \(t\) near zero; hence expected spherical width loss is strictly increased. Elementary successive transfers take any integer profile to the balanced minimum or the maximally imbalanced \((N-r+1,1,\ldots,1)\), and strictness gives exactly the stated equality classes.

**3. Independent marked upper and lower extremes.** Let \(b_N=\Phi^{-1}(1-1/N)\), where \(\Phi\) is the standard normal distribution function. Mills' inequalities give \(a_N/b_N\to1\) and, for each fixed real \(x\), \(N[1-\Phi(b_N+x/a_N)]\to e^{-x}\). Each fixed part \(c\) therefore generates an upper-tail Poisson point process with intensity \(\alpha_c e^{-x}\,dx\) after normalization \(a_N(g_i-b_N)\). The lower-tail processes of \(a_N(-g_i-b_N)\) have the same intensities and are jointly independent of all upper-tail limits, by the multinomial rare-event calculation for disjoint upper/lower threshold sets. All processes are independent across parts.

The superposed upper points have independently marked colors, with probabilities \(\alpha_c\), and so do the independent lower points. Transform a point at coordinate \(x\) to arrival time \(z=e^{-x}\): the resulting process has unit homogeneous Poisson intensity on \((0,\infty)\). Conditional on the first upper arrival bearing color \(c\), its time \(T\) is \(\operatorname{Exp}(1)\); the waiting time \(E\) to the first arrival outside color \(c\) is independently \(\operatorname{Exp}(1-\alpha_c)\). Thus the upper extreme-to-first-outside gap is \(\log(1+E/T)\), whose survival function equals
\[
\mathbb E\exp\{-(1-\alpha_c)(e^t-1)T\}
=\frac1{\alpha_c+(1-\alpha_c)e^t}.
\]
The lower end has an independent copy, and the two extreme colors both equal \(c\) with probability \(\alpha_c^2\). The deficit is the minimum of the two end gaps in that event and zero otherwise. Squaring this survival, multiplying by \(\alpha_c^2\), and summing proves the limiting survival law. The continuous-mapping step is legitimate because the limiting point processes have almost surely distinct extremal points and a finite first outsider for each color.

**4. Uniform integrability and the sharp mean.** With \(M_c\) the maximum within color \(c\) and \(M_{\neg c}\) the maximum outside it, the finite loss is bounded by
\[
0\le D_{\mathbf n}(g)\le\sum_c(M_c-M_{\neg c})_+.
\]
For each fixed \(c\), both samples defining these maxima have sizes proportional to \(N\). Classical Gaussian tail estimates, proved directly by \(\Pr(M_m>x)\le m[1-\Phi(x)]\) and \(\Pr(M_m<x)=\Phi(x)^m\), together with Mills' bounds, show that \(a_N(M_m-b_N)\) has uniformly bounded second moment whenever \(m/N\) stays in a compact subset of \((0,1]\). This implies \(\sup_N\mathbb E(a_ND_{\mathbf n}(g))^2<\infty\), hence uniform integrability and convergence of means. Projection onto \(H_N\) leaves every root pairing unchanged; the projected standard Gaussian has the independent polar decomposition \(g_H=R_NU_N\), with \(\mathbb E R_N=\sqrt2\,\Gamma(N/2)/\Gamma((N-1)/2)\sim\sqrt{N-1}\). Homogeneity therefore transfers both the limit law and expected loss to \(Z_N=a_N\sqrt{N-1}L_{\mathbf n}/2\).

Integrating the limit survival gives, for \(0<\alpha<1\),
\[
\alpha^2\int_0^\infty\frac{dt}{[\alpha+(1-\alpha)e^t]^2}
=-\log(1-\alpha)-\alpha.
\]
Summing and using \(\sum_c\alpha_c=1\) gives the sharp constant. Finally, for each fixed \(t\ge0\) and \(z=e^t\ge1\), the function \(f_t(x)=x^2/[x+(1-x)z]^2\) satisfies
\[
f_t''(x)=\frac{2z[z+2(z-1)x]}{[z-(z-1)x]^4}>0\quad(0<x<1).
\]
Therefore the limiting survival function \(\sum_c f_t(\alpha_c)\) is strictly Schur-convex; the balanced vector is its unique minimum up to permutation, and integrating preserves that strict order for the expected loss.

## Verification

The accompanying standard-library `verify.py` independently enumerates fixed-multiset label placements for several small three-part profiles and six cap thresholds, computing the graph support maximum directly; all comparisons agree with the exact conditional falling-factorial formula. It checks the transfer inequality over 5,352 integer cases and verifies the closed limiting mean constant against numerical integration of the limiting survival function. A seeded Monte Carlo check of the nonzero-loss probability is corroborative only. Run `python3 verify.py` from the directory containing these files. The probabilistic limit, moment convergence and classification rely on the analytical argument above, not on the finite checks.

## Relationship to prior work

The polytope definition and lattice-geometric motivation belong to D'Alì–Delucchi–Michałek [1], which treats symmetric edge, adjacency and Kantorovich–Rubinstein polytopes and concentrates on combinatorial, volume and Ehrhart invariants. Higashitani–Jochemko–Michałek [2] analyzes facets and Ehrhart theory, including the complete bipartite family and a general multipartite facet framework. Chen–Davis–Korchevskaia [3] relates facets to maximal bipartite subgraphs. These statements do not imply the distributional, conditional-rank or stochastic-majorization conclusions here. A previously established two-part Gaussian directional-width result is an important **covered special case**, not claimed as new: the present originality scope is the \(r\ge3\) all-profile *finite stochastic-order classification* and the marked-multicolor law (including every positive proportion vector). The latter cannot be obtained by a statement restricted to two group sizes without additional analysis of correlated subcuts and simultaneous extremes. Classical Gaussian Poisson convergence and majorization are used as standard tools, not claimed as new. For each of the source texts [1]–[3], relevant definitions and theorem sections were inspected, including their applications to graph joins, complete bipartite facets and facet-subgraphs; no directly covering distributional statement was found in those inspected sections.

## Limitations

The asymptotic law does not address vanishing color proportions, growing numbers of parts, or non-Gaussian directional sampling. The moment-convergence argument assumes every limiting proportion is positive. First-order stochastic dominance does not imply deterministic pointwise inclusion between polytopes with different block profiles under fixed vertex labels. No experimental finite-range check can certify literature-wide priority. Possible earlier treatment under the aliases **restricted sample range**, **colored extreme spacings**, **multipartite root polytope**, or **Kantorovich–Rubinstein polytope** remains a bibliographic risk.

## References

[1] A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (first public 2019-10-11), Electronic Journal of Combinatorics 29(3) (2022), P3.24. https://arxiv.org/abs/1910.05193.

[2] A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (2018-07-20), Mathematika 65 (2019), 763–784. https://arxiv.org/abs/1807.07678.

[3] T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315v1 (2021-07-26), Discrete Applied Mathematics 326 (2023). https://arxiv.org/abs/2107.12315.
