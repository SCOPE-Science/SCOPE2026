# Scientific review

## Correctness — PASS

The exact domination identity is a deterministic minimization fact for caterpillars: support vertices can replace leaves in minimum dominating sets; each intervening degree-two path needs exactly \(\lfloor k/3\rfloor\) additional vertices. The independent geometric-run decomposition has cycle length \(M=K+G+2\), domination reward \(R=1+\lfloor K/3\rfloor\), and spine reward \(C=K+1\). The four independent rational second-moment calculations for the centered rewards give the covariance matrix and positive determinant. Standard renewal-reward random-time CLT and moment convergence apply because cycles have exponential tails and boundary terms have bounded moments. The included verifier exhaustively checks \(1{,}022\) binary words and independently recomputes the centered cycle moments with exact rational arithmetic. Finite checks do not replace the infinite proof.

## Originality — PASS, with priority limitations

The closest primary source is Acan–Hitczenko, arXiv:1406.3958, §§2–3.4. It provides the binary-run bijection, caterpillar structure and diameter, but its §3.4 explicitly defines its purported domination statistic through incidence of every edge (a vertex-cover condition) and uses the distinct gap cost \(\lfloor k/2\rfloor\). The present closed-neighborhood vertex-domination cost \(\lfloor k/3\rfloor\) yields genuinely different linear rates. Baren et al., arXiv:1810.03409, study the correct domination definition on permutation graphs, but the inspected results concern enumerations, extremal sizes and algorithms rather than the random tree submodel's joint Gaussian law. Published semantic searches for exact constants, aliases, renewal representations and implication routes did not find a direct covering result. Earlier implicit presentations remain possible, especially among random-caterpillar generating functions. No uniqueness or independence of priority has been certified.

## Mathematical value — PASS

Ordinary graph domination is a natural optimization statistic relevant to covering a tree's vertex neighborhoods. The exact spine gap formula differs structurally from the well-studied edge-incidence problem, and determines a new first-order density, its variance and an explicit nonzero joint covariance with diameter. The positive limiting correlation \(\sqrt{2/7}\) quantifies global geometry's effect on the size of minimum dominating sets. The computation is not an arbitrary finite invariant or parameter substitution: it requires the nonlinear path optimization and a bivariate regenerative analysis.

## Sources and limitations

Primary full-text comparisons: H. Acan and P. Hitczenko, *On random trees obtained from permutation graphs*, arXiv:1406.3958 (first posted 2014-06-16); T. Baren et al., *On the Domination Number of Permutation Graphs and an Application to Strong Fixed Points*, arXiv:1810.03409 (2018). Additional contextual inspection: S. Janson, *The number of occurrences of patterns in a random tree or forest permutation*, arXiv:2203.04182 (2022). The finding is proved for uniform tree permutation graphs, not arbitrary labeled trees; no local limit theorem or exact all-size joint distribution is asserted. Independent historical-priority review is outstanding.

Self-review: passed. Independent audit: not yet performed.
