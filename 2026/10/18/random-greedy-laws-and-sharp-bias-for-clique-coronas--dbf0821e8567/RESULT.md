# Random-greedy laws and sharp bias for clique coronas

## Finding

Let \(H\) be any finite simple graph with \(r=|V(H)|\ge1\), let \(s\ge1\), and form the clique corona \(C_s(H)=H\odot K_s\): for each core vertex \(v\), attach a private clique \(P_v\) of \(s\) vertices, all adjacent to \(v\), with no other edges incident to these private vertices. The **random-greedy maximal-independent-set law** is obtained by scanning all labelled vertices in a uniformly random order, accepting a vertex iff it has no previously accepted neighbour. Let \(b(C_s(H))\) be its total-variation distance from the uniform distribution on all labelled maximal independent sets.

Write \(\mathcal I(H)\) for the family of independent vertex sets, including the empty set, and let \(Z_H(t)=\sum_{I\in\mathcal I(H)}t^{|I|}\). For \(B\subseteq V(H)\), let \(q_B(I)\) be the probability that ordinary uniformly random-order greedy selection on the induced graph \(H[B]\) yields \(I\), with \(q_{\varnothing}(\varnothing)=1\). Fix \(t=1/s\).

**Theorem (full law, rigidity and sharp bias).** Every maximal independent set of \(C_s(H)\) comprises an independent set \(I\in\mathcal I(H)\) of chosen core vertices and exactly one private vertex of \(P_v\) for each \(v\notin I\). The core marginal \(\mu_s\) of the random-greedy output is
\[
\mu_s(I)=(1+t)^{-r}\sum_{B\subseteq V(H)}t^{|B|}q_B(I),
\qquad I\in\mathcal I(H).
\]
Conditional on \(I\), the chosen private vertices are independent and uniform inside their respective private cliques. The uniform maximal-independent-set law has core marginal
\[
\nu_s(I)=\frac{t^{|I|}}{Z_H(t)}.
\]
In particular, the exact bias is \(b(C_s(H))=\tfrac12\sum_{I\in\mathcal I(H)}|\mu_s(I)-\nu_s(I)|\). Moreover,
\[
\boxed{b(C_s(H))=0\ \Longleftrightarrow\ E(H)=\varnothing,}
\]
and whenever \(E(H)\ne\varnothing\),
\[
\boxed{b(C_s(H))\ge\frac1{Z_H(1/s)}-\left(\frac{s}{s+1}\right)^r>0.}
\]
For every fixed \(H\), as \(s\to\infty\),
\[
\boxed{b(C_s(H))=\frac{|E(H)|}{s^2}+O_H(s^{-3}).}
\]
For the complete core \(H=K_r\), \(r\ge2\), the exact bias is
\[
\boxed{b(C_s(K_r))=\frac{s}{s+r}-\left(\frac{s}{s+1}\right)^r.}
\]
The exact-uniformity criterion also holds for **unequal positive private-clique sizes** \((s_v)_{v\in V(H)}\); in that case the greedy all-private probability is \(\prod_v s_v/(s_v+1)\), whereas its uniform probability is \(1/Z_H((1/s_v)_v)\), with \(Z_H((w_v)_v)=\sum_{I\in\mathcal I(H)}\prod_{v\in I}w_v\).

## Assumptions and scope

Graphs are finite, simple, vertex-labelled; \(r\ge1\), \(s\ge1\), and all private cliques have the same size except in the explicitly stated heterogeneous rigidity extension. No connectedness, degree, or regularity assumption is imposed on \(H\). A maximal independent set is inclusion-maximal, not necessarily of maximum cardinality. Total variation uses the full finite space of labelled maximal independent sets. Asymptotic \(O_H\) fixes the complete graph \(H\) while \(s\) increases. The theorem makes no assertion about universal minimizers of bias across graph families or joint limits with \(r\to\infty\).

## Proof

