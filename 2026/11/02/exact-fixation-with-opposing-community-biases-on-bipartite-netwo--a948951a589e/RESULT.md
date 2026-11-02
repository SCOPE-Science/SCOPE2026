# Exact fixation with opposing community biases on bipartite networks

## Finding

Consider a finite connected bipartite graph with nonempty vertex classes \(U\) and \(W\). Each vertex holds opinion \(0\) or \(1\). At each discrete time, one vertex is chosen uniformly, chooses a neighbor uniformly, and copies the neighbor's opinion, conditional on disagreement, with a probability determined by the receiving vertex's class and its current opinion. On \(U\), a \(0\)-to-\(1\) copy succeeds with probability \(p_U\) and a \(1\)-to-\(0\) copy with probability \(q_U\). The corresponding probabilities on \(W\) are \(p_W,q_W\), all strictly positive and at most one.

**Theorem (exact fixation in two regimes).** Write \(n_U=|U|\), \(n_W=|W|\). If \(G\) is biregular, with every vertex of \(U\) having degree \(d_U\) and every vertex of \(W\) degree \(d_W\), let \(k_U,k_W\) count the initially positive vertices in their respective classes. Define

\[
Q=\frac{q_Uq_W}{p_Up_W},\qquad
A=\frac{d_Uq_W}{d_Wp_U},\qquad
z_W=\frac{Q+A}{1+A},\qquad z_U=\frac{Q}{z_W}.
\]

When \(Q\ne1\), the probability of eventual fixation at unanimous opinion \(1\) is exactly

\[
\boxed{\mathbb P_{x}(\mathrm{fix\ at\ }1)=
\frac{1-z_U^{k_U}z_W^{k_W}}{1-z_U^{n_U}z_W^{n_W}}.}
\]

When \(Q<1\), both \(z_U\) and \(z_W\) are strictly between zero and one; when \(Q>1\), both exceed one. Thus the expression is defined for every noncritical four-rate choice and every initial configuration. In particular, the sign of the net selection is determined by the *product of cross-class adoption rates*, even when the communities individually favor opposite opinions.

At the **critical product balance** \(p_Up_W=q_Uq_W\), biregularity is unnecessary: on *every* finite connected bipartite graph,

\[
\boxed{\mathbb P_x(\mathrm{fix\ at\ }1)=
\frac{\frac{q_W}{p_U}\sum_{u\in U}d(u)x_u+\sum_{w\in W}d(w)x_w}
{\frac{q_W}{p_U}\sum_{u\in U}d(u)+\sum_{w\in W}d(w)}.}
\]

This is a graph-exact weighted-influence identity with arbitrary degree heterogeneity and unequal class-dependent responsiveness. Under biregularity, it reduces to \(\bigl(d_U(q_W/p_U)k_U+d_Wk_W\bigr)/\bigl(d_U(q_W/p_U)n_U+d_Wn_W\bigr)\). The formula is valid for all initial states, including consensus states.

## Assumptions and scope

The graph is finite, simple, connected, undirected and bipartite, with at least one edge; there are no isolated vertices. Opinion updates are asynchronous, one vertex per step. Each random choice at each step is fresh. The selected receiving vertex chooses among its neighbors with equal probability. Acceptance probabilities depend on the receiving vertex's *class* and *prior opinion* but not on neighbor identity. Each of \(p_U,q_U,p_W,q_W\) belongs to \((0,1]\), independently, so the classwise probabilities need not sum to one. There are no exogenous mutations and no opinion changes on agreeing pairs.

For the off-critical formula, the graph must be biregular; for the critical formula, it need only be bipartite and connected. The initial configuration \(x\in\{0,1\}^{V(G)}\) is deterministic but otherwise arbitrary. In either case, finite-state absorption occurs almost surely and the stated probability refers to the eventual *all-one* absorbing state, not finite-time marginal opinion.

## Proof

**Absorption.** The all-zero and all-one states are absorbing. Every nonconsensus configuration has at least one discordant edge by connectedness. From any configuration, there is a finite positive-probability sequence of updates spreading one currently present opinion along a spanning tree until the population agrees. Because each specified adoption probability is strictly positive, there is no other closed communicating class. Hence this finite Markov chain almost surely reaches one of its two consensus states.

**Off-critical edge martingale.** Suppose \(G\) is biregular and \(Q\ne1\), with the parameters defined above. Set

\[
H(x)=z_U^{k_U(x)}z_W^{k_W(x)}.
\]

The identities \(z_Uz_W=Q\) and

\[
\frac{p_U}{d_U}(z_U-1)
=\frac{q_W}{d_W}\frac{z_W-1}{z_W}
\]

follow immediately from \(z_W=(Q+A)/(1+A)\) and the definition of \(A\). Consequently, across a discordant edge with \(x_u=0,x_w=1\), the two possible directed copying changes contribute

\[
\frac{H(x)}{|V(G)|}
\left[\frac{p_U}{d_U}(z_U-1)+\frac{q_W}{d_W}(z_W^{-1}-1)\right]=0
\]

to the conditional drift. Across the reverse discordance \(x_u=1,x_w=0\), the contribution is

\[
\frac{H(x)}{|V(G)|}
\left[\frac{q_U}{d_U}(z_U^{-1}-1)+\frac{p_W}{d_W}(z_W-1)\right]=0,
\]

since \(z_Uz_W=q_Uq_W/(p_Up_W)\). Summing over edges shows \(H(X_t)\) is a bounded martingale. The relation \(z_W-1=(Q-1)/(1+A)\) and \(z_U-1=A(z_W-1)/z_W\) proves both bases are on the same side of one. In particular \(z_U^{n_U}z_W^{n_W}\ne1\). Optional stopping at the almost-sure finite absorption time gives

