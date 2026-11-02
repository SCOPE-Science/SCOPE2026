# Universal Gumbel coverage for uniformly sampled edges of regular graphs

## Finding

Let \(G_n\) be **any** finite simple \(d_n\)-regular graph on \(n\) vertices, not necessarily connected. At each integer round sample one edge independently and uniformly, and permanently mark both endpoints. Let \(K_n\) be the first number of rounds by which every vertex is marked. Assume only that \(2\le d_n\le n-1\) and \(nd_n\) is even. For every fixed real \(x\),

\[
\sup_{G_n}\left|\Pr\left(\frac{2K_n}{n}-\log n\le x\right)-\exp(-e^{-x})\right|\longrightarrow0,
\]

where the supremum is over all simple regular graphs of admissible degree at least two. The conclusion holds for degrees varying arbitrarily with \(n\), including disconnected unions of cycles and complete graphs. Furthermore, uniformly over this family,

\[
\mathbb E K_n=\frac n2\left(\log n+\gamma_E+o(1)\right),
\]

where \(\gamma_E\) is Euler's constant.

A quantitative statement holds for the rate-one continuous-time Poissonization. Let \(W_n(x)\) count vertices not marked by time
\(t_n(x)=\frac n2(\log n+x)\), whenever this time is nonnegative, and put \(\lambda=e^{-x}\). For every simple \(d\)-regular graph on \(n\) vertices with \(d\ge1\),

\[
\begin{aligned}
\mathbb E W_n(x)&=\lambda,\\
\operatorname{Var}W_n(x)&=\lambda-\frac{\lambda^2}{n}
+\frac{d\lambda^2}{n}\left(\exp\left(\frac{\log n+x}{d}\right)-1\right).
\end{aligned}
\]

For \(d\ge2\) the following **uniform total-variation bound** holds:

\[
 d_{\mathrm{TV}}\bigl(\mathcal L(W_n(x)),\operatorname{Poi}(\lambda)\bigr)
 \le (1-e^{-\lambda})\frac{\lambda}{n}
 \left[1+d\left(\exp\left(\frac{\log n+x}{d}\right)-1\right)\right]
 \le (1-e^{-\lambda})\frac{\lambda}{n}
 \left[2\exp\left(\frac{\log n+x}{2}\right)-1\right].
\]

Thus the error is \(O_x(n^{-1/2})\) independently of degree and graph topology. The first two moments are exactly determined by order and degree, even though the entire finite-volume law can depend on graph topology.

The degree threshold is exact. For \(d_n=1\), the graph is a perfect matching and the unmarked-vertex count is always even. If \(n\) is even, then

\[
 \Pr\left(\frac{2K_n}{n}-\log n\le x\right)
 \longrightarrow \exp\left(-\frac12e^{-x}\right),
 \qquad
 \mathbb E K_n=\frac n2 H_{n/2}
 =\frac n2(\log n+\gamma_E-\log 2+o(1)).
\]

Hence replacing regular degree two by regular degree one changes the limiting location by exactly \(\log2\), despite the same two-vertex size of every sampled coupon.

## Assumptions and scope

An edge sample is with replacement and independent from all preceding samples. There are no loops or parallel edges and the sampling law is uniform over actual edges. The graph can change with \(n\); no connectivity, expansion, girth or symmetry assumption is imposed beyond regularity. The weak-limit and expectation assertions are as \(n\to\infty\) through admissible simple regular graphs. The quantitative total-variation estimate concerns a rate-one Poisson arrival clock and requires \(\log n+x\ge0\). The discrete-time limit follows by de-Poissonization, not by treating multinomial edge counts as independent.

## Proof

**1. Exact Poissonized edge statuses.** Write \(m=nd/2\). Run a rate-one Poisson process of sampling times and label every arrival by an independent uniformly selected edge. Poisson thinning gives independent edge-arrival processes of rate \(1/m\). At a deterministic time \(t\), let \(Q_e\) indicate that edge \(e\) has not appeared. Then the \(Q_e\) are independent Bernoulli variables of parameter \(q=\exp(-t/m)\). The unmarked indicator for vertex \(v\) is

\[
I_v=\prod_{e\ni v}Q_e,
\qquad W=\sum_{v\in V(G)}I_v,
\qquad p=\mathbb E I_v=q^d.
\]

For two distinct vertices \(v,w\), their incident-edge sets overlap in exactly one edge if \(vw\in E(G)\), and otherwise in no edges. Thus

