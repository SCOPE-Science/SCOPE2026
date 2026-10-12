# Self-review

## Correctness
PASS. The proof writes the exact distance multiset for every omitted vertex in terms of the two omission index sets. There are only two possible types on each shore, forcing at most two omissions per shore; the equal-shore cases are then eliminated by an explicit cross-shore collision. The surviving five omission patterns are both necessary and sufficient. Their counts give the claimed minimum and the complete size enumerator. A direct graph-distance verifier checks every subset for \(3\le n\le8\).

## Originality
PASS. Searches covered crown, matching-deleted-biclique, bipartite-Kneser, bipartite-complement, basis-count, and size-enumerator formulations. The closest same-invariant published result is the complete-multipartite classification, which does not apply because \(\operatorname{Cr}_n\) is not complete multipartite for \(n\ge3\). The regular diameter-two theorem gives the undeleted \(K_{n,n}\) baseline but not the diameter-three crown value. The principal residual risk is an older equivalent result indexed under a different name for crown graphs.

## Value
PASS. Crown graphs are the canonical one-factor deletion of balanced bicliques. The theorem gives the exact invariant, every resolving set, every basis, and a sharp perturbation comparison with \(K_{n,n}\). The missing \(2n-2\) cardinality also exposes a nonmonotone feature of outer multiset resolving sets that is invisible from the minimum value alone.

## Closest literature and limitations
Peng, arXiv:2609.20073v1, is the recent same-invariant literature lead and has primary MSC \(05C12\). Klavžar--Kuziak--Yero, arXiv:2207.06834v1, gives the regular diameter-two extremal theorem and complete multipartite examples. The latter was inspected in full text; it contains no crown or matching-deletion theorem. The recent toroidal-grid full text was inaccessible during this review, so only its public metadata and abstract were used for scope, date, and MSC. The finite computation is supportive, not the infinite proof.

Self-review: passed. Independent audit: not yet performed.
