# Scientific review

## Correctness: PASS

The central implication is checked algebraically. I-symmetry forces units to commute by applying the idempotent condition to
\[
(v^{-1}u^{-1})uv=1;
\]
the transposed product is simultaneously an idempotent and a unit, hence is 1. Conversely, if R is symmetric and U(R) is abelian, an idempotent product p=abc is central. Symmetry forces q=acb into the corner pRp. In that reversible corner, ABC=p makes A,B,C units; the central-corner embedding U(pRp) -> U(R) then makes them commute, so q=ACB=ABC=p. The same unit substitution applied to the projection 1 proves the necessary unit-group condition for pro-symmetry. No computational evidence is needed for the general proof.

Stress tests agree with the theorem: commutative rings satisfy it; the real quaternion division ring is symmetric but has a nonabelian unit group and is not pro-symmetric; and the noncommutative free algebra F_2<x,y> has trivial unit group and is symmetric, giving a noncommutative pro-symmetric example with the word-reversal involution.

## Originality: PASS, qualified to the best of our knowledge

Alghazzawi--Leroy (2019) already introduced symmetric subsets, so applying that definition to E(R) is not new. Han--Lee--Lee (published online 2022) explicitly study this class under the name I-symmetric rings. Their abstract states the special result that for an abelian semiperfect ring, I-symmetry, an abelian unit group, and commutativity are equivalent. Chen--Wang--Zou (arXiv:2609.20084v1) formulate the same idempotent condition as their Condition 2 and separately introduce pro-symmetry through projections.

The claimed new content is restricted to the unrestricted criterion
\[
R\text{ I-symmetric}\iff R\text{ symmetric and }U(R)\text{ abelian},
\]
and the resulting identification of the 2026 pro-symmetric class with I-symmetric rings, including involution-independence and the stated consequences.

The full body of Han--Lee--Lee, DOI 10.1080/00927872.2022.2102177, was not inspected; only its abstract and bibliographic page were inspected. Because that paper directly studies I-symmetric rings and unit groups, it is the source most likely to overturn part of the originality claim. Its accessible abstract advertises only the abelian-semiperfect equivalence, not the unrestricted criterion. If the full article contains the unrestricted theorem, then the unit-group criterion would be prior art and the novelty would narrow to its connection with the 2026 pro-symmetric notion unless that connection is also independently covered.

Targeted searches for the exact unrestricted criterion, synonymous formulations involving E(R) as a symmetric subset, commuting units, and the pro-symmetric/I-symmetric identification did not locate an earlier statement. The relevant definition and Proposition 3.11 of Alghazzawi--Leroy were inspected in full text, as were the relevant statements of arXiv:2609.20084v1.

## Value: PASS

The result gives a simple structural test for a triple-product idempotent condition and shows that an apparently involution-dependent class is actually an established ring-theoretic class independent of the involution. It also immediately yields clean-ring and division-ring classifications while retaining noncommutative examples outside the clean setting.

Same-model review: passed. Independent audit: not yet performed.
