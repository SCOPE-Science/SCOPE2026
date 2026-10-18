# Six-vertex threshold for opposite mean and variance responses in neutral Moran absorption

## Finding
For a neutral birth-death Moran process started from a uniformly random single mutant on a finite connected simple undirected graph, define \(\mu(G)=\mathbb E[T_G]\) and \(v(G)=\operatorname{Var}(T_G)\), where \(T_G\) counts **every reproduction attempt**, including attempts that leave the configuration unchanged, until either extinction or fixation. An added edge \(e\) first permits \((\Delta\mu)(\Delta v)<0\) on six vertices. On at most five vertices no connected graph and nonedge have this property. Both possible opposite sign patterns occur on six vertices.

A six-vertex witness for **mean decreasing, variance increasing** has vertex set \(\{0,1,2,3,4,5\}\) and edges
\[
E(G_A)=\{01,12,14,15,23,24,25\}.
\]
Insert edge \(45\). Exact calculation yields
\[
\begin{aligned}
\mu(G_A+45)-\mu(G_A)&=-\frac{1081916058162303045866787}{963350233128823627873660}<0,\\
 v(G_A+45)-v(G_A)&=\frac{2649703944786197307161267260643446006651173670039}{37121746866774353314903473528963649187716871824}>0.
\end{aligned}
\]
Numerically these changes are approximately \(-1.123077\) and \(+71.378751\) steps and squared steps.

A six-vertex witness for **mean increasing, variance decreasing** is the path with edges
\[
E(G_B)=\{01,05,23,34,45\}.
\]
Insert edge \(04\). Its exact changes are
\[
\begin{aligned}
\mu(G_B+04)-\mu(G_B)&=\frac{105624967578948244284048503408}{1743903055352674650362722242735}>0,\\
 v(G_B+04)-v(G_B)&=-\frac{202967717778556498291917406194774045071459109551713420605765406}{3041197866468393825501595763452504490989129760874708260280225}<0.
\end{aligned}
\]
The changes are approximately \(+0.060568\) and \(-66.739399\). Thus adding a migration/replacement opportunity can improve the mean duration while worsening uncertainty, or conversely.

## Assumptions and scope
For every integer \(n\ge2\), let \(G=(V,E)\) be a connected simple undirected graph with \(V=\{0,\ldots,n-1\}\). Initially, choose \(U\) uniformly from \(V\) and make exactly the individual at \(U\) mutant. At every integer time step choose the reproducing vertex uniformly from \(V\), choose the recipient uniformly from its neighbors, and replace the recipient type by the reproducer type. Individuals have equal fitness, so replacement events that do not change the set of mutants still consume one unit of time. The process stops at the first all-mutant or all-resident configuration. The variance is over **both** the random starting vertex and all subsequent process randomness; it is not the average of vertex-conditional variances.

Only insertions of a **single missing undirected edge** are considered, keeping vertex count and all update conventions fixed. Connectedness holds before and after insertion. Neither selection, conditioned-on-fixation time, death-birth updating, directed edges, nor self-loops are part of the claim.

## Proof
Let \(\mathcal S\) be the collection of nonempty proper subsets \(S\subsetneq V\), interpreted as mutant locations. For any ordered neighboring pair \((u,w)\) whose endpoint types disagree, its transition probability is \(1/(n\deg_G(u))\); it replaces the type at \(w\), thereby switching membership of \(w\) in \(S\). Equal-type reproduction attempts are self-loops. Define \(Q_G\) as the transition submatrix between the \(2^n-2\) transient configurations, including its self-loops. Since \(G\) is connected, every transient configuration can reach an absorbing configuration through a finite positive-probability path; therefore absorption is almost sure and \(I-Q_G\) is invertible.

