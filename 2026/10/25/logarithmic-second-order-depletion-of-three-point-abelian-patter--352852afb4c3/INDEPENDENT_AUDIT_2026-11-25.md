# Independent mathematical audit

## correctness

PASS

Theorem E of Zeng–Xue–Zeng supplies the infinite forest characterization. The sum-c perfect matching contracts to the simple graph of distances A=c−a and B=c−b on c+1 vertices. Independently, on A+B vertices the two-distance graph is the union of gcd(A,B) cycles, obtained by stepping by A modulo A+B. Deleting the last gcd(A,B) vertices breaks all cycles since each lies in a different residue class, whereas deleting fewer leaves a full cycle. For larger vertex sets the graph still contains the original cycles. This proves the required cutoff and the strict arithmetic inequality. Strict doubling adds only disjoint new edges with fresh endpoints and cannot create a cycle, so the finite forest criterion is sufficient for an infinite support with exactly these first three positions. For gaps x=b−a, y=c−b, the allowable starts satisfy 0≤a≤N−x−y and a<y−gcd(x,y). Without the gcd term, set y=a+1+j and x=1+i; this gives 2a+i+j≤N−2 and leading volume 1/12. The gcd deficit is exact on x+2y≤N+1; outside this triangle the only nonzero deficit is in a strip of width gcd(x,y). Writing x=du,y=dv with d=gcd(x,y), each d gives at most one possible integer u+2v in the strip, yielding O(N²) in total. The main triangle has divisor-sum count Σφ(d)floor((floor((N+1)/d)−1)²/4) and leading term (N²/4)Σ_{d≤N}φ(d)/d², after truncating at d≤N. Möbius inversion gives (6/π²)log N+O(1) for this last sum, verifying the correction and the normalized proportion. Separately, bounded graph and count comparisons covered 969 triples with c≤18 and 22 cutoff values through N=23; these are checks of the finite reductions only.

## originality

PASS

Pass for the aggregate prefix count, in particular the explicit nonzero N² log N depletion with O(N²) remainder. The forest equivalence, the arithmetic admissibility test it yields and the totient estimates are not separately credited as new. The strongest inspected matching classification concerns a single prescribed triple, not the weighted loss in the population of triples.

## value

PASS

Passing from a decision criterion for one prefix to the prevalence of extendible prefixes fills a natural counting gap. The limiting one-half density by itself misses an arithmetic bias larger than the usual quadratic counting remainder. Isolating its coefficient separates geometric volume from gcd depletion, a meaningful use of the exact criterion rather than just evaluating small cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
