# Strict Moran suppression for every regular higher-order replacement hypergraph

## Finding

**Theorem (uniform strict suppression).** Let \(H=(V,E)\) be a finite connected simple hypergraph on \(N\ge3\) vertices. Suppose all vertices have the same positive incidence degree \(d\) and every edge has cardinality at least \(3\), with no assumption that the edge sizes are equal. Under the group-replacement birth--death rule defined below, let \(\rho_H(A;r)\) be the probability that type \(A\), initially occupying any particular nonempty proper set \(A\subset V\) of size \(i\), ultimately fills all vertices. Then, with

\[
M_N(i;r)=\begin{cases}
\dfrac{1-r^{-i}}{1-r^{-N}},&r\ne1,\\[4pt]
\dfrac{i}{N},&r=1,
\end{cases}
\]

the following strict comparison holds for **every** such initial set:

\[
\rho_H(A;r)\begin{cases}
<M_N(i;r),&r>1,\\
=M_N(i;1),&r=1,\\
>M_N(i;r),&0<r<1.
\end{cases}
\]

In particular, the model strictly suppresses selection relative to the ordinary \(N\)-individual Moran process for any number and placement of initial mutants, not just uniformly seeded single mutants. The statement applies to nonuniform edge-size mixtures.

## Assumptions and scope

The vertices carry two types, mutant \(A\) of constant fitness \(r>0\) and resident \(B\) of constant fitness \(1\). At each discrete time, choose one parent proportionally to its fitness; the parent chooses uniformly among its \(d\) incident hyperedges; every other vertex of that edge instantly copies the parent's type. This is model 1 of Liu--Masuda (2023), with no majority condition. The hypergraph is undirected, finite, connected by overlapping edges, and has no singleton or pairwise edges. The topology and types do not otherwise evolve.

The edges may have different cardinalities. The degree requirement is **incidence degree**, the number of hyperedges containing a vertex, not the number of pairwise neighbors. A uniform random choice of the initial mutant is **not** required. The neutral case is treated separately from the non-neutral cases.

## Proof

**Absorption.** Starting from any mixed configuration, connectedness gives a hyperedge meeting both types. Choose a mutant parent in that edge and then choose that edge; the number of mutant vertices increases by at least one, with positive probability. Repeating this move leads to the all-mutant state after at most \(N-1\) changes. Consequently every transient state of the finite Markov chain can reach an absorbing state. Since there are finitely many transient configurations and all relevant choice probabilities are positive, the absorption time \(\tau\) is finite almost surely (indeed it has a geometric tail on sufficiently large blocks of steps).

**One-step exponential drift.** Write \(I_t\) for the number of mutants and fix a state containing \(i\) mutants. Set \(T=ri+N-i>0\). For an edge \(e\), let \(a\) of its vertices be mutants and \(b=|e|-a\) be residents. Each mutant vertex in \(e\) can be chosen as parent and choose this edge with probability \(r/(Td)\); each resident vertex has probability \(1/(Td)\). When this edge is chosen through a mutant parent, \(I_t\) increases by \(b\). Through a resident parent, it decreases by \(a\). Therefore

\[
\mathbb E[r^{-I_{t+1}}-r^{-I_t}\mid X_t]
=\frac{r^{-i}}{Td}\sum_{e\in E}G_r(a_e,b_e),
\qquad
G_r(a,b)=ra(r^{-b}-1)+b(r^a-1).
\]

For a monochromatic edge \(G_r(a,b)=0\). If \(a,b\ge1\), the two finite geometric sums yield

\[
G_r(a,b)=(r-1)\left[
 b\sum_{j=0}^{a-1}r^j-a\sum_{j=0}^{b-1}r^{-j}
\right].
\]

If \(r>1\), the first sum is at least \(a\), the second at most \(b\), and at least one of these comparisons is strict when \(a+b\ge3\). Therefore the bracket is positive. If \(0<r<1\), the inequalities reverse, and the bracket is negative and strict under the same edge-size condition. In both cases **\(G_r(a,b)>0\)** whenever an edge is mixed and has size at least \(3\). Every mixed global configuration has such an edge by connectedness. Hence \(r^{-I_t}\) has strictly positive conditional drift at every transient state for every \(r\ne1\).

