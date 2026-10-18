# Clique-corona limited domination: a complete cardinality polynomial and an optimizer transition

## Finding

Let \(H\) be any finite simple graph with vertex set \(V\), \(|V|=n\ge1\), and let \(s\ge2\) and \(k\ge1\) be integers. Form its *clique corona* \(W_s(H)=H\odot K_s\) by adjoining to each core vertex \(v\) a private clique \(P_v\) of \(s\) vertices, adjacent to \(v\) and to no vertices outside the resulting \((s+1)\)-clique except for the original edges of \(H\). A \(k\)-limited dominating set \(D\) is a dominating set with \(|N_G(x)\setminus D|\le k\) for each \(x\in D\).

**Theorem.** Define \(\mathcal L_{H,s,k}(z)=\sum_{D}z^{|D|}\), where the sum ranges over **all** \(k\)-limited dominating sets of \(W_s(H)\). For \(B\subseteq V\), write \(d_B(v)=|N_H(v)\setminus B|\), and put
\[
R_{s,k}(z)=\sum_{j=\max\{1,s+1-k\}}^s {s\choose j}z^j,
\qquad
Q_{s,k,d}(z)=\sum_{j=\max\{0,s+d-k\}}^s {s\choose j}z^j.
\]
Empty sums are zero. Then the entire cardinality polynomial is
\[
\boxed{\mathcal L_{H,s,k}(z)
=\sum_{B\subseteq V}z^{|B|}R_{s,k}(z)^{n-|B|}
\prod_{v\in B}Q_{s,k,d_B(v)}(z).}
\]
In particular, independently of the core edges,
\[
\boxed{\gamma_k^{\mathrm L}(W_s(H))=n\max\{1,s+1-k\}.}
\]
All minimum sets admit the following *if-and-only-if* classifications.

For \(1\le k\le s\), every private cluster together with its core has exactly \(s+1-k\) selected vertices. The selected core vertices form a union of connected components of \(H\); conversely every such union, with any locally admissible private selections, is a minimum set. If the connected components of \(H\) have orders \(h_1,\ldots,h_c\), the number of distinct minimum sets is
\[
\boxed{M_{H,s,k}=\prod_{i=1}^c
\left[{s\choose k-1}^{h_i}+{s\choose k}^{h_i}\right].}
\]
For \(k>s\), a minimum set contains exactly one vertex in each \((s+1)\)-clique. Its selected core set \(B\) must and need only satisfy \(d_B(v)\le k-s\) for each \(v\in B\). Thus
\[
\boxed{M_{H,s,k}=\sum_{\substack{B\subseteq V\\ d_B(v)\le k-s\ \forall v\in B}}s^{n-|B|}.}
\]
At the common boundary \(k=s\) the component formula agrees with the second formula with tolerance zero. If \(k\ge s+\Delta(H)\), then \(M_{H,s,k}=(s+1)^n\). For connected \(H\), the low-capacity optimizer count \({s\choose k-1}^n+{s\choose k}^n\) depends only on the core order, whereas above the threshold it is governed by the core's directed edge boundary.

## Assumptions and scope

All graphs are finite, undirected, simple, and labeled for enumeration. The core may be disconnected or consist of one vertex. Each private clique is vertex-disjoint from every other private clique and the core; the core has precisely its original edges. The formula counts vertex subsets, not isomorphism types. The upper-capacity case \(k\ge\Delta(W_s(H))\) is included algebraically; it reduces to classical domination. No algorithmic polynomial-time claim is made for arbitrary core \(H\): the displayed formula contains a sum over all subsets of its vertex set.

## Proof

Write \(B=D\cap V\) and \(j_v=|D\cap P_v|\). The private clique \(P_v\) has no external neighbors other than its own core vertex. Therefore \(D\) dominates \(P_v\) exactly when \(v\in D\) or \(j_v\ge1\). When \(v\notin D\), domination of \(v\) itself is automatic if \(j_v\ge1\).

If \(v\notin B\), then \(j_v\ge1\). Each selected private vertex sees precisely \(s-j_v+1\) vertices outside \(D\) inside its cluster (the other unselected private vertices and the unselected core). Its capacity condition is thus \(j_v\ge s+1-k\). This yields the lower bound \(j_v\ge\max\{1,s+1-k\}\), and contributes the factor \(R_{s,k}\).

