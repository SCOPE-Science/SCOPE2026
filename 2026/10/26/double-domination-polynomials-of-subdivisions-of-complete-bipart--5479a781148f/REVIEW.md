# Review of the double-domination subdivision enumerator

## Correctness

PASS. Each inserted degree-two vertex forces the omitted original vertices to occur on at most one side of the bipartition. The exhaustive three-way partition has exactly determined forced subdivisions and independent nonempty row/column choices. Inclusion-exclusion counts edge covers in the all-original case, and the three classes are disjoint. The coefficient of the least power is reconstructed separately, including the exceptional \(p=q=2\) boundary. A standalone direct closed-neighborhood enumeration agrees for 1,755,392 tested subsets; these finite computations are corroboration, not proof of the unrestricted formula.

## Originality

PASS under best-knowledge comparison, not a claim of priority certification. Behtoei–Zarifian (arXiv:2408.05783, Section 2) address *exact* double domination in subdivisions, a stricter condition than the at-least-two condition enumerated here. Magima–Ragukumar (DOI:10.7546/nntdm.2024.30.3.640-653, Section 2.6, Theorem 2.19) already establish the scalar minimum \(p+2q\) and this review excludes it from novelty. Akbari–Oboudi's edge-cover polynomial is also known. The proposed distinct claim is the complete polynomial, its three-family classification, and the piecewise counts of all minimizers. Relevant search records did not identify an equivalent enumeration, but unindexed or alternate-name literature may exist.

## Value

PASS. The minimum double domination number for a complete bipartite subdivision was already known, but it does not record the exponentially different numbers of minimum solutions on the thin boundary \(p=2\). The full cardinality distribution is a natural invariant: it records all placements of two-fold closed-neighborhood monitors. The structural transfer combines two classical combinatorial mechanisms, edge covers and independently forced rows/columns, yielding a general exact answer for a two-parameter graph family. This is not a claim that the classical edge-cover polynomial or published minimum is novel.

## Limitations and closest literature

The theorem covers only one-step complete-bipartite subdivisions with both part sizes at least two. The closest source discussing subdivision graphs is arXiv:2408.05783; the closest source with identical graph parameters is Magima–Ragukumar's 2024 article, which treats the scalar optimum. The literature comparison cannot exclude nonindexed full-set counts or implicit equivalent formulas hidden in broad publications. The proof and computation have not received independent validation.

Self-review: passed. Independent audit: not yet performed.