\[
\mathbb E(I_vI_w)=\begin{cases}p^2/q,&vw\in E(G),\\p^2,&vw\notin E(G).\end{cases}
\]

Summing the \(nd\) ordered adjacent pairs proves, for every finite regular graph and every \(0<q\le1\),

\[
\mathbb EW=np,
\quad \operatorname{Var}W=np(1-p)+ndp^2(q^{-1}-1).
\]

Taking \(t=\frac n2(\log n+x)\) gives \(q=\exp[-(\log n+x)/d]\) and \(p=e^{-x}/n\), yielding the stated finite formulas.

**2. Explicit size-biased coupling.** Choose a vertex \(V\) uniformly, independently of all edge statuses. Set all incident-edge indicators \(Q_e\) at \(V\) to one, leaving all other indicators unchanged. Let \(W^{\mathrm s}\) be the resulting unmarked count. Independence of edge statuses and uniformity of \(p\) imply

\[
\mathbb E[Wf(W)]=np\,\mathbb E[f(W^{\mathrm s})]
\]

for every bounded function \(f\), so \(W^{\mathrm s}\) has the \(W\)-size-biased law. The modification can only create unmarked vertices, so \(W^{\mathrm s}\ge W\). Write \(D=W^{\mathrm s}-W\). If \(I_V=1\), then \(D=0\). Otherwise \(D=1+Z\), where \(Z\) is the number of *other* vertices newly unmarked by the modification. A vertex not adjacent to \(V\) cannot be newly unmarked; for each of its \(d\) neighbors, the change in its unmarked probability is precisely \(p(q^{-1}-1)\). Consequently,

\[
\mathbb E|W+1-W^{\mathrm s}|=p+\mathbb EZ
=p\{1+d(q^{-1}-1)\}.
\]

The standard Poisson size-bias Stein inequality, obtained by solving the Poisson Stein equation and using its first-difference factor \((1-e^{-\lambda})/\lambda\), states

\[
 d_{\mathrm{TV}}(\mathcal L(W),\operatorname{Poi}(\lambda))
 \le(1-e^{-\lambda})\mathbb E|W+1-W^{\mathrm s}|,
 \qquad \lambda=\mathbb EW.
\]

Combining it with the previous identity proves the first total-variation bound. For positive \(u\), the function \(z\mapsto z(e^{u/z}-1)\) is strictly decreasing: its derivative is \(e^{u/z}(1-u/z)-1<0\). Since \(d\ge2\), substitute \(u=\log n+x\) to obtain the second bound. For fixed \(x\), it is \(O_x(n^{-1/2})\), uniformly over all admissible degrees and graphs. This proves the Poisson limit of \(W_n(x)\), and since full coverage means \(W_n(x)=0\), the continuous-time Gumbel law follows.

**3. De-Poissonization.** Label the sampled edges in their independent arrival order. The label sequence has exactly the discrete-time sampling law. The continuous completion time \(\tau_n\) satisfies \(\tau_n=E_1+\cdots+E_{K_n}\), where the \(E_i\) are independent rate-one exponential interarrival times independent of the labels. A first-moment union bound gives, for every admissible regular graph,

\[
\Pr(K_n>n\log n)\le n(1-2/n)^{\lfloor n\log n\rfloor}\le n^{-1+o(1)}.
\]

Conditional on \(K_n\), the centered sum \(\tau_n-K_n\) has variance \(K_n\). Chebyshev's inequality on \(\{K_n\le n\log n\}\) therefore yields \((\tau_n-K_n)/n\to0\) in probability, uniformly over the graph family. The asserted discrete-time Gumbel limit follows.

**4. The order-\(n\) mean constant.** We show uniform integrability of \(Y_n=2\tau_n/n-\log n\). For \(a\ge0\), the same first-moment argument gives \(\Pr(Y_n>a)\le e^{-a}\). For \(0\le a\le\log n\), take \(x=-a\), so \(\lambda=e^a\). Full coverage and Chebyshev's inequality give

\[
\Pr(Y_n<-a)\le\frac{\operatorname{Var}W_n(-a)}{(\mathbb EW_n(-a))^2}
\le e^{-a}+\frac{d}{n}\left(\exp\left(\frac{\log n-a}{d}\right)-1\right)
\le e^{-a}+2n^{-1/2}e^{-a/2}.
\]

