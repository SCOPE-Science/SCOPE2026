# Orientation characters of independence-complex spheres of full rooted trees

## Finding

Let \(b\ge 2\) and \(h\ge 0\) be integers. Let \(T_{b,h}\) be the complete rooted \(b\)-ary tree of height \(h\): vertices are words over \(\{1,\ldots,b\}\) of lengths \(0,\ldots,h\), and each word is joined to its one-letter extensions. Let \(K_{b,h}=\operatorname{Ind}(T_{b,h})\) denote the ordinary independence complex, and let \(G_{b,h}\) be the group of root-preserving tree automorphisms. Write

\[
P_{b,h}=\{v\in V(T_{b,h}):\operatorname{depth}(v)=h-1-3j\ \text{for some integer }j\ge0\}.
\]

**Theorem.** If \(h\equiv0\pmod3\), then \(K_{b,h}\) is contractible. Otherwise \(K_{b,h}\) is homotopy equivalent to exactly one sphere of dimension

\[
d_{b,h}=|P_{b,h}|-1
=\sum_{\substack{j\ge0\\h-1-3j\ge0}}b^{\,h-1-3j}-1,
\]

and its unique nonzero reduced integral homology group carries the following *complete* one-dimensional integral representation of \(G_{b,h}\):

\[
\boxed{\quad
 g_*\bigm|\widetilde H_{d_{b,h}}(K_{b,h};\mathbb Z)
 =\operatorname{sgn}(g|_{P_{b,h}})\in\{+1,-1\}
 \quad(g\in G_{b,h}).\quad}
\]

Here the sign is the ordinary sign of the permutation induced on the *intrinsically defined set* \(P_{b,h}\). It is the trivial character for \(h=1\); for every \(h\ge2\) with \(h\not\equiv0\pmod3\), it is nontrivial. All reduced integral homology in other degrees vanishes. In particular the formula determines the orientation effect of every element of the iterated-wreath-product automorphism group, not merely the Betti numbers.

## Assumptions and scope

Graphs are finite, simple and undirected. An independent set is a subset of vertices containing no adjacent pair. The empty set is included as a face. Homology is reduced *integral* simplicial homology, with its action induced by simplicial vertex permutations. For \(h=0\), the complex is a point; no reduced homology generator is asserted. The rooted automorphism group fixes the empty-word vertex and permutes each level. There is no assumption that an arbitrary non-root-preserving graph automorphism acts on the chosen rooted structure; the result is stated for the canonical rooted symmetry group.

For illustration, \(h=2\) gives \(P_{b,2}\) equal to the \(b\) vertices at depth one; \(\widetilde H_{b-1}(K_{b,2};\mathbb Z)\cong\mathbb Z\), and swapping any two depth-one branches acts as multiplication by \(-1\). The presence of a negative homology action is information absent from the nonequivariant sphere classification.

## Proof

**1. Sphere-or-point reduction and exact evaluation.** For any finite graph \(T\), define its signed independence-set sum

\[
Z(T)=\sum_{I\subseteq V(T)\atop I\text{ independent}}(-1)^{|I|}.
\]

For \(T_{b,k}\), let \(A_k\) be the sum over independent sets omitting the root and \(B_k\) the sum over those containing the root. Directly partitioning the \(b\) branches gives the *exact integer recurrences*

\[
(A_0,B_0)=(1,-1),\qquad
A_{k+1}=(A_k+B_k)^b,\qquad B_{k+1}=-A_k^b,\qquad Z_k=A_k+B_k.
\]

When \(b\) is even, the pair cycles as \((1,-1)\to(0,-1)\to(1,0)\to(1,-1)\). When \(b\) is odd, it cycles as

\[
(1,-1)\to(0,-1)\to(-1,0)\to(-1,1)\to(0,1)\to(1,0)\to(1,-1).
\]

Thus \(Z_k=0\) precisely when \(k\equiv0\pmod3\), and \(Z_k\in\{-1,1\}\) otherwise. The forest theorem of Ehrenborg and Hetyei [1, Corollary 6.1] establishes that an independence complex of a forest is contractible or homotopy equivalent to a *single sphere*. Since \(Z(T)=-\widetilde\chi(\operatorname{Ind}(T))\), this dichotomy and the calculated sums prove that \(K_{b,h}\) is contractible exactly for the claimed congruence class and is otherwise a sphere up to homotopy. No numerical finite search is used in this deduction.

