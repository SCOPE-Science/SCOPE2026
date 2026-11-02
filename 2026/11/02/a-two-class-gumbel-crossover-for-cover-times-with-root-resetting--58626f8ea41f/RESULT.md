# A two-class Gumbel crossover for cover times with root resetting on complete bipartite graphs

## Finding

Fix a reset probability \(r\in(0,1)\), and put \(\gamma=1-r\). For each integer \(n\), let \(b_n=n\) and
\[
a_n=\left\lfloor\gamma n+\frac{\lambda n}{\log n}\right\rfloor,
\]
where \(\lambda\in\mathbb R\) is fixed and \(n\) is sufficiently large that \(a_n\ge1\). On the complete bipartite graph \(K_{a_n,b_n}\), start a discrete-time walk at one specified vertex in part \(A\). At each step, independently of the past, reset to this vertex with probability \(r\); otherwise move to a uniformly selected neighbor. Let \(T_{A,n}\) and \(T_{B,n}\) be the first times at which all vertices in the respective parts have been visited, counting the initial root as visited at time zero. Put
\[
s_n=\frac{1+\gamma}{\gamma}n,
\qquad c_\gamma(\lambda)=\gamma\exp(\lambda/\gamma).
\]
Then, as \(n\to\infty\),
\[
\left(\frac{T_{A,n}}{s_n}-\log n,\frac{T_{B,n}}{s_n}-\log n\right)
\ \Longrightarrow\ (G_A+\log c_\gamma(\lambda),G_B),
\]
where \(G_A,G_B\) are independent standard Gumbel variables, each with distribution function \(\exp(-e^{-x})\). In particular, for \(T_n=\max(T_{A,n},T_{B,n})\),
\[
\Pr\!\left(\frac{T_n}{s_n}-\log n\le x\right)
\longrightarrow\exp\!\left(-(1+c_\gamma(\lambda))e^{-x}\right)
\qquad(x\in\mathbb R).
\]
Moreover, if \(L_n\) is the part containing the last newly visited vertex, then
\[
\Pr(L_n=A)\longrightarrow
\frac{c_\gamma(\lambda)}{1+c_\gamma(\lambda)}.
\]
The imbalance scale \(n/\log n\), rather than \(\sqrt n\), separates the two competing extreme-value completion clocks. The location of the transition is set by the resetting probability.

## Assumptions and scope

All edges in \(K_{a_n,b_n}\) are undirected and loopless; multiple vertices may be in either part. Resets consume one discrete time step, take the walker directly to the designated root in part \(A\), and do not clear the visited set. Random move destinations are uniform among all neighbors, independently at each random-move step. The reset indicators are independent Bernoulli variables of fixed parameter \(r\in(0,1)\). The real number \(\lambda\) and the parameter \(r\) are fixed while \(n\) tends to infinity; no uniformity over them is claimed. The first step is indexed as time one.

## Proof

**1. Exact two-stream representation.** Write \(\gamma=1-r\). Irrespective of the identities of the visited vertices, the part containing the walker is a two-state Markov chain with ordered transition matrix
\[
P=\begin{pmatrix}r&\gamma\\1&0\end{pmatrix},
\]
where the states are \(A,B\). Its stationary distribution is
\[
(\pi_A,\pi_B)=\left(\frac1{1+\gamma},\frac\gamma{1+\gamma}\right),
\]
and the nontrivial eigenvalue is \(-\gamma\). Let \(M_A(t)\) count actual random moves from \(B\) to \(A\) among the first \(t\) steps, and let \(M_B(t)\) count actual random moves from \(A\) to \(B\). All other moves are resets to the already-seen root. Conditional on the entire reset-indicator sequence (and hence on the sequence of parts), the destinations of these \(M_A(t)\) moves are independent uniform vertices of \(A\), and those of the \(M_B(t)\) moves are independent uniform vertices of \(B\). The two destination streams are independent of one another and of the reset indicators. In particular, with independent uniform coupon streams in the two parts, the coverage event in each part is determined solely by its stream and its stream count.

