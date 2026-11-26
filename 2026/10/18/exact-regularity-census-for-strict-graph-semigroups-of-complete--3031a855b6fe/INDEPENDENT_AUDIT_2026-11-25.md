# Independent mathematical audit

## correctness

PASS

A strict composite stays strict because each edge fiber of the second map meets the first image in at most one point; hence a nonempty composite fiber is an unchanged original edge. For fixed edge-type occupancies, injectively assign labeled endpoints in each part and divide by the simultaneous edge permutations of each type; multiplying by the independent-image and labeling choices gives T_k. The equation fgf=f forces distinct selected preimages of the image labels into one part. Conversely these preimages form an independent image for g, and its domain pairs can cover the image of f because the k domain edges of f already show that at least k vertices lie outside the part containing that image. This proves the regularity test. Inclusion-exclusion stops at pairwise intersections even at k=1; for idempotents each output must be its own chosen endpoint. The empty map and rank bound agree. For three parts, a bad matching must use all three edge types and needs two vertices in each part and a rank-three image. For four or more parts the two disjoint part pairs give a rank-two witness whenever a part can support that image. For fixed n≥2 the leading terms of the total and regular counts are n^(2n) r^(2n+1)/2^n and n! n^n r^(n+2): the forbidden-edge correction loses one power of r, the pair-intersection term in b_n is O(r^2)=O(r^n), and lower ranks are smaller. The stated ratio follows. A fresh bounded enumeration of all strict maps, direct composition f², and search through all g for fgf=f reproduced (253,253,61) and (1021,877,133) for K_(2,2,2) and K_(2,2,3), respectively. Frozen verification notes and verify.py describe a separate replay and were read, not executed; the two direct samples do not prove the general theorem. The verifier's checks for at most two parts are outside the theorem's stated scope.

## originality

PASS

Credit the general strict-map description and regularity criterion to Margolis–Rhodes. The supported distinct result is the evaluated strict multipartite rank census and its global classification and sharp fixed-part-size rarity law, not a new map-by-map criterion. No inspected matching statement supplies that combined result or a stronger evaluated census specializing to it.

## value

PASS

The rank-refined counts distinguish regular and nonregular behavior in a natural non-bipartite test family for the general semigroup regularity problem. The classification exhibits a regular K_(2,2,2) and the immediate loss at K_(2,2,3); the census explains the exact proportion and yields a sharp polynomial scarcity law over a growing family, which the structural test alone does not quantify.

The dated certificate retains the supplied scientific assessment, sources and limitations.
