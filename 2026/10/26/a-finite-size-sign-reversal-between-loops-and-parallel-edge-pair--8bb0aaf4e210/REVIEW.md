# Independent mathematical audit

## correctness

PASS

For prescribed k disjoint pairing edges, probability is 1/[(q−1)(q−3)…(q−2k+1)]. Internal two-stub choices give EL=S/(q−1). Ordered cross-pair pairings on four stubs between i,j contribute 2 a_i a_j, yielding EP=B/[(q−1)(q−3)]. A loop compatible with such a double edge must avoid the four occupied stubs; its count is S−(2d_i−3)−(2d_j−3), yielding ELP=(BS−T)/[(q−1)(q−3)(q−5)]. Subtracting moments gives the exact covariance. For d_i=r, substitute S=va, B=v(v−1)a², T=2v(v−1)a²(2r−3), factor the sign vr(2−r)+(2r−3); r=2 is positive and r≥3 negative. The q=4 (v,r)=(2,2) perfect matchings give −4/9 directly, while asymptotics follow by powers of v. Independent enumeration of all labeled pairings across 701 weak degree profiles q=6,8,10 checked exact rational EL, EP, ELP, and covariance (2804 assertions) and 167 regular sign cases; these bounded checks supplement unrestricted counting.

## originality

PASS

Best-of-knowledge PASS. Wormald, Janson, and Angel–van der Hofstad–Holmgren give asymptotic independent-Poisson limits and compatible-indicator covariance tools for loops/multiple edges. A limiting zero covariance does not determine the sign of a finite nonzero covariance or the exact all-profile rational identity. The full accessible Angel paper does not state this exact regular r=2 versus r≥3 finite sign boundary; it could follow by additional arithmetic from general witness methods, so implicit coverage is a residual risk.

## value

PASS

A finite-size positive/negative dependence reversal at the natural degree-two boundary is a mathematically meaningful correction to the heuristic that asymptotically independent defect counts should have no signed dependence. The all-profile closed formula and the different O(v^−2) versus O(v^−1) decay scales can inform finite configuration-model approximations and are not merely restating Poisson limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
