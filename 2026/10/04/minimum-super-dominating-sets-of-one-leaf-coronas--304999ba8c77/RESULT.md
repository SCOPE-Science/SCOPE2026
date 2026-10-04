# Minimum super dominating sets of one-leaf coronas
## Finding
Let \(H\) be any finite simple graph of order \(n\ge1\) with \(c(H)\) connected components, and let \(H\circ K_1\) be its corona obtained by attaching one new leaf \(u_v\) to every \(v\in V(H)\). Then \(\gamma_{\mathrm{sp}}(H\circ K_1)=n\), and the minimum super dominating sets are in bijection with unions of connected components of \(H\): for a union \(X\) of components, select \(u_v\) when \(v\in X\) and select \(v\) when \(v\notin X\). Consequently \[N_{\mathrm{sp}}(H\circ K_1)=2^{c(H)}.\] In particular, if \(H\) is connected then \(H\circ K_1\) has exactly two minimum super dominating sets, namely the original vertex set and the full pendant-leaf set; if \(H\) is a tree, this gives an infinite tree family with exactly two minima.

## Assumptions and scope
All graphs are finite, simple, and undirected. Let \(H\) have vertex set \(V(H)\), order \(n\ge1\), and \(c(H)\) connected components. The corona \(H\circ K_1\) is formed by adjoining, for every \(v\in V(H)\), a new leaf \(u_v\) adjacent only to \(v\).

A set \(D\subseteq V(G)\) is super dominating if every \(x\notin D\) has a neighbor \(y\in D\) such that
\[
N_G(y)\cap(V(G)\setminus D)=\{x\}.
\]
Write \(N_{\mathrm{sp}}(G)\) for the number of minimum-cardinality super dominating sets.

## Proof
The graph \(H\circ K_1\) has \(2n\) vertices. The standard lower bound for super domination gives
\[
\gamma_{\mathrm{sp}}(H\circ K_1)\ge n.
\]
The original vertex set \(V(H)\) is super dominating: each outside leaf \(u_v\) is super dominated by \(v\), because every neighbor of \(v\) inside \(H\) is selected. The full pendant-leaf set is also super dominating: each outside original vertex \(v\) is super dominated by its selected leaf \(u_v\). Hence
\[
\gamma_{\mathrm{sp}}(H\circ K_1)=n.
\]

Let \(D\) be a minimum super dominating set, so \(|D|=n\). For every \(v\in V(H)\), at least one vertex of the pair \(\{v,u_v\}\) belongs to \(D\). Otherwise the outside leaf \(u_v\) would have no neighbor in \(D\). Since there are \(n\) disjoint pairs and \(|D|=n\), exactly one vertex from every pair belongs to \(D\).

Define
\[
X=\{v\in V(H):v\notin D\}.
\]
If \(v\notin X\), then \(v\in D\) and \(u_v\notin D\). The leaf \(u_v\) has only one neighbor, namely \(v\), so \(v\) itself must super dominate \(u_v\). Therefore no neighbor of \(v\) in \(H\) can lie outside \(D\), and hence
\[
N_H(v)\cap X=\varnothing.
\]
Thus no edge of \(H\) joins \(X\) to \(V(H)\setminus X\). Equivalently, \(X\) is a union of connected components of \(H\).

Conversely, let \(X\) be any union of connected components of \(H\), and put
\[
D_X=\{u_v:v\in X\}\cup\{v:v\in V(H)\setminus X\}.
\]
For every outside original vertex \(v\in X\), its selected leaf \(u_v\) is adjacent to no other outside vertex, so it super dominates \(v\). For every outside leaf \(u_v\) with \(v\notin X\), the selected vertex \(v\) has no neighbor in \(X\), because no edge crosses the component union; hence its only outside neighbor is \(u_v\), which it super dominates. Thus \(D_X\) is a minimum super dominating set.

The map \(X\mapsto D_X\) is bijective between unions of connected components of \(H\) and minimum super dominating sets of \(H\circ K_1\). Since a graph with \(c(H)\) components has exactly \(2^{c(H)}\) unions of components,
\[
N_{\mathrm{sp}}(H\circ K_1)=2^{c(H)}.
\]
For connected \(H\), only \(X=\varnothing\) and \(X=V(H)\) occur, giving exactly the original vertices and the pendant leaves.

## Verification
The included checker independently enumerates every labeled simple graph \(H\) on one through five vertices. For each base graph it constructs \(H\circ K_1\), enumerates every vertex subset of size at most \(|V(H)|\), tests the super domination condition directly, computes the connected components of \(H\), and compares the complete list of minimum sets with the component-union classification.

The verification covers all \(1099\) labeled base graphs of orders at most five and all relevant candidate subsets, without using the theorem in the super-domination test.

## Relationship to prior work
Klein, Rodríguez-Velázquez, and Yi study the super domination number of corona products and obtain closed formulas for the scalar parameter \(\gamma_{\mathrm{sp}}\). Their corona section does not enumerate all minimum super dominating sets; an exact value of \(\gamma_{\mathrm{sp}}\) alone does not determine their number or structure.

Ghanbari, Jäger, and Lehtilä later introduce \(N_{\mathrm{sp}}(G)\), count minimum super dominating sets for selected families such as paths and cycles, and explicitly list counting minimum super dominating sets in trees as a future direction. The one-leaf corona theorem above gives a complete enumeration for every base graph and, when \(H\) is a tree, for an infinite tree family. Their paper distinguishes the usual corona \(G\circ H\) from the neighborhood corona, and its enumeration section does not state the component-union formula above.

A 2026 paper on the super domatic number proves that \(H\circ K_1\) admits a partition into two super dominating sets, using the original vertices and the leaves. That partition result does not classify all minimum super dominating sets and does not imply the factor \(2^{c(H)}\) for disconnected bases.

## Limitations
The theorem concerns the ordinary corona with exactly one pendant vertex attached to each base vertex. It does not enumerate minimum super dominating sets of \(H\circ F\) for larger attached graphs \(F\), nor of the neighborhood corona. The count depends only on the connected-component partition of the base, but no claim is made here about nonminimum super dominating sets or the full super domination polynomial. Literature searches cannot exclude a differently phrased or non-indexed prior enumeration.

## References
1. D. J. Klein, J. A. Rodríguez-Velázquez, E. Yi, “On the super domination number of graphs,” arXiv:1705.00928v1, 2 May 2017; Communications in Combinatorics and Optimization 5(2) (2020), 83–96, DOI 10.22049/cco.2019.26587.1122.
2. N. Ghanbari, G. Jäger, T. Lehtilä, “Super Domination: Graph Classes, Products and Enumeration,” arXiv:2209.01795v1, 5 September 2022; Discrete Applied Mathematics 349 (2024), 8–24, DOI 10.1016/j.dam.2024.01.039.
