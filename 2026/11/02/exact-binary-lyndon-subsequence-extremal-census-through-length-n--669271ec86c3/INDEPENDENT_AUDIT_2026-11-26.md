# Independent mathematical audit

## correctness

PASS

The frozen recurrence is an exact set union because a subsequence either uses the last host position or omits it; the sentinel encoding separates lengths. The C membership tags, saved pre-append list length, rotation comparisons (strict, including the unary and periodic cases), and full fixed-length host loop implement these definitions within the stated integer bounds. I recomputed by a different, pattern-first count: a Lyndon pattern is strictly smaller than all proper nonempty suffixes. For each tuple of earliest greedy match positions ending at n, all skipped bits must be the opposite of the next required bit, fixing a single length-n host for this pattern/tuple. Different tuples cannot count that pattern twice in a host. The per-host score is its prefix score plus the new patterns whose greedy match ends at n. Exact integer accumulation recovers all 19 maxima, all 19 tie counts and the first witnesses, as well as both length-twelve attainers. At n=17,18,19 the results are 1292,1941,3132, all unique. Replay: /workspace/review-work/lyndon_dual.py 1 19 (Python/NumPy); recorded results in lyndon_small.txt, lyndon_middle.txt and lyndon_upper.txt in the same directory. The frozen Python crosscheck differs in data structure and predicate but shares the set recurrence; the pattern-first replay is independent of that recurrence. No claim outside n=1..19.

## originality

PASS

The precise maximum of distinct scattered Lyndon strings was posed before; the inspected papers, open-problem note and closest catalogue records do not give the exact ordered-binary census or its attainer counts. The pass is limited to the finite result, not the problem, underlying definitions, or an all-length characterization.

## value

PASS

This is a reproducible finite answer to the binary specialization of a published open extremal question, not a recomputation of occurrence or factor counts. Exact numbers of optimizing hosts add information beyond the maximum sequence; the length-twelve tie and changing extremizer shapes are useful constraints on any proposed characterization. The complete contiguous range of verified host lengths is useful as a benchmark without implying an all-length solution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
