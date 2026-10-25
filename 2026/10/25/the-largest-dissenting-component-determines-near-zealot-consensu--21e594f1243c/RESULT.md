# The largest dissenting component determines near-zealot consensus lifetimes

## Finding

**Theorem (rare-preference consensus law).** Consider the continuous-time partisan imitation process defined below on any finite connected simple graph. Let \(A\) be the nonempty set of permanently positive agents and let the initially negative agents form components \(C_1,\ldots,C_q\) of the induced graph on \(B=V\setminus A\). Set \(m_j=|C_j|\) and \(m_*=\max_j m_j\). There are explicit strictly positive rational constants \(k_j\), defined by the finite subset recursion below, such that as the strength of the negative preference approaches its zealot limit, \(\delta\downarrow0\),

\[
\delta^{m_*}\tau_\delta\ \Longrightarrow\ \max_{j:m_j=m_*} X_j,
\]

where the \(X_j\) are independent exponential random variables of rates \(k_j\). Moreover,

\[
\lim_{\delta\downarrow0}\delta^{m_*}\mathbb E\tau_\delta
=\int_0^\infty\!\left[1-\prod_{j:m_j=m_*}(1-e^{-k_jt})\right]dt.
\]

In particular, the **power-law divergence exponent** of the expected consensus time is \(m_*\): the largest connected initially dissenting component, rather than the total number of dissenters. The result holds for every fixed finite connected graph and every nonempty proper zealot set, with no graph regularity assumption.

## Assumptions and scope

Let \(G=(V,E)\) be a finite connected simple undirected graph with at least two vertices. Fix a nonempty proper vertex set \(A\subset V\) of permanent agents of opinion \(+1\). Every vertex in \(B=V\setminus A\) initially has opinion \(-1\), and all such vertices have the same fixed personal preference \(h=-1+\delta\), with \(0<\delta<2\). Each \(B\)-vertex has its own rate-one Poisson clock. Upon a clock ring, it chooses one neighbor uniformly and copies the neighbor's opinion with probability \((1+h\sigma_{\rm neighbor})/2\), where \(\sigma_{\rm neighbor}\in\{-1,+1\}\); otherwise its opinion does not change. Vertices in \(A\) never update. The random time \(\tau_\delta\) is the first time every vertex has opinion \(+1\). All clocks and random choices are independent. For each fixed \(\delta>0\), this state is reached almost surely and has finite mean first-passage time.

Write \(d_v=|N(v)|\), \(z_v=|N(v)\cap A|\). For every connected component \(C\) of \(G[B]\) and every subset \(S\subseteq C\), define

\[
b_v(S)=\frac{z_v+|N(v)\cap S|}{d_v}\quad(v\in C\setminus S),
\qquad
q_C(S)=\sum_{u\in S}\frac{|N(u)\cap(C\setminus S)|}{d_u}
\quad(\varnothing\ne S\subsetneq C).
\]

Define the finitely many values \(H_C(S)\) backward from \(H_C(C)=1\) by

\[
H_C(S)=\frac{\displaystyle\sum_{v\in C\setminus S}b_v(S)H_C(S\cup\{v\})}{2q_C(S)}
\qquad(\varnothing\ne S\subsetneq C).
\]

The strictly positive component rate is

\[
k_C=\frac12\sum_{v\in C}\frac{z_v}{d_v}H_C(\{v\}).
\]

The recursion is well-defined because any nonempty proper subset of a connected component has an internal outgoing edge, so \(q_C(S)>0\). At least one vertex of each component is adjacent to \(A\), so \(k_C>0\). The coefficients are rational numbers for finite simple graphs.

## Proof

**1. Exact component generators.** Fix a connected component \(C\) of size \(m\), and let \(S\subseteq C\) record its currently positive vertices. A negative vertex \(v\notin S\) becomes positive at rate \(\delta b_v(S)/2\). A positive vertex \(u\in S\) becomes negative at rate \((1-\delta/2)|N(u)\cap(C\setminus S)|/d_u\). All other neighbor selections cause no state change. Every edge incident to another component of \(G[B]\) is absent by the definition of components; the agents in \(A\) are fixed. Consequently the component chains are independent and their all-positive states are absorbing. Since the whole graph is connected, each component receives some positive zealot neighbors, so the finite chain has no other closed communicating class when \(\delta>0\).

