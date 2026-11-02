# Scientific review: exact two-tortoise Thue–Morse complexity

## Correctness (C): PASS

The theorem has quantified scope \(n\ge18\). For every pair of distinct factors with identical two-tortoise images, the length-18 prefix map injects its fibre into one of four **exhaustively certified** size-two fibres. Their two explicit prefix patterns are preserved by all later extensions, because removing the first two ones leaves the same suffix. Every remaining possible new pair has the form \(\{0110y,1001y\}\). The proved lifting lemma uses automatic-word parity synchronization twice: all sufficiently long left-special factors begin at even substitution boundaries and desubstitute to shorter left-special factors; resubstitution produces both required length-four left contexts. Thus the new classes are in bijection with left-special factors two lengths shorter than the first-pass ones. The existing exact first-pass theorem gives \(D_2(n)=D_1(n)+D_1(n-2)\) and the digit formula, without relying on finite extrapolation.

The self-contained verifier builds all length-18 factors from four adjacent substituted block pairs; it checks exactly the four enumerated pairs, forbidden alternating length-five factors and sharp failure at length 17. As a separate robustness check it exhaustively checks the statement for every length from 18 through 512. The symbolic proof explicitly handles the infinite range. Residual risk: the parity/desubstitution proof should receive independent mathematical scrutiny, particularly its odd-length alignment and the fibre-prefix injection.

## Originality (O): PASS under accessible-priority review

The directly relevant Campbell–Rampersad primary source was read in full in its accessible HTML preprint version, including all of Sections 3, 4, 6 and the final remarks. Its Theorems 4–6 calculate only the **one-pass** Thue–Morse quotient; the end of Section 6 explicitly invites similar higher-iterate relations without supplying this two-pass formula, complete four-pair classification or length-18 sharpness. The Defant–Kravitz source defines tortoise sorting of general words but does not state this infinite automatic-word factor count in the accessible material. The closest accessible existing mathematical record proves the maximum two-pass fibre multiplicity equals two; that upper bound does not determine the number of such fibres and therefore does not imply the present \(4,6,8\) deficit law. Searches for aliases, second iterates, special factors and the explicit two-term identity found no stronger covering result.

Priority limitations: semantic and searchable records are not complete bibliographic exhaustions. The complete 2018 original was not available as machine-readable full text in this check; the 2026 relevant primary preprint was available and inspected materially. A rephrasing in older substitution-dynamical literature is a residual priority risk.

## Value (V): PASS

The April 2026 primary source isolates fixed-iterate tortoise complexity as a natural new refinement of abelian complexity, proves the first iterate and explicitly encourages higher-iterate analysis. The theorem settles the first nontrivial **second** iterate for an infinite, canonical automatic word; the identity makes its class deficit an exact shifted convolution of the previously known first-pass deficit. The four-pair boundary, the symbolic left-special lifting mechanism, and the sharp failure at length 17 are meaningful structural information rather than arbitrary finite experimentation. The result does not merely re-state a known fibre maximum.

## Closest sources and limitations

1. Campbell–Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811v1/v2, Sections 3, 4 and 6, especially Theorems 4–6 and the sentence encouraging higher-iterate study.
2. Defant–Kravitz, *Stack-sorting for words*, arXiv:1809.09158, operator definition and general-word setting.
3. de Luca–Varricchio, *Some combinatorial properties of the Thue-Morse sequence and a problem in semigroups* (1989), predecessor left-special enumeration used by the 2026 source.

The theorem is not extended to arbitrary words or three tortoise passes. Independent formal review and definitive priority determination remain outstanding.

Self-review: passed. Independent audit: not yet performed.
