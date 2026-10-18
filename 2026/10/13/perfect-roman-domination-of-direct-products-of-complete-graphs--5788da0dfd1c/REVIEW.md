# Independent mathematical audit

## correctness

PASS

For G=K_m tensor K_n, distinct cells are adjacent iff both coordinates differ. Fix A the label-two support (size t); any outside cell can be labeled zero iff it has exactly one neighbor in A; all other outside cells must be one to minimize, giving exact canonical weight w(A)=mn+t-q(A). Single support gives mn+1-(m-1)(n-1)=m+n. For t=2 the three row/column positions each yield strict excess. For t>=3, row with s_i supports outside admits at most 0,n-1,2,1 eligible unselected cells for s_i=0,1,2,>=3 respectively, and at most one row has s_i=1. Hence q<=n+2m-3 and sym q<=m+2n-3, so equality forces t=3=m=n. In 3x3, q=6 requires exactly one selected per row and column, yielding 3!=6 extra permutation supports plus 9 singletons, 15 minima. Independent bitmask exhaustive supports at (3,3),(3,4),(3,5),(4,3),(4,4),(5,3) verified value/count; universal proof is the row bounds, not enumeration.

## originality

PASS

Cabrera Martínez–Peterin–Yero Proposition 2.1 treats ordinary Roman domination of exactly K_m tensor K_n (at-least-one rather than exactly-one defender), with 5 or 6 optimal weight, so does not cover growing m+n perfect Roman number or its unique exception. Almulhim–Akwu–Al Subaiei perfect Roman Cartesian path/cycle products have different graph adjacency. Published Resultary perfect Roman complete multipartite polynomials apply to a different graph type; the tensor product is the rook-graph complement and not generally complete multipartite. Search aliases categorical/Kronecker/tensor and complete-graph direct products yielded no checked stronger exact perfect Roman classification. Best-of-knowledge pass with remaining unindexed source risk.

## value

PASS

For a canonical graph product family this gives a complete optimizer classification, a single exceptional 3x3 permutation type, and a growing separation from the known bounded ordinary Roman number. The all-m,n exact family is independently useful in product domination theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
