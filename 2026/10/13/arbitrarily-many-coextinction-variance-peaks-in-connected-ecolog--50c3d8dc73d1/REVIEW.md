# Independent mathematical audit

## correctness

PASS

For k>=2 take k primary blocks B_i of size s_i=100^(i-1), N=sum s_i, specialists C_i attached to each B_i and one generalist G attached to all N. Every primary has exactly degree two, the bipartite graph is connected, and secondary neighborhoods are distinct. Under iid primary extinction probability q, Y_i are independent Bernoulli(q^s_i), Z=product Y_i, secondary count X=sum Y_i+Z. Direct covariance gives Var X=sum_i(q^s_i-q^(2s_i))+q^N-q^(2N)+2sum_i(q^N-q^(N+s_i)), while EX=sum_i q^s_i+q^N strictly increases. Using a_i=s_i/(s_i+2), b_i=5s_i/(5s_i+1) and scale separation 100, elementary bounds show qV prime(a_i)>0 and qV prime(b_i)<0 for each i, even with the connected generalist correction; a_i<b_i<a_{i+1}. Each disjoint (a_i,b_i) contains a strict local maximum and each between contains a strict local minimum. Independently recomputed qV prime for k=2,3 with 80-digit mpmath from the exact symbolic formula: k=2 signs (0.111111111,-0.555550977) and (39.1168566,-210.850978); k=3 (0.111111111,-0.555554348), (9.05073131,-53.2220851), (3861.82164,-21072.1588). These are corroborations only; all k follows from the displayed uniform analytic inequalities.

## originality

PASS

Earlier ecology papers analyze secondary-extinction indicator rules and robustness moments. The highly relevant Chabert-Liddell et al 2021/22 primary source was read in full and its Proposition 3 treats variance in a bipartite stochastic-block model at fixed extinction counts, not the exact common-q independent-removal connected-degree-two arbitrary-multimodality theorem. The construction separates scales while keeping graph connected, distinct consumer neighborhoods, and each primary degree two. This statement is not simply the known Bernoulli marginal extinction rule or a direct specialization of the published robustness-variance formula.

## value

PASS

The theorem constructs arbitrarily many genuine strict uncertainty peaks under one monotone control parameter despite monotone expected extinctions, in connected ecological interaction networks satisfying a strong degree restriction. This exposes a robust structural obstacle to unimodality intuitions and is mathematically motivated as a qualitative global shape classification, though the huge networks and q near 1 limit empirical transfer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
