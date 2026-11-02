# Sharp fixation ceiling and degree-scaled incentive in the positional voter star

## Finding

For every integer \(m\ge2\), the loopless undirected star \(K_{1,m}\) admits an exact fixation probability under one positional incentive. When a single mutant opinion A starts at a uniformly random vertex and only the hub is biased in favor of adopting A, the probability of eventual all-A consensus is

\[
F_m(r)=\frac{(mr+1)(mr+m+3r-1)}{(m+1)^2(r+1)(m+2r-1)},\qquad r\ge1.
\]

Biasing any one leaf instead has no effect: fixation remains \(1/(m+1)\). For every \(r>1\), biasing the hub is strictly better than biasing a leaf. At strong hub bias,

\[
\sup_{r\ge1}F_m(r)=\frac{m(m+3)}{2(m+1)^2}
=\frac{9}{16}-\frac{(m-3)^2}{16(m+1)^2}.
\]

Thus the sharp global fixation ceiling for **any single biased vertex of any loopless star with at least two leaves** is \(9/16\), approached on the three-leaf star as \(r\to\infty\); no finite incentive attains it.

If the advantage depends on graph size and \(r_m/m\to\vartheta\in[0,\infty]\), the sharp population limit is

\[
\lim_{m\to\infty}F_m(r_m)=\frac{\vartheta}{1+2\vartheta},
\]

where \(\vartheta=\infty\) gives the limit \(1/2\). Therefore positive asymptotic fixation from a uniform single seed requires an incentive at least comparable to hub degree; a proportional incentive yields a strictly positive probability, but arbitrary amplification at just one vertex cannot force fixation.

## Assumptions and scope

Let \(m\ge2\) be an integer, and consider the simple undirected star with one hub and \(m\) leaves and **no self-loops**. Every vertex carries either opinion A or B. At each discrete update, independently choose one vertex uniformly. The chosen vertex copies the opinion of a neighbor selected with weight \(r\) if the neighbor carries A and the chosen vertex is the sole biased vertex; all other neighbor-selection weights are 1. The parameter \(r=1+\delta\) satisfies \(r\ge1\), matching the positional voter convention. Exactly one uniformly sampled initial vertex holds A. The fixation event is eventual all-A consensus; all-B extinction is the other absorbing state.

These statements do not concern bias affecting the **speaker's** fitness rather than the **updater's** preferences, multiple biased vertices, self-loops, directed graphs, or alternative initial seeding laws.

## Proof

Write \(c\in\{0,1\}\) for the A-status of the hub and \(k\in\{0,1,\dots,m\}\) for the number of A leaves. When the hub alone is biased, put

\[
D_k=m+(r-1)k,\qquad E_k=D_k+1.
\]

Let \(u_k\) and \(v_k\) be the probabilities of all-A fixation starting from \((0,k)\) and \((1,k)\), respectively. The only nontrivial transitions out of \((0,k)\) are loss of an A leaf, with rate proportional to \(k\), and adoption of A by the hub, with rate proportional to \(rk/D_k\). Similarly, from \((1,k)\) the only nontrivial transitions are conversion of a B leaf, with rate proportional to \(m-k\), and adoption of B by the hub, with rate proportional to \((m-k)/D_k\). The uniform updater factor \(1/(m+1)\) cancels in the backward equations:

\[
 u_k-u_{k-1}=\frac{r}{D_k}(v_k-u_k)\quad (1\le k\le m),
 \qquad
 v_{k+1}-v_k=\frac{1}{D_k}(v_k-u_k)\quad (0\le k<m),
\]

with \(u_0=0\) and \(v_m=1\).

Here is an explicit harmonic solution valid at every transient state:

\[
 u_k=\frac{rk(mr+1)}{m(r+1)[m+r+(r-1)k]},
\]

\[
 v_k=\frac{mr+1}{(m+1)(r+1)}
 \left(1+\frac{(m+r)k}{m[m+1+(r-1)k]}\right).
\]

Direct algebra verifies both backward identities and both absorbing boundary values for arbitrary \(m\), \(r\), and all indicated \(k\). One can also derive the solution rather than guess it: writing \(d_k=v_k-u_k\), the recurrence gives

\[
\frac{d_{k+1}}{D_{k+1}}=\frac{d_k}{D_k}\frac{E_k}{E_{k+2}},
\qquad
\frac{d_k}{D_k}=\frac{C}{E_kE_{k+1}},
\]

for a constant \(C\); then the elementary telescoping identity

\[
\sum_{k=0}^{m-1}\frac1{E_kE_{k+1}}=\frac{m}{E_0E_m}
\]

determines \(v_0=(mr+1)/[(m+1)(r+1)]\). [The intermediate recurrence is interpreted by continuity when \(r=1\).] Because the finite chain has exactly two accessible absorbing states and is absorbed almost surely, the harmonic solution with those boundary values is the actual fixation probability. In particular,

