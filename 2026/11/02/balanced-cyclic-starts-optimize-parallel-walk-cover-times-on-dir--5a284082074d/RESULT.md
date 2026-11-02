# Balanced cyclic starts optimize parallel-walk cover times on directed periodic networks

## Finding

For integers \(d\ge 3\), \(n\ge 2\), and \(k\ge 1\), consider the directed network with \(d\) disjoint classes \(V_0,\ldots,V_{d-1}\), each containing \(n\) vertices. Every vertex of \(V_j\) has an arc to every vertex of \(V_{j+1\pmod d}\), and there are no other arcs. Run \(k\) independent synchronous simple random walks, recording their initial locations at time \(0\). Choose a deterministic start-class allocation \(h=(h_0,\ldots,h_{d-1})\) with nonnegative integer coordinates summing to \(k\); within the chosen class, each initial vertex is selected independently and uniformly. Let \(T_h\) be the first time at which every vertex has been visited by some walk.

Write \(F_n(r)=n!S(r,n)/n^r\), with \(F_n(r)=0\) when \(r<n\), where \(S(r,n)\) is a Stirling number of the second kind. For every integer \(t\ge 0\), write \(t+1=qd+s\) with \(0\le s<d\), and put

\[
M_j(t,h)=qk+\sum_{a=0}^{s-1}h_{(j-a)\bmod d}.
\]

Then the exact cover-time distribution is

\[
\mathbb P(T_h\le t)=\prod_{j=0}^{d-1}F_n(M_j(t,h)). \tag{1}
\]

Define the mechanical starting allocation

\[
h_j^\star=\left\lfloor\frac{(j+1)k}{d}\right\rfloor-\left\lfloor\frac{jk}{d}\right\rfloor,\qquad 0\le j<d.
\]

For every \(h\) and every time \(t\),

\[
\mathbb P(T_h\le t)\le\mathbb P(T_{h^\star}\le t). \tag{2}
\]

Moreover, equality in (2) **simultaneously for every integer time** holds if and only if, for each \(1\le s<d\), the \(d\) circular window sums

\[
W_{j,s}(h)=\sum_{a=0}^{s-1}h_{(j-a)\bmod d}
\]

have maximum minus minimum at most \(1\). Thus (2) gives a stochastic optimum, and the window criterion characterizes all start-class allocations with the same optimal cover-time law. Any violation of the criterion produces a strictly smaller cover probability at some finite time.

There is an explicit *macroscopic-start penalty*. Fix \(d\) and a residue \(s\in\{0,\ldots,d-1\}\). Suppose \(n\to\infty\), \(k_n/n\to\lambda\in(0,\infty)\), and \(h_{j,n}/k_n\to p_j\), with \(p_j\ge0\) and \(\sum_jp_j=1\). Along any integer sequence \(q_n\) for which

\[
x_n=\frac{k_n}{n}\left(q_n+\frac{s}{d}\right)-\log n\longrightarrow x\in\mathbb R,
\]

define \(a_{j,s}=\sum_{a=0}^{s-1}p_{(j-a)\bmod d}\). Then

\[
\lim_{n\to\infty}\mathbb P(T_{h_n}\le q_nd+s-1)
=\exp\left[-e^{-x}\sum_{j=0}^{d-1}
\exp\left(-\lambda\left(a_{j,s}-\frac{s}{d}\right)\right)\right]. \tag{3}
\]

The coefficient of \(e^{-x}\) in (3) is at least \(d\), and is exactly \(d\) if and only if every \(a_{j,s}=s/d\). In particular, at residue \(s=1\) this occurs only for uniform start proportions \(p_j=1/d\), whereas mechanical starts attain the value \(d\) at *every* residue. The formulation is necessarily subsequential, because integer cover times retain a lattice phase when \(k_n/n\to\lambda>0\).

The equal-class-size hypothesis is material. For a directed three-class cycle with class sizes \((2,2,3)\) and \(k=2\), the unique start allocation maximizing the probability of complete coverage by time \(3\) is \((0,0,2)\), with probability \(1/9\), while the unique maximizer at time \(4\) is \((0,1,1)\), with probability \(1/4\). Hence in this unequal-class-size example no start allocation stochastically dominates all others.

## Assumptions and scope

The network is a finite **directed**, deterministic, complete cyclic multipartite graph. At each step a walker jumps to an independently and uniformly sampled vertex in the next class; transition choices are independent across walkers and times. Start classes may be chosen deterministically, but conditioned on their classes the actual starting vertices are independent uniform samples, with replacement. Coverage includes time-zero observations. The comparison concerns the whole cover-time distribution in the usual stochastic order; it does not assume stationary or deterministic initial vertices inside a class. There is no restriction that \(k\le n\) or \(k\le d\).