The indicator of being in \(B\) at time \(j\) has exponentially decaying covariances because the second eigenvalue is \(-\gamma\). The expected number of transitions \(A\to B\), respectively \(B\to A\) *without resetting*, through time \(t\) therefore satisfies
\[
\mathbb E M_B(t)=\frac\gamma{1+\gamma}t+O_r(1),
\qquad
\mathbb E M_A(t)=\frac{\gamma^2}{1+\gamma}t+O_r(1).
\]
Both counts have variance \(O_r(t)\). For \(M_B\), this follows by summing covariances of the indicator of \(B\)-state arrivals; for \(M_A\), use the indicator of \(B\)-state followed by an independent nonreset coin, or directly sum covariances of the finite-state transition indicators. Thus at \(t=O(n\log n)\) both counts have standard deviation \(O_r(\sqrt{n\log n})=o(n)\).

**2. Exact conditional occupancy and its critical scaling.** Given the count \(M_B(t)=m\), coverage of \(B\) is equivalent to collecting all \(n\) coupons in \(m\) independent uniform draws. Given \(M_A(t)=m\), coverage of \(A\) is equivalent to observing every one of the \(a_n-1\) nonroot coupons in \(m\) independent uniform draws from \(a_n\) possibilities. By inclusion–exclusion, for any nonnegative integer \(m\), the corresponding deterministic coverage probabilities are
\[
F_{B,n}(m)=\sum_{j=0}^{n}(-1)^j\binom nj(1-j/n)^m,
\quad
F_{A,n}(m)=\sum_{j=0}^{a_n-1}(-1)^j\binom{a_n-1}j(1-j/a_n)^m.
\]
At any deterministic times \(t,u\), conditional independence of the streams gives the *exact* joint identity
\[
\Pr(T_{A,n}\le t,\ T_{B,n}\le u)
=\mathbb E\left[F_{A,n}(M_A(t))F_{B,n}(M_B(u))\right].
\]
Let \(t_n(x)=\lfloor s_n(\log n+x)\rfloor\) for fixed \(x\in\mathbb R\), which is nonnegative for all sufficiently large \(n\). The count bounds above yield
\[
\frac{M_B(t_n(x))}{n}-\log n\ \xrightarrow{\Pr}\ x,
\qquad
\frac{M_A(t_n(x))}{a_n}-\log(a_n-1)
\ \xrightarrow{\Pr}\ x-\frac\lambda\gamma-\log\gamma.
\]
Indeed \(M_B(t_n(x))=n(\log n+x)+o_{\Pr}(n)\), \(M_A(t_n(x))=\gamma n(\log n+x)+o_{\Pr}(n)\), and
\[
\frac{\gamma n}{a_n}=1-\frac\lambda{\gamma\log n}+o((\log n)^{-1}),
\qquad
\log(a_n-1)=\log n+\log\gamma+o(1).
\]
For the classical uniform coupon collector on \(m\) equally likely types, the number of missing types after \(m(\log m+z+o(1))\) independent draws converges to \(\operatorname{Poi}(e^{-z})\). This follows, for example, from the exact factorial moments
\[
\mathbb E[(U)_j]=(m)_j(1-j/m)^k
\]
when \(k\) draws have been made; fixed \(j\) gives convergence to \(e^{-jz}\). The same statement holds when one specified coupon is marked as already collected, since deleting a single coupon from the missing count changes its probability by at most \((1-1/m)^k=O(m^{-1})\) at this scale. Monotonicity of coverage in the sample count extends this deterministic result to sample counts with the displayed \(o_{\Pr}(n)\) errors, by sandwiching them between two deterministic counts differing by \(\delta n\) and then letting \(\delta\downarrow0\).

Consequently,
\[
F_{B,n}(M_B(t_n(x)))\ \xrightarrow{\Pr}\ \exp(-e^{-x}),
\]
and
\[
F_{A,n}(M_A(t_n(x)))\ \xrightarrow{\Pr}\
\exp\!\left(-\gamma e^{\lambda/\gamma}e^{-x}\right).
\]
Each factor lies between zero and one. Substituting these limits at possibly different fixed \(x,y\) into the exact joint identity, bounded convergence in probability implies
\[
\Pr(T_{A,n}\le t_n(x),\ T_{B,n}\le t_n(y))
\longrightarrow
\exp(-c_\gamma(\lambda)e^{-x})\exp(-e^{-y}).
\]
This proves joint convergence to independent, shifted standard Gumbels and, on the diagonal \(x=y\), the asserted cover-time distribution.

