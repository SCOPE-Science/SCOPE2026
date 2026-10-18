# A degree-to-farness reversal of epidemic-outbreak variance on every nontrivial contact tree

## Finding
For **every** finite contact tree with at least three vertices, changing the per-edge infection probability forces a change in which initially infected vertex maximizes *final-outbreak-size variance*. At weak transmission every maximizing source is a maximum-degree internal vertex. At almost-certain transmission every maximizing source is a leaf of maximum total distance (maximum **farness**). The universal first-order laws, with explicit graph invariants, are
\[
\operatorname{Var}(X_v(p))=\deg_T(v)\,p+O_T(p^2),\qquad p\downarrow0,
\]
\[
\operatorname{Var}(X_v(p))=(1-p)\bigl(nD_T(v)-W(T)\bigr)+O_T((1-p)^2),\qquad p\uparrow1.
\]
The smallest possible network is the three-vertex path. On that path the center has strictly larger variance for \(0<p<(\sqrt{13}-3)/2\), while either leaf has strictly larger variance for \((\sqrt{13}-3)/2<p<1\); all three tie only at the unique interior transition (and at the excluded endpoints).

## Assumptions and scope
Let \(T=(V,E)\) be an arbitrary finite, undirected, connected acyclic simple graph with \(n=|V|\ge3\). Infect exactly one designated vertex \(v\) at generation zero. An individual remains infectious for exactly one generation, independently infecting each still-susceptible neighbor across a contact edge with fixed probability \(p\in(0,1)\), then recovering permanently. Transmission attempts on distinct edges are mutually independent. An edge has at most one potential successful attempt on a tree. Let \(X_v(p)\) count all infected vertices, including the seed. Define
\[
D_T(v)=\sum_{u\in V}\operatorname{dist}_T(v,u),\qquad W(T)=\sum_{\{u,w\}\subseteq V}\operatorname{dist}_T(u,w).
\]
The big-O constants may depend on \(T\) but are uniform over the finitely many candidate roots \(v\). Optimization means maximizing \(\operatorname{Var}(X_v(p))\) over every possible initially infected vertex of the *same* tree.

## Proof
**Percolation representation and low-transmission regime.** Sample each tree edge as independently open with probability \(p\). Since a tree has a unique path from the seed to every other vertex and no retransmission along alternative paths, the infected set is exactly the open component of \(v\). At \(p=0\), \(X_v=1\); to first order the only nontrivial outcome is one open edge incident to \(v\), causing \(X_v=2\) with total probability \(\deg_T(v)p+O_T(p^2)\). Outcomes with at least two open edges have probability \(O_T(p^2)\). Consequently \(\operatorname{Var}(X_v(p))=\deg_T(v)p+O_T(p^2)\), uniformly across vertices. Because degrees are integers and the vertex set is finite, there is \(\varepsilon_0(T)>0\) such that every maximizing root for \(0<p<\varepsilon_0(T)\) has maximum degree. Every tree with \(n\ge3\) has maximum degree at least two, and a leaf has degree one, hence all these roots are internal.

**Near-certain transmission.** Write \(q=1-p\). For an edge \(e\), let \(s_e(v)\) denote the number of vertices in the component of \(T-e\) not containing \(v\). With zero closed edges \(X_v=n\). With exactly one closed edge \(e\), \(n-X_v=s_e(v)\), and the probability of this exact failure event is \(q(1-q)^{n-2}=q+O_T(q^2)\). The total probability of two or more closed edges is \(O_T(q^2)\), and \(0\le n-X_v\le n-1\). Therefore
\[
\mathbb E[(n-X_v)^2]=q\sum_{e\in E}s_e(v)^2+O_T(q^2),\quad \mathbb E[n-X_v]=O_T(q),
\]
so
\[
\operatorname{Var}(X_v)=q\sum_{e\in E}s_e(v)^2+O_T(q^2).
\]
If removing edge \(e\) produces components with cardinalities \(s_e(v)\) and \(n-s_e(v)\), then
\[
s_e(v)^2=n\,s_e(v)-s_e(v)(n-s_e(v)).
\]
The sum \(\sum_e s_e(v)\) counts the number of edges on the unique path from \(v\) to every other vertex, hence equals \(D_T(v)\). The sum \(\sum_e s_e(v)(n-s_e(v))\) counts each unordered vertex pair once for every separating edge, hence equals the Wiener index \(W(T)\). Thus
\[
\sum_{e\in E}s_e(v)^2=nD_T(v)-W(T),
\]
which proves the second asymptotic law.

