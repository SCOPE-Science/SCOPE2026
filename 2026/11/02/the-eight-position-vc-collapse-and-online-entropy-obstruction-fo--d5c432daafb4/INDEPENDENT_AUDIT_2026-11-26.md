# Independent mathematical audit

## correctness

PASS

Independent computation reproduced all eight (concept count, VCdim, Ldim) triples: (1,0,0), (2,1,1), (6,2,2), (23,3,4), (93,4,6), (360,5,8), (1312,6,10), (4541,6,11). Reproduce with python3 /workspace/audit-reproductions/review5.py, or pass 8 to run only the decisive row. The independent enumerator places positions in increasing value order; when i is placed after i+1, a descent is irrevocable and can be counted immediately. This enumerates every admissible order once, with all positional pair labels. VC supports are forests because an undirected cycle can be labeled as a directed cycle; a support with n-1 edges must therefore be a spanning tree. Independent Prüfer enumeration found a spanning-tree witness for every 2<=n<=7, excluded all 262144 candidates at n=8, and confirmed all 64 patterns of the size-six witness. The exact online decision procedure deduplicates unordered splits and prunes only when a child has fewer concepts than the number of leaves required. Any feasible tree needs an admissible root split with both children feasible, which proves completeness by induction on depth. At n=8 it rejects depth 12 and constructs feasibility at depth 11; at smaller sizes the entropy upper bound is attained. The claimed infinite-family lower bound follows by concatenating disjoint ascending value ranges, preserving the sum of the internal descent counts and enabling sequential copies of the depth-eleven tree. The forest VC bound is unchanged, so the gap is at least 3s+1.

## originality

PASS

In the bounded comparisons, the supported distinct claim is the two-adjacent-descent family's first simultaneous deficits at n=8 under positional-pair queries, with exact dimensions and the accompanying block lower bound. The catalog has related finite entropy failures in other classes, including the unrestricted class at n=7, but those are not this family. Generic recurrence algorithms, the concept count and known ceiling arguments are not themselves credited as new.

## value

PASS

At most two descents is a canonical low-run-complexity restriction allowing three increasing runs with free boundaries, beyond a single break. A first strict deficit of both natural bounds is a motivated finite cutoff rather than an isolated table row. The exact values distinguish the ability to realize all fixed support labels from adaptive shattering, and the exact depth-eleven witness yields a linear gap by repetition while keeping a descent budget of one quarter of the number of positions. The independent finite determination and its amplification are useful without an all-size closed formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