**2. Sphere dimension.** When \(h\not\equiv0\pmod3\), the levels making up \(P_{b,h}\) are separated by three edges. Their closed graph neighborhoods cover the entire tree: the bottom selected level is at depth \(h-1\), and the top selected level is at depth zero or one. Therefore \(P_{b,h}\) is a dominating set, giving \(\gamma(T_{b,h})\le |P_{b,h}|\).

For each \(v\in P_{b,h}\), choose one child \(q(v)\). This is always possible because the greatest depth in \(P_{b,h}\) is \(h-1\). The vertices \(q(v)\) are pairwise at graph distance at least three: different selected levels are separated by three, and distinct parents on the same level yield children separated by at least four. Hence the closed neighborhoods of the \(q(v)\) are pairwise disjoint. Every dominating set meets each of these \(|P_{b,h}|\) neighborhoods, so \(\gamma(T_{b,h})\ge |P_{b,h}|\). Consequently

\[
\gamma(T_{b,h})=|P_{b,h}|.
\]

For a forest whose independence complex is spherical, the sphere dimension is its domination number minus one [2, Section 4.2, discussion immediately before Theorem 4.7, citing the corresponding cross-polytope collapse]. This yields the dimension stated above. The dimension and the nonequivariant sphere-or-point classification are background components, not claims of new priority.

**3. Signed fixed-face trace.** Fix \(g\in G_{b,h}\). Let \(\mathcal O(g)\) be the cycles of \(g\) on the vertex set. A \(g\)-invariant independent set is a union of such cycles. Define

\[
Z_g=\sum_{\substack{\mathcal A\subseteq\mathcal O(g)\\
\cup\mathcal A\text{ independent}}}(-1)^{|\mathcal A|}.
\]

For each \(g\)-invariant face \(I\), the sign of the induced permutation of its vertices is \((-1)^{|I|-c_g(I)}\), where \(c_g(I)\) is its number of \(g\)-cycles. Multiplying by the alternating degree sign on the augmented simplicial chain basis shows that the reduced Lefschetz number is \(-Z_g\); this includes the empty face. In the noncontractible cases the only reduced homology is a single copy of \(\mathbb Z\) in degree \(d_{b,h}\), so

\[
(-1)^{d_{b,h}}\deg(g)=-Z_g,\qquad
(-1)^{d_{b,h}}=-Z_{\mathrm{id}},\qquad
\deg(g)=\frac{Z_g}{Z_{\mathrm{id}}}.
\]

The denominator is \(\pm1\) by Step 1. This identity computes the exact *integral* orientation character, because every automorphism of a rank-one integral homology group acts by \(\pm1\).

**4. Branch-swap generators.** Every automorphism of a complete rooted tree is generated by transpositions of two children at an individual vertex, together with all their descendants. Let \(s\) be such a transposition at depth \(j<h\) and put \(t=h-j\), the height of the affected rooted subtree. The quotient of vertex cycles under \(s\) is a rooted tree with \(b-1\) branches at the swapped vertex and \(b\) at all other nonleaf vertices; there are no edges within individual vertex cycles. Consequently \(Z_s\) is exactly the ordinary signed independent-set sum of this quotient.

At the affected vertex the pair \((A_t,B_t)\) in Step 1 is replaced by

\[
(A'_t,B'_t)=\bigl((A_{t-1}+B_{t-1})^{b-1},-A_{t-1}^{b-1}\bigr).
\]

Inspection of the *proved* two- or six-cycle of pairs in Step 1 gives \((A'_t,B'_t)=\lambda_t(A_t,B_t)\), where

\[
\lambda_t=
\begin{cases}
-1,&b\text{ even and }t\equiv2\pmod3,\\
-1,&b\text{ odd and }t\equiv2,3,4\pmod6,\\
+1,&\text{otherwise}.
\end{cases}
\]

This scalar is retained unchanged on moving up to the full root: if one child contribution \((A,B)\) is replaced by \(\lambda_t(A,B)\), both parent state sums are multiplied by \(\lambda_t\), since they are products of child contributions. Thus \(Z_s=\lambda_t Z_{\mathrm{id}}\) and \(\deg(s)=\lambda_t\).

The same swap permutes two identical descendant blocks of \(P_{b,h}\), each with cardinality

