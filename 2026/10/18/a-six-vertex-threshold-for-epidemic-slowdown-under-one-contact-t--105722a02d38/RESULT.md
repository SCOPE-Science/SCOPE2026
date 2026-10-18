# A six-vertex threshold for epidemic slowdown under one-contact transmission

## Finding

In the one-contact, one-generation susceptible–infectious–removed process defined below, adding one contact edge can **decrease** the expected final outbreak size. Six vertices are necessary and sufficient for such a decrease among finite connected, undirected, simple contact networks when the initial case is uniformly distributed over vertices.

Specifically, let \(G_m=K_{2,m}\) for an integer \(m\ge 1\), with its two vertices of degree \(m\) called hubs. Let \(H_m\) add the edge between those hubs (the \(m\)-page book graph). Writing \(M\) for the uniform-seed expected number ever infected, one has

\[
M(G_m)=\frac{4m+3}{m+2},\qquad
M(H_m)=\frac{8m^3+21m^2+23m+8}{2(m+1)^2(m+2)},
\]
\[
M(H_m)-M(G_m)=-\frac{m^2-3m-2}{2(m+1)^2(m+2)}.
\]

Consequently the edge **increases** the expectation when \(m\in\{1,2,3\}\), and **decreases** it for every integer \(m\ge4\). The first witness, on six vertices, has \(M(K_{2,4})=19/6\), \(M(H_4)=79/25\), and decrease \(1/150\). An exhaustive exact-rational check proves that no edge addition can decrease this expectation in any connected simple graph on at most five vertices.

## Assumptions and scope

The contact network is any finite connected undirected simple graph \(G=(V,E)\) with at least two vertices. The index case is chosen uniformly from \(V\). At each discrete generation there is exactly one infectious individual. That individual independently chooses **one** neighbor uniformly from all its graph neighbors, not just from susceptible neighbors, then immediately becomes permanently removed. If the chosen neighbor has never been infected, that neighbor is infected for the next generation; otherwise transmission fails and the outbreak ends. Contact succeeds with probability one when its target is susceptible; no one loses immunity. In particular, repeatedly contacting an already infected individual consumes the entire final contact opportunity. The outcome is equivalently a simple random walk stopped on its **first return to any previously visited vertex**; the final outbreak size counts distinct visited vertices before that return.

This is deliberately **not** the usual model in which an infectious individual independently attempts transmission across every incident edge. The conclusion concerns a fixed one-contact budget, a uniformly random index case, and expected cumulative infections; it does not concern a reproduction number, a long-time SIS prevalence, or an epidemic on an infinitely large population.

## Proof

For a current infectious vertex \(v\) and already-infected set \(S\ni v\), write \(F(v,S)\) for the conditional expected number of newly counted vertices **including \(v\)** from this generation onward. With \(d(v)\) the graph degree, first-step conditioning yields the exact acyclic recurrence

\[
F(v,S)=1+\frac{1}{d(v)}\sum_{w\sim v,\,w\notin S}F(w,S\cup\{w\}).
\]

The sum is empty when all neighbors of \(v\) have already been infected. Since every recursive call strictly increases \(|S|\), this recurrence uniquely determines a rational result and terminates after at most \(|V|\) levels. Averaging over roots gives

\[
M(G)=\frac{1}{|V|}\sum_{v\in V}F(v,\{v\}).
\]

For the two graph families, count probabilities of reaching successive new vertices. Before the hub-to-hub edge is added, the outbreak starting at a hub visits two vertices surely, a third with probability \(1/2\), and a fourth with probability \((m-1)/(2m)\). It cannot infect more than four. Starting at a peripheral vertex, it visits two surely; the probabilities of reaching its third, fourth, and fifth vertices are respectively \((m-1)/m\), \((m-1)/(2m)\), and \((m-1)(m-2)/(2m^2)\). These probabilities apply also when \(m=1\), with zero probability for unavailable longer paths. Thus

\[
F_{G_m}(\mathrm{hub})=3-\frac{1}{2m},\qquad
F_{G_m}(\mathrm{peripheral})=4-\frac{3}{m}+\frac{1}{m^2}.
\]

After the edge is added, a hub has \(m+1\) neighbors. A hub-rooted outbreak reaches its third vertex with probability \(m/(m+1)^2+m/(2(m+1))\), and its fourth with probability \(m(m-1)/(2(m+1)^2)\). A peripheral-rooted outbreak reaches its third vertex with probability \(m/(m+1)\), its fourth with probability \((m-1)/(m+1)^2+(m-1)/(2(m+1))\), and its fifth with probability \((m-1)(m-2)/(2(m+1)^2)\). Therefore

