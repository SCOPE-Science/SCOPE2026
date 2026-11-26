# Independent mathematical audit

## correctness

PASS

Nonedge molecules are midpoints of edge molecules, and each oriented edge is exposed by assigning values 1/2 and −1/2 at its two endpoints and zero elsewhere. Polar vertex rank is equivalent to spanning tight-edge connectivity; its tight tree forces integral values up to constants. Diameter two leaves binary cuts and the ternary case with the unique 0/2 pair. In a binary cut the tight graph is complete bipartite minus a matching. If both classes have size at least two it is connected: a class facing at least three vertices has common neighbors for pairs, and the two smaller-side vertices in the size-two case have a common neighbor on the larger side. Singletons fail because their mates are isolated. Pair multiplicities give m²−(a−b)²−c, with the two constants and 4m singletons removed and 2m ternary facets added. For a uniform binary cut, edge-crossing indicators for distinct edges are pairwise independent even if they share one endpoint; their sum has mean m(m−1) and variance m(m−1)/2. The explicit deletion/addition changes the raw second sum by 16m(m−1)² and not the first. The iid pair difference has variance 1/2 and the split fraction tends to 1/2, yielding the shifted chi-square by CLT/LLN and an O(m/4^m) total-variation modification. Minimizing (a−b)²+c gives the parity maxima; comparison with 4m−4 gives the tie only at m=3. The unordered (a,b) pair labels and a single ternary orbit yield the Burnside count and orbit sizes. Independent enumeration fixing one potential coordinate and using union-find and canonical pair labels reproduced the histograms and orbit counts for m=3,4,5 (python3 /workspace/review-evidence/check_frozen.py, facets). The frozen separate m=3–6 output was inspected as recorded evidence, not independently executed.

## originality

PASS

The facet criterion and total facet count are established and get no novelty credit. The supported distinct contribution is the distribution by actual vertex incidence, in particular the uniform-facet fluctuation law and the exact extremal/orbit refinements; no inspected source supplies those statements for this family.

## value

PASS

The ball and facet vertex count are natural combinatorial objects. Knowing the number of facets alone does not tell how nonsimplicial they are, how many maximize incidence, or what a typical facet looks like. The finite distribution answers those questions and the non-Gaussian limit exposes the quadratic imbalance mechanism, beyond a routine re-evaluation of the known total.

The dated certificate retains the supplied scientific assessment, sources and limitations.
