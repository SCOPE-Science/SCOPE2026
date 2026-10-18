# Independent mathematical audit

## correctness

PASS

With exactly two nonoverlapping adjacent-pair deletions, a hitting set of output words H yields |C|<=|H| for a code with disjoint deletion balls. For n=5,6 output space gives size 2,4 transversals. At n=7,9 keep an output whose odd slots agree, by pigeonhole among original odd slots and pair each removed odd slot with distinct adjacent even indices; gives hitting sets 4 and 8. At n=8 the period-two H={0000,0101,1010,1111} meets every ball: repeated aligned binary pair case immediately and six complement/reversal orbit witnesses for 24 distinct-pair cases; independently enumerated all 256 input words. Period-two length n words have pairwise disjoint balls for n=6,7,8. The 3 generator rows for n=9 yield 8 binary codewords with output ball sizes 1,1,1,1,7,7,7,7 summing 32; independent output-set computation proves pairwise disjointness and union all 32 five-bit words. Exact maxima (2,4,4,4,8), perfect n=9. No n>=10 theorem.

## originality

PASS

PASS best-of-knowledge with material literature-access risk: Ye et al 2024/26 gives asymptotic two-exact-burst constructions and a general graph-independent-set lower bound, not these five consecutive small optimal sizes. Wang et al 2026 public abstract gives general multiple-burst bounds; source assigned package correctly credits known n=6 special case. Full 2026 Wang arXiv PDF was inaccessible through current channels and protected retrieval reported vpn_disconnected; do not claim it is wholly noncovering. Neither inspected full Ye text nor available Wang material contains an explicit n=7,8 plateau and perfect linear n=9 partition.

## value

PASS

These are small but mathematically natural first nontrivial exact blocklengths for two-burst deletion coding, with the sharp n=8 plateau, first growth at n=9, and a perfect linear length-nine code partitioning the output space. Such extremal anchors and explicit perfect packing can inform coding constructions, finite bounds and benchmark algorithms despite absence of n>=10 census. Not an arbitrary fragment: the channel and initial spectrum are canonical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