## Proof

**1. Exact independent-occupancy reduction.** For any walker started in class \(V_i\), the class occupied at time \(r\) is deterministically \(V_{i+r\bmod d}\). Its vertex at each time is uniform within that class and independent of its previously observed vertex; the same independence is assumed initially and across walkers. Therefore all vertex labels observed within one class form independent uniform draws, and the label arrays for distinct classes are independent. During \(t+1=qd+s\) rounds, every walker visits every class \(q\) times, plus one visit in each of its first \(s\) successive classes. Consequently class \(j\) receives exactly \(M_j(t,h)\) draws. The number of onto functions from an \(r\)-set of labeled draws to \(n\) vertices is \(n!S(r,n)\), proving (1), including \(r<n\).

**2. Strict log-concavity of the coupon completion CDF.** Let \(\tau_n\) be the number of independent uniform draws needed to see all \(n\) coupon types. Its probability mass sequence \(b_r=\mathbb P(\tau_n=r)\), \(r\ge n\), is positive and log-concave. To verify this, write \(\tau_n\) as a sum of independent geometric waiting times with success probabilities \(1, (n-1)/n,\ldots,1/n\). Each geometric mass sequence is log-concave with interval support; convolution preserves this property. One direct proof of the latter uses the Toeplitz matrix of a nonnegative log-concave interval-supported sequence: monotone adjacent ratios imply every ordered \(2\times2\) minor is nonnegative. The Toeplitz matrix of the convolution is the product of the two Toeplitz matrices. The Cauchy–Binet identity then makes every such minor nonnegative. For any finite index under consideration, truncate the geometric tails beyond the relevant index, so only finite matrices are required.

Since \(b_r>0\) for \(r\ge n\), log-concavity implies \(b_{r+1}b_m\ge b_rb_{m+1}\) whenever \(n\le r\le m\). As \(F_n(m)=\sum_{r=n}^m b_r\), for \(m\ge n\) we obtain

\[
\begin{aligned}
F_n(m)^2-F_n(m-1)F_n(m+1)
&=F_n(m)b_m-F_n(m-1)b_{m+1}\\
&\ge F_n(m)b_m-(F_n(m)-b_n)b_m\\
&=b_nb_m>0.
\end{aligned}
\]

Here the inequality uses \(b_r b_{m+1}\le b_{r+1} b_m\) term by term for \(n\le r<m\). The strict inequality also holds at \(m=n\), since \(F_n(n-1)=0\). Before the first positive index the CDF vanishes. Thus redistributing a fixed total number of draws to make all class counts differ by at most one weakly increases their product, and the increase is strict whenever all counts in both compared configurations are at least \(n\) and the original counts are not balanced. This follows by repeatedly transferring one draw from a count at least two larger to a smaller count and applying the strict inequality \(F_n(a-1)F_n(b+1)>F_n(a)F_n(b)\) when \(a\ge b+2\) and both relevant counts are at least \(n\). When some counts are below \(n\), the original product is zero and the weak statement remains valid.

**3. A single construction balances every time horizon.** Extend \(h^\star\) periodically to all integers. Because \(k\) is an integer, the floor difference defining \(h^\star_j\) is periodic with period \(d\). Every circular window of \(s\) entries telescopes to a difference of two floors at arguments separated by \(sk/d\), and hence is one of \(\lfloor sk/d\rfloor\) and \(\lceil sk/d\rceil\). Thus the counts \(M_j(t,h^\star)\) differ by at most one. Their sum is \(k(t+1)\) for any allocation \(h\). The fixed-sum product inequality from Step 2 proves (2).

**4. Necessity of the circular-window condition.** If every circular window profile is balanced, then \(M_j(t,h)\) is balanced for every \(t\), giving equality in (2). Conversely, suppose for some \(1\le s<d\) its window profile has spread at least two. Take \(t=qd+s-1\) and choose \(q\) so large that every count \(M_j(t,h)\) and \(M_j(t,h^\star)\) is at least \(n\). They have the same sum, but the first vector is not balanced while the second is. By strict log-concavity, its product is strictly smaller; hence the corresponding time has strict inequality in (2). This proves the if-and-only-if statement.

**5. Macroscopic density and the lattice penalty.** If \(r_n=n\log n+zn+o(n)\), the number \(U_n\) of coupons not yet seen after \(r_n\) independent uniform draws satisfies, for every fixed positive integer \(r\),

