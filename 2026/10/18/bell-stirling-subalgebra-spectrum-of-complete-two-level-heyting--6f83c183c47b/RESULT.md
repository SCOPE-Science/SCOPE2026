# Bell–Stirling subalgebra spectrum of complete two-level Heyting frames

## Finding

For integers \(a,b\geq1\), let \(P_{a,b}=A\sqcup B\) be the finite poset with \(|A|=a\), \(|B|=b\), all elements within either layer pairwise incomparable, and \(x<y\) for every \(x\in A\) and \(y\in B\). Let \(H_{a,b}=\operatorname{Up}(P_{a,b})\) be its full Heyting algebra of upward-closed sets. A **Heyting subalgebra** contains both constants and is closed under intersection, union, and Heyting implication.

Define \(\mathcal P_{a,b}\) to be the family of set partitions of \(A\sqcup B\) satisfying the following *whole-upper-layer condition*: whenever a block meets both \(A\) and \(B\), that block contains **all** of \(B\). Order these partitions by refinement. Then the entire inclusion-ordered lattice of Heyting subalgebras is anti-isomorphic to \(\mathcal P_{a,b}\). More precisely, the subalgebra associated with \(\pi\in\mathcal P_{a,b}\) consists of those upsets that are unions of blocks of \(\pi\).

Let \(\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}\) be a Stirling number of the second kind, with the usual zero conventions, and let \(B_n=\sum_k\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}\) be a Bell number. The **complete subalgebra-size generating polynomial** is

\[
\sum_{C\leq_{\mathrm H}H_{a,b}} z^{|C|}
=\sum_{i=0}^{a}
\left\{\begin{smallmatrix}a+1\\i+1\end{smallmatrix}\right\}
 z^{2^i+1}
+\sum_{i=1}^{a}\sum_{j=2}^{b}
\left\{\begin{smallmatrix}a\\i\end{smallmatrix}\right\}
\left\{\begin{smallmatrix}b\\j\end{smallmatrix}\right\}
 z^{2^i+2^j-1}.
\]

(The second sum is empty when \(b=1\).) Thus the exact total number of subalgebras is

\[
\boxed{\ B_{a+1}+B_a(B_b-1)\ }.
\]

The subalgebra lattice is graded, with the rank of the subalgebra corresponding to \(\pi\) equal to \(|\pi|-1\), where \(|\pi|\) denotes the number of partition blocks. In particular, when \(b=1\) the entire subalgebra lattice is the dual of the ordinary partition lattice on \(a+1\) elements. The number of maximal proper subalgebras is \(\binom{a+1}{2}\) for \(b=1\), and \(\binom a2+\binom b2\) for \(b\geq2\).

For \(a\geq1\) and \(b\geq2\), the intersection of all maximal proper Heyting subalgebras is exactly the three-element chain \(\{\varnothing,B,A\sqcup B\}\); for \(b=1\) it is \(\{\varnothing,A\sqcup B\}\). This last statement is a specialization of the earlier general theory of maximal Heyting subalgebras, not a separate novelty claim.

## Assumptions and scope

The parameters \(a,b\) are arbitrary positive integers. The order is the complete two-level order, not an arbitrary bipartite incidence relation. All worlds are distinguished (labelled); subalgebras are **distinct subsets of the specified algebra**, not subalgebra isomorphism classes. Algebraic implication is

\[
U\to V=\{x\in P_{a,b}:\uparrow x\cap U\subseteq V\}.
\]

The term \(\leq_{\mathrm H}\) in the polynomial denotes inclusion as Heyting subalgebras. The rank in the theorem is the rank **inside the lattice of subalgebras**, not the number of elements of an individual subalgebra. A partition with \(i\) pure lower blocks and \(j\) upper blocks has a quotient with \(2^i+2^j-1\) upsets when \(i,j\geq1\); a quotient with a single upper block and \(i\) lower blocks has \(2^i+1\) upsets, including \(i=0\).