**1. Maximal independent sets and the uniform law.** Each cluster \(\{v\}\cup P_v\) is a clique, so an independent set uses at most one vertex from each cluster. It is maximal only if it uses at least one vertex from each cluster: otherwise any private vertex of the empty cluster can be added. The chosen core vertices form an independent set \(I\) of \(H\); conversely every independent core set \(I\), complemented by one arbitrary private vertex in each unchosen cluster, is maximal. Hence the number of labelled maximal independent sets with core set \(I\) is \(s^{r-|I|}\), and their total number is \(s^r Z_H(1/s)\). Dividing gives \(\nu_s(I)=s^{-|I|}/Z_H(1/s)\).

**2. Local candidates and exact greedy law.** Realize a uniformly random vertex permutation by independent continuous \(\operatorname{Unif}[0,1]\) arrival times. Let \(T_v\) be the minimum arrival time among vertices of \(\{v\}\cup P_v\), and let \(X_v\) indicate that this earliest vertex is the core vertex \(v\). These clusters are disjoint, so the \(X_v\)'s are independent with probability \(1/(s+1)=t/(1+t)\). In each cluster, symmetry of independent continuous times makes the identity of the minimum independent of its value. Thus the \(T_v\)'s are i.i.d. and independent of all the \(X_v\)'s.

When \(X_v=0\), a private vertex is accepted at \(T_v\), and \(v\) cannot subsequently be selected. When \(X_v=1\), the only potential obstacle to selecting \(v\) is an earlier accepted core neighbour: its private neighbours have later arrival times. Therefore the accepted core vertices are exactly the result of uniformly random-order greedy selection on \(H[B]\), where \(B=\{v:X_v=1\}\). Since \(\Pr(B)=t^{|B|}/(1+t)^r\), conditioning on \(B\) proves the stated formula for \(\mu_s\). For each cluster with no selected core vertex, the chosen private vertex is the earliest private vertex. Permuting the labels inside every private clique preserves all core decisions and all arrival-time order symmetries. Conditional on any core outcome, the chosen private labels are therefore independent and uniformly distributed; the same is true under the uniform maximal-independent-set law. Their total-variation distance is consequently exactly the distance between \(\mu_s\) and \(\nu_s\).

**3. Strict obstruction.** No core vertex is selected iff \(B=\varnothing\): if \(B\ne\varnothing\), its earliest candidate core must be accepted. Consequently \(\mu_s(\varnothing)=(1+t)^{-r}\), whereas \(\nu_s(\varnothing)=1/Z_H(t)\). Since \(Z_H(t)\) sums over independent subsets whereas \((1+t)^r\) sums over *all* subsets, strict inequality \(Z_H(t)<(1+t)^r\) holds for every \(t>0\) precisely when \(H\) has an edge. This yields the positive displayed lower bound on total variation. If \(H\) is edgeless, the corona is a disjoint union of cliques \(K_{s+1}\); independent local earliest vertices are each uniform, so its random-greedy law is the uniform maximal-independent-set law.

For unequal sizes, the same characterization of maximal sets and the same all-private event apply. The all-private greedy probability is \(\prod_v s_v/(s_v+1)\), the uniform probability is the reciprocal of \(\sum_{I\in\mathcal I(H)}\prod_{v\in I}(1/s_v)\); these differ strictly in the presence of any edge. When the core is edgeless, independent disjoint cliques again yield exact uniformity.

