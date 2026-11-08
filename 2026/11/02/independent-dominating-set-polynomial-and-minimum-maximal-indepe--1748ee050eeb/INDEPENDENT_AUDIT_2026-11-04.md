# Independent mathematical audit

## correctness

PASS

In F_2(K_{m,n}), configurations split into same-part pairs P and mixed pairs X; both are independent classes, with adjacency precisely when a mixed pair meets an endpoint of a chosen same-part pair. For any maximal independent set with mixed members, the active endpoints S,T are proper, sizes 0 or >=2; maximality forces all C(S,2), C(T,2), and the complete unused rectangle. Conversely every such I(S,T) dominates all omissions; its internal edges uniquely recover S,T. This proves the polynomial with binomial multiplicities, count 1+(2^m-m-1)(2^n-n-1), and all maximizers P/X. Minimizing f(s,t) by its integer k=s+t bound proves i(H)=2 for (2,2), 2a-3 for b=2<a, and a+C(b-1,2)-1 for b>=3, a>=b; convexity bounds max, with triangular-part ties. Independently enumerated maximal cliques of the complement for (2,2),(2,3),(3,3),(3,4),(4,4) and compared every coefficient; these finite checks are not the all-parameter proof. Inspected both verifier implementations; do not infer infinity from finite logs.

## originality

PASS

The 2016 token-graph paper already proves the scalar maximum independent-set size, not the coefficient distribution, smallest maximal set, or exact labeled optimizer classification. The 2026 K_{m,n} two-token domination papers count unrestricted dominating sets, which need not be independent. Resultary searches for token-graph independent domination and maximal-stable-set polynomials found related complete multipartite polynomials for different graphs, not a dominating theorem. The full independent-dominating enumerator and its extremal consequences therefore survive best-of-knowledge; primary-paper and hidden-equivalent-table risks remain.

## value

PASS

A maximal independent set is a natural independent dominating configuration of the exclusion/token graph. Its whole size enumerator, smallest independent dominating cardinality and complete maxima describe structural optimization not supplied by the older scalar alpha. The infinite triangular-number tie family is a sharp boundary. This is a reusable exact baseline for a canonical graph family, not a parameter-renaming exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