## Proof

**1. Subalgebras and surjective bounded morphisms.** For a finite poset \(P\), the bounded distributive lattice of upsets carries the displayed implication. Finite Esakia duality gives a one-to-one correspondence between Heyting subalgebras \(C\subseteq\operatorname{Up}(P)\) and surjective bounded (or \(p\)-) morphisms \(f:P\twoheadrightarrow Q\), up to isomorphism of the codomain. Here \(f\) is order-preserving and satisfies

\[
f(\uparrow x)=\uparrow f(x)\quad\text{for every }x\in P.
\]

The subalgebra is the family \(\{f^{-1}(V):V\in\operatorname{Up}(Q)\}\). Surjectivity makes its kernel partition \(\pi_f\) recoverable: two points have the same membership in **every** member of the subalgebra exactly when they have equal \(f\)-images. Therefore distinct kernel partitions yield distinct subalgebras.

**2. Classification of the kernels.** Let \(f:P_{a,b}\twoheadrightarrow Q\) be a bounded morphism. For every \(y\in B\), the upper cone of \(y\) is a singleton. Hence \(\uparrow f(y)=f(\uparrow y)=\{f(y)\}\), so every point of \(f(B)\) is maximal in \(Q\). For every \(x\in A\),

\[
\uparrow f(x)=f(\uparrow x)=\{f(x)\}\cup f(B).
\]

If \(f(x)=f(y)\) for some \(y\in B\), then \(f(x)\) is maximal; the displayed identity forces \(f(B)\) to be a singleton. Thus any kernel block intersecting both levels contains all of \(B\). This proves necessity of the whole-upper-layer condition.

Conversely, consider any partition satisfying that condition. If no block mixes levels, take as quotient \(Q\) the complete two-level poset of its pure lower and pure upper blocks, ordered with every lower block below every upper block. If a mixed block occurs, it contains every upper point; take that block as the unique maximal point of \(Q\) and all remaining pure lower blocks as incomparable points immediately below it. In either case, the quotient map is order-preserving and sends each principal upper cone onto the corresponding principal upper cone; hence it is a surjective bounded morphism. Its kernel is exactly the given partition. The case in which every point lies in one block yields the one-point quotient and the two-element subalgebra.

The explicit inverse-image description proves the claimed anti-isomorphism: refining a partition permits more block-union upsets, so corresponds to enlarging its Heyting subalgebra.

**3. Exact sizes and enumeration.** Split admissible partitions into disjoint cases. If the \(b\) upper points occupy **one** block, collapse \(B\) temporarily to a new symbol \(*\). The remaining data are precisely an arbitrary partition of \(A\sqcup\{*\}\). If \(i\) blocks do not contain \(*\), there are

\[
\left\{\begin{smallmatrix}a+1\\i+1\end{smallmatrix}\right\}
\]

such partitions. Their quotient poset has \(i\) lower points and one upper point, hence \(2^i+1\) upsets. If the upper points occupy \(j\geq2\) blocks, no block can mix levels; the lower points have \(i\geq1\) blocks, yielding

\[
\left\{\begin{smallmatrix}a\\i\end{smallmatrix}\right\}
\left\{\begin{smallmatrix}b\\j\end{smallmatrix}\right\}
\]

choices. Their quotient contains \(i\) lower and \(j\) upper points, so its upsets consist of arbitrary subsets of the upper layer plus the whole upper layer together with a nonempty subset of the lower layer: \(2^j+2^i-1\) in all. Summing the contributions gives the polynomial. Evaluating it at \(z=1\) gives \(B_{a+1}+B_a(B_b-1)\).

**4. Grading and maximal subalgebras.** A permitted partition can always be coarsened to any specified permitted coarsening by successive mergers of exactly two blocks, each intermediate partition still permitted. Indeed, first merge within pure lower and upper blocks of the target; when the target has a mixed block, merge all its upper blocks first and only then merge its lower blocks into that unique upper block. Therefore every cover in the admissible refinement order changes the number of blocks by exactly one. The partition with one block corresponds to the smallest Heyting subalgebra and has rank zero, proving \(\operatorname{rank}(C_{\pi})=|\pi|-1\).