\[
 v_0=\frac{mr+1}{(m+1)(r+1)},\qquad
 u_1=\frac{r(mr+1)}{m(r+1)(m+2r-1)}.
\]

Uniform placement of the initial A yields \(F_m(r)=[v_0+mu_1]/(m+1)\), which simplifies to the claimed rational function.

A leaf has only the hub as a neighbor, so modifying that leaf's neighbor-selection weights changes no transition. With only a leaf biased, the degree-weighted mutant occupation \([mc+k]/(2m)\) is a martingale under unbiased voter updating, and its uniform-seed expectation is \(1/(m+1)\). For hub bias, the same degree-weighted occupation has one-step conditional drift

\[
\frac{k(m-k)(r-1)}{2(m+1)m[m+(r-1)k]}\ge0.
\]

It is strictly positive on any configuration with \(0<k<m\) when \(r>1\), which occurs with positive probability at the first step of the uniform-seed experiment. Bounded convergence to the fixation indicator proves \(F_m(r)>1/(m+1)\) for every finite \(r>1\).

The exact formula is monotone in \(r\) by the standard coupling that strengthens the updater's preference for A. For each fixed \(m\), the displayed formulas yield \(v_0\to m/(m+1)\), \(u_1\to1/2\), and the stated strong-bias supremum. Its difference from \(9/16\) is exactly \(-(m-3)^2/[16(m+1)^2]\), so the unique maximizing leaf count is \(m=3\). Every finite \(r\) has strictly lower fixation than the corresponding strong-bias limit.

Finally, if \(r_m/m\to\vartheta>0\), then \(r_m\to\infty\), \(v_0\to1\), and

\[
 u_1=\frac{r_m}{m+2r_m-1}\cdot\frac{mr_m+1}{m(r_m+1)}
 \longrightarrow\frac{\vartheta}{1+2\vartheta}.
\]

The initial hub occurs with probability \(1/(m+1)\), hence its contribution vanishes. If \(r_m/m\to0\), the bound \(0\le F_m(r_m)\le 1/(m+1)+r_m/(m+2r_m-1)\) forces the limit 0. The same formula gives the limit \(1/2\) as \(r_m/m\to\infty\).

## Verification

The program `verification/star_check.py` checks the symbolic backward equations, boundary values, closed form, strong-bias optimization identity, and population scaling limit using exact symbolic simplification. Separately, for each \(m\in\{2,\dots,8\}\) and each \(r\in\{1,2,3,7\}\), it builds and solves the complete \(2m\)-state absorbing Markov linear system over exact rational numbers and compares all transient probabilities to the analytic formulas. All 28 independently solved small chains agree. Run with Python 3.10 or later and SymPy (`python verification/star_check.py`). These finite calculations are independent checks; the arbitrary-size theorem follows from the proof above.

## Relationship to prior work

Petsinis, Pavlogiannis, and Karras introduced the positional voter model with bias attached to the updater and proved general monotonicity and complexity/approximation results. Their statements do not provide this star-specific exact fixation function, universal one-vertex strong-bias ceiling, or network-size/bias scaling. Durocher and collaborators investigate the voter process with a globally applied invasion preference rather than one biased updater. Brendborg and collaborators study positional **Moran** updating, where the advantaged agent is selected for birth, not positional voter updating. The classical heterogeneous-network voter analysis explains the neutral degree-weighted martingale but does not cover the hub-only positional preference. The present formula is specific to the original positional voter transition rule.

## Limitations

The theorem assumes a loopless unweighted star, one biased site, a uniformly random single A seed, and \(r\ge1\). The sharp bound and asymptotics are not assertions about arbitrary networks, multiple incentives, other placement laws, or different updating rules. Localized positional-bias versions of a star may be considered elsewhere under different terminology; independent bibliographic review is still needed.

## References

1. P. Petsinis, A. Pavlogiannis, and P. Karras, *Maximizing the Probability of Fixation in the Positional Voter Model*, arXiv:2211.14676, first posted 2022-11-26; see definition (3), monotonicity Lemma 4, and the main results in Sections 3–6. https://arxiv.org/abs/2211.14676
2. L. Durocher, P. Karras, A. Pavlogiannis, and J. Tkadlec, *Invasion Dynamics in the Biased Voter Process*, arXiv:2201.08207 (2022). https://arxiv.org/abs/2201.08207
3. J. Brendborg, P. Karras, A. Pavlogiannis, A. U. Rasmussen, and J. Tkadlec, *Fixation Maximization in the Positional Moran Process*, arXiv:2201.02248 (2022). https://arxiv.org/abs/2201.02248
4. V. Sood, T. Antal, and S. Redner, *Voter models on heterogeneous networks*, Physical Review E **77**, 041121 (2008). https://doi.org/10.1103/PhysRevE.77.041121