**3. Last-covered side and the crossover.** Since one step can first visit at most one vertex, the finite random cover times \(T_{A,n},T_{B,n}\) cannot be equal (the root does not make an exception for sufficiently large \(n\), when both parts have other vertices). Thus \(L_n=A\) precisely when \(T_{A,n}>T_{B,n}\). The joint limiting variables have a continuous difference distribution, so the portmanteau theorem yields
\[
\lim_{n\to\infty}\Pr(L_n=A)
=\Pr(G_A+\log c_\gamma(\lambda)>G_B).
\]
For independent standard Gumbels, \(e^{-G_A}\) and \(e^{-G_B}\) are independent mean-one exponentials. Thus the last probability equals \(c_\gamma(\lambda)/(1+c_\gamma(\lambda))\), as claimed. The perturbation \(\lambda n/\log n\) of the part size produces an order-one shift \(\lambda/\gamma\) in the A-side coupon completion clock, explaining the critical window.

## Verification

The standalone `check_reset_biclique.py` implements two mathematically distinct exact finite-state constructions. One propagates a rational-valued Markov distribution over the current labelled vertex and two visited-vertex masks. The other propagates the reset-coin two-state process and the two uniform coupon sample counts, evaluating exact coverage probabilities by inclusion–exclusion. For reset probabilities \(1/4\), \(1/2\) and \(2/3\), all part sizes \(1\le a,b\le4\), and horizons \(0\le t\le8\), the two methods agree on three coverage probabilities per case. Twelve additional rational checks test the part-chain stationary frequencies; six floating-point scaling checks test the limiting centering algebra. The script reports 1314 assertions. These finite computations test decomposition and normalization; they are not used as proof of the asymptotic theorem.

Run with `python3 check_reset_biclique.py` in a standard Python 3 environment; no third-party package is needed.

## Relationship to prior work

Chen and Ye [1] analyze discrete-time network walks with stochastic resetting, including stationary occupation probabilities and mean first-passage times under resetting protocols. Their analysis does not assert the two-part cover-time limit or the critical part-size window derived here. Linn and Lawley [2] study cover times under stochastic resetting, with general-network results in the *frequent-resetting limit for a fixed target network*, not the fixed-reset-probability, growing-bipartite-graph regime of this result. Colombani, Bertagnolli and Artime [3] study self-avoiding walkers whose *memory* resets, a distinct dynamic from moving to a root. Chupeau, Bénichou and Voituriez [4] develop broad Gumbel cover-time asymptotics for random searches, providing relevant extreme-value context without an explicit reset-root bipartite two-intensity crossover. The elementary coupon-collector factorial-moment limit used in the proof is classical and is not asserted as new.

The substantive claim is the explicit joint independent two-class limit for the given reset walk, including the reset-dependent location of the critical window and last-covered-side law. The result should not be interpreted as asserting a universally new coupon-collector limit theorem. A broader general theorem on heterogeneous fast-mixing or Markov-modulated coupon collection might subsume this example; complete historical priority has not been established.

## Limitations

The proof requires a fixed reset probability strictly between zero and one, complete bipartite graphs, resetting to a fixed root in \(A\), independent reset choices, and uniform nonreset neighbor selection. It treats a fixed parameter \(\lambda\) in the \(n/\log n\) critical window. The behavior under vanishing reset rates, nonuniform destinations, more than two classes, growing reset-rate parameters, and arbitrary graphs is not claimed. The limiting laws have been analytically established for these assumptions, but their historical novelty and independent validation remain open.

## References

1. H. Chen and Y. Ye, *Random walks on complex networks under time-dependent stochastic resetting*, arXiv:2208.06212, initially public 2022-08-12. https://arxiv.org/abs/2208.06212
2. S. Linn and S. D. Lawley, *Cover times with stochastic resetting*, arXiv:2406.12154, initially public 2024-06-17. https://arxiv.org/abs/2406.12154
3. G. Colombani, G. Bertagnolli and O. Artime, *Efficient network exploration by means of resetting self-avoiding random walkers*, arXiv:2310.03203, initially public 2023-10-04. https://arxiv.org/abs/2310.03203
4. M. Chupeau, O. Bénichou and R. Voituriez, *Cover times of random searches*, arXiv:1511.06173, initially public 2015-11-19. https://arxiv.org/abs/1511.06173
