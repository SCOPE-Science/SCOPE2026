# Sharp wild number of properly colored complete-bipartite prisms

## Finding

**Theorem.** For every integer \(n\ge2\), set \(H_n=K_{n,n}\square K_2\). In each of the two layers use any proper \(n\)-edge coloring of \(K_{n,n}\), with a common palette of \(n\) horizontal colors; the colorings of the two layers may be different. Assign all \(2n\) vertical edges the same new color. This defines a minimum proper \((n+1)\)-edge coloring \(\rho\). Its wild number is exactly

\[
\operatorname{wld}_{\rho}(H_n)=2n+1.
\]

A single size-\(2n+1\) construction works for **every pair of independent horizontal 1-factorizations** of the two layers. The lower bound is sharp simultaneously in every dimension parameter \(n\ge2\).

## Assumptions and scope

All graphs are finite and simple. Label the two sides of \(K_{n,n}\) by \(A=\{a_0,\ldots,a_{n-1}\}\) and \(B=\{b_0,\ldots,b_{n-1}\}\). A vertex of the prism is \((x,h)\), with layer \(h\in\{0,1\}\). Its edges are the horizontal edges \((a_i,h)(b_j,h)\) for each layer and the vertical edges \((x,0)(x,1)\). Each horizontal layer uses an arbitrary proper \(n\)-edge coloring onto the same \(n\) named horizontal colors; all vertical edges get a single additional named color. Since every vertex has degree \(n+1\), this is a minimum proper edge coloring.

For any edge coloring \(\rho:E(H)\to\mathcal C\), a *color-connecting edge set* is a set \(W\subseteq E(H)\) such that, for every \(c\in\mathcal C\), the spanning graph with edges \(W\cup\rho^{-1}(c)\) is connected. The *wild number* \(\operatorname{wld}_{\rho}(H)\) is the minimum cardinality of such a set \(W\). The edges in \(W\) become usable in every color.

## Proof

**Lower bound.** The prism has \(4n\) vertices. Because \(\rho\) is a proper coloring with exactly \(n+1\) colors of an \((n+1)\)-regular graph, every monochromatic class \(M_c\) is a perfect matching with \(2n\) edges and hence \(2n\) connected components. Given any color-connecting set \(W\), at least \(2n-1\) edges from \(W\setminus M_c\) are required to join these components. Thus

\[
|W|-|W\cap M_c|\ge 2n-1\qquad(c\in\mathcal C).
\]

The \(n+1\) classes \(M_c\) partition the edge set, so summing the inequalities gives

\[
n|W|\ge(n+1)(2n-1)=2n^2+n-1.
\]

Since \(n\ge2\) and \(|W|\) is integral,

\[
|W|\ge\left\lceil 2n+1-\frac1n\right\rceil=2n+1.
\]

This is an application of the component-count obstruction already available in the wild-number literature; sharpness is the new issue.

**Construction.** Choose \(a_0\in A\) and \(b_0\in B\). Let \(W\) contain the following three disjoint classes of edges:

1. In layer zero, the \(n-1\) horizontal edges \((a_0,0)(b_j,0)\) for \(j\in\{1,\ldots,n-1\}\).
2. In layer one, all \(n\) horizontal edges \((a_i,1)(b_0,1)\), for \(i\in\{0,\ldots,n-1\}\).
3. The two vertical edges \((a_0,0)(a_0,1)\) and \((b_0,0)(b_0,1)\).

Therefore \(|W|=(n-1)+n+2=2n+1\).

For the vertical color, the monochromatic vertical matching contracts each pair \((x,0),(x,1)\) to one vertex. Under this contraction, the horizontal edges of \(W\) become a double star on \(A\sqcup B\): all edges \(a_i b_0\) and all edges \(a_0 b_j\) with \(j\ne0\). These \(2n-1\) edges form a spanning tree of \(K_{n,n}\), so the original union is connected.

