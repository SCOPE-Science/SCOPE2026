# Universal Moran suppression under balanced group broadcasts

## Finding

**Theorem (balanced-group suppression and exact fixation defect).** Let \(H=(V,E,w)\) be a finite connected undirected hypergraph on \(N\ge 2\) vertices. Every hyperedge \(e\in E\) has cardinality at least two and positive weight \(w_e\), and all vertices have the same positive incident weight
\[
 d=\sum_{e\ni v}w_e\quad\text{for every }v\in V.
\]
There are two types: mutants of fixed fitness \(r>0\) and residents of fitness one. At each discrete step, choose one parent proportionally to fitness; the parent chooses an incident hyperedge \(e\) with probability \(w_e/d\); then every other vertex of \(e\) adopts the parent's type. There is no mutation. For every deterministic, nonempty proper initial mutant set \(S\subsetneq V\), write \(m=|S|\) and let \(\rho_H(S;r)\) denote the mutant fixation probability. Set
\[
 B_N(m,r)=\begin{cases}
 \dfrac{1-r^{-m}}{1-r^{-N}},&r\ne1,\\[4pt]
 \dfrac mN,&r=1.
 \end{cases}
\]
Then
\[
 \rho_H(S;r)\begin{cases}
 \le B_N(m,r),&r>1,\\
 =m/N,&r=1,\\
 \ge B_N(m,r),&0<r<1.
 \end{cases}
\]
For every \(r\ne1\), the inequality is **strict for every such initial set** if \(H\) contains any hyperedge of size at least three. If every hyperedge has size two, equality holds for every \(S\) and every \(r>0\). Thus any genuinely higher-order, connected, incident-weight-balanced group-broadcast system is a strict Moran suppressor, simultaneously for every nontrivial deterministic initialization and all nonneutral fitness ratios. Neither hyperedge sizes nor their weights must be uniform.

A more precise identity quantifies the entire fixation gap. Let \(S_t\) be the mutant set after step \(t\), let \(M_t=|S_t|\), let \(\tau\) be the first consensus time, and for each hyperedge set \(a_e(t)=|e\cap S_t|\), \(b_e(t)=|e|-a_e(t)\). Define
\[
 Q_{a,b}(r)=ar(r^{-b}-1)+b(r^a-1).
\]
For every \(r\ne1\),
\[
 \boxed{\displaystyle
 B_N(m,r)-\rho_H(S;r)
 =\frac{1}{d(1-r^{-N})}\,\mathbb E_S\left[
 \sum_{t=0}^{\tau-1}\frac{r^{-M_t}}{rM_t+N-M_t}
 \sum_{e\in E}w_e Q_{a_e(t),b_e(t)}(r)
 \right].}
\]
The numerator in this identity is nonnegative, and it is positive whenever a mixed hyperedge of size at least three is encountered with positive probability. Its denominator changes sign across neutrality, giving the two opposite inequalities above.

## Assumptions and scope

A hyperedge is a subset of vertices with no repeated vertices; different hyperedges may have different sizes and positive weights. Connectivity means that every nonempty proper vertex set meets a hyperedge also meeting its complement. Equal incident weight \(d\) is the balance condition; uniform weights on any regular hypergraph are a special case. Parent selection is global, proportional to fixed fitness; conditional hyperedge selection is weighted and broadcasts to *all* other members. All statements hold for every \(N\ge2\), every such connected weighted hypergraph, every \(r>0\), and every nonempty proper initial mutant set, without averaging over initial placements. For \(N=2\), only pair edges are possible and equality holds.

## Proof

**1. Absorption and integrability.** In a nonconsensus state, choose either existing type and repeatedly select a parent of that type in a hyperedge crossing from its currently occupied set into the other type. Each such choice has positive probability and strictly expands the selected type's occupied set. Connectivity guarantees a crossing hyperedge until consensus. Hence consensus is reachable in at most \(N-1\) selected changes, from every transient state. Finiteness of the state space gives a uniform positive probability of absorption within a bounded number of steps; thus \(\tau<\infty\) almost surely and \(\mathbb E\tau<\infty\).

**2. Exact one-step drift.** Put \(Y_t=r^{-M_t}\) and \(W_t=rM_t+N-M_t\). For an edge with \(a\) mutants and \(b\) residents, each of its \(a\) mutant possible parents has probability \(r w_e/(dW_t)\) and converts the \(b\) residents, while each of its \(b\) resident possible parents has probability \(w_e/(dW_t)\) and converts the \(a\) mutants. All unchanged outcomes contribute zero. Thus for the natural history \(\mathcal F_t\),
\[
 \mathbb E[Y_{t+1}-Y_t\mid\mathcal F_t]
 =\frac{r^{-M_t}}{dW_t}\sum_{e\in E}w_e Q_{a_e(t),b_e(t)}(r).
\]
The equality of incident weights is what allows all possible parents of a fixed edge to share the same denominator \(d\).

**3. Sign of the edge defect.** If \(ab=0\), the edge defect is zero. If \(a,b\ge1\), the two finite geometric-series identities yield
\[
 Q_{a,b}(r)=(r-1)\left[
 b\sum_{j=0}^{a-1}r^j-a\sum_{j=0}^{b-1}r^{-j}
 \right].
\]
For \(r>1\), the first sum is at least \(a\), and the second at most \(b\); for \(0<r<1\), both inequalities reverse. Multiplying by \(r-1\) therefore gives \(Q_{a,b}(r)\ge0\) in either case. For nonneutral \(r\), equality in a mixed edge occurs exactly when \(a=b=1\), i.e. a size-two edge. Hence \(Y_t\) is a bounded submartingale for every positive \(r\), with strict drift precisely at configurations where a size-at-least-three edge is mixed.

