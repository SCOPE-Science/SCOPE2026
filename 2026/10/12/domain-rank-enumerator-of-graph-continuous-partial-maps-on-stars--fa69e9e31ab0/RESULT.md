# Domain-rank enumerator of graph-continuous partial maps on stars

## Finding
For every integer \(n\ge 1\), let \(K_{1,n}\) have center \(0\) and leaves \(1,\ldots,n\). Let \(M(K_{1,n})\) be the monoid of all partial functions on its vertices whose inverse image of each face (vertex or edge) is again a face or the empty set. Write
\[
F_n(u,v)=\sum_{f\in M(K_{1,n})}u^{|\operatorname{dom}f|}v^{|\operatorname{im}f|}.
\]
Define the partial-injection polynomials
\[
P_n(u,v)=\sum_{k=0}^{n}\binom nk^2 k!(uv)^k,\qquad
Q_n(u,v)=\sum_{k=0}^{n-1}\binom nk\binom{n-1}k k!(uv)^k.
\]
Then the **complete bivariate domain-rank distribution** is
\[
\boxed{F_n=(1+uv)P_n+nuvQ_n+n^2u^2vP_{n-1}+nuv+n^2u^2v^2+nu^2v.}
\]
In particular, substituting \(u=v=1\) gives
\[
\boxed{|M(K_{1,n})|=2P_n(1,1)+nQ_n(1,1)+n^2P_{n-1}(1,1)+n(n+2).}
\]
The orders for \(n=1,2,3,4,5\) are respectively \(9,36,185,1278,10857\). These are exact consequences of the formula, not a conjectured sequence.

## Assumptions and scope
A partial function \(f:V\rightharpoonup V\) is an ordinary single-valued function defined on a subset \(\operatorname{dom}f\subseteq V\); its rank is \(|\operatorname{im}f|\). For the star, its nonempty faces are the singleton vertices and the pairs \(\{0,i\}\), \(1\le i\le n\). A partial function is called *continuous* here **by inverse image of faces**, not by the graph-homomorphism condition of preserving edges in the forward direction. The empty inverse image is allowed. In particular, the empty map is counted once. The two indeterminates \(u,v\) are formal and commute. The result holds for every positive integer \(n\), with no finite-size cutoff; there are no field hypotheses.

## Proof
We give a disjoint exhaustive classification, refined by domain size and image size. The central observation is that if the images include two adjacent target vertices, then their entire joint inverse image must be a vertex or a source edge; in a star every source edge contains the source center. Similarly, a nonempty inverse image of a target vertex is a singleton or a source edge. All descriptions below also satisfy this condition, so the restrictions are sufficient.

**Case I: the target center \(0\) is not in \(\operatorname{im}f\).** Thus all outputs are target leaves, which are pairwise nonadjacent. Each nonempty fiber is a singleton or one source edge. Since two source edges intersect at the source center, at most one output has a two-point fiber.

(Ia) If the source center is outside the domain, the map is an arbitrary partial injection between the \(n\) source leaves and the \(n\) target leaves. For rank \(k\), the choices are \(\binom nk^2 k!\), and this contributes \(P_n\).

(Ib) If the source center is in the domain but its output fiber is a singleton, choose that output leaf in \(n\) ways. The remaining \(n\) source leaves can be partially injected into the remaining \(n-1\) target leaves. This contributes \(nuvQ_n\).

(Ic) If the source center belongs to a two-point output fiber, its partner is one of the \(n\) source leaves and their common output is one of the \(n\) target leaves. The remaining \(n-1\) source leaves can be partially injected to the remaining \(n-1\) target leaves. The contribution is \(n^2u^2vP_{n-1}\).

**Case II: the target center \(0\) is in \(\operatorname{im}f\).** The inverse image of the target center is either a singleton or a source edge.

(IIa) If the target center has singleton preimage equal to the source center, any additional outputs must be different target leaves with pairwise distinct source-leaf preimages; conversely every such partial injection works, since the inverse image of each occupied target edge is a source edge. This contributes \(uvP_n\).

