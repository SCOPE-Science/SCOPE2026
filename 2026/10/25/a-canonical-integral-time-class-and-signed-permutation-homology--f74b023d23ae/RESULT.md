# A canonical integral time class and signed-permutation homology of graph flex complexes

## Finding
Let \(G\) be a finite connected simple undirected graph with \(n\ge2\) vertices. Let \(F(G)=\operatorname{Flex}(G)\) be the cubical complex of source/sink changes of all edge orientations, and let \(J\) reverse every edge orientation. Write \(\mathcal C(G)\) for the set of connected components of \(F(G)\) with the homotopy type of a circle. The graph automorphism group and \(J\) act on \(F(G)\), and commute.

**Integral equivariant classification.** There is a *canonical*, simultaneously equivariant choice of generator \(\eta_C\in H_1(C;\mathbb Z)\) for every \(C\in\mathcal C(G)\), characterized by the same positive period \(n\) under a natural integral cubical cocycle \(\alpha\). For every \(g\in\operatorname{Aut}(G)\), every \(j\in\{0,1\}\), and every circle component \(C\),
\[
(gJ^j)_*\eta_C=(-1)^j\eta_{(gJ^j)C}.
\]
Consequently, as an integral module for \(\operatorname{Aut}(G)\times C_2\),
\[
H_1(F(G);\mathbb Z)\cong\mathbb Z[\mathcal C(G)]\otimes\varepsilon,
\]
where \(\varepsilon(gJ^j)=(-1)^j\); the group acts on the permutation-module basis by its actual action on components. All integral homology above degree one vanishes, while \(H_0(F(G);\mathbb Z)\) is the ordinary permutation lattice on all connected components. In particular,
\[
\operatorname{tr}(gJ^j\mid H_1(F(G);\mathbb Q))
=(-1)^j\#\{C\in\mathcal C(G):(gJ^j)C=C\}.
\]

**All finite symmetry quotients.** Let \(H\le\operatorname{Aut}(G)\times C_2\). Then
\[
\dim_{\mathbb Q}H_1(|F(G)|/H;\mathbb Q)
=\#\{\mathcal O\in\mathcal C(G)/H:\operatorname{Stab}_H(C)\subseteq\operatorname{Aut}(G)\times\{1\},\quad C\in\mathcal O\}.
\]
The criterion is independent of the representative \(C\) of the orbit. When \(G\) is a tree, \(\mathcal C(G)\) has one element: every graph automorphism acts as \(+1\) on integral first homology, global arrow reversal as \(-1\). Thus the first rational Betti number of the quotient by all graph automorphisms is one, and that of the quotient also identifying reversed orientations is zero.

## Assumptions and scope
An *orientation* assigns one direction to every edge. At a *sink* (all incident arrows point inward) or *source* (all point outward), a flex reverses all incident edges. A one-cell of \(F(G)\) is labeled by the flipped vertex, and cubes encode mutually independent simultaneous flexes. Each one-cell has a unique direction from the orientation where its vertex is a sink to the orientation where it is a source. The connectivity assumption and \(n\ge2\) ensure no isolated graph vertices, avoiding the degenerate ambiguity of a vertex that is both a source and a sink.

The complete nonequivariant description of the components and their core cycles is previously established by Kozlov (2026), Theorems 5.18 and 6.1: every component is collapsible or collapses onto an \(n\)-edge core cycle, and the edges of such a core may be traversed by flexing each vertex exactly once *as a sink*. These published results are used as inputs, not claimed here. The new assertions are the integral time-class normalization, its universal symmetry character, and the quotient-homology criterion for arbitrary connected graphs.

## Proof
**1. The integral time cocycle.** Give each one-cell of \(F(G)\) the orientation from sink to source at its labeled vertex, and define the integral cellular one-cochain \(\alpha\) to have value \(+1\) on every one-cell with this orientation. The two independent flexes defining any square commute. In the four oriented boundary edges of each square, two have positive and two negative signs relative to these sink-to-source orientations. Therefore \(\alpha\) evaluates to zero on the cellular boundary of every square. Since these are all two-cells, \(\delta\alpha=0\). Thus \([\alpha]\in H^1(F(G);\mathbb Z)\) is well-defined. No orientation choice of the edges of the *underlying graph* enters this definition.

**2. Primitive normalized generator of every circular component.** Fix a circular component \(C\). By Kozlov's core-cycle theorem, it deformation retracts through cubical collapses onto an \(n\)-cycle obtained by flexing each graph vertex once in an admissible cyclic order. Traverse this cycle in its published sink-to-source direction. Its oriented cellular cycle \(z_C\) is primitive in \(H_1(C;\mathbb Z)\cong\mathbb Z\), because the collapse identifies the core cycle with a generating topological circle. The evaluation of \(\alpha\) on each of the \(n\) traversed edges equals \(+1\), so \(\langle[\alpha],[z_C]\rangle=n\). Since \(H_1(C;\mathbb Z)\) has rank one, there is a **unique** generator \(\eta_C\) on which \([\alpha]\) evaluates to \(+n\). Any other choice of vertex labeling or core cycle therefore gives this same homology class. Equivalently, \([\alpha]|_C=n\,u_C\) for the canonical primitive integral cohomology generator \(u_C\).

