# Independent mathematical audit

## correctness

PASS

For each edge species e, define I_e to indicate that both endpoints lie in the uniformly unselected h=n-k vertices. R_k=(n-1)-X, X=Σ_e I_e. Then E I_e=p2, E I_e I_f=p3 when edges meet and p4 when disjoint; summing m diagonal and 2*C(m,2) offdiagonal terms gives Var(X)=m p2+m(m-1)p4+2W(p3-p4)-m^2 p2^2 exactly. Here p3-p4=P(these 3 vertices unselected, a fourth selected)>0 exactly 1<=k<=n-3, including k=1 where Var(R_1)=(2m+2W)/n-(2m/n)^2. Tree excess degrees t_v=d_v-1>=0 with Σt=n-2 prove W_min=n-2 only for a path and W_max=C(n-1,2) only for a star. Direct small n=4,5 classification gives distinct W on nonisomorphic trees. A/B are six-site trees with the same degree profile (3,2,2,1,1,1) and W=5 but k=2 histograms 5,5,5,0 versus 4,8,2,1 for R=2..5. For each n>=6 attach n-6 leaves to site 0 in both trees: same W=C(n-3,2)+2, distinct high-degree-site leaf neighborhoods, and exactly one extra sample pair gives R2=2 in A (two leaves or a leaf+degree-2 adjacent pair account for all such pairs), so probabilities differ by 1/C(n,2). Boundary k=0,n are degenerate and formula remains valid. Independent implementation, not package verifier logs, exhaustively reproduced all 18,244 labeled trees of n=4..7, 144,358 tree/sample-size combinations and 2,238,496 selected subsets, plus the all-order witness combinatorial count to n=30; this is finite corroboration of the symbolic proof.

## originality

PASS

Qualified best-of-knowledge PASS restricted to the precise fixed-size ecological conditional moment-information result and, especially, the explicit persistent all-orders counterfamily with an exact sample-two probability gap. The general rarefaction expectation/covariance method (Ugland 2003), the tree degree/wedge extrema (Ferrer-i-Cancho), the first degree-sequence ambiguity at n=6 (OEIS A295637), and the full induced-component polynomial and injectivity through nine vertices (Tittmann et al.) are established and receive no independent novelty credit. In combination those sources already strongly anticipate the six-site base ambiguity, so the six-site number by itself is not independently novel. What remains in the submitted complete claim is the exact specialized equivalence of entire first-two-moment curves to W and a constructive for-all-n>=6 *fixed k=2* richness-law separation with numerator exactly one. The inspected prior texts and relevant published records do not supply this combined all-orders precise conditional-law result. Search cannot exclude equivalence under another name or an unindexed tree-polynomial specialization.

## value

PASS

For a finite incidence network with each species on two sites and a fixed tree of possible shared species, the first two uniform sample-order moments are natural observation summaries. The exact six-site information-loss threshold and persistent all-n>=6 fixed-two-site witness show precisely what such summaries cannot recover, even when connectivity and occupancy are fixed; a concrete event probability differs by one out of C(n,2). This is a mathematically motivated sharp inference boundary and constructive family, not an arbitrary enumeration. General covariance identities and path/star degree extrema are old, and the first pair of trees with the same degree sequence is tabulated; neither these old ingredients nor the finite computation alone is counted as the value. Scope strictly tree, uniform fixed-size subset, binary 2-site occupancy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