(IIb) If the target center has singleton preimage equal to a source leaf \(j\), any other output would have to be a target leaf and its nonempty inverse image would have to be the unique source vertex adjacent to \(j\), namely the source center. Thus either the target center is the sole output, in \(n\) ways with weight \(uv\), or the source center maps to one chosen target leaf, in \(n^2\) ways with weight \(u^2v^2\). The combined contribution is \(nuv+n^2u^2v^2\).

(IIc) If the target center has two-point preimage, that preimage must be \(\{0,j\}\), where \(j\) is a source leaf. Any additional output would make the inverse image of the target edge containing that output and the target center have at least three vertices, so there are no additional outputs. The contribution is \(nu^2v\).

These six alternatives partition the maps by target-center membership and by the source-center fiber. They are all continuous and distinct. Adding their generating polynomials proves the displayed identity. Substitution at \(u=v=1\) proves the order formula: the three last small terms sum to \(n^2+2n=n(n+2)\). \(\square\)

## Verification
The supplied standalone Python 3 script `verify.py` calculates all coefficients of the proposed generating polynomial by binomial and factorial arithmetic. Independently, for every \(1\le n\le5\), it loops through all \((n+2)^{n+1}\) possible partial functions (including an undefined output), directly checks inverse images of **every** target singleton and edge, and accumulates domain-rank pairs. It compares the two coefficient dictionaries exactly and prints `EXHAUSTIVE_STAR_CASES=5 VERIFY_OK` on success. The exhaustive small cases support but do not replace the preceding proof for arbitrary \(n\).

## Relationship to prior work
Margolis and Rhodes introduced graph-continuous partial transformation monoids and described their general fiber, singular, and injective structure in *Degree 2 Transformation Semigroups as Continuous Maps on Graphs: Foundations and Structure* (arXiv:2005.02606, especially Section 2 and Lemmas 2.5–2.6). Their worked examples include empty and complete graphs and strict transformations of complete bipartite graphs; these general principles are compatible with, but do not state, the closed bivariate star enumerator above. Their later *The Margolis-Rhodes Monoid of a Graph* (arXiv:2609.39370v1, first available September 30, 2026) explicitly advertises enumeration for paths and cycles. The present theorem addresses the complementary branching-tree class of stars (with genuinely nonpath stars beginning at \(n=3\)) and counts *both* domain size and image rank simultaneously, rather than merely enumerating a monoid's elements. It is an exact specialization of the inverse-face-continuity notion, not a claim of a new definition or general structural theorem for all graphs.

## Limitations
This is a theorem solely for star graphs, not arbitrary trees or all graphs. It counts elements by domain size and image rank, but does not classify Green's relations, ideals, complexity, or conjugacy classes. The relevant sections of the earlier foundational paper are publicly accessible and were inspected. The complete text of the September 2026 preprint could not be inspected from available public access routes; its accessible abstract mentions paths and cycles but cannot establish that it contains no unpublished star discussion. Thus historical novelty beyond the inspected source passages is not independently established. The finite computations cannot prove the all-\(n\) statement without the argument above.

## References
1. Stuart W. Margolis and John Rhodes, *Degree 2 Transformation Semigroups as Continuous Maps on Graphs: Foundations and Structure*, arXiv:2005.02606 (first posted May 6, 2020), International Journal of Algebra and Computation 31 (2021), 1065–1091. Author-uploaded full-text version: https://www.researchgate.net/publication/341176939_Degree_2_Transformation_Semigroups_as_Continuous_Maps_on_Graphs_Foundations_and_Structure
2. Stuart Margolis and John Rhodes, *The Margolis-Rhodes Monoid of a Graph*, arXiv:2609.39370v1 (first posted September 30, 2026). Abstract: https://arxiv.org/abs/2609.39370
3. Stuart Margolis and John Rhodes, *Degree 2 Transformation Semigroups as Continuous Maps on Graphs: Complexity and Examples*, preprint posted November 2020; International Journal of Algebra and Computation 33 (2023), 289–316. Author-uploaded full-text version: https://www.researchgate.net/publication/345720424_Degree_2_Transformation_Semigroups_as_Continuous_Maps_on_Graphs_Complexity_and_Examples
