# Independent mathematical audit

## correctness

PASS

For an induced subforest of tree T, the component count is the exact Bernoulli polynomial C=S-E, with S retained vertices and E retained edges. E[C] and Var(C) involve n,m=n-1 and wedge count W=Σ_v binom(deg(v),2), fixed by degree multiset. In E[C^3], terms with at most two distinct edges cancel under degree matching. Among three-edge sets, only 3-edge paths L(T)=Σ_{uv edge}(deg u-1)(deg v-1) are not degree-determined once star, wedge+disjoint, and disjoint counts are related. The difference κ3(C_T)-κ3(C_U)=-6(L(T)-L(U))p^4(1-p)^2 follows for all n,p, not a finite extrapolation. For PGF difference, terms with <=3 survivors yield p^4, <=1 removed yield (1-p)^2, empty survivor gives z and matching first two factorial moments give (z-1)^3, hence full integer polynomial divisibility. For n<=5 degrees determine trees; at n=6 only the degree class (3,2,2,1,1,1) has two trees. Independent direct enumeration of 64 retained subsets for arm lengths (3,1,1) vs (2,2,1) yields signed size-4 counts (-1,3,-3,1), so H_A-H_B=p^4(1-p)^2 z(z-1)^3 and Δκ3=+6p^4(1-p)^2.

## originality

PASS

Tittmann–Averbouch–Makowsky already introduced the universal induced-subgraph component polynomial; our H_T is a specialization and that general framework is NOT new. Their inspected introductory, structural and random-subgraph sections do not state the exact degree-matched tree third-cumulant formula or sharp six-vertex pair. Liao–Hou studies a P4-sensitive coefficient in a different regular bipartite graph context. A general graph-component polynomial formula could mechanically yield the tree identity with additional combinatorial extraction, and this implication risk remains noted.

## value

PASS

Degree-multiset summaries and variance cannot detect habitat fragmentation differences induced by tree arrangement; the exact third-cumulant obstruction identifies the first arrangement-sensitive invariant and its uniform p dependence, while the six-vertex pair is sharp. This is a natural component-count and degree-identification question in network reliability and ecological habitat modeling, beyond a table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
