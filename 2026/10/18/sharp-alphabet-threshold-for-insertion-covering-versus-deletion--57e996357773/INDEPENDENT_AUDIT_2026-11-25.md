# Independent mathematical audit

## correctness

PASS

The frozen theorem's two numerical boundaries are sound. To force a deletion target y, it suffices to construct one ambient word whose every allowed subsequence contains y. At m=n−R=1 or for repeated length-two targets use a constant word. For distinct a,b, the word a^(R+1)b^(R+1) has no ab-avoiding subsequence longer than R+1. At m=3 over any q≥3, a word of length 2R+3 has at most R copies of at least one prescribed letter from {0,1,2}, since 3(R+1)>2R+3 for R≥1. Delete all its copies, then pad to R deletions; the avoidance code insertion-covers but misses 012. That proves the repaired q≥3 onset and covers the boundary R=1. The frozen binary comparison also holds: 000, 001 and 010 witnesses up to symmetries cover m=3; for 010 the between-selected-zeros restriction bounds an avoiding length by R+2. At m=4 any alleged ambient word forcing 0110 must have exactly R+2 of each symbol, but its R+1 consecutive-zero gaps would each require two ones. The repaired RESULT.md and SLOGAN.txt retain the binary threshold only as credited context. Independent replay: python3 -B /workspace/branches/reproduce_frozen_checks.py 5 maximizes avoiding-subsequence length via a greedy-prefix automaton on every ambient word, for (q,R)=(2,1),(2,2),(3,1) through each onset. It confirms the stated implication below and failure at the boundary in those cases only; the uploaded code and recorded counts were inspected but not rerun.

## originality

PASS

Pass applies to the narrowed all-positive-radius nonbinary first-blocklength theorem. The frozen all-alphabet framing presented a binary threshold that is fully covered by a distinct indexed record, which even classifies the maximal separators. That is an overlap, not a claim of chronological priority for the later-dated record. The ternary q=3,R=1 existence slice is also indexed. The corrected RESULT.md explicitly distinguishes these from the general nonbinary onset; neither overlapping result supplies the nonbinary theorem for general q,R.

## value

PASS

The nonbinary onset is a natural missing threshold after the earlier binary non-equivalence construction. It both excludes every earlier length and produces a one-symbol improvement that holds for all positive radii and every larger alphabet, explaining it by a third distinct symbol. This structural separation is useful independently of binary maximality and does not claim a code-size optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
