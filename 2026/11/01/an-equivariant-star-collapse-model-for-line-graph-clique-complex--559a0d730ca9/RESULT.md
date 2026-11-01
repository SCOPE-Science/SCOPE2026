# An equivariant star-collapse model for line-graph clique complexes

## Finding

**Theorem.** Let \(G\) be any finite simple graph of minimum degree at least three, and let \(K=\operatorname{Cl}(L(G))\) be the clique complex of its line graph. Subdivide once, stellarly, every maximal simplex whose vertices are the edges of \(G\) incident to a fixed vertex. The resulting complex admits a canonical \(\operatorname{Aut}(G)\)-invariant, orbitwise simplicial collapse onto the edge-midpoint subdivision of \(\operatorname{Cl}(G)^{(2)}\), the two-skeleton of the clique complex of \(G\). In particular, this gives an automorphism-equivariant simple-homotopy equivalence, and the associated equivalences on all subgroup-fixed realizations and finite symmetry quotients.

For \(G=K_n\), \(n\ge4\), set \(A_n=\ker(\mathbb Z^n\xrightarrow{\varepsilon}\mathbb Z)\), where \(\varepsilon\) sums coordinates. Under the natural permutation action of \(S_n\), this collapse identifies the **integral** second reduced homology with the exterior cube of the augmentation lattice:

\[
\widetilde H_2\bigl(\operatorname{Cl}(L(K_n));\mathbb Z\bigr)\cong_{\mathbb Z[S_n]}\bigwedge^3 A_n.
\]

All other reduced integral homology groups vanish, and nonequivariantly the complex has homotopy type \(\bigvee^{\binom{n-1}{3}}S^2\). Over \(\mathbb Q\), the representation is the hook Specht module \(S^{(n-3,1,1,1)}\). The nonequivariant wedge and the general rational character determination are acknowledged as previous coverage; the asserted advance is the explicit **automorphism-invariant simple collapse** and its integral equivariant identification.

## Assumptions and scope

A graph is finite, loopless, undirected, and simple. The minimum-degree hypothesis is \(\deg_G(v)\ge3\) at every vertex. Write \(m_{ij}\) for the vertex of \(K\) corresponding to an edge \(\{i,j\}\) of \(G\). For each original vertex \(i\), set \(A_i=\{m_{ij}:\{i,j\}\in E(G)\}\). These sets are facets because of minimum degree, and distinct sets have at most one vertex in common. Every clique of \(L(G)\) lies in some \(A_i\) or is exactly the three edge-vertices of a triangle of \(G\).

The canonical edge-midpoint subdivision \(B(G)\) of \(\operatorname{Cl}(G)^{(2)}\) has original vertices denoted \(b_i\), midpoint vertices \(m_{ij}\), subdivided edges \([b_i,m_{ij}]\) and \([m_{ij},b_j]\), and, for every triangle \(\{i,j,k\}\), the four triangles \([b_i,m_{ij},m_{ik}]\), \([b_j,m_{ij},m_{jk}]\), \([b_k,m_{ik},m_{jk}]\), and \([m_{ij},m_{ik},m_{jk}]\). The \(\operatorname{Aut}(G)\) action permutes both kinds of vertices in the evident way.

## Proof

**(1) Facet classification.** A set of at least four different two-element subsets of \(V(G)\) that pairwise intersect has a common vertex. For three such subsets, either they have a common vertex or they are the three edges of a triangle. This proves the facet description. A star of size at least three cannot be contained in a triangle facet, hence every \(A_i\) is a maximal simplex; distinct star facets share at most one vertex.

**(2) Canonical subdivision.** Stellarly subdivide all facets \(A_i\) by introducing \(b_i\) and replacing \(A_i\) by the cone \(b_i*\partial A_i\). The interiors of these facets are disjoint, so the subdivisions commute, and the construction is invariant under every graph automorphism. All original central triangle facets are unaffected.

**(3) Orbitwise free-face eliminations.** For each \(i\), each proper subset \(F\subsetneq A_i\) with \(|F|\ge3\), in descending order of \(|F|\), eliminate the pair of simplices \((F,F\cup\{b_i\})\). The pair is free: no distinct star contains two edge-vertices of \(A_i\), no central triangle contains three of them, and all larger star faces and their cones have already been removed. After this, if \(j\ne k\) are neighbors of \(i\) with \(\{j,k\}\notin E(G)\), eliminate the free pair \((\{m_{ij},m_{ik}\},\{b_i,m_{ij},m_{ik}\})\). The only possible *other* coface of that two-element set would have been the central triangle of edges \(ij,ik,jk\), which is absent exactly when \(jk\) is not an edge.

All remaining faces have at most two edge-vertices in a star. Such pairs survive precisely when the other endpoints are adjacent, hence exactly the triangles of \(B(G)\) listed above survive. The other remaining faces are their subsets and the subdivided original edges. Thus the final complex is exactly \(B(G)\), not merely abstractly homotopy equivalent to it. If \(d_i\) is the degree of \(i\) and \(t_i\) its number of incident graph triangles, the number of elementary pairs removed at \(i\) is exactly \(2^{d_i}-d_i-2-t_i\): all proper star subsets of cardinality at least three, together with the nontriangle pairs.

