# Independent mathematical audit

## correctness

PASS

For any singleton trace, the endpoint used to hit its only edge must have degree one, so each edge has a leaf endpoint. In a connected edge component two nonleaves would force an edge with both endpoints nonleaves along their shortest path; hence every component is a star. On a star of s edges, the empty trace costs zero, the full trace one, and a nonempty proper trace of t edges requires and is realized by t leaves because the hub is forbidden. Disjointness makes costs additive, and maximizing independently yields sum max(1,s-1). The empty trace requires r outside vertices, which also suffice to pad any minimal-cost trace. For k>0 edges and m star components the support is k+m; with a singleton stars the cost is k-m+a. The minimum a is max(0,2m-k), attained by using twos and distributing surplus or using a mixture of ones and twos. Thus m>=max(1,k-r), m<=min(k,r), and k+m<=n-r; the minimum feasible m gives exactly k<=2r and n>=max(r+k+1,2k). This also handles r=n and the empty edge set. At r=2 the budget gives precisely the six nonempty types and their support sizes plus two outside vertices. On prescribed supports the count factors are 1,3,3,4,30,90, with automorphism orders 4 for the star-plus-edge and 8 for the pair of two-edge stars. The independent complementary-trace replay /workspace/branches/replay_4.py checked every F for n=2..6 and all r, every F of size at most four at n=7,8 for all r, and that size range at n=9 for r=2. It returned e.g. [1,21,210,770,0] at n=7 and [1,28,378,1960,2520] at n=8. General exhaustion follows from the analytic criterion, not truncation.

## originality

PASS

The distinct claim supported by the comparison is the exact constant-cardinality structural budget, and the resulting dimension over all r. The closed triangular specialization also overlaps exactly with a later indexed statement, and its dimension is equivalent to rank-two open Kneser VC dimension. The earlier open Johnson theorem does not give these closed traces. No checked broader prior supplies both the unused-vertex and maximal trace costs across fixed r.

## value

PASS

This is a complete local-to-global characterization of a natural exact-size incidence range system, distinguishing empty-trace space from the worst requested trace cost. It yields genuine finite-order thresholds and all support types, including the informative open/closed difference at order seven, rather than only numerical dimension checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