**4. Sharp small-activity expansion.** Put \(m=|E(H)|\) and \(t=1/s\). As \(t\downarrow0\),
\[
Z_H(t)=1+rt+\left({r\choose2}-m\right)t^2+O_H(t^3),
\qquad (1+t)^r=1+rt+{r\choose2}t^2+O_H(t^3).
\]
Thus \(\nu_s(\varnothing)-\mu_s(\varnothing)=m t^2+O_H(t^3)\). For any singleton core set \(\{v\}\), the candidate sets of size at most two contributing to its greedy probability are \(B=\{v\}\), and \(B=\{v,u\}\) when \(uv\in E(H)\), in which case \(v\) wins with probability \(1/2\). Hence
\[
\mu_s(\{v\})=t+\left(\frac{\deg_H(v)}2-r\right)t^2+O_H(t^3),
\quad \nu_s(\{v\})=t-rt^2+O_H(t^3).
\]
For each independent two-element core set, both laws have leading term \(t^2\), so their difference is \(O_H(t^3)\); for larger core sets both probabilities are \(O_H(t^3)\). As \(\sum_v\deg_H(v)/2=m\), the total-variation sum equals \(\tfrac12(m+m)t^2+O_H(t^3)=m t^2+O_H(t^3)\). All expansions have finitely many terms indexed by subsets of fixed \(H\), so the error estimates are uniform over the finite core-outcome set.

**5. Complete-core equality.** When \(H=K_r\), all nonempty core independent sets are singletons; the maximal-set count is \(s^r+r s^{r-1}\), so \(\nu_s(\varnothing)=s/(s+r)\). Permutation symmetry makes every singleton equally likely under either law. Thus every singleton has the opposite-sign discrepancy to the empty state and total variation is exactly \(\nu_s(\varnothing)-\mu_s(\varnothing)\), giving the closed expression.

## Verification

Run the self-contained standard-library program `python verify_corona_greedy.py`. It explicitly builds each labelled corona graph, enumerates *all* vertex orders in each finite test, performs the original greedy algorithm on literal neighbourhoods, and compares the exact core-output probabilities against an independently implemented Bernoulli-candidate expression using rational arithmetic. It also checks normalization, the all-private event, strict nonuniformity for nonempty core edge sets, and exact uniformity for edgeless cores. The tested suite comprises 24 core-graph/clique-size cases, 1,418,450 complete vertex orders, including all core graphs up to three vertices and a selection on four vertices. All tests passed. Finite enumeration is not a proof for unbounded core graphs; the proof above is unrestricted.

## Relationship to prior work

The motivating October 2026 work on greedy uniformity proves rigidity for *trees* and constructs near-uniform mixed spiders [1]; it neither describes clique-corona terminal laws nor gives the coefficient \(|E(H)|\) in a private-clique-size bias expansion. The independently verified local candidate representation uses the standard uniformly random priority model. Kryven, Versendaal and de Vries [2, Proposition 3.8] provide a **sufficient** regular-independent-set criterion for exact uniformity; their 2-uniformity classification does not furnish a necessary criterion for every graph with a uniform random-greedy MIS law, and does not imply the quantitative corona statement. Krivelevich and collaborators [3] principally study the size/density of greedy outputs and local limits, not this labelled terminal-law comparison. Direct comparisons with prior related claims for threshold graphs, chain graphs, clique bouquets, and clique coronas under *different* observables did not produce the formula or the asymptotic coefficient here. Non-identification in searched literature is not a certificate of worldwide priority.

## Limitations

The classification is confined to clique coronas (including unequal private-clique sizes only for rigidity); it does not classify exact uniformity for all graphs. The sharp bias expansion fixes the core graph; constants may depend on it, so no jointly uniform estimate in \(r\) and \(s\) is asserted. The full law uses finite sums of possibly exponentially many subsets, not a claim of polynomial-time evaluation for arbitrary cores. Independent validation and conclusive bibliographic-priority determination have not been performed; a differently named equivalent derivation may exist.

## References

[1] J. Fairfax-Ball, *Greedy Uniformity on Trees: Exact Obstruction and Near-Uniform Spiders*, arXiv:2610.02276v1, first posted October 1, 2026. https://arxiv.org/abs/2610.02276

[2] I. Kryven, R. Versendaal, M. de Vries, *Unified framework for asymptotically uniform iterative construction of generalised random graphs with local constraints*, arXiv:2608.07239v1, August 7, 2026. https://arxiv.org/abs/2608.07239

[3] M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms 64 (2024), 986–1015, DOI:10.1002/rsa.21200.