**2. A small-rate hitting expansion.** Let \(h_\delta(S)\) be the probability that the component chain starting from a nonempty subset \(S\) hits \(C\) before returning to \(\varnothing\). At \(\delta=0\), the chain on the nonempty proper states only loses positive vertices. Each such state has total loss rate \(q_C(S)>0\) and therefore hits \(\varnothing\) in finite time. The transient generator at \(\delta=0\), ordered by subset cardinality, is triangular with strictly negative diagonal and thus invertible. Perturbation of this finite linear system makes all hitting probabilities analytic at \(\delta=0\). For any nonempty \(S\subsetneq C\), the first-step equation is

\[
\begin{aligned}
0={}&\frac{\delta}{2}\sum_{v\in C\setminus S}b_v(S)\bigl(h_\delta(S\cup\{v\})-h_\delta(S)\bigr)\\
&+(1-\delta/2)\sum_{u\in S}\frac{|N(u)\cap(C\setminus S)|}{d_u}
\bigl(h_\delta(S\setminus\{u\})-h_\delta(S)\bigr),
\end{aligned}
\]

with \(h_\delta(\varnothing)=0\), \(h_\delta(C)=1\). Any successful path must make at least \(m-|S|\) positive flips. This bounds \(h_\delta(S)=O(\delta^{m-|S|})\), uniformly over the finitely many subsets. Substituting into the first-step equation and inducting downward on \(|S|\) yields

\[
h_\delta(S)=\delta^{m-|S|}H_C(S)+O(\delta^{m-|S|+1}),
\]

because the lowest-order terms are \(q_C(S)H_C(S)\) from losses and \(\tfrac12\sum_{v\notin S}b_v(S)H_C(S\cup\{v\})\) from positive flips. This also holds for \(S=C\) with \(H_C(C)=1\). Positivity of \(k_C\) follows from an ordering of vertices starting at any zealot-adjacent vertex and expanding through the connected graph \(G[C]\).

**3. Excursions and exponential limit.** From \(\varnothing\), the rate of the first positive flip is \(\delta r_C\), where

\[
r_C=\frac12\sum_{v\in C}z_v/d_v>0.
\]

Conditional on a flip, the new state is \(\{v\}\) with probability \((z_v/d_v)/(2r_C)\). The probability that an excursion succeeds before a return to \(\varnothing\) is therefore

\[
p_\delta=\sum_{v\in C}\frac{z_v}{2r_Cd_v}h_\delta(\{v\})
=\delta^{m-1}\frac{k_C}{r_C}+O(\delta^m).
\]

Each attempt consists of an exponential waiting time of mean \((\delta r_C)^{-1}\) at \(\varnothing\), followed by an excursion that hits either \(C\) or \(\varnothing\). The numbers of attempts until success form a geometric law of parameter \(p_\delta\). At \(\delta=0\) every nonempty proper state reaches \(\varnothing\) through downward transitions with positive rates; finite-state perturbation implies that excursion lengths have uniformly bounded first and second moments for sufficiently small \(\delta\). Summing the waiting times for the geometric number of attempts gives an **exact exponential variable** of rate \(\delta r_Cp_\delta=k_C\delta^m+O(\delta^{m+1})\). The total time spent on excursions is \(O(\delta^{-(m-1)})\) in expectation, negligible on the \(\delta^{-m}\) scale. By Markov's inequality and the exponential identity,

\[
\delta^m\tau_C\ \Longrightarrow\ \operatorname{Exp}(k_C),
\qquad
\delta^m\mathbb E\tau_C\longrightarrow 1/k_C.
\]

The same conclusion holds for \(m=1\), where each excursion succeeds immediately. The geometric-renewal decomposition and the bounded second moments of excursions also give uniformly bounded second moments for \(\delta^m\tau_C\), establishing uniform integrability.

