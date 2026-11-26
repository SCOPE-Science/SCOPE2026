# Independent mathematical audit

## correctness

PASS

Reconstructed the proof in RESULT.md lines 29–53. Position j has letter 1+ν₂(j), and deleting the separator positions divisible by 2^k leaves exactly 2^(n−k) copies of Z_k. A factor with largest letter k cannot cross any separator and covers the unique k in its block. Its occurrence transfers at the same offset to every other block. Thus its union of occurrence intervals contains the entire class P_{n,k}; the singleton-letter factor realizes that class exactly. Nonempty disjoint classes then give the exact minimal coverage antichain and the criterion for arbitrary position sets. Independent nonempty choices per class give the stated generating polynomial; one representative per class gives the stated minimum size and count. For n≥2 the required n and n−1 positions force span at least 2^(n−2); equality fixes one of the two intervening intervals, whose interior is Z_{n−2} (empty for n=2). Counting one position per remaining class there gives the stated extremal count. The n=1 result is immediate. Inspected the frozen checker and recorded n=1,…,6 checks; no supplied script was executed, and these finite results are not needed for the all-order argument. Scope is the literal words with distinct symbols, not morphic images.

## originality

PASS

Within the evidence inspected, the all-cardinality Zimin characterization and exact minimal antichain are distinct from known general checking algorithms, from exact classifications for other word families and from the closest indexed repeated-permutation classification. The enumeration and span count are supported consequences of that Zimin structure, not claims of a novel general counting technique.

## value

PASS

The Zimin family is natural and the result replaces all factor checks on a word of length 2^n−1 with an irredundant n-edge certificate for arbitrary position sets, not just a witness for optimum cardinality. It also resolves exactly how many optimum transversals fit inside a shortest interval. The transport property, rather than routine multiplication once the edges are known, is the substantive structural contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
