# Independent mathematical audit

## correctness

PASS

First forced vertex v of part V_i must see lambda-1 colours outside, leaving exactly its final part colour; thus its completed part is monochromatic, all lambda colours occur and every multichromatic part is initially fully seeded. Two initially seedless monochromatic parts prevent any first force; conversely all others seeded permits completion, first filling the unique seedless monochromatic part. Unique completed colouring gives the exact profile/Stirling-weight generating function, counting total colourings once by subtracting x^N from each non-total profile term. For lambda-r=k>0, allocating k extra colours to a proper subset H of multichromatic parts requires |H|<=k<=sum_H(n_i-1); optimal seed domain is min{N,r-1+min_H sum_H(n_i-1)}. Independent exhaustive local-rule enumeration corroborated K_(2,2,3),lambda=5 coefficients {4:600,5:1800,6:2280,7:1620}; K_(1,2,2),lambda=4 coefficients {3:144,4:144,5:72}; and K_(1,1,2),lambda=4 coefficients {3:48,4:48}. The algebraic proof covers every r>=3,lambda>=r+2 including lambda>N (then only totals force).

## originality

PASS

The q=r formula for complete multipartite graphs and q=3 bipartite formula are established and credited. Neither alone contains the new q>=r+2 poly-part allocation or min-seed subset-capacity optimization.

## value

PASS

There is a natural transition from one extra colour to multiple independently multicoloured multipartite parts, yielding a nontrivial Stirling-profile formula for every seed-domain coefficient and a precise capacity subset-sum minimum. This is a motivated infinite-family evaluation of a forcing polynomial, not a renamed ordinary chromatic polynomial or a tiny finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