**Maximizers are peripheral near \(p=1\).** If an internal vertex \(v\) has degree at least two, the disjoint branches obtained by deleting \(v\) have positive sizes totaling \(n-1\). At least one neighboring branch has size \(b<n/2\). Let \(w\) be its neighbor. Distances from \(w\) increase by one to the \(n-b\) vertices outside that branch and decrease by one to its \(b\) vertices. Hence \(D_T(w)-D_T(v)=n-2b>0\). Therefore no internal vertex maximizes \(D_T\): every maximizer of farness is a leaf. Uniformity of the high-transmission expansion and finiteness of \(V\) give \(\varepsilon_1(T)>0\) such that for \(1-\varepsilon_1(T)<p<1\), every variance-maximizing root maximizes \(D_T(v)\), and so is a leaf. The low- and high-transmission optimal sets are disjoint, proving unavoidable optimizer change on **every** tree with \(n\ge3\).

**Sharp minimum.** A one- or two-vertex tree has equivalent root positions, so no change of optimal location is possible. For the unique three-vertex path, direct independent-edge enumeration gives the variance difference
\[
V_{\mathrm{center}}(p)-V_{\mathrm{leaf}}(p)=p(p-1)(p^2+3p-1).
\]
The quadratic has one positive zero \((\sqrt{13}-3)/2\in(0,1)\). Since \(p(p-1)<0\) on \((0,1)\), the center is strictly optimal below this root and either leaf is strictly optimal above it. This proves sharpness and the exact first transition.

## Verification
The attached `verify.py` independently constructs exact outbreak-size moment polynomials by enumerating root-to-vertex paths and their edge unions. It checks both asymptotic coefficients and the Wiener/farness identity for every root of every nonisomorphic tree on three through nine vertices, as well as the exact three-vertex crossover factorization. The script requires Python 3, `networkx`, and `sympy`, and prints a success message on complete execution. Finite checks supplement, but do not replace, the general proof above.

## Relationship to prior work
Network epidemic/percolation representations and component-size calculations are established; see Newman–Jensen–Ziff (2002), Newman (2002), and Kenah–Robins (2006 preprint, published 2007). Those sources motivate the model, not a claim of novelty for percolation coupling itself. The distinct claim here is a uniform, all-finite-trees **variance-optimal seed switch** and the exact high-transmission link to the Wiener index and vertex farness. The older abstract-accessible sources did not supply this rank-reversal theorem in inspected material; full-text overlap remains an explicit bibliographic risk.

## Limitations
This is a *variance* criterion, not a statement that the source giving the largest expected outbreak changes or that infecting a leaf is more dangerous in expectation. The small- and large-transmission regimes are tree-dependent; no universal numerical threshold is asserted. The result does not cover contact graphs with cycles, heterogeneous/dependent transmission, multiple initial seeds, or stochastic infection periods. Independent bibliographic validation has not been performed. Since full text of some historically relevant material was not accessible, an unlocated equivalent argument cannot be excluded.

## References
1. Newman, M. E. J., Jensen, I., and Ziff, R. M. (2002), *Percolation and epidemics in a two-dimensional small world*, Physical Review E 65, 021904. First published January 16, 2002. https://doi.org/10.1103/PhysRevE.65.021904
2. Newman, M. E. J. (2002), *Spread of epidemic disease on networks*, Physical Review E 66, 016128. https://doi.org/10.1103/PhysRevE.66.016128
3. Kenah, E., and Robins, J. M. (2007), *Second look at the spread of epidemics on networks*, Physical Review E 76, 036113; preprint arXiv:q-bio/0610057 (October 30, 2006). https://doi.org/10.1103/PhysRevE.76.036113
