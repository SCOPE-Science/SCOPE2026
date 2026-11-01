# Complete bipartite strong Morse complexes collapse to doubled graph spines

## Finding
Let \(K_{m,n}\) be the complete bipartite graph regarded as a one-dimensional simplicial complex, with integers \(m,n\geq2\). Let \(\mathcal{SM}(K_{m,n})\) be the **full** strong discrete-Morse matching complex of Knudson and Owens–White, formed as the downward closure of all strong matchings induced by injective vertex filtrations. Then \(\mathcal{SM}(K_{m,n})\) **simplicially collapses onto a connected graph** with exactly \(2mn\) vertices and \(4mn-m-n\) edges. Consequently,

\[
|\mathcal{SM}(K_{m,n})|\simeq\bigvee^{\,2mn-m-n+1}S^1.
\]

Equivalently, the homotopy type is that of the multigraph obtained from \(K_{m,n}\) by replacing each edge with two parallel edges. In particular its fundamental group is free of rank \(2mn-m-n+1\), its first integral homology is free abelian of that rank, and all higher reduced integral homology vanishes. The statement holds for unequal part sizes and includes \(K_{2,2}\cong C_4\), whose five-circle case was previously established.

## Assumptions and scope
Write the bipartition as disjoint nonempty sets \(A,B\), with \(|A|=m\) and \(|B|=n\). The matching-complex vertices are ordered pairs \((u,v)\) with \(uv\) an edge, encoding the vertex–edge pair \(\{u,uv\}\). There are \(2mn\) such vertices. For a vertex ordering of the one-dimensional graph, the descending link of a vertex is a discrete set of its earlier neighbors. It is a nonempty cone exactly when that vertex has **one** earlier neighbor. Accordingly, the strong matching contains \((u,v)\) exactly when \(v\) is the unique earlier neighbor of \(u\). The resulting matching is downward-closed to obtain \(\mathcal{SM}\), as required by the cited definition. No higher-dimensional faces are inserted into the input graph.

