# General-position polynomial of rectangular rook graphs via bipartite star forests

## Finding
Let \(m,n\ge 2\) be integers and let \(R_{m,n}=K_m\square K_n\), the rook graph on an \(m\)-by-\(n\) board. Write
\[
\Psi_{m,n}(z)=\sum_{\substack{S\subseteq V(R_{m,n})\\S\text{ is in general position}}} z^{|S|},
\]
where a vertex set is in general position when no three of its vertices lie on a common shortest path. Then the entire two-parameter family has the bivariate exponential generating function
\[
\boxed{\sum_{m,n\ge0}\Psi_{m,n}(z)\frac{u^m v^n}{m!\,n!}
=\exp\!\left(u e^{zv}+v e^{zu}-zuv\right).}
\]
Here \(\Psi_{m,n}\) is extended by the same subset definition to nonnegative \(m,n\); an empty factor gives an edgeless rook graph and polynomial \(1\).

The degree and leading coefficient for \(m,n\ge2\) are
\[
\deg\Psi_{m,n}=m+n-2,
\qquad
[z^{m+n-2}]\Psi_{m,n}(z)=
\begin{cases}
6,&m=n=2,\\
2^{\max\{m,n\}},&\min\{m,n\}=2<\max\{m,n\},\\
mn,&m,n\ge3.
\end{cases}
\]
The degree formula is an established result, recalled for context; the complete polynomial and its leading-coefficient classification are the contribution here. For example,
\[
\Psi_{2,3}(z)=1+6z+15z^2+8z^3,\qquad
\Psi_{3,3}(z)=1+9z+36z^2+48z^3+9z^4.
\]

## Assumptions and scope
Graphs are finite, undirected, and simple. Board positions are individually labeled by a row in \([m]\) and a column in \([n]\). A general-position set is an **unordered subset of positions**, so no set is counted more than once. The generating-function variables \(u,v\) mark row and column labels, respectively, and \(z\) marks selected positions. All generating functions are formal power series; no analytic convergence assumption is needed.

The complete bipartite graph \(K_{m,n}\) has one vertex for each row and one for each column. Selecting a board position corresponds to selecting its row-to-column edge. Thus subsets of the rook graph's vertices correspond bijectively to spanning subgraphs of \(K_{m,n}\), with isolated vertices retained.

## Proof
**Step 1: Exact structural bijection.** In a rook graph two distinct positions are adjacent precisely when they share a row or column; otherwise their graph distance is two. A triple violates general position exactly when it can be ordered \(a,b,c\) with \(a\) and \(c\) in different rows and columns and \(b\) sharing a row or column with each. Their three bipartite edges then form a simple three-edge path in the selected subgraph of \(K_{m,n}\). Conversely, every simple three-edge path in a selected bipartite subgraph produces such a forbidden triple of rook positions.

A bipartite graph has no simple three-edge path if and only if every connected component is a star, allowing isolated vertices and single edges. Indeed, if an edge joins two vertices of degree at least two, distinct extra neighbors at its endpoints produce a three-edge path (the extra neighbors lie in opposite bipartition classes and hence are different). If no such edge exists, every nontrivial connected component has at most one vertex of degree greater than one, so is a star. Consequently general-position sets are in a weight-preserving bijection with **spanning star forests** of \(K_{m,n}\).

**Step 2: Enumerate the connected components.** Use two colors of labels for the parts of \(K_{m,n}\). An isolated row vertex contributes \(u\); an isolated column vertex contributes \(v\). A single-edge component contributes \(uvz\) and is counted exactly once. A star having its center in the row part and at least two column leaves contributes
\[
u\sum_{d\ge2}\frac{(vz)^d}{d!}=u(e^{vz}-1-vz).
\]
The opposite orientation contributes \(v(e^{uz}-1-uz)\). The exponential formula for sets of disjoint labeled components gives
\[
\sum_{m,n\ge0}\Psi_{m,n}(z)\frac{u^m v^n}{m!\,n!}
=\exp\!\left(u+v+uvz+u(e^{vz}-1-vz)+v(e^{uz}-1-uz)\right).
\]
Simplifying the exponent yields the claimed expression \(\exp(u e^{zv}+v e^{zu}-zuv)\).

