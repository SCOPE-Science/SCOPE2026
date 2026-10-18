# Branch-use polynomial for surjective p-morphisms of three-level rooted trees

## Finding

**Theorem (labeled branch-use enumeration).** Let \(r,k\ge1\), and let \(\mathbf{s}=(s_1,\ldots,s_r)\) and \(\mathbf{t}=(t_1,\ldots,t_k)\) be vectors of positive integers. Write \(T(\mathbf{s})\) for the rooted three-level poset with minimum \(o\), incomparable middle vertices \(c_1,\ldots,c_r\), and exactly \(s_i\) incomparable maximal successors of \(c_i\), with no additional comparisons except their transitive consequences. Define \(T(\mathbf{t})\) analogously, using minimum \(o'\), middle vertices \(d_1,\ldots,d_k\), and \(t_j\) maximal successors of \(d_j\). All vertices are individually distinguished, and maps are counted as functions on these labeled vertex sets.

Set \(L=\sum_{j=1}^{k}t_j\) and
\[
 A_{ij}=\sum_{a=0}^{t_j}(-1)^{t_j-a}\binom{t_j}{a}a^{s_i}
 =t_j!\,\left\{\begin{matrix}s_i\\t_j\end{matrix}\right\},
\]
where the braces denote a Stirling number of the second kind. Define the branch-use polynomial
\[
 P_{\mathbf{s},\mathbf{t}}(u,z_1,\ldots,z_k)
 =\prod_{i=1}^{r}\left(Lu+\sum_{j=1}^{k}A_{ij}z_j\right).
\]
For all integers \(c\ge0\) and \(d_1,\ldots,d_k\ge1\) with \(c+\sum_j d_j=r\), the coefficient
\[
 [u^c z_1^{d_1}\cdots z_k^{d_k}]P_{\mathbf{s},\mathbf{t}}
\]
is exactly the number of surjective bounded morphisms \(f:T(\mathbf{s})\to T(\mathbf{t})\) with exactly \(c\) source middle vertices mapped to target maximal vertices and exactly \(d_j\) source middle vertices mapped to \(d_j\). Equivalently, the total count is
\[
 N(\mathbf{s},\mathbf{t})=
 \sum_{J\subseteq\{1,\ldots,k\}}(-1)^{k-|J|}
 \prod_{i=1}^{r}\left(L+\sum_{j\in J}A_{ij}\right).
\]
In particular, the formula applies to arbitrary positive, unequal branch sizes on both sides. Coefficients with any \(d_j=0\) are **not** asserted to count surjective bounded morphisms: they enumerate local branch assignments missing a target middle vertex.

## Assumptions and scope

Here a bounded morphism (also called a \(p\)-morphism) between posets is an order-preserving function \(f\) satisfying \(f(\uparrow x)=\uparrow f(x)\) for every source vertex \(x\), with \(\uparrow x=\{y:y\ge x\}\). Surjectivity is onto **all** target vertices. The theorem treats finite, rooted, three-level posets whose cover relations form a tree and whose nonleaf vertices, apart from the root, are precisely the branch centers. Every branch has at least one terminal successor. It does not address trees of other depths, arbitrary posets, maps carrying valuations, or isomorphism classes of maps.

The rank-three convention counts the root, the middle layer and the leaf layer. The variables \(u,z_j\) are formal indeterminates, and the cardinalities are ordinary integers.

## Proof

**Root and leaf images.** Surjectivity forces \(f(o)=o'\): the target root is attained somewhere, and order preservation makes \(f(o)\) a point below it. For every maximal source leaf \(x\), the equality \(f(\uparrow x)=\uparrow f(x)\) implies that \(f(x)\) is a maximal target leaf.

**One source branch.** Fix the source middle vertex \(c_i\). Its image cannot be the target root: the bounded-morphism back condition at \(c_i\) would then require some point in \(\uparrow c_i\) to map to each target middle vertex, whereas \(c_i\) would map to the root and all its proper successors, being leaves, must map to maximal target vertices. Thus \(f(c_i)\) is either a target leaf or a target middle vertex.

If \(f(c_i)\) is one of the \(L\) target leaves, all \(s_i\) source leaves above it must map to that same target leaf, giving exactly \(L\) possibilities for this branch. If \(f(c_i)=d_j\), its leaves must map into the \(t_j\) target leaves above \(d_j\). The back condition at \(c_i\) holds precisely when every one of those target leaves is attained. Inclusion–exclusion therefore gives exactly \(A_{ij}\) possibilities. No other branch configuration satisfies the local back conditions.

**Independence and global back condition.** Distinct source branches have no comparisons with one another except via the common root. Once a local configuration is selected for each source branch, all nonroot bounded-morphism and monotonicity requirements hold automatically. At the root the back condition is precisely global surjectivity. The target root is already attained, and the target leaves above any attained target middle vertex are all attained by its source preimages. Hence surjectivity is equivalent to requiring at least one source branch to map its middle vertex to every \(d_j\). The independent factors \(Lu+\sum_j A_{ij}z_j\) consequently yield the stated coefficient formula, provided every \(d_j\ge1\). Inclusion–exclusion over the set of missing target middle vertices yields the displayed formula for \(N(\mathbf{s},\mathbf{t})\). This proves both identities for all indicated integer vectors.

As a check, a surjective bounded morphism exists exactly when the source branch sizes can be matched injectively onto the target branch sizes with each matched source size at least the corresponding target size; after sorting both profiles in nonincreasing order, this amounts to \(r\ge k\) and \(s_{(j)}\ge t_{(j)}\) for every \(1\le j\le k\). This **existence** consequence is elementary and covered by stronger published existence algorithms; the new claim is the labeled numerical and coefficient enumeration, not the Boolean criterion.

## Verification

The accompanying standalone `verify.py` uses standard Python only. Run `python3 verify.py`. Its exhaustive mode explicitly enumerates every function with the source root fixed and checks the full equation \(f(\uparrow x)=\uparrow f(x)\) for every source point. It agrees with the formula on all \(50\) tested small source–target profile pairs (maximum source size \(7\) vertices, maximum target size \(6\) vertices), including \(16\) zero-count cases. A distinct subset-of-used-branches dynamic program agrees with the closed formula and the matching feasibility test on another \(13{,}260\) finite parameter pairs, of which \(10{,}521\) have positive counts.

For example, \(N((2,3,2),(2,2))=368\) and \(N((1,2),(2,2))=0\). The proof, not the finite enumeration, establishes the result for arbitrarily many branches and arbitrarily large positive branch sizes.

## Relationship to prior work

De Jongh and Yang (2011, Definition 1.1 and Section 3) establish the role of surjective bounded morphisms for finite rooted intuitionistic Kripke frames and Jankov's theorem. Rzążewski and Stronkowski (2025 preprint, Section 5, Theorem 5.1 and Lemma 5.4) give a polynomial-time **existence** algorithm for a surjective bounded morphism from any finite rooted tree poset onto a poset, using successor matching; its existence coverage includes the present trees. Neither of these full texts supplies the claimed all-profile count or branch-use polynomial. Benjamins, Bezhanishvili and Moraschini (2026 manuscript, Section 2.3, Proposition 3) recall the general characterization of kernels of surjective bounded morphisms by suitable equivalence partitions; this does not state the explicit parameterized fiber counts.

The present result quantitatively refines the existence question: it distinguishes, for example, maps that collapse many source middle vertices to target leaves from maps covering each target middle vertex with several source branches. Its labeled count also measures distinct embeddings of the dual finite Heyting-algebra objects under finite Esakia duality. This is a mathematical motivation, not a separate claimed structural theorem.

## Limitations

The answer is for labeled vertices and the exact three-level tree family. The formula does not provide an efficient method for general rooted trees, nor does it imply any new decidability boundary. Matching feasibility and the underlying definition of bounded morphism are established prior results. No exhaustive search of all published and unpublished descriptions of this exact enumerator is possible; an equivalent unindexed formula remains a bibliographic risk. Independent mathematical review has not been performed.

## References

1. D. de Jongh and F. Yang, *Jankov's Theorems for Intermediate Logics in the Setting of Universal Models*, in *Logic, Language, and Computation*, pp. 53–76 (2011). DOI: 10.1007/978-3-642-22303-7_5. Public author manuscript: https://staff.fnwi.uva.nl/d.h.j.dejongh/Jankov040310.pdf.
2. P. Rzążewski and M. Stronkowski, *Tabular intermediate logics comparison*, arXiv:2509.06841 (first posted 2025-09-08), Section 5. https://arxiv.org/pdf/2509.06841.
3. T. Benjamins, N. Bezhanishvili and T. Moraschini, *Local Finiteness and Colorings for Varieties of Heyting Algebras of Bounded Width*, manuscript dated 2026-01-05, Section 2.3. https://staff.fnwi.uva.nl/n.bezhanishvili/Papers/Kuznetsov-Volume.pdf.