For column vectors of first and second hitting-time moments \(a_S=\mathbb E[T\mid S]\) and \(b_S=\mathbb E[T^2\mid S]\), first-step decomposition gives
\[
(I-Q_G)a=\mathbf 1,\qquad (I-Q_G)b=2a-\mathbf 1.
\]
The second equality follows from \(T=1+T'\) and \(Q_Ga=a-\mathbf1\), with zero moments at either absorbing state. Consequently
\[
\mu(G)=\frac1n\sum_{u\in V}a_{\{u\}},\quad
v(G)=\frac1n\sum_{u\in V}b_{\{u\}}-\mu(G)^2.
\]
These formulas use the full, not conditional, absorption-time distribution and are rational for unweighted finite graphs.

For the **lower bound**, the accompanying `moran_absorption.py` enumerates every labeled simple graph by its edge bitmask for \(2\le n\le5\), retaining the connected ones. It inspects **every** missing-edge insertion in each connected graph. It may canonically relabel vertices to cache statistics, but this does not discard a graph or insertion: all initial labeled pairs are still visited, and both statistics are invariant under relabeling. Its matrix entries and Gaussian elimination use arbitrary-precision fractions throughout. The checked numbers of labeled connected-graph/nonedge pairs are respectively \(0,3,84,3140\) at \(n=2,3,4,5\). In every comparison the product of the two exact changes is nonnegative; hence no smaller graph witnesses opposition. There are no nonedge insertions in a connected one-vertex graph.

For the **upper bound and both directions**, the same program constructs \(G_A\) and \(G_B\) directly from the displayed edge lists, forms \(G_A+45\) and \(G_B+04\), solves the two linear systems exactly, and reproduces the four displayed rational differences. Their strict signs give both six-vertex witnesses. All four graphs are connected and the inserted edges are absent initially. This proves the claimed sharp minimum.

## Verification
Run `python moran_absorption.py` using Python 3 and the standard library only; no data downloads are necessary. It enumerates every relevant labeled graph at orders \(2\) through \(5\), uses canonical relabeling only for exact-statistic caching, tests the sign product with exact fractions, and prints the exact witness differences. The method computes absorption time for every transient bitmask, with both absorbing bitmasks assigned zero moments. The displayed counts refer to **labeled graph/nonedge pairs**, not just isomorphism classes. An independent symbolic matrix calculation was also used for both witnesses. The reproduced outputs appear in `VERIFICATION.md`.

## Relationship to prior work
Lieberman, Hauert and Nowak introduced the Moran birth-death process on graphs and its dependence on network topology [1]. Hindersin and Traulsen studied all six connected four-vertex networks and showed that adding an edge can **increase mean conditional fixation time**; their results also introduce expected sojourn times [2]. This is not the same claim: here absorption includes extinction, and the sign comparison involves the *variance* as well as the mean of the same unconditioned duration. Díaz and collaborators studied expected **absorption time** and polynomial-time bounds for such processes [3], not the simultaneous behavior of first and second moments under one-edge insertion. Hathcock and Strogatz studied higher moments and distributions of **conditioned fixation times** on the complete graph and ring, primarily asymptotically [4]. Their cumulant theory does not classify single-edge changes to **unconditioned** absorption mean and variance on arbitrary six-vertex networks. The Markov moment recurrence itself is standard and is not claimed as new.

## Limitations
The minimality proof is an exact, finite exhaustive computer-assisted argument on graphs through five vertices; it is **not** a human-derived structural characterization of those graphs. The two six-vertex examples are analytically certified by rational linear algebra, but no claim is made that these are the only six-vertex examples. There is no assertion that a given direction is typical, nor an infinite-family or large-population theorem. Unseen literature using aliases such as consensus-time variance or evolutionary first-passage risk might contain an equivalent observation. Empirical and biological interpretation depends on the precise uniform-neutral birth-death rule.

## References
[1] E. Lieberman, C. Hauert and M. A. Nowak, *Evolutionary dynamics on graphs*, Nature **433**, 312--316 (20 January 2005), DOI: 10.1038/nature03204.

[2] L. Hindersin and A. Traulsen, *Counterintuitive properties of the fixation time in network-structured populations*, first arXiv posting 17 June 2014, arXiv:1406.4415; J. R. Soc. Interface **11**, 20140606 (2014).

[3] J. Díaz, L. A. Goldberg, D. Richerby and M. Serna, *Absorption Time of the Moran Process*, initial arXiv posting 29 November 2013, arXiv:1311.7631; Random Structures & Algorithms **49**, 137--159 (2016).

[4] D. Hathcock and S. H. Strogatz, *Fitness dependence of the fixation-time distribution for evolutionary dynamics on graphs*, initial arXiv posting 13 December 2018, arXiv:1812.05652; Phys. Rev. E **100**, 012408 (2019).
