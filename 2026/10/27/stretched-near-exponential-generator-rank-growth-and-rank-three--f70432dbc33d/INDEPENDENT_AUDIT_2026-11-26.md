# Independent mathematical audit

## correctness

PASS

GGJ Proposition 4.2 supplies m=3+r₃+r₂ for semigroup endomorphisms and n≥5. In each e-fiber the image point of e is a distinguished t-fixed point, and et=te=e preserves the fibers; t³=t limits components to height-one stars and leaf-decorated two-cycles. A size-j two-cycle has ⌊j/2⌋ unordered leaf-split types. Multisets first within and then across fibers give G−G₀ after omitting pairs with t²=t, and rank-two orbits lie in G₀. Analytically, Σj exp(−jx)=(2 sinh(x/2))^(−2)≤x^(−2); summing the log Q expansion gives c/t² with c=ζ(3)/2. The multiset logarithm is at most 2t^(−2)exp(ζ(2)/t+c/t²). At t=√((c+ε)/log n) this is o(n/√log n), yielding the stated Cauchy upper constant. Line 78 writes an equality where only an upper bound has been proved; replacing it by ≤ gives the needed conclusion with no change in the theorem. Taking t=2ζ(2)/log n instead for G₀ yields the stated rank-two bound. For L=⌊6√log n⌋ the number M of available types lies between L²/3 and L(L+1). The binomial pigeonhole bound gives T≥n³ at one common size s, since 12 log 2>3 and the denominator is polylogarithmic. The tighter upper bound s≤1+L²(L+1) in particular implies s≤648(log n)^(3/2) eventually. Padding by one smaller fiber preserves injectivity for each large integer n. The multiset lower bound gives log r₃≥n/(648√log n), dominating log(1+r₂) and proving m/r₃→1. Independent truncated product multiplication reproduces m(5), m(10), m(20), m(40)=35, 2880, 10998182, 30328785627967; replay with node /workspace/review-evidence/bounded-checks.js. This is a finite series check, not an independent generator classification or asymptotic proof.

## originality

PASS

The prior Resultary enumeration covers the exact Euler products and finite generator counts, and GGJ supplies the structural rank formula. Neither is passed as new. The supported distinct claim is the two-sided logarithmic growth scale (including the explicit bounds) and rank-three dominance. These follow here from uniform coefficient estimates and the large equal-size fiber construction, not from a reindexing or finite recomputation of the older formula.

## value

PASS

The result answers the order-of-growth part of an explicit question about a natural semigroup invariant. It separates that growth from both plane-partition scale and ordinary exponential scale and quantifies which generator orbits matter asymptotically; neither is visible from a finite list of exact values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
