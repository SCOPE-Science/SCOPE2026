# Review of Exact generalized power-domination profile of crown graphs

## Correctness
PASS. The proof handles all set types. Mixed sets leave at most one unobserved vertex on each side after domination, so \(k\ge1\) completes propagation. For a one-sided set of size \(t\ge2\), all opposite-side vertices are immediately observed and the remaining count \(r=n-t\) propagates exactly when \(r\le k+1\). Singletons are checked separately and work exactly when \(k\ge n-2\). These cases are exhaustive and symmetric. The enumerator is a disjoint count of mixed and one-sided sets. The packaged exhaustive checker agrees for every subset for \(3\le n\le8\) and \(1\le k\le n\).

## Originality
PASS with a disclosed access risk. The closest same-object publication is Chandrasekaran–Sulthana (2019). Its indexed publisher text states \(\gamma_{P,k}\ge n-k\) for \(n\ge k+2\) and an algorithm output \(\gamma_{P,k}=n-k\); this is contradicted by the proved mixed-pair construction, for example \(\{a_1,b_2\}\) in \(\operatorname{Cr}_5\) for \(k=1\). The general regular-graph result of Dorbec et al. implies only an upper bound in the slice \(k=n-3\), not the classifier. The full searchable Brimkov et al. power-domination-polynomial paper has no crown occurrence, and the inspected 2025 full-text power-domination-polynomial treatment also has no crown occurrence. Semantic database searches for the same object, parameter, aliases, polynomial, and exact classification returned no stronger or equivalent claim. The complete 2019 publisher PDF could not be locally retrieved because of interactive verification, so the possibility of additional inconsistent statements elsewhere in that three-page article remains a residual source-access risk.

## Value
PASS. The result resolves a natural exact invariant on a canonical highly symmetric bipartite family, gives every generalized power-dominating set rather than only a minimum value, derives all minimum-set counts and the full cardinality enumerator, and corrects a published same-object scalar formula under the standard definition. The phase transition at \(k=n-3\) and \(k=n-2\) is structural rather than an arbitrary finite slice.

## Closest literature and limitations
The principal comparison is the 2019 crown-graph article, whose stated \(n-k\) value is not compatible with the standard propagation process. Generalized power domination was introduced by Chang et al.; Dorbec et al. give regular-graph bounds. Brimkov et al. introduce the power-domination polynomial. The finite checker is corroborative only. The exact contradiction is stated only under the standard generalized propagation convention.

Self-review: passed. Independent audit: not yet performed.
