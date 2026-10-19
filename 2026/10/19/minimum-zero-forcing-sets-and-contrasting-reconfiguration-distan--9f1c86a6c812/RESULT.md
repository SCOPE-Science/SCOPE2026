# Minimum zero forcing sets and contrasting reconfiguration distances in the Pappus graph

## Finding
Let \(P\) be the Pappus graph, with nine point vertices \(p_{x,y}\) and nine line vertices \(\ell_{m,b}\), indexed by \(x,y,m,b\in\mathbb F_3\), where \(p_{x,y}\sim\ell_{m,b}\) precisely when \(y=mx+b\). Write \(Z(P)\) for the minimum cardinality of an initial blue set from which the usual zero-forcing color-change rule colors every vertex blue.

**Finite classification theorem.** One has \(Z(P)=7\), and exactly \(6912\) minimum zero-forcing sets. Among these, \(3456\) contain three point vertices and four line vertices; the remaining \(3456\) contain four point vertices and three line vertices.

Let \(J(P)\) have the minimum sets as vertices, with an edge between sets differing by replacement of one vertex by any unselected vertex (token jumping). Let \(T(P)\) restrict the replacement to an edge of \(P\) (token sliding). Both graphs are connected, but their distance geometry is sharply different:

\[
\begin{aligned}
|V(J(P))|&=6912,&|E(J(P))|&=97524,&\operatorname{rad}(J(P))&=7,&\operatorname{diam}(J(P))&=7,\\
|V(T(P))|&=6912,&|E(T(P))|&=10962,&\operatorname{rad}(T(P))&=16,&\operatorname{diam}(T(P))&=18.
\end{aligned}
\]

All \(6912\) vertices of \(J(P)\) have eccentricity seven. In \(T(P)\), the numbers of vertices of eccentricities \(16,17,18\) are respectively \(648,4968,1296\). An explicitly checked group of \(216\) automorphisms of \(P\) has \(35\) orbits on the optimal seed sets, and preserves both reconfiguration graphs.

## Assumptions and scope
Throughout, graphs are finite, undirected, and simple. Write \(B_0=S\) for an initial set of blue vertices. Given \(B_t\), a blue vertex forces its unique white neighbor, if one exists; let \(B_{t+1}\) contain \(B_t\) and all such vertices forced at this step. A set is zero forcing if some \(B_t\) is the full vertex set. The sequential color-change rule yields the same closure: each legal force can only become redundant when other vertices become blue, and no white vertex is ever reintroduced. A set is minimum if its size equals \(Z(P)\).

Each configuration is an *unordered* seven-vertex set. A jump changes precisely one selected vertex; a slide additionally requires its departing and arriving vertices to be adjacent in the original Pappus graph. No intermediate suboptimal configurations are allowed. Radius, diameter and eccentricity refer to shortest-path distances in these connected undirected reconfiguration graphs.

## Proof
**(1) Exact base graph and forcing census.** The displayed incidence rule gives \(18\) labeled vertices, \(27\) edges, and degree three at each vertex. The bundled programs `verification/verify_pappus_cpp.cpp` and `verification/verify_pappus_python.py` construct this graph independently, with different vertex indexings. Both test *every* subset of sizes \(1\) through \(7\) by repeated, simultaneous application of all currently enabled forcing moves. They find no forcing subset of sizes \(1\) through \(6\), and exactly \(6912\) forcing subsets of size \(7\). Thus no smaller zero-forcing set exists, and all optimal sets have been enumerated. Counting their incidences with the point class produces the two populations of size \(3456\) each, with no other splits.

**(2) Exact exchange graphs.** For each enumerated optimal set \(S\), the programs test every pair \((u,v)\) with \(u\in S\) and \(v\notin S\), admitting the exchange \((S\setminus\{u\})\cup\{v\}\) exactly when the replacement is another enumerated optimum; for sliding they also require \(u\sim v\) in \(P\). Since each exchange has a unique departure and arrival vertex, this construction finds every allowed undirected edge exactly twice. The two independent implementations obtain \(97524\) and \(10962\) undirected edges, respectively. Breadth-first component searches show a single component with all \(6912\) states in both graphs.

