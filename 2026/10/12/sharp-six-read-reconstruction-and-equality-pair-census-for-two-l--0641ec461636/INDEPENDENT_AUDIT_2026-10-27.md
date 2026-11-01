# Independent mathematical audit

## correctness

PASS

For n=6, exactly two sequential adjacent-two-symbol deletions leave precisely the six original index pairs (1,2),(1,4),(1,6),(3,4),(3,6),(5,6). Hence D(a,b,c,d,e,f)={(a,b),(a,d),(a,f),(c,d),(c,f),(e,f)} as a set, even when alphabet labels coincide. If |D(x)|=6 then a,c,e must be pairwise distinct (otherwise edges duplicate), likewise b,d,f. Ordered-pair first-coordinate degrees are exactly 3,2,1 and second-coordinate indegrees exactly 1,2,3; the unique degree classes recover a,b,c,d,e,f even when a symbol participates in both first and second coordinates. Thus no different x,y have 6 shared outputs. The distinct ternary witness x=(0,0,1,0,2,1), y=(0,1,1,0,2,1) has equal five-element balls. For any q, every ordered input pair induces a unique set partition of twelve positions, a canonical restricted-growth encoding with k blocks and precisely (q)_k alphabet-label injections; x=y is removed. Independent C++ implementation generated all B_12=4,213,597 partitions (including 203 x=y partitions), with max distinct-input overlap 5 and ordered-pattern counts (k: both-five, mixed-five/six, both-six): 3:(72,96,42), 4:(72,288,222), 5:(12,144,207), 6:(0,16,55), 7:(0,0,4); no other nonzero categories. Divide the ordered labeled-pair sum by 2 to obtain T(q) and its leading 2q^7 term. A second direct two-step-deletion simulator independently gave q=2 overlap4/count120, q=3 overlap5/count630, q=4 overlap5/count9504. The infinite q statement follows by the finite partition-type bijection, not by testing finitely many alphabets.

## originality

PASS

Best-of-knowledge priority survives. Lan, Sun, Yu and Ge, arXiv:2504.20460v1 (2025), Sections IV.A–B, Theorem IV.10, Lemma IV.19 and Theorem IV.16 treat the exact same sequential multiburst model. They prove q-ary single-ball maxima and an explicit q-ary five-overlap lower construction, while their proven pair-overlap maximum is restricted to q=2. Neither implication supplies the sharp q>=3 upper bound five or all-q extremizer polynomial. Schoeny et al. arXiv:1602.06820v2 concerns single-burst correcting codes. Sun, Xi and Ge (IEEE TIT 2023) concern a single burst; its full text remained inaccessible, and an authorized full-text access action was blocked by safety controls, so no whole-paper noncoverage was asserted. Later papers on unrestricted deletions do not establish this sequential two-burst subchannel bound. Published mathematical-record searches returned related single-deletion and ordinary-deletion statements but no covering exact census. Searches alone are not proof of originality; unindexed exact censuses and inaccessible pertinent texts remain named risks.

## value

PASS

The six-symbol/two-length-two-burst channel is the first output-length-two instance for these two bursts: at input length five only one symbol survives. Determining its sharp q≥3 reconstruction read threshold is a motivated exact boundary between uniquely reconstructable full six-output relations and confusable five-output pairs, while the all-q equality-pair polynomial classifies how often the worst-case channel ambiguity occurs among labeled words. Its fraction 4q^{-5}+O(q^{-6}) is quantitatively informative for comparing worst-case and typical reconstruction, and the output-set versus input-pair distinction is essential. This is a natural exact finite-channel invariant with an all-alphabet combinatorial proof, not an arbitrary integer slice or recomputation of the binary theorem. No algorithmic guarantee for longer words or arbitrary burst counts is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