For \(a>\log n\), the probability is zero because \(\tau_n\ge0\). Integrating both tail bounds proves that the contribution of \(\{|Y_n|>A\}\) to \(\mathbb E|Y_n|\) vanishes as \(A\to\infty\), uniformly in the large-\(n\) limit. Since \(Y_n\) converges to the standard Gumbel law, whose mean is \(\gamma_E\), we obtain \(\mathbb E\tau_n=\frac n2(\log n+\gamma_E+o(1))\). Finally, independence of edge labels and the exponential interarrival times implies \(\mathbb E\tau_n=\mathbb E K_n\), completing the mean result.

**5. The degree-one obstruction.** A simple one-regular graph with \(n\) vertices is a disjoint union of \(m=n/2\) edges. Sampling edges uniformly is the classical \(m\)-type coupon collector; when an edge is collected, both its vertices are marked together. In continuous time, the number of untouched edges is binomial with parameters \(m\) and \(\exp(-t/m)\), and \(W=2\) times that count. At \(t=\frac n2(\log n+x)\), the binomial converges to \(\operatorname{Poi}(e^{-x}/2)\); thus the coverage probability tends to \(\exp(-e^{-x}/2)\). The elementary coupon-collector expectation is \(mH_m\). The same de-Poissonization argument gives the discrete-time limit.

## Verification

The standalone standard-library program `verify.py` enumerates independent untouched-edge configurations with rational probabilities on triangles, cycles, disconnected regular graphs, complete graphs, bipartite graphs and three-dimensional prism examples. It checks the exact first and second moments and, independently, exact discrete-time completion probabilities against inclusion–exclusion. It tests the Poisson coupling inequality numerically, including examples with different finite-volume laws but equal order and degree, and checks the monotonicity used in the uniform error bound. On execution it reports 593 passed assertions/checks. These finite checks corroborate the algebra but are **not** used as proofs of the asymptotic assertions; those are established above.

## Relationship to prior work

Betken and Thäle (first posted 2022-02-15; published 2023) prove quantitative Poisson/normal approximation for *all* equally probable fixed-size groups, using a size-biased construction. Uniform sampling over the edges of an arbitrary sparse regular graph is not uniform over all pairs: most pairs may have probability zero. Their Theorems 1 and 2 therefore do not state or directly instantiate the present graph-uniform bound. Schilling and Henze (2021), Section 3, allow perturbations of the fully uniform group distribution of order \(1/\log n\) **on each group**; the zero weights of absent edges are outside that model. Falgas-Ravry, Larsson and Markström (first posted 2016), Section 3, give general sharp *first-order concentration* criteria for structured coupons, not the stated Gumbel profile, exact variance or uniform finite-rate estimate. The standard Poisson Stein factor is a known tool; the graph-specific coupling, cancellation, uniform-degree boundary and coverage consequences are the mathematical claims here.

The comparison is statement-level rather than title-level. A general theorem encompassing all balanced dependent two-element coupons under arbitrary sparse support could subsume the claimed limit; such historical coverage is not excluded by the searches alone, and an independent literature review remains necessary.

## Limitations

The result does not treat irregular graphs, weighted edge laws, edge samples dependent across rounds, directed graphs, or multi-coverage of each vertex. In the continuous-time statement, the error bound concerns the count of unmarked vertices at one deterministic time, not full process-level total-variation approximation. No exact discrete-time \(O(n^{-1/2})\) bound is claimed; the discrete-time Gumbel convergence uses de-Poissonization. The expectation error is \(o(n)\) with no asserted universal finite-size coefficient. The degree-one formula is a classical coupon-collector reduction, presented to show the sharp structural boundary, not as a new standalone theorem. Historical novelty has not been independently certified.

## References

1. C. Betken and C. Thäle, “Approaching the coupon collector's problem with group drawings via Stein's method,” arXiv:2202.07485, first submitted 15 February 2022; *Journal of Applied Probability* 60 (2023), 1352–1366. https://arxiv.org/abs/2202.07485 ; https://doi.org/10.1017/jpr.2023.6
2. J. Schilling and N. Henze, “Two Poisson limit theorems for the coupon collector's problem with group drawings,” *Journal of Applied Probability* 58 (2021), 966–977. Full text: https://www.math.kit.edu/stoch/~henze/seite/aiwz/media/ap-17926-final.pdf
3. V. Falgas-Ravry, J. Larsson and K. Markström, “Speed and concentration of the covering time for structured coupon collectors,” arXiv:1601.04455, first submitted 18 January 2016; *Advances in Applied Probability* 52 (2020), 433–462. https://arxiv.org/abs/1601.04455
4. A. D. Barbour, L. Holst and S. Janson, *Poisson Approximation*, Oxford University Press, 1992 (standard size-bias/Stein bounds).
