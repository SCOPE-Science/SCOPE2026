# Review: square-root price singularity in resistance-optimal subdivided bicliques

## Correctness — PASS

The theorem covers all integer bipartitions with at least two vertices in each class, all strictly positive edge prices and budgets, and the whole unrestricted edge-conductance simplex. Strict convexity is obtained from the second derivative of the positive-definite trace-inverse after fixing the all-ones eigenvector; injectivity of the edge-weighted Laplacian supplies uniqueness. The four spectral sectors have total dimension equal to the subdivided graph, and direct reciprocal-eigenvalue summation gives the explicit Kirchhoff index. Budget elimination yields the stationarity equation; the same convexity proves it has exactly one positive optimizer. The balanced asymptotic follows from the coefficient ratio, and the critical-window profile follows from a strictly decreasing rational bijection. The standalone verifier independently confirms small full spectra, price optimizers, polynomial identities and limiting comparisons. Finite numerical checks are not the proof of the infinite statements.

## Originality — PASS, with residual coverage risk

Ghosh, Boyd and Saberi's 2006 proceedings article gives general convex conductance allocation, including analytic barbell results; it does not derive the stated two-price edge-subdivided biclique formulas. Yang and Klein's March 7, 2014 arXiv preprint treats unweighted Kirchhoff indices of subdivisions and triangulations, not independently priced conductances or their optimizing singular asymptotics. The exact objects, limiting ratio, order-inverse-size price window, and possible stronger reductions were compared with these sources and indexed related mathematical claims. Generic convexity and unweighted subdivision formulas alone do not imply the priced optimality or limit curve without the weighted decomposition and optimization proved here. Specialized historical or nonindexed treatment might still cover parts of the result; the search does not establish absolute uniqueness.

## Mathematical value — PASS

Private relay vertices on every biclique edge form a standard natural network subdivision. Optimizing total effective resistance under classwise pricing is a meaningful allocation question with a completely explicit objective. The result identifies a nontrivial singular structure: the expensive class remains essential for connectivity at every finite size yet receives an asymptotically vanishing relative conductance, with square-root scaling; the critical window of price asymmetry is exactly inverse-size, not simply a smooth fixed-price perturbation. The exact arbitrary-imbalance formula and balanced crossover give usable test cases for resistance-network design and spectral optimization beyond a routine unweighted index evaluation.

## Limitations and relevant literature

The asymptotics are specific to balanced bipartitions; the finite graph formula covers arbitrary bipartitions of the stated size. The work is not a general theory for every subdivided graph. The closest inspected primary texts are the 2006 Ghosh–Boyd–Saberi proceedings paper and Yang–Klein's arXiv:1403.1851. Broader or uncatalogued weighted-subdivision studies remain a legitimate coverage risk.

Self-review: passed. Independent audit: not yet performed.