**(3) Exact shortest-path and centrality census.** The C++ program independently performs breadth-first search from **every one** of the \(6912\) states of each reconfiguration graph and records the maximum distance in every search. It finds the complete eccentricity distributions \(\{7:6912\}\) for jumping and \(\{16:648,17:4968,18:1296\}\) for sliding; taking minima and maxima yields the stated radii and diameters.

**(4) Independent group-orbit distance check.** The Python program builds the same graph from a coordinate convention different from C++, constructs \(108\) affine incidence automorphisms, and composes each with a point–line polarity, obtaining \(216\) distinct vertex permutations. Every one is checked against all \(27\) edges, so these are genuine graph automorphisms. They induce reconfiguration-graph automorphisms, because being a minimum forcing set and being an allowed exchange are invariant under graph automorphisms. The \(6912\) optimal sets partition into exactly \(35\) resulting orbits. Python performs breadth-first searches from one representative of every orbit and multiplies eccentricity counts by its orbit size; it reproduces every eccentricity and both radii and diameters from part (3). Independent degree distributions and edge counts agree as well. These exhaustive finite checks complete the claim. \(\square\)

## Verification
Run from the directory containing the bundled `verification/` subdirectory:

```
g++ -O3 -std=c++17 verification/verify_pappus_cpp.cpp -o verify_pappus_cpp
./verify_pappus_cpp
python3 verification/verify_pappus_python.py
```

The expected stdout is recorded verbatim in `verification/cpp_output.txt` and `verification/py_output.txt`. The C++ code enumerates complete state spaces and executes all-root breadth-first searches; the Python code independently generates and verifies the automorphism reduction and checks all state exchanges. These are executable *finite* proof certificates for the 18-vertex graph, rather than sampled evidence or an unproved induction.

## Relationship to prior work
Zero forcing was introduced to bound maximum nullity and minimum rank by the AIM Minimum Rank group. Davila and Kenter's arXiv preprint (publicly posted 2014-06-02) proves lower bounds for girth-constrained graphs, not a minimum-set or transformation classification for \(P\). Gentner and Rautenbach prove more refined zero-forcing bounds for regular large-girth graphs, not these counts or distances. Geneson, Haas and Hogben introduce and study the general zero-forcing reconfiguration graph, including a token-jumping definition equivalent to \(J(P)\); their primary manuscript's complete text treats general theorems and selected families, without giving the present Pappus-graph calculation. The minimum forcing-set count, full two-move comparison, and exact eccentricity distributions are not implied by those general statements. The original graph is the biaffine incidence graph over \(\mathbb F_3\).

## Limitations
This is an exact result only for the 18-vertex Pappus graph. It does **not** assert a formula for larger biaffine incidence graphs, nor polynomial-time computation for general graphs. This is a same-model finite proof and literature assessment, not an independently validated or externally certified result. Novelty remains subject to independent examination of unindexed literature, supplementary tables, and equivalent formulations. The C++ and Python implementations are structurally distinct but share the same mathematical definitions.

## References
1. AIM Minimum Rank – Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* **428** (2008), 1628–1648, DOI:10.1016/j.laa.2007.10.009.
2. R. Davila and F. Kenter, “Bounds for the Zero-Forcing Number of Graphs with Large Girth,” arXiv:1406.0482, version 1 publicly posted 2014-06-02. https://arxiv.org/abs/1406.0482
3. M. Gentner and D. Rautenbach, “Some Bounds on the Zero Forcing Number of a Graph,” arXiv:1608.00747 (2016). https://arxiv.org/abs/1608.00747
4. J. Geneson, R. Haas and L. Hogben, “Reconfiguration graphs of zero forcing sets,” arXiv:2009.00220 (2020). https://arxiv.org/html/2009.00220v1
5. “Pappus graph,” DistanceRegular.org graph record. https://www.math.mun.ca/distanceregular/graphs/pappus.html