\[
N_{b,h,j}=\sum_{\substack{\ell=h-1-3a>j\\a\ge0}}b^{\,\ell-j-1},
\]

and fixes all remaining selected vertices. Its sign on \(P_{b,h}\) is \((-1)^{N_{b,h,j}}\). If \(b\) is even, this exponent is odd exactly when the selected depth equals \(j+1\), that is, \(t\equiv2\pmod3\). If \(b\) is odd, the exponent's parity is that of the number of selected depths strictly above \(j\), which is odd exactly when \(t\equiv2,3,4\pmod6\). Therefore

\[
\deg(s)=\lambda_t=\operatorname{sgn}(s|_{P_{b,h}})
\]

for every branch-swap generator. Both sides are homomorphisms from \(G_{b,h}\) to \(\{\pm1\}\), so their equality on generators proves equality for all \(g\in G_{b,h}\). For \(h\ge2\) and \(h\not\equiv0\pmod3\), taking \(j=h-2\) gives \(t=2\), hence a generator of degree \(-1\), proving nontriviality. For \(h=1\), \(P_{b,1}\) contains only the root, hence the character is trivial. This proves the theorem.

## Verification

The standalone Python 3 scripts `verify_orientation.py` and `verify_simplices.py` use only the standard library. Execute `python3 verify_orientation.py` and `python3 verify_simplices.py` from the directory containing them. The first checks the exact integer state recurrences and all local branch-swap character formulas for \(2\le b\le10\), \(0\le h\le30\) (2,700 generator cases). The second independently constructs the actual simplicial chain complexes and computes reduced boundary ranks over \(\mathbb F_2\) and signed fixed-face traces for several small rooted trees (17 generator cases). Both completed with all assertions passing.

The finite tests verify implementation and boundary examples; only the general recurrence, forest topology theorem, domination argument and equivariant trace computation prove the infinite-parameter statement. The supplied source code and printed counts make the finite checks reproducible without dependencies.

## Relationship to prior work

Ehrenborg and Hetyei [1] proved the general sphere-or-point dichotomy for forest independence complexes. Marietti and Testa [2] related the sphere dimension to domination number. Deshpande and Singh [3, Theorem 5.6] explicitly classified nonequivariant higher-independence homotopy types for perfect \(m\)-ary trees; setting their independence parameter to one covers sphere dimensions and contractibility for this family. Those conclusions are **not presented here as original**.

The new assertion identifies the full integral one-dimensional automorphism representation in every noncontractible case, including exactly which branch-swaps reverse orientation. None of the inspected pertinent results [1–3] states or implies the permutation-sign formula from its nonequivariant homotopy type alone. Kawamura [4] supplies a different nonequivariant forest homotopy procedure. A homotopy equivalence with a sphere does not canonically specify a group action on that sphere; the signed fixed-face argument supplies the missing data.

## Limitations

Only the rooted automorphism action on the *ordinary* independence complex is classified. No equivariant homotopy equivalence, action on arbitrary rooted trees, higher independence parameter, or classification of orientation representations for forests in general is asserted. The classification of nonequivariant homotopy types is due to the cited authors. The literary comparison does not exclude an equivalent unindexed theorem. The full text of [4] was not available for close inspection; its abstract is limited to detecting nonequivariant homotopy types.

## References

1. R. Ehrenborg and G. Hetyei, "The topology of the independence complex," *European Journal of Combinatorics* **27** (2006), 906–923, DOI: `10.1016/j.ejc.2005.04.010`; available online 28 November 2005; Corollary 6.1. Public author PDF: `https://www.ms.uky.edu/~jrge/Papers/Independence.pdf`.
2. M. Marietti and D. Testa, "A simple uniform approach to complexes arising from forests," arXiv `0705.1461v1` (10 May 2007), especially Section 4.2 and Theorem 4.7. Open preprint: `https://arxiv.org/pdf/0705.1461`.
3. P. Deshpande and A. Singh, "Higher independence complexes of graphs and their homotopy types," arXiv `2001.05448` (initial preprint January 2020; inspected version 2, 1 February 2021), Theorem 5.6. Open preprint: `https://arxiv.org/pdf/2001.05448`.
4. K. Kawamura, "Homotopy types of independence complexes of forests," *Contributions to Discrete Mathematics* **5** (2010), DOI: `10.55016/ojs/cdm.v5i2.62064`. Abstract available at `https://cdm.ucalgary.ca/article/view/62064`.
