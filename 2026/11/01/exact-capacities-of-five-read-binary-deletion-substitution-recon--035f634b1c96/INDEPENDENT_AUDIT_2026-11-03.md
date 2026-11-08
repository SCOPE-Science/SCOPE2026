# Independent mathematical audit

## correctness

PASS

The distinct-output ball is the union of Hamming radius-one neighborhoods of every one-deletion descendant; codebooks are exactly cliques of the graph with an edge iff intersection cardinality <5. Inspected the actual verify.py and its complete bit-set maximum-clique branch-and-bound proof: independent sets in its greedy coloring give a safe upper bound for each remaining branch; every compatible extension is considered. Reimplemented channel-ball construction and full exact maximum-clique search independently for all lengths 3..9: maxima (8,5,5,6,8,12,16), edges (28,38,115,552,2917,15194,75483), and at n=9 exactly 416465 recursive calls. Verified the seven lower-bound witnesses logically against the same channel model. This is a complete finite-domain computation, not an infinite claim. A codeword is padded to exactly n bits; repeated output words are deduplicated.

## originality

PASS

Direct five-read primary work studies constructions and bounds; a closely related full exact finite classification refers to disjoint-ball (one-read) codes and cannot settle maximum five-read code cardinalities. Actual Resultary and primary-source comparisons found no dominating exact table. The novelty conclusion is best-of-knowledge and limited to this finite profile, not channel definitions or algorithms.

## value

PASS

The natural finite-blocklength five-read reconstruction capacity is a primary optimization invariant. A complete n=3..9 capacity profile, including a 512-vertex n9 optimum and the counterintuitive decrease 8 to 5 from n3 to n4, is a meaningful benchmark for designs and finite-channel bounds, even without an all-length theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
