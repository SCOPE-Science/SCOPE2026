# Independent audit — 2026/09/09/033

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS

For all 406 stored posets ((n=0,ldots,6), counts 1,1,2,5,16,63,318), I independently generated order ideals of every induced subset and counted weak maps into (m+1) colors for every (0le mle n) by assigning the lowest color to an ideal. Every computed Ehrhart value agrees with the table. I independently counted linear extensions by removing a minimal element, and obtained the stored (e(P)) for all 406. Binomial-basis inversion of the values reproduced all stored (h^*)-vectors. The recorded poset counts match the published small-poset census. The volume identity (n![m^n]i(O(P),m)=e(P)), Ehrhart/order-polynomial relation and reciprocity are established general theorems. The maximum (e(P)=n!) occurs uniquely at an antichain for elementary reasons: every permutation is a linear extension exactly when there are no comparabilities.

## Originality — PASS only for the compiled finite table

Stanley's 1986 work already gives the Ehrhart, volume and reciprocity identities, and existing poset catalogues and linear-extension statistics cover the small objects and their volumes. The complete joined per-type rational Ehrhart and (h^*) table for the 318 six-element isomorphism classes was not found in the checked sources. It is a computable data compilation; the maximum-volume theorem, its unique witness, and the 406 identities are not new mathematical discoveries.

## Scientific value — PASS, bounded

The cross-indexed table lets one compare full order polynomials against linear-extension counts and test poset enumeration software. The 121 distinct six-element Ehrhart value vectors refine 62 distinct (e)-values in the stored census. This is limited small-parameter reference data, with no new general inequality or polytope theorem.

## Sources

- Stanley, *Two poset polytopes*, author-hosted full text: https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf
- OEIS A000112 small unlabeled-poset counts: https://oeis.org/A000112
- FindStat Posets collection and linear-extension statistic: https://www.findstat.org/CollectionsDatabase/Posets/ ; https://www.findstat.org/StatisticsDatabase/St000100/
- Candidate `artifacts/posets.json` and `artifacts/ehrhart.json`; independent ideal/extension recursions above.
