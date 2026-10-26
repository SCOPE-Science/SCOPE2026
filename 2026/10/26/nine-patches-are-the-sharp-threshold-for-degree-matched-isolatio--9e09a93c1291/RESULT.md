# Nine patches are the sharp threshold for degree-matched isolation-risk reversals

## Finding

In independent patch survival on a tree-shaped habitat network, the expected number of isolated surviving patches is determined by the degree multiset. The variance is not. For every pair of nonisomorphic degree-matched trees of order at most eight, the difference in isolation-count variances has a constant weak sign for all survival probabilities \(0<p<1\). At nine patches, exactly three degree-matched tree pairs exhibit a sign reversal, among all \(96\) degree-matched pairs of the \(47\) unlabelled nine-vertex trees.

For one pair of nine-patch trees, labelled \(0\) through \(8\), the edge sets are

\[E(T)=\{04,07,01,12,23,45,46,78\},\qquad E(H)=\{05,01,12,14,23,56,58,67\}.\]

Both have degree multiset \((1,1,1,1,2,2,2,3,3)\). Their exact isolation-count variance difference is

\[\operatorname{Var}(I_T(p))-\operatorname{Var}(I_H(p))=-2p^4(1-p)(2p^2-6p+3).\]

Thus \(T\) has smaller variance for \(0<p<(3-\sqrt3)/2\) and larger variance for \((3-\sqrt3)/2<p<1\), despite equal expected isolation counts at every \(p\).

## Assumptions and scope

A habitat network is a finite simple connected undirected tree. Each patch survives independently with the same probability \(p\in(0,1)\). A surviving patch is *isolated* exactly when all of its adjacent patches fail. The statistic \(I_T(p)\) counts such patches, not the total number of connected components, not the largest component, and not the number of originally isolated vertices. The comparison concerns pairs with the same degree multiset. No geographic, ecological, or stochastic dynamics beyond independent survival are assumed.

## Proof

Let \(q=1-p\), let \(d_v\) be the degree of vertex \(v\), and define the isolate indicator \(Y_v=\mathbf1\{v\text{ survives and every neighbor of }v\text{ fails}\}\). Independence gives

\[\mu_T(p)=\mathbb E I_T(p)=p\sum_{v\in V(T)}q^{d_v}.\]

For distinct adjacent vertices, \(\mathbb E[Y_uY_v]=0\). For distinct nonadjacent vertices of a tree, their neighborhoods overlap in exactly one vertex when their distance is two and are disjoint otherwise. Therefore

\[\mathbb E[Y_uY_v]=p^2 q^{d_u+d_v-\mathbf1\{\operatorname{dist}(u,v)=2\}}\quad\text{if }\operatorname{dist}(u,v)\ge2.\]

Define the finite polynomial

\[F_T(q)=\sum_{\{u,v\}:\operatorname{dist}(u,v)\ge2}q^{d_u+d_v-\mathbf1\{\operatorname{dist}(u,v)=2\}}.\]

Summing all second-moment terms gives the exact identity

\[\boxed{\operatorname{Var}(I_T(p))=\mu_T(p)-\mu_T(p)^2+2p^2F_T(1-p).}\]

If two trees have identical degree multisets, their \(\mu\) polynomials agree. Hence their variance difference is exactly \(2p^2(F_T(1-p)-F_H(1-p))\). Because \(2p^2>0\) in the interior, a reversal occurs if and only if \(F_T(q)-F_H(q)\) changes sign on \(0<q<1\).

An exhaustive canonical enumeration of unlabelled trees of orders two through nine yields class counts \((1,1,2,3,6,11,23,47)\). The numbers of unordered nonisomorphic pairs with matching degree multiset, respectively, are \((0,0,0,0,1,5,23,96)\). For each pair, the polynomial \(F_T-F_H\) is computed with exact integer coefficients; all factors vanishing at \(q=0\) or \(q=1\) are removed and Sturm's theorem counts remaining distinct real roots in \((0,1)\) exactly. Orders two through eight have zero interior roots for every pair; at order nine precisely three pairs have one interior root each. Among the ninety-six order-nine pairs, exactly one has identical variance curves and ninety-five have nonzero differences. The certificate reports every crossing pair and its factorization.

For the displayed pair, exact pair-counting gives

\[F_T(q)-F_H(q)=-q(1-q)^2(2q^2+2q-1).\]

Substitution yields the stated variance difference. The quadratic has exactly one root in the open unit interval, \(p=(3-\sqrt3)/2\), and has opposite signs on either side. This proves the sharp threshold and direction of reversal. The exhaustive finite cutoff is not an infinite-order classification; no assertion about all larger trees is required.

## Verification

Execute `python verify.py` in a directory containing `verify.py`, with `networkx` and `sympy` installed as specified in `requirements.txt`. It prints one exact JSON certificate. The attached `certificate.json` was obtained from that executable. The computation enumerates all unlabelled tree classes, compares degree-matched pairs, and uses exact Sturm root counting. A separate brute-force method enumerates all \(512\) possible survival sets for each displayed tree. At \(p=1/2\), it gives equal means \(3/2\) and variances \(83/64\) and \(85/64\); at \(p=4/5\), it gives equal means \(468/625\) and variances \(351236/390625\) and \(317956/390625\), verifying the reversal directly.

## Relationship to prior work

Callaway, Newman, Strogatz and Watts developed site-percolation robustness theory for random graph degree distributions and the sizes of surviving clusters. Their results do not provide the present finite, degree-matched tree variance classification. Rayfield, Fortin and Fall explain ecological distinctions among habitat-network connectivity metrics; the precise probabilistic isolation variance here is different from their framework. He and Hubbell relate species occupancy patterns and percolation. Previously published mathematical studies of network/component polynomials are important background but do not, from material inspected, imply this sharp isolate-count variance reversal. A different coextinction-variance reversal for bipartite plant–pollinator loss concerns different independent random variables and extinction rules and does not furnish this theorem.

## Limitations

The claim is confined to finite simple tree networks, independently and identically retained patches, and exact variance of the number of singleton *surviving* components. Degree-matching is essential for the mean equality. The classification is exhaustive only through nine vertices. No conclusions for networks with cycles, correlated failures, different patch survivabilities, recovery, dispersal dynamics, or noisy observations are established. A stronger or equivalent result may exist in site-percolation or graph-statistics literature that was not located in this bibliographic inspection. Independent scientific and bibliographic assessment remains outstanding.

## References

1. D. S. Callaway, M. E. J. Newman, S. H. Strogatz, D. J. Watts, “Network robustness and fragility: Percolation on random graphs,” arXiv:cond-mat/0007300, first posted 2000-07-18; *Physical Review Letters* 85 (2000), 5468–5471. https://arxiv.org/abs/cond-mat/0007300
2. B. Rayfield, M.-J. Fortin, A. Fall, “Connectivity for conservation: a framework to classify network measures,” *Ecology* 92 (2011), 847–858. https://doi.org/10.1890/09-2190.1
3. F. He, S. P. Hubbell, “Percolation theory for the distribution and abundance of species,” *Physical Review Letters* 91 (2003), 198103. https://doi.org/10.1103/PhysRevLett.91.198103