Maximal proper subalgebras correspond to admissible mergers of one pair from the discrete partition. They may merge two lower points or two upper points. Cross-level merging is possible in a single step only when \(b=1\). This gives the stated binomial formulas.

**5. Frattini intersection.** Intersecting subalgebras corresponds to joining their kernel partitions. If \(b=1\), the admissible single-pair mergers generate the indiscrete partition, giving the two-element intersection. If \(b\geq2\), they merge all lower points within \(A\) and all upper points within \(B\), but never mix the layers. The quotient then is a two-point chain, whose inverse-image upsets are exactly \(\varnothing\), \(B\), and \(A\sqcup B\). This is consistent with Adams's general maximal-subalgebra criterion.

## Verification

Run `python3 verify.py` with standard Python 3. The script independently enumerates every subset of \(H_{a,b}\) that contains the constants for each \(1\leq a,b\leq3\), tests closure under both lattice operations and implication, and compares the resulting full set of subalgebras to the independently generated admissible partitions. It checks the exact size histogram, Bell formula, reversed kernel-refinement inclusions, maximal proper subalgebra count, and Frattini intersection.

The completed execution returned:

```text
VERIFY_OK families=9 exhaustive_subalgebras=106 kernel_order_pairs=2142
```

The nine exhaustive cases include the \((3,3)\) frame with a 15-element Heyting algebra, 35 subalgebras, and its complete size spectrum. The universal conclusions for all positive integers \(a,b\) follow from the proof, **not** these finite tests.

## Relationship to prior work

Finite Esakia duality and the relation between implication-preserving subalgebras and surjective bounded morphisms are established background, not claimed as new. Bezhanishvili, Carai, and Morandi (2023), *Heyting frames and Esakia duality*, develops a general category-theoretic version. Grilletti and Quadrellaro (2023), *Esakia Duals of Regular Heyting Algebras*, supplies explicit poset and p-morphism conventions, but concentrates on regular-generation conditions and their logical applications.

Adams (1986), *Maximal subalgebras of Heyting algebras*, gives a general separating-set characterization of **maximal** proper Heyting subalgebras. Its criterion covers the maximal-subalgebra specialization above; we do not claim that specialization in isolation as new. The asserted contribution here is the *all-subalgebra* kernel-partition classification, its complete two-parameter Stirling size spectrum, and the resulting Bell total and grading for complete two-level frames. These are not supplied as formulas or an equivalent two-layer partition model by the inspected general-duality or maximal-subalgebra results.

## Limitations

The theorem assumes complete comparability between the two layers and does not cover arbitrary height-two partial orders. It counts labelled embedded subalgebras, not quotient isomorphism classes or subalgebras of arbitrary finite distributive lattices. No claim is made about effective recognition for arbitrary frames, or a general answer to finite Heyting subalgebra enumeration. Some older subalgebra monographs and unindexed literature may contain an equivalent formula or a stronger specialized result; independent publication-priority audit remains outstanding. The checker only exhausts the specified small cases.

## References

1. G. Bezhanishvili, L. Carai, P. J. Morandi, *Heyting frames and Esakia duality*, arXiv:2302.07913v1 (first posted 2023-02-15), https://arxiv.org/abs/2302.07913.
2. G. Grilletti, D. E. Quadrellaro, *Esakia Duals of Regular Heyting Algebras*, arXiv:2303.11246v1 (first posted 2023-03-20), https://arxiv.org/abs/2303.11246.
3. M. E. Adams, *Maximal subalgebras of Heyting algebras*, Proceedings of the Edinburgh Mathematical Society 29 (1986), 359–365, doi:10.1017/S0013091500017806.
