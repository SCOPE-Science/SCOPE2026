# Scientific review of optimal outer-independent two-rainbow labelings of star coronas

## Correctness — PASS

Every original vertex and its private leaves form a disjoint block. The rainbow condition at an empty private leaf rules out singleton-labeled centers unless all leaves are positive; outer-independence forces all private leaves positive at an empty center. These cases yield a sharp lower bound of two per block. Equality gives the complete two-state classification when there are exactly two leaves, and a unique state when there are three or more leaves. Independence of empty centers and the precise four-versus-two choices of ordered leaf singleton colors imply \((1+2t)^i I_{G^\circ}(4t)\). The counting-hardness proof reduces bipartite independent-set counting by polynomial interpolation through independent clone blow-ups. The included direct-definition brute-force tests agree in 30 small cases, with three additional clone identities. Finite tests corroborate the proof but do not extend its quantifiers.

## Originality — PASS, with residual priority risk

The scalar corona minimum is known: Samadi–Soltankhah, arXiv:2208.02340, Theorem 3.4, obtains \(2|V(G)|\) for the two-isolated-leaf corona when the base has no isolated vertices. Cabrera-Martínez, Mathematics 10 (2022), 2287, treats scalar parameters of coronas whose second factor has no isolated vertices; it cannot be applied directly to the two-isolated-leaf factor. Neither inspected source presents the polynomial enumerating **all** minimum labelings or the phase transition to uniqueness beyond two leaves. The source comparison distinguished independent rainbow domination (positive-support independence) from **outer-independent** rainbow domination (empty-support independence), and ordinary two-rainbow enumerations from the present objects. Published mathematical record searches, relevant prior claims, and available local claim histories did not show this enumeration. Exact priority is not certified: an older open-access publisher page was rate-limited and unindexed results may exist.

## Mathematical value — PASS

The theorem converts the optimizer distribution of a natural, arbitrarily structured corona family into the full independence polynomial, rather than adding a scalar to the already known minimum. The data therefore retain all independent-set cardinality counts of the base graph. At the exact two-versus-three private-leaf boundary the number of optimum labelings changes from a potentially \(\#\mathrm P\)-hard hard-core partition function to exactly one. The resulting proof that counting optima is \(\#\mathrm P\)-complete on bipartite two-leaf coronas exhibits a nontrivial gap between a trivial minimum weight and computationally hard optimizer multiplicity. This is motivated by the precise corona-product gap in the published scalar theory, not an arbitrary finite slice.

## Scope, prior results, and remaining risks

The foundational definitions date to Kang and collaborators (2019). The 2022 preprint establishes the original scalar minimum for relevant coronas; the 1983 Provan–Ball theorem supplies the established counting-hardness premise. Full access to the later arXiv preprint allowed inspection of its statements and proofs, whereas the Cabrera-Martínez publisher page was not fully retrievable. The reduction establishes only polynomial-time Turing hardness, and no all-function enumeration or \(k=1\) theorem is supplied. Other unindexed work may contain a similar equality-case enumeration.

Self-review: passed. Independent audit: not yet performed.