For every group element \(g\in\operatorname{Aut}(G)\), the pair indexed by \((i,F)\) is sent to the pair indexed by \((g(i),g(F))\). Each face of size at least two identifies its star center uniquely, so disjoint pairs in a given dimension form complete automorphism orbits; the free pair and its cone have identical stabilizers. Their orbitwise removals are therefore equivariant elementary collapses. Stellar subdivision is an equivariant PL homeomorphism, proving the first assertion and the fixed-point and quotient consequences.

**(4) Integral \(S_n\)-lattice.** For \(G=K_n\), the target is the two-skeleton of the \((n-1)\)-simplex. With \(E=\mathbb Z^n\) on the vertex basis and \(\varepsilon(e_i)=1\), its degree-two simplicial chain group is \(\bigwedge^3E\), and its differential is contraction by \(\varepsilon\):

\[
\partial_2(e_i\wedge e_j\wedge e_k)
=e_j\wedge e_k-e_i\wedge e_k+e_i\wedge e_j.
\]

The splitting \(E=A_n\oplus\mathbb Ze_n\), valid over \(\mathbb Z\), shows directly that \(\ker\partial_2=\bigwedge^3A_n\). This is an identity of \(\mathbb Z[S_n]\)-lattices, because \(\partial_2\) and \(\varepsilon\) are permutation-equivariant. Explicit generators are \((e_i-e_n)\wedge(e_j-e_n)\wedge(e_k-e_n)\) with \(1\le i<j<k<n\); each is a primitive signed boundary of one tetrahedron. The full simplex chain complex is exact below degree two, so \(\widetilde H_1=0\), and there are no chains above degree two in the target. Its two-skeleton is simply connected for \(n\ge4\), and Hurewicz plus the homological Whitehead theorem yield the stated nonequivariant sphere wedge. The rational Specht identification follows from \(\bigwedge^3\) of the rational standard permutation-augmentation representation.

## Verification

Run `python3 verify.py` with Python 3.10 or later; no nonstandard packages are needed. The included `verification_output.txt` is the actual output of this program. The verifier enumerates every simplex, independently recreates all stellar subdivisions, checks each proposed free-face pair against **all current cofaces**, and compares the final complex as a set of simplices with the declared midpoint subdivision. It verifies complete symmetric-group equivariance of the final complex and every pair orbit for \(K_4,K_5,K_6\); checks the full procedure for \(K_7\), the cube, the triangular prism, a one-edge deletion of \(K_5\), and the Petersen graph; and checks integral three-cycle boundaries and all group-action matrices for \(S_4,S_5,S_6,S_7\). It terminates with `VERIFY_OK`.

Finite checking supports, but does not replace, the uniform combinatorial proof of the free-face condition and the exterior-algebra argument. No claim of a machine proof for all graphs is made.

## Relationship to prior work

Linusson, Shareshian, and Welker (first publicly posted 2004-10-15) introduced the bounded-matching complexes \(\mathrm{NM}_k(n)\) and established the nonequivariant wedge result; \(\mathrm{NM}_2(n)=\operatorname{Cl}(L(K_n))\). Their Question 1.13 asks for the symmetric-group action on the top homology. Thus the wedge count is *not* new. Goyal, Shukla, and Singh (2020) explicitly proved the general nonequivariant homotopy equivalence \(\operatorname{Cl}(L(G))\simeq\operatorname{Cl}(G)^{(2)}\) by a nerve argument (Lemma 3.2); that equivalence is prior coverage, and this statement does not claim to rediscover it. A 2026 online investigation of the bounded-matching question gives a general rational character formula via equivariant Euler–Poincaré; that formula already determines the rational character in principle, but neither an integral augmentation-lattice identification nor the graph-uniform orbitwise simplicial collapse is established there. Larrión, Pizaña, and Villarroel-Flores (2008) develop equivariant collapse techniques for *iterated clique graphs*, whose vertices are maximal graph cliques rather than the original graph edges; those results concern a different graph operation and do not specify the star-face pairs here. The present comparison is therefore deliberately restricted to **integral equivariant structure and constructive equivariant simple homotopy**, not generic sphere counts, generic character formulas, or ordinary homotopy equivalences.

## Limitations

The explicit construction assumes every graph vertex has degree at least three. It does not classify the \(\mathbb Z[S_n]\)-lattices for \(\mathrm{NM}_k(n)\) when \(k>2\). The abstract two-sphere-wedge equivalence is nonequivariant; no claim of an equivariant splitting into independently permuted spheres is made. Other equivalent constructions may exist, particularly through stronger equivariant nerve or subdivision theorems not exhaustively indexed. No independent external mathematical audit or definitive publication-priority determination has been performed.

## References

1. Svante Linusson, John Shareshian and Volkmar Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345, first posted 2004-10-15; especially Theorem 1.1 and Question 1.13. https://arxiv.org/abs/math/0410345
2. Shuchita Goyal, Samir Shukla and Anurag Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130, first posted 2020-09-25; especially Lemma 3.2. https://arxiv.org/abs/2009.12130
3. *Complexes of Graphs with Bounded Matching Size*, ProbXiv discussion of the general rational character of bounded-matching complexes, posted 2026-08-17. https://probxiv.com/problems/complexes-of-graphs-with-bounded-matching-size-2 (online mathematical discussion, not independently certified).
4. F. Larrión, M. A. Pizaña and R. Villarroel-Flores, *Equivariant collapses and the homotopy type of iterated clique graphs*, Discrete Mathematics **308** (2008), 3199–3207, DOI 10.1016/j.disc.2007.06.021. This studies iterated maximal-clique intersection graphs, not line graphs.
