# Four pairs are the sharp separation threshold for Nash-welfare and egalitarian stable matching

## Finding
For every complete strict two-sided stable-marriage instance with \(n\le3\) agents on each side, the set \(\mathcal N\) of Nash-product-optimal stable matchings is contained in the set \(\mathcal E\) of egalitarian (minimum-rank-sum) stable matchings. For \(n=3\), exactly \(43{,}728\) of \(46{,}656\) labeled profiles give \(\mathcal N=\mathcal E\); exactly \(2{,}928\) give the proper inclusion \(\mathcal N\subsetneq\mathcal E\). There is a complete strict \(4\)-by-\(4\) instance with \(\mathcal N\cap\mathcal E=\varnothing\). Hence four matched pairs are the sharp first size where maximizing rank-induced Nash welfare can require a strictly worse egalitarian rank total.

## Assumptions and scope
There are \(n\) agents in each of two named groups. Every agent strictly ranks every member of the other group, with rank \(r\in\{0,\ldots,n-1\}\). For a perfect matching \(\mu\), define the egalitarian cost \(E(\mu)=\sum_a r_a(\mu(a))\) and the Nash utility product \(N(\mu)=\prod_a (n-r_a(\mu(a)))\). Maximizing the geometric mean is equivalent to maximizing this positive integer product. A matching is stable if no unmatched pair strictly prefers one another to their existing partners. Sets \(\mathcal E\) and \(\mathcal N\) minimize \(E\) and maximize \(N\), respectively, over all stable matchings; ties are retained. All statements include every strict, complete labeled profile, without stochastic assumptions.

## Proof
For \(n\in\{1,2,3\}\), enumerate the \((n!)^{2n}\) profiles by choosing one permutation of the opposite side for each of the \(2n\) agents. For each profile enumerate all \(n!\) bijections. For each bijection and each unmatched pair, test the two strict preference inequalities; retain precisely those bijections with no blocking pair. Calculate \(E\) and \(N\) with integer arithmetic and compute the full two arg-optimum sets. This is finite exhaustive proof, not a random sample or asymptotic extrapolation. The attached independent executable specification `stable_welfare_boundary_check.py` implements these definitions directly, asserts \(\mathcal N\subseteq\mathcal E\) for **every** profile through \(n=3\), and tests the exact counts. For \(n=1\), the only profile gives equality. For \(n=2\), all \(16\) profiles give equality: \(14\) have one stable matching and \(2\) have two.

For \(n=3\), the exact exhaustive partition by number of stable matchings and optimum relation is:

| Number of stable matchings | Equal optimum sets | Proper Nash-set inclusion |
| --- | ---: | ---: |
| 1 | 34,080 | 0 |
| 2 | 9,180 | 2,304 |
| 3 | 468 | 624 |

The counts sum to \(46{,}656=6^6\). This proves the universal inclusion and the exact labeled-profile census.

For sharpness, set \(n=4\). Give the four agents on the first side the following rank vectors over agents \(0,1,2,3\) on the second side, in order:

`(2,3,0,1); (0,3,2,1); (1,2,3,0); (3,0,1,2)`.

Give the four agents on the second side the following rank vectors over agents \(0,1,2,3\) on the first side:

`(0,1,3,2); (0,1,2,3); (3,1,0,2); (3,1,2,0)`.

Every vector is a permutation of \(0,1,2,3\), so these are admissible strict complete preferences. Represent a perfect matching by its four second-side partners, in first-side order. Checking the \(24\) bijections against the blocking-pair criterion leaves **exactly** four stable matchings, with respective \((E,N)\) values:

| Matching | Egalitarian cost | Nash product |
| --- | ---: | ---: |
| `(0,1,2,3)` | 11 | 768 |
| `(0,2,1,3)` | 11 | 1,536 |
| `(0,3,1,2)` | 11 | 1,728 |
| `(2,0,3,1)` | 9 | 1,536 |

Thus the unique egalitarian optimum is `(2,0,3,1)`, whereas the unique Nash optimum is `(0,3,1,2)`. Their disjointness completes the sharpness proof.

## Verification
Run `python stable_welfare_boundary_check.py` with Python 3. The code is self-contained and imports only standard-library modules. It exhausts the \(1\), \(16\) and \(46{,}656\) strict-profile spaces at \(n=1,2,3\), tests Nash-optimum inclusion on every profile, records the complete \(n=3\) frequency table above, and recomputes all four stable matchings and their objective values for the \(n=4\) witness. All compared quantities are exact integers. This does **not** enumerate arbitrary markets with more than three pairs and does not claim such an enumeration.

## Relationship to prior work
Desai, Rasheed, Ghalme and Gujar (2026) introduced an algorithm to optimize rank-induced Nash social welfare among stable matchings and empirically compared it with egalitarian and other criteria. Their identified results do not state the sharp four-pair separation threshold or the exact three-pair inclusion census. Earlier standard stable-marriage results provide the stability lattice and egalitarian objective, but not this pair of finite-set assertions. Related exact studies on the first divergence of egalitarian from *minimum-regret*, *sex-equal*, and *rank-maximal* criteria consider different objectives and do not logically imply the Nash-product inclusion. The result is specific to utilities \(u=n-r\); replacing this cardinalization need not preserve the assertion.

## Limitations
The positive theorem is restricted to \(n\le3\), with a concrete negative witness at \(n=4\). It neither computes the proportion of failures for all \(n=4\) profiles nor establishes any large-market approximation guarantee. The finite exhaustive checker supplies a transparent, reproducible certificate for the small universal statement; no formal independent external proof audit has been performed. Historical priority remains subject to broader literature review, especially work on utility products and stable-marriage fairness.

## References
1. Parth Desai, Rasheed M., Ganesh Sambhaji Ghalme and Sujit Gujar, *Fair Stable Matching: A Nash Social Welfare Approach*, arXiv:2609.02354v1, first posted 2026-09-02, https://arxiv.org/abs/2609.02354 .
2. D. Gale and L. S. Shapley (1962), *College Admissions and the Stability of Marriage*, American Mathematical Monthly 69, 9–15.
3. R. W. Irving, P. Leather and D. Gusfield (1987), *An Efficient Algorithm for the “Optimal” Stable Marriage*, Journal of the ACM 34, 532–543.
