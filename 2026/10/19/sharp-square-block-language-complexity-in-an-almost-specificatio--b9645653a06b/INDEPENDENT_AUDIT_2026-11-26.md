# Independent mathematical audit

## correctness

PASS

Partitioning by the first marker gives the disjoint count pq^n+G_n+p sum_{i=1}^{n-1} q^i G_{n-i}. The marker boundaries uniquely determine the free blocks, whose suffix counts depend only on cardinality of the restrictions. The nested sets ensure that truncated prefixes of restricted runs remain restricted; a factor starting inside a run starts with an unrestricted monochromatic prefix. Normalization gives total renewal mass 1/(1-rho) including g_0 and deficit p sum_{m>=n} g_m-g_n. Summing the square blocks exactly gives the displayed A_n, of order sqrt(n) q^{-sqrt(n)} uniformly in phase. Moving the index by h=floor(n^(1/3)) changes A_n by o(A_n), and the central convolution has sqrt(j)+sqrt(n-j)>=sqrt(n)+c sqrt(h), making it negligible even with the polynomial factor. The two edge tails give subexponentiality by matching upper and lower bounds. The cited light-tailed stopped-sum relation applies to the independent geometric count and identifies the renewal-tail constant (1-rho)^(-2). Consecutive tail equivalence makes g_n negligible. At p=2,q=4 the exact tail gives coefficient 1296/25 for the bracket, and s taking every integer from 0 to 2k realizes every limit in [864/25,3456/25].

## originality

PASS

Credit the language construction, free/good recurrence, square-root cardinality and both placements to Kwietniak–Oprocha–Rams, and the random-sum theorem to the heavy-tail literature. Count independence is an elementary consequence of the decomposition, not a standalone novelty claim. The supported distinct contribution is the sharp normalized deficit with its explicit nonconstant square-block phase and full limit interval.

## value

PASS

The exact leading error shows what usual entropy and a stretched-exponential rate miss: a changing prefactor across each square block, with a full nontrivial phase interval in the original model. It gives a quantitative invariant and a useful benchmark for finite-length word counts; equal counts in the two variants also show that word complexity cannot detect their prior weak-specification distinction. Value rests on the sharp deficit law, not on rederiving the recurrence or evaluating one numerical case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
