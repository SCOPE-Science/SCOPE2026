# Scientific review: even-order trees and normalized-Laplacian transfer

## Correctness

PASS. The domain comprises all finite simple unweighted trees with even order at least four. The generalized characteristic polynomial is integral; its first nonzero coefficient is determined independently of the graph shape by Kirchhoff cofactors. For even order, the coefficient has exactly one factor of two. Rational-root divisibility plus bipartite spectral reflection excludes every interior rational eigenvalue whose reduced numerator is even. The transfer analysis then separates opposite and equal bipartition classes. Opposite-class transfer forces such a forbidden rational phase; equal-class transfer forces a unique negative eigenvalue at one, sibling leaves, and an additional positively signed forbidden rational phase. The argument covers repeated eigenvalues through projectors, not individual eigenvectors. The \(P_2\) exception and all quantifiers are explicit. The standard-library checker passes 34 independently constructed finite examples, without being used as an infinite proof.

## Originality

PASS, with the limited literature-access risk below. The primary 2022 article explicitly leaves the general normalized-Laplacian tree exclusion open and proves only necessary conditions. The earlier 2014 normalized-Laplacian path theorem is restricted to paths; the 2014/2015 matching-polynomial paper supplies a spectral formula but not the resulting transfer prohibition. The new statement covers all even-order trees, including branched, asymmetric, arbitrary-depth examples, and uses the two-adic invariant absent from the inspected transfer results. Existing mathematical claims on particular tree families are special cases, not equivalent universal coverage; previously studied depth-two trees also include odd-order examples and therefore are incomparable in their complete domains. Searching exact phrasings, aliases, spectral parity, transfer-phase and cofactor formulations identified no stronger covering theorem. This is evidence of noncoverage in checked sources, not proof that an unlocated work cannot exist.

## Value

PASS. The original source conjectures no normalized-Laplacian perfect state transfer on trees except the paths on two and three vertices. The theorem resolves the complete even-order half of this problem, not an arbitrary finite slice, and isolates a reusable parity obstruction connected to the number of spanning trees. Its proof avoids spectral enumeration, regularity, symmetry or bounded-degree assumptions. Both the exact theorem and its mechanism are motivated by the published gap.

## Sources and remaining risks

Coutinho--Baptista, arXiv:2209.04668v1, Sections 3--5 and closing conjecture; Alvir et al., arXiv:1409.5840, normalized-Laplacian paths and products; Banerjee--Mehatari, arXiv:1406.7769, Theorem 2.1 and tree characteristic-polynomial treatment. A closely related 2022 dissertation by Baptista was identified and snippets of its tree chapter and conclusion were inspected, but its full PDF could not be obtained during this review. The excerpts describe necessary conditions and an unfinished global tree question; remaining uninspected pages are a residual overlap risk. Independent audit has not been performed; possible unlocated stronger transfer or normalized-Laplacian spectral-divisibility results remain risks.

Self-review: passed. Independent audit: not yet performed.