**4. Fixation comparison and exact identity.** At consensus, \(Y_\tau\) is \(r^{-N}\) upon mutant fixation and one otherwise. Consequently,
\[
 \mathbb E_S[Y_\tau]-r^{-m}
 =(1-r^{-N})\,[B_N(m,r)-\rho_H(S;r)].
\]
Optional stopping is legitimate because \(Y_t\) is bounded and \(\tau\) is finite almost surely. Summing the conditional drifts through \(\tau\) gives the displayed fixation-defect identity; the interchange of expectations is also justified by bounded drift and finite \(\mathbb E\tau\). Its sign proves the desired bounds, reversed for \(0<r<1\) because \(1-r^{-N}<0\).

**5. Strictness.** Fix an edge \(e_*\) with at least three vertices. If it is initially mixed, the first-step drift is positive. Otherwise it is monochromatic, and choose a vertex of the opposite type outside \(e_*\). Expand the opposite type by selecting a parent of that type on a currently mixed edge. If a selected mixed edge has size at least three, a positive-drift state has already been reached. Otherwise it has size two and exactly one new vertex is converted. Repetition must reach \(e_*\), unless an earlier mixed larger edge has been met: crossing into \(e_*\) by a two-vertex edge makes \(e_*\) mixed, since \(|e_*|\ge3\). Every prescribed finite expansion path has positive probability. Thus from every initial nonconsensus state the process has positive probability of visiting a positive-drift state before absorption. At that visit the conditional drift is strictly positive, while all other drifts are nonnegative, proving a strictly positive expected cumulative defect and strict comparison. Conversely, if all edges have size two, every edge defect vanishes and the bounded process \(Y_t\) is a martingale, giving equality.

**6. Neutrality.** At \(r=1\), for every edge the conditional drift of \(M_t\) is proportional to \(ab-ba=0\). The mutant count is a bounded martingale. Its terminal expectation is \(N\rho_H(S;1)\), hence \(\rho_H(S;1)=m/N\).

## Verification

Run `python verify.py` with Python 3 and SymPy. The program constructs the full finite-state transition matrix independently from the parent/edge rule and solves the rational absorbing-chain equations. It checks 330 nonabsorbing state/parameter combinations in five unweighted structures and one genuinely weighted balanced structure, including complete and cyclic triple systems, mixed edge sizes, a single all-vertex hyperedge, and a pairwise-only control. It also checks the one-step defect identity for each tested state and verifies 294 positive-rational mixed-edge defect instances. The checks were executed successfully. These are finite tests of the transition semantics and algebra, not a proof of the all-size theorem; that proof is given above.

## Relationship to prior work

Liu and Masuda introduced precisely the global parent-selection and whole-hyperedge broadcast dynamics (their model 1). They numerically and semianalytically compared fixation to the Moran benchmark for selected complete, cyclic, and star triple hypergraphs. Their source does not establish the present all-parameter theorem for arbitrary connected balanced hypergraphs, nonuniform edge sizes, weighted hyperedges, and every initial set. The present proof turns the suppression observed in the regular examples into a structural theorem, without asserting suppression for arbitrary irregular hypergraphs.

Liu and Masuda later used a bounded exponential submartingale for a *different* two-layer process where each event replaces a single replica in a layer with cross-layer fitness. This is a methodological antecedent, but its transition rule and theorems do not imply the simultaneous entire-hyperedge replacement defect computed here. Wang and collaborators analyzed weak-selection public-goods games under five group interaction rules, each centered on payoff-dependent strategy updating; those update rules do not broadcast a single fitness-weighted parent's type to all members of an incident hyperedge. The weighted graph isothermal/Moran result is recovered here only as the pair-edge equality boundary.

## Limitations

The theorem requires equal **total incident edge weight** for every vertex. It does not classify unequal-degree hypergraphs, where the parent-edge denominators differ and the edgewise sign argument fails. It does not apply to majority-gated replacement, one-recipient replacement, state-dependent game payoffs, or mutation. It compares fixation probabilities but does not compute their exact values on general hypergraphs or provide a universal quantitative size for the strict gap. The novelty comparison cannot exclude an unindexed equivalent formulation, particularly in mathematical evolutionary-process literature. No claim of independent validation is made.

## References

1. R. Liu and N. Masuda, *Fixation dynamics on hypergraphs*, PLOS Computational Biology **19** (2023), e1011494; arXiv:2301.05343 (first public preprint January 13, 2023). https://arxiv.org/abs/2301.05343 ; https://doi.org/10.1371/journal.pcbi.1011494
2. R. Liu and N. Masuda, *Fixation Dynamics on Multilayer Networks*, SIAM Journal on Applied Mathematics **84** (2024), 2028–2050. https://doi.org/10.1137/23M1620144
3. D. Wang, P. Yi, Y. Hong, J. Chen and G. Yan, *Evolutionary game on any hypergraph*, arXiv:2404.03305 (April 4, 2024). https://arxiv.org/abs/2404.03305