**4. Several components.** Independent Poisson clocks imply independence of the component absorption times. The global hitting time is their maximum. For components of size smaller than \(m_*\), their absorption times vanish when multiplied by \(\delta^{m_*}\), in probability and in \(L^1\). The components of maximal size converge jointly to independent exponentials of rates \(k_j\). Their maximum therefore has the asserted limiting distribution. Uniform integrability of their scaled maxima gives the stated expectation limit. For independent exponential variables, the survivor function of their maximum is precisely \(1-\prod(1-e^{-k_jt})\), completing the proof.

## Verification

The accompanying standalone `verify.py` builds the subset-generator for finite graphs, solves exact-rational mean hitting times symbolically, independently evaluates the recursion for \(k_C\), and checks the predicted leading asymptotics. It covers a star, a clique, two three-agent path configurations, and a two-zealot clique, including both connected and disconnected dissenting induced subgraphs. Executing `python verify.py` requires Python 3 and SymPy and returns `All exact symbolic assertions passed.` These tests corroborate, but do not replace, the arbitrary finite-graph proof.

For a single positive zealot at the center of the star with \(m\ge1\) negative leaves, every dissenting component is a singleton and the leaf flip times are independent exponentials of rate \(\delta/2\). Consequently
\[
\mathbb E\tau_\delta=\frac{2}{\delta}\sum_{j=1}^m\frac1j
\qquad\text{(exactly, for every \(0<\delta<2\)).}
\]
For one positive zealot and \(m\) negative vertices in the complete graph on \(m+1\) vertices, the recursion gives \(k_C=m/2^m\), hence
\[
\mathbb E\tau_\delta\sim\frac{2^m}{m\delta^m}.
\]
In particular, with four total vertices (one zealot and three dissenters), the star has exact expectation \(11/(3\delta)\), while the complete graph has expectation \((25\delta^2+8\delta+16)/(6\delta^3)\), an exact symbolic identity. The two graphs have the same number of vertices but different consensus-divergence exponents, one versus three.

## Relationship to prior work

The partisan, neighbor-copying mechanism is the finite-network analogue of the biased voter models developed by Masuda, Gibert, and Redner and analyzed by Llabrés, San Miguel, and Toral (arXiv:2301.09563). Zimmaro, Contucci, and Kertész (arXiv:2303.09587) analyze heterogeneous preferences on modular networks using mean-field and pair approximations and simulations. The present statement instead establishes the exact rare-flip, finite-graph metastable exponent, finite recursive prefactors, and limiting maximum-of-exponentials law with fixed positive zealots and initially negative free agents. The asymptotic derivation uses standard finite-state perturbation and renewal principles; these principles are not claimed as new. The theorem is not implied by a mean-field fixed-point phase diagram or an average polarization prediction alone. A broader general-purpose resistance-tree or rare-transition theory may provide an alternative derivation and remains a publication-priority risk.

## Limitations

The graph and zealot set remain fixed as \(\delta\downarrow0\); the result does not quantify simultaneous large-population limits. All free agents start negative and have the same negative preference, zealots are permanently positive, and update clocks are independent and rate one. The theorem concerns first reaching positive unanimity, not an opinion stationary distribution in the absence of fixed agents. No claim is made for adaptive graphs, irreversible infection dynamics, genuinely mixed preference assignments among free agents, or uniqueness of this derivation in the literature. An independent scientific audit has not been performed.

## References

1. J. Llabrés, M. San Miguel, and R. Toral, *Partisan Voter Model: Stochastic description and noise-induced transitions*, arXiv:2301.09563 (first public version 2023-01-23), https://arxiv.org/abs/2301.09563.
2. F. Zimmaro, P. Contucci, and J. Kertész, *Voter-like dynamics with conflicting preferences on modular networks*, arXiv:2303.09587 (first public version 2023-03-16), https://arxiv.org/abs/2303.09587; *Entropy* **25** (2023), 838, https://doi.org/10.3390/e25060838.
3. N. Masuda, N. Gibert, and S. Redner, *Heterogeneous voter models*, arXiv:1003.0768 (2010), https://arxiv.org/abs/1003.0768.