**3. Equivariance and reversal.** A graph automorphism \(g\) takes sinks to sinks and sources to sources. It therefore sends every canonically oriented flex one-cell to another with the same orientation, giving \(g^*[\alpha]=[\alpha]\). Global arrow reversal \(J\) takes sinks to sources and conversely and reverses the canonical orientation of each one-cell, so \(J^*[\alpha]=-[\alpha]\). These maps commute, and they permute connected components while preserving the contractible/circular distinction. For \(C\in\mathcal C(G)\), naturality of the evaluation yields
\[
\langle[\alpha],(gJ^j)_*\eta_C\rangle=(-1)^j n.
\]
The target component has rank-one integral homology with its unique positively normalized generator. Hence \((gJ^j)_*\eta_C=(-1)^j\eta_{(gJ^j)C}\), establishing the module and character formulas. Kozlov's collapse theorem also shows there is no homology above degree one and that \(H_0\) is freely generated by components. No claim is made that the collapses themselves are equivariant.

**4. Quotient homology.** Every finite group action on a finite cubical complex can be made simplicial after a common subdivision. Over \(\mathbb Q\), averaging and the transfer for finite group actions identify the homology of the orbit space with the invariant part of the original rational homology. On the summand spanned by one \(H\)-orbit \(\mathcal O\subseteq\mathcal C(G)\), the signed-permutation representation has a one-dimensional invariant subspace exactly when the sign character \((-1)^j\) is trivial on the stabilizer of any representative; otherwise it has none. Summing over component orbits proves the quotient formula. For a tree, Kozlov's Corollary 6.13 gives exactly one circular component and no other components, yielding the stated specialization.

## Verification
The standard-library program `verify.py` constructs the full orientation graph and the finite cubical cell collection independently from the adjacency lists. It checks the Euler-characteristic identity, each square's time-cocycle cancellation, mod-two first-homology ranks by constructing and reducing all two-cell boundaries, positive sink traversals of an \(n\)-edge core cycle in every detected circular component, and all graph-automorphism and arrow-reversal actions on those periods.

Execute `python3 verify.py` from a directory containing the file. `verification_output.txt` is the recorded output. Across 18 graphs (paths, stars, cycles, complete graphs, a complete bipartite graph, and two nontrivial five-vertex graphs), the run checked 126 connected components, 48 circular components, 256 squares, and 582 graph-automorphism/core combinations. It ended with `VERIFY_OK`. The finite checks corroborate the formula; the proof for arbitrary \(n\) uses the published general core-cycle theorem and the exact cocycle argument, not extrapolation.

## Relationship to prior work
Kozlov's article establishes the cubical model, the circle-versus-contractible homotopy alternatives, the \(n\)-step sink core cycles, and the integral *orientation-cycle signature* on the original graph. That signature concerns connected-component labels; it is distinct from the new canonical time cohomology class on the flex complex itself. The original article does not state the action of graph automorphisms and simultaneous arrow reversal on first homology or the quotient rank formula.

A published published-finding corpus finding, *Equivariant homology and symmetry quotients of complete-graph flex complexes* (2026), proves a stronger **explicit enumeration** for the specialized family \(G=K_n\); it also observes preservation of the sink direction there. This supplies a consistency check and a known special case, but it does not cover general finite connected graphs or arbitrary reversal-containing subgroups. A separate published-finding corpus finding, *A complete cycle-anchor invariant and geodesic formula for graph flexes* (2026), classifies orientation connectivity and shortest flex paths, rather than the integral homology symmetry module or quotient homology. The present theorem neither replaces these sharper results nor asserts a new nonequivariant classification.

## Limitations
The graphs must be finite, simple, connected, and have at least one edge. The quotient statement determines **rational homology**, not the integral homology or homeomorphism type of the quotient. The theorem reduces the equivariant first-homology character to the action on circular components; it does not provide a closed enumeration of component orbits for every graph family. The primitive normalization uses the published, general core-cycle collapse and would not follow from counting homology ranks alone. Bibliographic uniqueness cannot be certified from finite literature searches.

## References
1. D. N. Kozlov, “Flex complexes of graphs,” *Journal of Applied and Computational Topology* **10**, article 10 (first publicly available May 23, 2026), DOI: 10.1007/s41468-026-00235-1. In particular §§2, 5–7, Theorems 5.18 and 6.1 and Corollary 6.13. Lawful open-access full text: https://link.springer.com/content/pdf/10.1007/s41468-026-00235-1.pdf.
2. “Equivariant homology and symmetry quotients of complete-graph flex complexes,” published published-finding corpus record (October 11, 2026), identifier `2026/10/11/SCOPE-equivariant-homology-and-symmetry-quotients-of-complete-graph-fl--d33423646847`, RESULT.md.
3. “A complete cycle-anchor invariant and geodesic formula for graph flexes,” published published-finding corpus record (October 11, 2026), identifier `2026/10/11/SCOPE-a-complete-cycle-anchor-invariant-and-geodesic-formula-for-graph--adc90e8a9935`, RESULT.md.
4. A. Hatcher, *Algebraic Topology*, Cambridge University Press (2002), finite-group transfer and cellular homology background.