\[
F_{H_m}(\mathrm{hub})=\frac{3m+2}{m+1},\qquad
F_{H_m}(\mathrm{peripheral})=\frac{8m^2+9m+3}{2(m+1)^2}.
\]

In each graph there are exactly two hubs and \(m\) peripheral vertices. Averaging with weights \(2/(m+2)\) and \(m/(m+2)\) proves the two displayed rational expressions for \(M\), and their difference simplifies to the displayed quadratic fraction. Its denominator is positive. The integer sign threshold follows from \(m^2-3m-2<0\) for \(m=1,2,3\) and \(m^2-3m-2>0\) for all \(m\ge4\).

It remains to prove minimality. The accompanying standalone Python program enumerates every labelled graph on \(n\in\{2,3,4,5\}\) by its \(\binom n2\)-bit edge mask, discards only disconnected graphs, and considers **every missing undirected edge** in each remaining graph. For each comparison it computes both expectations by exact rational Bellman recursion and independently by enumerating all self-avoiding infection paths with their exact contact-probability weights, including the terminal unsuccessful contact. It asserts equality of the two calculations and asserts that no added edge lowers the uniform-root mean. The run finds respectively \(1,4,38,728\) connected labelled graphs and \(0,3,84,3140\) eligible edge-addition comparisons for \(n=2,3,4,5\), totalling \(3227\) comparisons, with zero decreases. The program explicitly includes all graphs with at least two vertices up to five and all their edge insertions; it uses neither random sampling nor graph-isomorphism assumptions. Together with the six-vertex witness, this establishes the claimed exact minimum order.

## Verification

Execute `python3 contact_outbreak_check.py` using Python 3's standard library. It recomputes every connected labelled graph of orders \(2\) through \(5\), evaluates every permitted edge addition with `fractions.Fraction`, compares two independent algorithms for the same expectation, verifies the analytic formulas for every integer \(1\le m\le16\), and prints the six-vertex and seven-vertex exact examples. The arbitrary test range \(m\le16\) is **not** used to infer the infinite-family theorem; the above algebra proves the formula and sign for **all** integers \(m\ge1\).

## Relationship to prior work

Kenah and Robins (2006 preprint) develop a broad epidemic-percolation description for stochastic SIR networks; that framework does not by itself assert monotonicity or give the present exact first-order edge-addition cutoff under a constrained one-contact budget. Gómez and colleagues (2009 preprint) distinguish contact-based from reactive spreading, with the one-neighbor probability normalized by vertex degree; their primary analysis is SIS prevalence and thresholds rather than this permanently immune, one-generation final-size problem. Enright and Kao (public online in 2016) compute exact expected outbreak sizes on outbreak-invariant directed acyclic contagion networks, with different contact-independence assumptions; their results supply computational context but do not imply the present graph-family expressions or exhaustive minimum size. Holme (2015) explores how contact-pattern representations affect prediction of SIR outbreak sizes but does not classify this exact finite combinatorial boundary.

The decisive distinction is that inserting an edge changes each endpoint's **contact allocation probabilities** rather than simply adding an independent new opportunity. The exact counterexample exploits competition for a fixed single contact.

## Limitations

The minimality assertion covers only the specified epidemic process and **uniform seed distribution**, and is exhaustively proved only through five-vertex graphs before the six-vertex witness. Other transmission budgets, recoveries, contact success probabilities, directed or weighted graphs, and nonuniform seed distributions require separate analysis. The analytic family is infinite, but no claim is made to classify all larger graphs or to quantify prevalence in realistic populations. This is an internally checked mathematical result; no independent external audit is claimed.

## References

1. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, first public arXiv preprint 2006-10-30, arXiv:q-bio/0610057, https://arxiv.org/abs/q-bio/0610057 .
2. S. Gómez, A. Arenas, J. Borge-Holthoefer, S. Meloni, Y. Moreno, *Discrete-time Markov chain approach to contact-based disease spreading in complex networks*, first public arXiv preprint 2009-07-07, arXiv:0907.1313, https://arxiv.org/abs/0907.1313 .
3. J. Enright and R. R. Kao, *A fast algorithm for calculating an expected outbreak size on dynamic contagion networks*, published online 2016-05-24, *Epidemics* 16 (2016), 56–62, DOI:10.1016/j.epidem.2016.05.002, https://eprints.gla.ac.uk/131522/ .
4. P. Holme, *Information content of contact-pattern representations and predictability of epidemic outbreaks*, first published 2015-09-25, *Scientific Reports* 5, 14462 (2015), DOI:10.1038/srep14462, https://www.nature.com/articles/srep14462 .