## Proof
**1. An exact facet family.** For each original vertex \(v\), put
\[
T_v=\{(u,v):uv\in E(K_{m,n})\},
\]
and regard this set as a simplex. These \(m+n\) simplices have pairwise disjoint vertex sets. For every \(a\in A,b\in B\), define the additional simplices
\[
F^A_{a,b}=\{(b,a)\}\cup\{(a',b):a'\in A\setminus\{a\}\},
\]
\[
F^B_{a,b}=\{(a,b)\}\cup\{(b',a):b'\in B\setminus\{b\}\}.
\]
We claim that these \(m+n+2mn\) simplices are exactly the facets of the full strong Morse complex.

Every listed simplex is realized by an order: \(T_a\) by placing \(a\) first, then every vertex of \(B\), then the other vertices of \(A\); \(T_b\) symmetrically; \(F^A_{a,b}\) by placing \(a,b\), then \(A\setminus\{a\}\), then \(B\setminus\{b\}\); and \(F^B_{a,b}\) symmetrically. Conversely consider an arbitrary order. Suppose its first vertex belongs to \(A\). If at least two vertices of \(A\) precede the first vertex of \(B\), no vertex of \(B\) ever has exactly one earlier neighbor; all strong pairs point into the first vertex of \(B\), so the matching is contained in its target simplex. Otherwise write \(a\) for the first vertex and \(b\) for the first opposite-part vertex. Until the second vertex of \(A\) arrives, all paired vertices, if any, point into \(a\). If two or more vertices of \(B\) have appeared by then, no vertex of \(A\) can subsequently pair, and the matching lies in \(T_a\). If exactly one \(B\)-vertex has appeared, \(b\) pairs toward \(a\), and all subsequent possible pairings point into \(b\), with their sources in \(A\setminus\{a\}\); the matching lies in \(F^A_{a,b}\). The case when the first vertex belongs to \(B\) is symmetric. Hence the family generates exactly the complex. Every listed simplex is maximal: each \(F\) has an exclusive mixed-target edge, and no \(T_v\) is contained in a different generator. The count follows.

**2. Collapse the mixed-target cones.** The simplex \(F^A_{a,b}\) is a cone from the apex \((b,a)\in T_a\) over the face \(T_b\setminus\{(a,b)\}\). Similarly \(F^B_{a,b}\) is a cone from \((a,b)\in T_b\) over \(T_a\setminus\{(b,a)\}\). A face containing at least one vertex from each of two distinct target simplices lies in precisely **one** such cone: it contains a directed two-step configuration \((b,a),(a',b)\), with \(a'\ne a\), or its opposite-part counterpart, and the middle vertex and orientation determine the unique cone. Thus mixed-target faces of positive dimension are not shared between different cones.

For each cone, choose a base vertex \(r\). For every nonempty subset \(S\) of the other base vertices, in **decreasing order of \(|S|\)**, delete the elementary free-face pair
\[
\{\mathrm{apex}\}\cup S\quad<\quad\{\mathrm{apex},r\}\cup S.
\]
Every indicated lower face is free when removed: larger mixed-target cofaces have already been deleted, and no different cone contains the mixed-target face. What remains of this cone is its base simplex, its apex, and a single edge joining the apex to \(r\).

**3. Collapse the target simplices.** After all mixed-target cones have been reduced to edges, each \(T_v\) meets the rest of the complex only along its own vertices. Choose a root \(r_v\in T_v\). For every subset \(S\subseteq T_v\setminus\{r_v\}\) of size at least two, in decreasing size order, collapse the pair
\[
S\quad<\quad S\cup\{r_v\}.
\]
These are free-face pairs because no surviving mixed edge contains two vertices of the same target simplex, and higher faces within \(T_v\) have been removed. Thus \(T_v\) becomes its star tree on all its original vertices. This gives an explicit sequence of simplicial elementary collapses of the **entire** complex onto a graph.

**4. Count the graph and identify its homotopy type.** All \(2mn\) complex vertices remain. The target trees contribute
\[
\sum_{v\in A\cup B}(|T_v|-1)=n(m-1)+m(n-1)=2mn-m-n
\]
edges. The mixed cones contribute exactly \(2mn\) further distinct edges, one per \(F^A\) or \(F^B\). The graph is connected because each target tree is connected and, for every \(a\in A,b\in B\), the mixed cones provide edges between the two target trees. Its cycle rank is therefore
\[
(4mn-m-n)-(2mn)+1=2mn-m-n+1.
\]
Contracting a spanning tree gives the stated wedge of circles. Alternatively, contract each individual target tree: the resulting graph has one vertex per original graph vertex and precisely two parallel edges for each original edge, showing the claimed doubled-graph interpretation. These contractions are graph homotopy equivalences, whereas the preceding reductions are genuine simplicial collapses. This proves the result for all \(m,n\ge2\). \(\square\)

## Verification
The accompanying standard-library Python checker independently enumerates every injective vertex ordering for nine parameter pairs, builds the strong matching directly from earlier-neighbor counts, and compares its entire face complex with the explicit generator family. It then checks the exact proposed elementary collapse sequence one free-face pair at a time, confirms the final connected graph and its edge/vertex counts, and calculates its first Betti number. Tested pairs: \((m,n)=(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4)\). The test covers \(132624\) orderings and checks \(738\) elementary collapses, returning `VERIFY_OK`. Run `python3 verify.py` using Python 3.9 or later. The infinite-family conclusion follows from the symbolic collapse proof, not from this finite test.

## Relationship to prior work
Knudson and Owens–White introduce the full strong Morse complex and compute paths, cycles, stars, simplices, and their boundaries. Their Theorem 7.1 treats \(K_{1,n}\) and their Proposition 8.5 computes \(K_{2,2}\cong C_4\), which agrees with the five-circle specialization here; neither provides the all-parameter classification for \(m,n\ge2\). Their Proposition 10.3 concerns disjoint unions, not joined bipartite parts. Indexed calculations for the **ordinary** Morse complex of \(K_{2,n}\) and \(K_{3,3}\) apply to the larger space of all acyclic Morse matchings, not to the strong subcomplex, and do not imply the present strong-complex homotopy type. In particular, the ordinary Morse complex of \(K_{3,3}\) has been reported as a wedge of eighty four-spheres, whereas this theorem gives a wedge of thirteen circles for its strong counterpart.

## Limitations
This is a theorem about the **full strong** complex, not its pure subcomplex or the ordinary Morse complex. Its proof uses complete bipartite adjacency with both parts of size at least two; it does not establish an analogous formula for missing-edge bipartite graphs, complete multipartite graphs with three or more parts, or higher-dimensional input simplicial complexes. No equivariant homotopy equivalence or integral automorphism-module classification is asserted. The indexed comparisons do not exclude an equivalent treatment in inaccessible or unindexed literature.

## References
1. K. P. Knudson and A. Owens–White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, first posted 2026-09-06. https://arxiv.org/html/2609.06844v1 (Definitions 3.2 and 4.2, Theorem 7.1, Proposition 8.5, Propositions 10.2–10.3).
2. M. K. Chari and M. Joswig, *Complexes of discrete Morse functions*, Discrete Mathematics 302 (2005), 39–51 (ordinary discrete-Morse matching complex; cited in reference 1).
