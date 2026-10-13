# Minimal forts of triangular graphs are spanning star forests or proper cycles

## Finding
For an integer \(n\ge2\), let \(T_n=L(K_n)=J(n,2)\), the triangular graph whose vertices are the edges of the complete graph on \([n]\), with adjacency when edges meet. Identify a subset \(F\subseteq V(T_n)\) with the edge set of the spanning graph \(H=([n],F)\).

**Theorem.** A nonempty \(F\) is an inclusion-minimal fort of \(T_n\) if and only if exactly one of the following holds:

1. \(H\) is a spanning star forest: every connected component is a star on at least two vertices, and there are no isolated vertices. An isolated edge is a permitted two-vertex star.
2. \(H\) is one simple cycle of length \(\ell\) with \(3\le\ell<n\), together with \(n-\ell\) isolated vertices.

Consequently, writing \(M_n(z)=\sum_{F\text{ minimal fort}}z^{|F|}\), with \(M_0(z)=M_1(z)=0\), the complete cardinality enumerator satisfies
\[
\sum_{n\ge0}M_n(z)\frac{u^n}{n!}
=\exp\!\left(\frac{zu^2}{2}+u(e^{uz}-1-uz)\right)-1
+\frac{e^u-1}{2}\left(-\log(1-uz)-uz-\frac{(uz)^2}{2}\right).
\]
In particular the total minimal-fort counts for \(n=2,3,4,5,6,7\) are respectively \(1,3,11,60,308,1659\). The first coefficients of the polynomials for the larger checked orders are
\[
\begin{aligned}
M_5(z)&=40z^3+20z^4,\\
M_6(z)&=35z^3+195z^4+78z^5,\\
M_7(z)&=35z^3+420z^4+777z^5+427z^6.
\end{aligned}
\]
The smallest minimal-fort cardinalities at orders \(2,3,4,5\) and all subsequent orders are respectively \(1,2,2,3\) and \(3\). For \(n\ge7\) there are exactly \(\binom n3\) minimal forts of smallest cardinality, namely the triangles on three of the original labels.

## Assumptions and scope
All graphs are finite, simple, and undirected. A **fort** in a graph \(G\) is a nonempty set \(F\subseteq V(G)\) for which no vertex outside \(F\) has exactly one neighbor in \(F\). It is **inclusion-minimal** if no nonempty proper subset is a fort. Minimal refers to inclusion, not necessarily to minimum cardinality. The variables \(u,z\) are formal; the exponential generating-function identity is an identity in formal power series with rational coefficients, not an assertion about analytic convergence. The count concerns distinct labeled vertex subsets, not isomorphism classes.

## Proof
**Step 1: Translate the fort condition.** Fix a nonempty selected-edge graph \(H=([n],F)\). For every edge \(ab\) absent from \(H\), the corresponding vertex of \(T_n\) has exactly
\[
\deg_H(a)+\deg_H(b)
\]
neighbors in \(F\): these are the selected edges incident with either endpoint; the two sets are disjoint because the edge \(ab\) itself is absent. Therefore \(F\) fails to be a fort precisely when an absent edge has one endpoint of degree zero and the other of degree one. Because \(K_n\) is the ambient graph, every pair consisting of an isolated vertex and a degree-one vertex is joined by an absent edge. Hence, for nonempty \(F\),
\[
F\text{ is a fort}\quad\Longleftrightarrow\quad
\bigl(\delta(H)\ge1\bigr)\ \text{or}\ \bigl(\text{every vertex has degree }0\text{ or at least }2\bigr).
\]
(The two alternatives can overlap.)

**Step 2: Minimal forts without isolated vertices.** Suppose \(F\) is a minimal fort and \(H\) has no isolated vertices. Then \(F\) is an edge cover of \(K_n\)'s labeled vertex set. If deleting one of the selected edges leaves no isolated vertex, the remaining edge set is a proper fort, a contradiction. Thus every selected edge has a degree-one endpoint. In a simple graph without isolated vertices, this means every component is a star: any connected nonstar contains an edge whose endpoints both have degree at least two. Therefore \(H\) is a spanning star forest. Conversely, in a spanning star forest, each edge has a leaf endpoint and is indispensable to covering all vertices. Every nonempty proper selected-edge subset therefore has an isolated vertex. It is also a nonempty forest and thus has a degree-one vertex. By Step 1 it is not a fort, proving inclusion-minimality.

**Step 3: Minimal forts with isolated vertices.** Suppose \(F\) is a minimal fort and \(H\) has at least one isolated vertex. By Step 1 it has no degree-one vertices. Since \(F\ne\varnothing\), some nontrivial connected component of \(H\) has minimum degree at least two and therefore contains a simple cycle. Its cycle edge set is a nonempty fort: its selected degrees are only zero and two, and at least one original vertex is isolated. This cycle edge set is a subset of \(F\), so minimality forces equality. Because the original isolated vertex lies outside this cycle, the cycle has length less than \(n\). Conversely, deleting at least one edge from a proper cycle leaves each nonempty proper selected-edge subset as a forest with a degree-one vertex; the original vertices outside the cycle remain isolated. Such a subset is not a fort. Thus precisely the proper cycles constitute the second class.

