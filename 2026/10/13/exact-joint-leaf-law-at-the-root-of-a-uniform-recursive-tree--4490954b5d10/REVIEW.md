# Self-review

## Correctness — PASS
The root-leaf deletion bijection is exact for every subset of marked root leaf-children. The exceptional all-star term is essential and explicitly included. Reconstructing the falling-factorial transform gives the full bivariate polynomial; differentiation and Eulerian moments give the claimed half-unit covariance and exact correlation. The 1-dependent Eulerian-descent central limit theorem together with summable factorial transforms proves independent Poisson/Gaussian limits. Independent exhaustive tree enumeration in `verify.py` supports, but does not replace, the infinite proof. The bound is for uniform recursive trees, with the deterministic two-vertex case excluded from the covariance and correlation statements.

## Originality — PASS, with historical-priority uncertainty
Devroye and Janson, *Protected nodes and fringe subtrees in some random trees* (arXiv:1310.0665v1), Section 7, identify the number of root leaf-children in a continuous-time Yule tree by thinning, without coupling it to global leaf number in a fixed-size recursive tree. Mahmoud and Ward, *Asymptotic properties of protected nodes in random recursive trees* (2015), instead study the number of protected vertices. Janson's degree-frequency results concern global outdegrees, not the stated root-specific mixed polynomial. Existing individual marginal distributions, as well as the root-degree/leaf covariance, are not sufficient to determine the bivariate transform. The author's hosted full copy of Janson's 2004/05 degree paper was inaccessible through repeated fetch timeouts; a broader classical increasing-tree polynomial may contain an indirect specialization. Priority is provisional; no global uniqueness or independent confirmation is represented.

## Mathematical value — PASS
Root singletons and total tree leaves quantify local versus global terminal branching. The result gives a complete exact joint law for every tree order, a nonzero constant covariance, an exact decaying correlation, and an independent mixed limit. These findings distinguish the different scales of root-neighborhood and whole-tree fluctuations; they are more than a recomputation of the known marginal Eulerian and Poisson laws.

## Verification scope and limitations
Exact enumeration covers all 46,233 trees with orders 2 through 9, with all joint coefficients and factorial transforms checked. Higher orders and the distributional limit are established analytically rather than enumerated. No analogous result is claimed for alternative recursive-tree models. Full priority assurance requires additional independent literature assessment.

Self-review: passed. Independent audit: not yet performed.
