# Independent mathematical audit

## correctness

PASS

Linearity of expectation and independent failures give protection gain sum(q^d) over neighboring plants. With two pollinators the shared terms cancel, leaving a fixed sign difference. With at most three plants either a target covers them all or each singleton target is dominated by a two-plant target (by connectivity for at least two plants), and any two two-plant neighborhoods differ by at most one substituted term q^d. Their order cannot change on (0,1). I independently checked 4x3 without relying on the frozen enumeration: write s_i for the count of singleton rows at i and t_i for the count of two-pollinator rows opposite i. Removing common terms and dividing the gains by q leaves the scores s_i-t_i q. A universal target exists iff the maximizers at 0 and 1 intersect. With disjoint maximizer sets, any initial maximizer i and final maximizer j satisfy s_i>s_j and t_i-t_j>=s_i-s_j+1, so t_i>=2 and at least one singleton is required. Three singleton rows leave too few pairs. If two singleton rows have the same holder then that holder needs t_i>=3; if they have different holders both need t_i>=2. Both are impossible with four rows. Thus there is one singleton at A and at least two opposite pairs BC. Connectivity forces precisely two BC rows and the last row to be AB, AC, or ABC, giving exactly the two classes up to guild-preserving relabeling. The displayed expectation vectors follow by summing q^degree over unprotected plant neighborhoods; their leading difference q(1-2q) gives the switch and all ties, including a three-way tie at the crossing for the second class. For the denominator, 7^4-3*3^4+3=2161 labeled matrices have no isolated vertices. Exactly 3[4(3^3-2^3)+6(3^2-2^2)+4(3-2)]=330 split as a one-pollinator and a connected two-pollinator component; 3^4-3*2^4+3=36 split into three one-pollinator components. This leaves 1795. The first class has 12 row arrangements and six distinct column permutations of the multiset, the second 12 and three; hence 72+36=108.

## originality

PASS

Both the expected-richness gain formula and survival-dependent protection choices are prior in the closest indexed model. The part supported as distinct is the minimum total order for loss of a universal target, with the full two-class first obstruction layer and its multiplicities. Same-model reentry results answer a different extremal question, and the other coverage and ecological comparisons use different objectives or stochastic mechanisms.

## value

PASS

The first-layer classification tells exactly when a single best target is guaranteed to work without knowing p, and gives two minimal examples in which it provably cannot. This is a natural sharp boundary for a robust choice problem in an established model. The count is useful because it measures the incidence of the first obstructions under uniform labeled sampling and the two class descriptions explain what drives the switch; a numerical crossing example alone would not do either.

The dated certificate retains the supplied scientific assessment, sources and limitations.