**Step 4: Enumerate star forests.** In a labeled component of size two there is exactly one star, contributing the exponential-generating-function term \(zu^2/2\). For component size \(s\ge3\) there are \(s\) choices of center and \(s-1\) selected edges, so these components contribute
\[
\sum_{s\ge3} \frac{s\,u^s z^{s-1}}{s!}
=u(e^{uz}-1-uz).
\]
A spanning star forest is an unordered set of these labeled components. The exponential formula gives \(\exp(zu^2/2+u(e^{uz}-1-uz))\). Subtract one to exclude the empty graph, which would correspond to no fort.

**Step 5: Enumerate proper cycles.** On a fixed set of \(\ell\ge3\) labels there are \((\ell-1)!/2\) unoriented simple cycles, contributing
\[
\sum_{\ell\ge3}\frac{(\ell-1)!}{2}\frac{u^\ell z^\ell}{\ell!}
=\frac12\left(-\log(1-uz)-uz-\frac{(uz)^2}{2}\right).
\]
A proper cycle must leave at least one unused labeled vertex, giving the independent factor \(e^u-1\). The two minimal-fort classes are disjoint, so adding their contributions proves the generating-function identity.

**Step 6: Minimum-cardinality consequences.** A spanning star forest covering \(n\) vertices has at least \(\lceil n/2\rceil\) selected edges; each proper cycle has at least three. At \(n=2,3,4\), inspect the possible star forests to obtain minima \(1,2,2\). At \(n=5,6\), the possible minimum three-edge configurations consist respectively of thirty spanning star forests plus ten triangles, and fifteen perfect matchings plus twenty triangles. For \(n\ge7\), every spanning star forest uses at least four edges, so the \(\binom n3\) proper triangles are exactly the minimum forts. This also follows coefficientwise from the established generating function.

## Verification
Run the included Python 3 standard-library program `python3 verify.py`. It constructs \(T_n\)'s actual adjacency masks, checks every nonempty selected vertex subset for the fort condition, and tests inclusion-minimality using all proper subsets rather than assuming the fort property is monotone. The verifier compares the resulting size distribution to a separately computed labeled-star recurrence plus a proper-cycle count. At \(n\le6\), it additionally tests candidate classification for every subset, including rejected candidates. The direct test runs over \(2{,}131{,}018\) subsets for \(2\le n\le7\). It also checks the labeled-component recurrence through \(n=20\). Captured exact output is included in `verification_output.txt`. The infinite theorem is justified by Steps 1–5, not by finite computation.

## Relationship to prior work
The fort condition and its relevance to zero forcing and fort hypergraphs were developed by Cameron, Hogben, Kenter, Mojallal and Schuerger [1]. Becker, Cameron, Hanely, Ong and Previte [2] systematically count minimal forts of paths, cycles, spiders, and several product and bouquet families, and explain their role in fort-cover models. Those results motivate the present full minimal-fort census but do not give the triangular-graph structural classification or polynomial stated here. The related work of Afzali, Ghodrati and Maimani [3] studies the scalar **failed zero-forcing number** for Johnson and other graphs; that scalar result is not an all-minimal-forts enumerator. In particular, the minimum-cardinality-three phenomenon for sufficiently large triangular graphs is not claimed as an original contribution. Unlike that scalar information, this theorem determines all inclusion-minimal forts by shape and size at every order.

## Limitations
The claim concerns only triangular graphs \(J(n,2)\) with the ordinary, not skew, fort condition; it does not classify forts of general Johnson graphs \(J(n,k)\). The generating function counts labeled vertex sets, not unlabelled orbit types. A plausible related Johnson-graph paper [3] was accessible only at the abstract level, so equivalent enumeration results appearing in its full text or in unindexed graph-enumeration literature remain a bibliographic risk. The proof is self-contained; no independent audit or formal verification is asserted.

## References
[1] T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904v1, first posted 2023-10-27. https://arxiv.org/abs/2310.17904

[2] P. Becker, T. R. Cameron, D. Hanely, B. Ong, J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963v1, first posted 2024-04-09. https://arxiv.org/abs/2404.05963

[3] F. Afzali, A. H. Ghodrati, H. R. Maimani, *Failed zero forcing numbers of Kneser graphs, Johnson graphs, and hypercubes*, *Journal of Applied Mathematics and Computing*, 70 (2024), 2665–2675, DOI:10.1007/s12190-024-02064-w; published abstract consulted, full text unavailable.