\[
\mathbb E[(U_n)_{\underline r}]=(n)_{\underline r}(1-r/n)^{r_n}\longrightarrow e^{-rz}.
\]

The factorial moments identify a Poisson distribution with mean \(e^{-z}\), yielding \(F_n(r_n)\to\exp(-e^{-z})\). From (1),

\[
\frac{M_j(q_nd+s-1,h_n)}{n}-\log n
=x_n+\frac{k_n}{n}\left(\sum_{a=0}^{s-1}\frac{h_{(j-a)\bmod d,n}}{k_n}-\frac{s}{d}\right).
\]

Apply the preceding Poisson limit to each of the finitely many independent classes and multiply to prove (3). Summing the bracketed offsets over all classes gives zero, so Jensen's inequality proves the coefficient bound and its equality condition. At \(s=1\), the window proportions are precisely the individual \(p_j\), implying the uniqueness assertion. The mechanical class allocations differ from \(k_n/d\) by less than \(1\), so their limiting proportions are uniform.

**6. Equal-size boundary check.** With class sizes \((2,2,3)\), the same independent-occupancy argument gives the product of \(F_2\), \(F_2\), and \(F_3\) at the corresponding class visit counts. Evaluating the six possible allocations of two walkers produces:

| Allocation \(h\) | \(\mathbb P(T_h\le3)\) | \(\mathbb P(T_h\le4)\) |
|---|---:|---:|
| \((0,0,2)\) | \(1/9\) | \(7/36\) |
| \((0,1,1)\) | \(1/12\) | \(1/4\) |
| \((0,2,0)\) | \(0\) | \(7/36\) |
| \((1,0,1)\) | \(1/12\) | \(7/48\) |
| \((1,1,0)\) | \(0\) | \(7/48\) |
| \((2,0,0)\) | \(0\) | \(0\) |

The strict and incompatible maximizers at the two time horizons establish the claimed absence of a universal optimizer.

## Verification

The standalone standard-library program `check_cyclic_cover.py` prints `PASS: 190,907 exact finite assertions`. It verifies strict coupon-CDF log-concavity at rational arithmetic precision for \(2\le n\le12\); telescoping mechanical balance for \(3\le d\le16\) and \(1\le k\le38\); exhaustive allocation comparisons and the optimality criterion for \(2\le n\le5\), \(3\le d\le6\), \(1\le k\le6\); and direct enumeration of underlying walker trajectories for representative small configurations, independent of the occupancy-product formula. The unequal-class example above was checked by exact fractional arithmetic. These finite calculations check arithmetic and boundary conventions; the proofs for unrestricted integer parameters are in Steps 1–6.

## Relationship to prior work

Rivera, Sauerwald and Sylvester (2020) establish bounds for many parallel walkers on general finite *undirected* networks, considering stationary and worst-case starts; they do not provide a stochastic ordering of all deterministic class-count allocations for the directed periodic network here, nor its equality classification or macroscopic allocation penalty. Kim and Lawley (2023) study moments of cover times for many *continuous-time* Markovian searchers on discrete networks in a distinct large-searcher regime and likewise do not state this circular-class allocation theorem. Alon and collaborators' earlier multiple-walk framework concerns speedups in undirected graphs. Coupon occupancy formulas and log-concavity are classical ingredients, not claimed as new. The proposed contribution is the joint all-horizon stochastic-optimal allocation classification, its period-sensitive macroscopic penalty, and the sharp unequal-class boundary.

## Limitations

Uniform random initial vertices *within* each predetermined class are essential for the exact independent-occupancy factorization. The theorem is for synchronous, non-lazy, directed complete cyclic transitions and identical class sizes; it does not classify optimal placement of deterministic individual starting vertices, arbitrary directed graphs, unequal class sizes, continuous-time walkers, or nonsynchronous movement. The limiting law applies only along integer time subsequences satisfying the stated lattice-centering hypothesis. The example demonstrates a failure of universal optimization for one unequal-size graph, not for every such graph. No independent mathematical audit has been performed, and historical priority beyond the searched literature remains a risk.

## References

1. N. Rivera, T. Sauerwald, J. Sylvester, *Multiple Random Walks on Graphs: Mixing Few to Cover Many*, arXiv:2011.07893, first posted 2020-11-16. https://arxiv.org/abs/2011.07893
2. H. Kim, S. D. Lawley, *Cover times of many random walkers on a discrete network*, arXiv:2310.07905, first posted 2023-10-11. https://arxiv.org/html/2310.07905
3. N. Alon et al., *Many Random Walks Are Faster Than One*, arXiv:0705.0467, first posted 2007-05-03. https://arxiv.org/abs/0705.0467