\[
z_U^{k_U}z_W^{k_W}
=(1-F)+Fz_U^{n_U}z_W^{n_W},
\]

which rearranges to the asserted expression.

**Critical graph-general martingale.** Now take \(Q=1\) and permit arbitrary degrees. Put \(c=q_W/p_U>0\) and

\[
M(x)=c\sum_{u\in U}d(u)x_u+\sum_{w\in W}d(w)x_w.
\]

Across an edge with \((x_u,x_w)=(0,1)\), the conditional one-step expected changes in \(M\) are \(cp_U/|V(G)|\) and \(-q_W/|V(G)|\), and cancel by \(cp_U=q_W\). Across the reverse edge they are \(-cq_U/|V(G)|\) and \(p_W/|V(G)|\), and cancel because \(cq_U=q_Uq_W/p_U=p_W\). Every edge has zero drift; hence \(M(X_t)\) is a bounded martingale. Its value at all zeroes is zero and at all ones is \(c\sum_U d(u)+\sum_Wd(w)>0\). Optional stopping yields the critical formula. No biregularity was used.

**Boundary agreement.** Let \(Q\to1\) through strictly positive four-rate vectors with their limiting ratios fixed and positive. Since \(z_W-1=(Q-1)/(1+A)\) and \(z_U-1=A(Q-1)/(Q+A)\), a first-order expansion of the noncritical expression yields the critical biregular ratio. This confirms the removable singularity at balance without deriving the irregular-graph result from biregular assumptions.

## Verification

The included standalone `verify.py` checks all \(5760\) state/parameter combinations for the vanishing exact Markov drift on four differently sized biregular graphs and five strictly positive four-rate tuples. Separately, it solves the full absorbing Markov-chain linear system over exact rational arithmetic for \(366\) nonabsorbing states, and verifies the critical formula and an independent rational solve for \(30\) nonabsorbing states of an irregular five-vertex path. Run `python3 verify.py`. These finite tests corroborate, but do not replace, the general proof.

For an explicit noncritical example, on the incidence graph of a complete four-vertex graph take \(d_U=2\), \(d_W=3\), \(n_U=6\), \(n_W=4\) and
\(p_U=3/4,q_U=1/4,p_W=1/2,q_W=1/3\). Then \(Q=2/9\), \(z_U=5/9\) and \(z_W=2/5\). A single positive opinion on the degree-two side has fixation probability

\[
\frac{4/9}{1-(5/9)^6(2/5)^4},
\]

whereas a single positive opinion on the degree-three side has probability \((3/5)/(1-(5/9)^6(2/5)^4)\); their exact ratio is \(27/20\).

At product balance on a five-vertex path, put \(U\) at positions \(0,2,4\), \(W\) at positions \(1,3\), with \(p_U=1/2,q_U=1/4,p_W=1/2,q_W=1\). Here \(c=2\): one positive opinion at the central vertex has fixation probability \(1/3\), versus \(1/6\) at a leaf or either adjacent vertex.

## Relationship to prior work

The 2012 exact bithermal-graph analysis by Houchmandzadeh and Vallade contains the *uniform global adoption bias* specialization: it is not claimed as new. The alternating equal-intensity unbiased martingale on bipartite networks is also already known and is explicitly excluded from the new contribution. The present theorem adds independent class-dependent rates, including opposing biases of unequal strength and the critical condition in which total class responsiveness differs; the critical formula applies to irregular graphs and is not the ordinary degree-proportion identity.

Becchetti, Bonifaci, Cruciani and Pasquale analyze a context-dependent voter model with globally shared adoption probabilities, obtaining particular exact results on regular graphs. Zimmaro, Contucci and Kertész study conflicting partisan preferences on modular networks, mainly through pair and mean-field approximations. Their models motivate distinguishing the two communities, but neither checked text states the exact four-rate biregular fixation formula or arbitrary-irregular-graph balanced formula for this update mechanism. The positional voter model changes the probability of *selecting* neighbors through fitness weights, which is not the acceptance-after-uniform-sampling dynamics assumed here.

## Limitations

The noncritical formula assumes biregularity; no exact expression is asserted for arbitrary irregular graphs away from product balance. Strict positivity is essential to the absorption argument. Graphs with mutations, directed edges, synchronous updates, class-dependent neighbor selection, or spatially varying rates within a class are excluded. The classical uniform-bias subcase and the previously known alternating equal-intensity neutral case are not novel results. Although literature comparisons were conducted at the level of update rules and implications, an unindexed equivalent specialized theorem cannot be ruled out. No independent mathematical audit has been performed.

## References

- Houchmandzadeh, B., and Vallade, M., *Exact results for fixation probability of bithermal evolutionary graphs* (2012), arXiv:1211.2782, https://arxiv.org/abs/1211.2782.
- Becchetti, L., Bonifaci, V., Cruciani, E., and Pasquale, F., *On a Voter Model with Context-Dependent Opinion Adoption* (2023), arXiv:2305.07377, https://arxiv.org/abs/2305.07377.
- Zimmaro, A., Contucci, P., and Kertész, J., *Voter-like Dynamics with Conflicting Preferences on Modular Networks* (2023), DOI:10.3390/e25060838, https://doi.org/10.3390/e25060838.
- Petsinis, A., Pavlogiannis, A., and Karras, P., *Maximizing the Probability of Fixation in the Positional Voter Model*, arXiv:2211.14676, https://arxiv.org/abs/2211.14676.