Fix any horizontal color \(c\). In either layer, its edges form a perfect matching between \(A\) and \(B\), regardless of the chosen 1-factorization. In layer one, all \(n\) selected edges incident with \((b_0,1)\), together with the monochromatic matching, connect every vertex of that layer: each \((a_i,1)\) is in the selected star, and its matched \((b_j,1)\) is then attached by its color-\(c\) edge.

In layer zero, the selected star at \((a_0,0)\) connects that vertex to all \((b_j,0)\) with \(j\ne0\), and the color-\(c\) matching connects those vertices to their matched \(A\)-vertices. All of layer zero is thereby connected except possibly the matching pair containing \((b_0,0)\). If the color-\(c\) matching pairs \(a_0\) with \(b_0\), then this pair already attaches to the selected star and the whole layer is connected. Otherwise the only remaining component is the color-\(c\) matched pair \((a_i,0),(b_0,0)\), where \(i\ne0\). In both cases the component of \((a_0,0)\) attaches to the connected first layer using the selected vertical edge at \(a_0\); if a second component exists, it attaches using the selected vertical edge at \(b_0\). Therefore \(W\cup M_c\) connects every vertex.

This reasoning is independent of which matching represents color \(c\) in either layer. Hence \(W\) is color-connecting simultaneously for all \(n+1\) colors. Combining the construction with the lower bound proves the formula. \(\square\)

## Verification

A standalone Python 3 script, `verify_wild_prism.py`, independently constructs both layer 1-factorizations using randomly permuted cyclic Latin-square color assignments, enumerates all horizontal and vertical graph edges, checks that every color is a perfect matching, and performs independent union-find connectivity tests on \(W\cup M_c\). It also exhaustively excludes every edge set smaller than five from being color-connecting for the eight-vertex base case \(n=2\).

Run `python3 verify_wild_prism.py`; the executed output was `VERIFY_OK graph_instances=97 connected_color_checks=671 exhaustive_K22_smaller_subsets=794`. These finite tests do not prove the infinite theorem; the preceding component count and structural connectivity arguments do.

## Relationship to prior work

Anders, Foster-Greenwood, Garcia, and Krawzik introduced color-connecting sets and wild numbers and proved a general monochromatic-component-count lower bound [1]. Their paper treats specific small examples including a six-vertex prism, but not the present four-times-\(n\)-vertex infinite family.

Dawkins, Nappo, Tong, and Zimbizi [2, Sections 4.2 and 5] show that every minimum proper coloring of \(K_{m,n}\) has wild number \(n\) when \(2\le m\le n\), and establish lower bounds for Cartesian products of two nontrivial complete bipartite factors. Their stated bipartite product hypothesis requires both part sizes of the second factor to be at least two, excluding \(K_2\). Neither their component lower bounds nor their single-factor star construction supplies the two-layer color-connecting construction and exact formula here. Their published product-coloring convention uses the same factor coloring across layers; the present upper construction remains valid for arbitrary independent layer colorings using the shared color palette.

Targeted searches under color-connecting sets, wild numbers, edge-coloring 1-factorizations and complete-bipartite prisms did not locate earlier exact coverage. This is evidence from the searched material, not an assertion that all literature has been exhausted.

## Limitations

The assertion covers \(n\ge2\) and precisely the specified \((n+1)\)-colorings (the same vertical color on every vertical edge, horizontal proper colorings that share a common palette). It does **not** establish an exact result for arbitrary minimum proper colorings that mix these classes or for \(K_{m,n}\square K_2\) with \(m\ne n\). The formula is for the minimum size, not a classification of all optimal sets. Historical priority needs independent further comparison; no independent mathematical audit has been performed.

## References

[1] Katie Anders, Briana Foster-Greenwood, Rebecca Garcia, Naomi Krawzik, *The wild number of an edge-colored graph*, arXiv:2508.06711, first posted 8 August 2025. https://arxiv.org/abs/2508.06711

[2] Aleyah Dawkins, Alexander Nappo, Jessie Tong, Christopher Zimbizi, *Wild number for spanning trees in complete and complete bipartite graphs*, arXiv:2610.22142v1, first posted 15 October 2026. https://arxiv.org/html/2610.22142