**Comparison with the Moran fixation function.** When \(r\ne1\), \(M_N(i;r)=(1-r^{-i})/(1-r^{-N})\) equals \(0\) at \(i=0\) and \(1\) at \(i=N\). The preceding drift identity implies that \(M_N(I_t;r)\) has strictly **negative** conditional drift in every mixed state if \(r>1\), because \(1-r^{-N}>0\). It has strictly **positive** drift in every mixed state if \(0<r<1\), because \(1-r^{-N}<0\). The process is bounded between \(0\) and \(1\), so optional stopping at \(\tau\), justified also by bounded convergence, gives respectively

\[
\rho_H(A;r)=\mathbb E[M_N(I_\tau;r)]
<M_N(i;r)\quad(r>1),
\]

and the reverse strict inequality for \(0<r<1\). Strictness follows already at the first step and persists under expectation thereafter.

**Neutral fitness.** For \(r=1\), the expected change of mutant count contributed by any edge is proportional to \(ab-ba=0\), since all parent-vertex incidence choices are equally likely under degree regularity. Thus \(I_t\) is a bounded martingale. At absorption \(I_\tau\in\{0,N\}\), and bounded stopping gives \(N\rho_H(A;1)=i\), as claimed. \(\square\)

## Verification

The standalone program `verification/verify.py` independently builds exact rational transition matrices for finite regular hypergraphs and solves their absorbing-state fixation equations. It checks all mixed initial states and rates \(r\in\{1/2,1,2\}\) on: a single triple, a four-vertex complete triple system, a five-vertex cyclic triple system, and a degree-four mixed-size system containing triples and a five-vertex edge. It also checks the sign of the mixed-edge drift polynomial at \(9\times9\) integer compositions and six rational fitness values, and reproduces the source's four-vertex expression \(r^2/(r+1)^2\). These finite checks corroborate the proof; the theorem for arbitrary size follows from the analytic drift and absorption arguments, not from enumeration.

## Relationship to prior work

Liu and Masuda (2023), Sections 2, 3.1 and 5, define the precise hypergraph updating rule and provide semianalytical or numerical suppressor evidence for complete, cyclic and star \(3\)-uniform families and several empirical examples. They explicitly pose general bounds on hypergraph amplification as future questions. Their calculations do not establish this topology-independent, every-initial-state theorem for all regular incidence structures of arbitrary hyperedge sizes. The pairwise-graph isothermal theorem instead gives exact equality with Moran on regular graphs, so it is not a proof of the strict group-replacement inequality.

Keller and Ugurlu (2024) use martingales for single-replacement graph processes; Liu and Masuda (2024) use exponential-count submartingales in a two-layer network model with one-neighbor replacement. The method has precedents, but those models have different transition kernels, and their theorems do not entail the explicit mixed-hyperedge drift inequality above.

## Limitations

The result is confined to **model 1** (full hyperedge replacement). It is not asserted for majority-conditioned model 2, irregular incidence degrees, directed or weighted hyperedge selection, selective replacement of just one edge member, stochastic fitness, time-varying topology, or infinite hypergraphs. The result proves only the direction of the Moran comparison, not an optimal quantitative gap or the fixation-time distribution. No independent external verification has been performed. The available bibliographic searches leave residual risk of an equivalent result in unindexed literature.

## References

1. Ruodan Liu and Naoki Masuda, *Fixation dynamics on hypergraphs*, arXiv:2301.05343 (first submitted 2023-01-13); *PLOS Computational Biology* 19 (2023), e1011494. DOI: 10.1371/journal.pcbi.1011494.
2. Peter Keller and Mert Ugurlu, *Fixation probability in Moran-like Processes on graphs*, arXiv:2403.12598 (2024). Comparison restricted to accessible abstract and model description.
3. Ruodan Liu and Naoki Masuda, *Fixation Dynamics on Multilayer Networks*, *SIAM Journal on Applied Mathematics* 84 (2024), 2028–2050. DOI: 10.1137/23M1620144, especially Sections 3–4.