If \(v\in B\), then \(v\) has \(s-j_v+d_B(v)\) neighbors outside \(D\), so its capacity condition is \(j_v\ge s+d_B(v)-k\). Selected private vertices, if any, see only \(s-j_v\) neighbors outside \(D\); their capacity constraints follow from that of the core. Hence the necessary and sufficient range is \(j_v\ge\max\{0,s+d_B(v)-k\}\), contributing \(Q_{s,k,d_B(v)}\). Choosing which of the \(s\) private vertices are selected gives binomial coefficients. As the choice of \(B\) is unique and all other conditions are local conditional on \(B\), multiplying these factors and summing proves the polynomial identity with no omissions or double-counting.

Every feasible \(D\) meets each clique-cluster, because otherwise private vertices would be undominated. If \(k\ge s\), this gives \(|D|\ge n\), attained by all core vertices (each then sees exactly \(s\) outside private neighbors). If \(1\le k<s\), an occupied cluster with omitted core must have at least \(s+1-k\) selected private vertices. If its core is selected, it must have at least \(s-k\) selected private vertices (since \(d_B(v)\ge0\)), so it also contains at least \(s+1-k\) selected vertices in total. This lower bound is attained by taking exactly \(s+1-k\) private vertices in each cluster and no cores. The exact value of \(\gamma_k^{\mathrm L}\) follows.

For \(1\le k\le s\), a minimum set must have exactly \(t=s+1-k\) vertices in every cluster. When its core \(v\) is selected, \(j_v=t-1=s-k\); the core capacity condition becomes \(k+d_B(v)\le k\), hence \(d_B(v)=0\). Conversely, any core subset \(B\) with this boundary-zero property (equivalently a union of connected components) gives a minimum set by taking \(s-k\) of the \(s\) private vertices for every \(v\in B\) and \(s+1-k\) of them for every \(v\notin B\). The former has \({s\choose k}\) private choices, the latter \({s\choose k-1}\). For a component of size \(h\), either all its cores are selected, contributing \({s\choose k}^h\), or none, contributing \({s\choose k-1}^h\). Multiply independently over components.

For \(k>s\), each cluster has exactly one selected vertex in a minimum set. If it is private, its outside-neighbor count is \(s\le k\). If it is the core \(v\), its outside-neighbor count is \(s+d_B(v)\), giving the stated condition. For each admissible \(B\) the \(n-|B|\) other clusters each offer exactly \(s\) private choices. This proves the second counting formula. Since \(d_B(v)\le\Delta(H)\), all \(B\) are admissible if \(k\ge s+\Delta(H)\), and the binomial theorem gives \((s+1)^n\). The \(k=s\) overlap obeys the same zero-boundary condition as the first case.

## Verification

The standalone Python 3 verifier `verify_clique_corona.py` constructs the actual graph adjacency bitmasks, exhaustively tests domination and outside-neighbor capacity for each labeled vertex subset, and independently reconstructs the stated coefficient formula and both minimum-count formulas. It covers every labeled simple graph on one through four core vertices, with \(s\in\{1,2,3\}\) for up to three core vertices and \(s\in\{1,2\}\) for four, across the tested positive capacities through \(k=s+n\). A total of 857 graph-parameter cases and 1,877,184 candidate subsets were checked. The script's output is embedded as `verification_output.txt`. Small finite enumeration is a consistency check; the theorem for all \(n,s,k\) rests on the proof above.

## Relationship to prior work

Božović, Radić, Kovijanić-Vukićević and Tepeh (2026) introduced \(k\)-limited domination and obtained general bounds and results for paths, stars, complete and complete bipartite graphs. Their results do not provide the above all-subset polynomial for arbitrary clique coronas or the optimizer transition. Their analysis of ordinary leaf coronas concerns the distinct special case \(s=1\), and the general lower bound is already prior work. Tepeh (2026) analyzes Cartesian products of *leaf* coronas, attaching independent pendant vertices rather than clique gadgets, and does not imply the present full counting statement. The local clique computation here is motivated by contrasting low-capacity component rigidity and high-capacity core-cut dependence, not by claiming the easier domination number as the sole contribution.

## Limitations

The closed polynomial is a finite exponential subset sum in general. It does not yield a polynomial-time coefficient algorithm for unrestricted core graphs and does not characterize isomorphism classes of optimizers. The low-capacity component count is specific to uniform clique gadgets; it does not extend without changes to pendant independent-set gadgets. Searches did not exclude every synonym or unindexed prior work. The result has undergone self-review only and has not received an independent external mathematical audit.

## References

1. D. Božović, G. Radić, Ž. Kovijanić-Vukićević and A. Tepeh, *On \(k\)-limited domination in graphs*, arXiv:2606.22422v1 (first posted 2026-06-21), https://arxiv.org/abs/2606.22422 ; open-access journal text https://doi.org/10.1007/s40314-026-03902-2 .
2. A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428v1 (first posted 2026-06-21), https://arxiv.org/abs/2606.22428 .
