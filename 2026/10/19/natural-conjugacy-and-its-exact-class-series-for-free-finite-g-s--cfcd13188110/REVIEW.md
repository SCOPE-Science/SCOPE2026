# Scientific review: natural conjugacy on free finite \(G\)-sets

## Correctness — PASS

The claim specifies finite groups (including nonabelian groups), positive orbit count, four defining natural-conjugacy equations, image restriction, group-valued gauges, and ordinary formal generating functions. The proof reduces the four semigroup equations to equivariant conjugacy on images in both directions, using freeness to extend the required witnesses. On the image, the gauge equations imply and are implied by equality of conjugacy classes of ordered cycle products; tree labels are removable recursively. The exact realization constraint is \(r+s\le m\), where \(s\) counts indegree-zero vertices of the restricted map, not of the original full map. The weighted rooted-tree recursion and classical directed-cycle/multiset transforms yield the claimed product and cumulative divisor \(1/(1-z)\). The argument holds uniformly for all finite \(G\) and \(m\ge1\).

Checks against the four original defining equations enumerate every pair of \(144\) endomorphisms for nonabelian \(S_3\) on two free orbits, compare the relation with image conjugacy, and recover twelve classes. Independent unlabeled-map calculations for trivial \(G\) and up to five free orbits reproduce the initial coefficients. These finite checks support, but do not replace, the infinite proof. Reproduction uses only the standard Python library.

## Originality — PASS with residual risks

Araújo–Bentz–Kinyon–Konieczny–Malheiro–Mercier, arXiv:2301.04252, Section 4.4, Theorem 4.29, assumes \(G\) abelian, while Problem 7.4 explicitly asks for a nonabelian extension. Its full transformation-monoid case covers the trivial-\(G\) specialization of the *classification* but not this combined nonabelian free-orbit theorem and source-weighted exact class-count series. The image-restriction reduction is elementary in the free-action setting and is not presented as a universal new semigroup lemma. Completed targeted mathematical-result searches on nonabelian group actions, conjugacy of transformation wreath products, image functional digraphs, and cycle-product gauges produced no equivalent or stronger nonabelian enumeration. A published wreath-product relative-rank theorem concerns a distinct numerical invariant and has no implication to natural-conjugacy classes on the available evidence. Classical species formulas provide the counting mechanism, not an already-established class-number theorem.

Risks remain from potentially unindexed literature, material read only at abstract level for some less-direct sources, and formulations under different notions of semigroup conjugacy. These risks do not constitute a decisive contrary implication in the checked primary source, which expressly leaves the nonabelian extension open.

## Value — PASS

This is a concrete complete free-orbit solution to a published nonabelian-extension problem, not a formal renaming of an abelian theorem. It supplies a classification for arbitrary finite groups and a computable exact natural-conjugacy invariant in every rank, with an unexpected independence from all group structure beyond its class number. The source-marking construction also explains exactly why an image digraph on \(r\) vertices requires an ambient free action with at least \(r+s\) orbits. It gives a useful structural bridge between transformation wreath monoids and cycle-index enumeration; the nonfree extension remains genuinely open.

## Limits and closest literature

The result does not classify nonfree finite \(G\)-sets or other conjugacy relations. The proof relies on the freeness of source orbits to extend equivariant witnesses. Relevant primary references are arXiv:2301.04252 (full relevant sections examined), arXiv:1810.03208 (inverse-semigroup scope distinguished), and classical cycle-index literature. Possible parallel results expressed as group-decorated functional digraph species remain a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
