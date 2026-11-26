# Independent mathematical audit

## correctness

PASS

At an unequal boundary a,b|c,d the two exterior-bond changes are +1 for matching the adjacent interior color, -1 for matching the opposite interior color, and 0 otherwise. Strict positivity requires no -1 and at least one +1. This holds at long-long boundaries and gives exactly the stated flank and isolation rules for singletons, including the wrapped n=3 case. After removing singletons the cyclic long-domain colors form a proper coloring, counted by the trace of the kth power of the off-diagonal all-ones matrix. Each long domain and optional singleton contribute t=z²[1+(q−2)uz]/(1−z); counting configurations with a distinguished long-domain start in two ways gives the n/k factor even for rotationally symmetric words. Adding constants cancels the factors (1−z), giving the claimed two polynomials, with the first two coefficients conventionally q. The positive solution of (q−1)t=1 is simple and the consecutive support powers rule out another zero at its modulus, including the q=2 test for 1+t. Continuity of the other roots gives a uniform spectral gap for the dominant reciprocal root near u=1. Thus the logarithm of the moment generating function of the singleton count has first two derivatives of order n, with limiting mean density α′(1)/α(1); implicit differentiation and Chebyshev give the stated limit (identically zero at q=2). Independent replay: /workspace/review_reproduction.py 3, direct full-energy enumeration of 180008 configurations in the three recorded grids, and exact polynomial agreement by evaluating −zW′/W at more marks than the coefficient degree. This corroborates only the finite grids.

## originality

PASS

Pass concerns the multicolor strict-blocking classification and its marked cyclic enumeration and density, not transfer matrices, cyclic color counting, binary domain heuristics, or a claim of absolute priority. The closest exchange and coloring comparators differ in either the move rule or the underlying state space in ways that change the count.

## value

PASS

The exact labeled-ring count separates available frozen states from dynamically selected states and shows a substantive kinetic distinction: strict binary blocking forbids singletons but for q≥3 the all-populations blocked ensemble has a positive limiting singleton density. The marked finite-volume law gives exact benchmarking information as well as the growth rate, without making an unsupported claim about relaxation or fixed-population ensembles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