**Step 3: The top degree and every maximizer.** A spanning star forest with \(c\) components on \(m+n\) vertices has exactly \(m+n-c\) edges. When \(m,n\ge2\), no star spans all vertices, hence \(c\ge2\) and every general-position set has size at most \(m+n-2\). Two disjoint stars with opposite-side centers attain this bound.

If \(m,n\ge3\), equality forces exactly two components, each nontrivial. Both centers cannot lie in the same part, since that would leave an isolated vertex in that part. Thus choose one row center and one column center; all other vertices are forced to attach to the center in the opposite part. This gives exactly \(mn\) distinct maximizers.

If \(m=2<n\), the equality size is \(n\). A selected column vertex of degree two would have both row vertices as neighbors and preclude all other selected edges, giving only two edges, less than \(n\). Thus every column vertex must have degree one to attain \(n\) edges, and its unique row neighbor may be chosen independently, yielding \(2^n\) maximizers. The case \(n=2<m\) is symmetric. Finally \(R_{2,2}\) is the four-cycle; any two of its four vertices form a general-position set, yielding \(\binom42=6\) maximizers. This also proves the stated degree in all cases.

## Verification
The accompanying standalone script `check.py` implements a labeled-component recurrence, and separately enumerates every subset of a small rook graph, rejecting triples according to the metric definition, without using the star-forest bijection. For \(m,n\ge0\), with \(F_{0,n}=F_{m,0}=1\), its recurrence is
\[
F_{m,n}(z)=F_{m-1,n}(z)
+\sum_{d=1}^{n}\binom nd z^d F_{m-1,n-d}(z)
+n\sum_{q=1}^{m-1}\binom{m-1}{q}z^{q+1} F_{m-1-q,n-1}(z).
\]
For a distinguished row vertex, the three terms treat it as isolated, as a star center with \(d\) leaves, or as one leaf in a column-centered star with \(q\ge1\) other row leaves. Execute `python3 check.py` with Python 3; its exhaustive checks cover 24 ordered size pairs with \(1\le m\le5\), \(1\le n\le6\), and \(mn\le16\), totaling 146,762 candidate vertex subsets. Exact agreement of polynomial coefficients and extremal counts was observed. The general theorem follows from the combinatorial proof, not the finite tests.

## Relationship to prior work
Aroca and Lladó (arXiv:1512.02161v1; publicly available 2015-12-07) study **ascending decompositions** of bipartite graphs into star forests, motivating attention to the same structural class. Their results neither enumerate all spanning star forests of complete bipartite graphs nor address general-position polynomials. Ghorbani and collaborators (arXiv:1903.04286) already establish \(\operatorname{gp}(K_m\square K_n)=m+n-2\); the scalar degree is not claimed as original. Iršič and collaborators (arXiv:2401.05696) introduce and investigate the general-position polynomial and calculate Cartesian products of paths, but their displayed results do not yield the bivariate rook-graph formula. Stones (2014) counts **all** spanning forests of complete bipartite graphs by edge number; those counts do not separate star forests from other forests, so cannot directly supply this general-position enumeration.

## Limitations
The theorem treats only Cartesian products of two complete graphs, not three or more factors or arbitrary line graphs. It supplies exact enumerators and maximizing-set counts, but does not assert unimodality, real-rootedness, or asymptotic coefficient estimates. A prior unindexed enumeration of bipartite star forests, if available, could give an equivalent generating function; the literature comparison does not establish absolute novelty. No independent audit has been performed.

## References
1. J. M. Aroca and A. Lladó, *On star-forest ascending subgraph decomposition*, arXiv:1512.02161v1, 2015-12-07, https://arxiv.org/html/1512.02161v1.
2. M. Ghorbani, S. Klavžar, H. R. Maimani, M. Momeni, F. R. Mahid, and G. Rus, *The general position problem on Kneser graphs and on some graph operations*, arXiv:1903.04286v2, https://arxiv.org/html/1903.04286v2.
3. V. Iršič, S. Klavžar, G. Rus, and J. Tuite, *General Position Polynomials*, arXiv:2401.05696v1, https://arxiv.org/html/2401.05696v1.
4. R. J. Stones, *Computing the number of h-edge spanning forests in complete bipartite graphs*, Discrete Mathematics & Theoretical Computer Science 16 (2014), 313–326, https://dmtcs.episciences.org/articles/1248.
