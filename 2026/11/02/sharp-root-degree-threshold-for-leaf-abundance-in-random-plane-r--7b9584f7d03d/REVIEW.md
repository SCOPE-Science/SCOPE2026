# Self-review

## Correctness — PASS

For \(n\ge3\) and the full support \(1\le r\le n-1\), the coefficient proof derives the conditional leaf mean from the bivariate increasing-plane-tree EGF and Lagrange inversion. Positivity of every denominator and endpoint \(r=n-1\) are explicit; direct rational differences prove strict regression monotonicity and the perfect-square zero classification. A separate tree-growth conditional covariance recursion telescopes to the exact finite expression. The indicated second moments verify the correlation asymptotic. The packaged standard-library verifier returned 7,374 exact assertions after separate exact small-tree enumeration and full-support dynamic programming to 60 vertices. Enumeration alone is not asserted to prove the infinite statement.

## Originality — PASS, with historical-priority risk

The nearest explicitly inspected primary literature is Mahmoud–Smythe–Szymański (1993), whose Sections 2–3 establish marginal root-degree and leaf statistics; Janson (2008) supplies the Stirling-permutation duality (top-level components versus plateaux), but analyzes a different triple of statistics; and Acan–Hitczenko (2014), who analyze asymptotic covariance matrices for counts of outdegree classes. Kuba–Panholzer (2006) give degree-distribution generating functions. None of the examined substantive statements implies the exact mixed conditional regression without further analysis. Searches of the semantic findings database for the conditional law and aliases primarily returned a result for the *uniform-parent* recursive tree, which is a different random model and has a bounded covariance. Existing increasing-tree constructions and marginal moments are credited, not presented as novel. The precise theorem might still follow implicitly from an uninspected multivariate result; a search is not an absolute priority certificate.

## Mathematical value — PASS

The distinguished root's degree is a natural hub statistic in the plane recursive tree, while leaves measure global branching. The all-size regression identifies which observed root degrees predict an excess or deficit of leaves, with a sharp square-root boundary and exact neutral cases, and relates a growing covariance to a vanishing correlation. Its joint-dependence information is not determined by individual marginals and is useful for finite-sample conditioning in this classical probability model. The finite classification is structural, not an arbitrary computation or tiny numerical refinement.

## Scope, evidence, and limitations

The tree model, definitions and all integer endpoints are specified in `RESULT.md`; `verify.py` checks the displayed quantities. The included checks are self-contained finite diagnostics but do not constitute an external audit. Relevant implicit historical coverage remains the principal originality uncertainty. No full conditional distribution or theorem for other attachment kernels is asserted.

Self-review: passed. Independent audit: not yet performed.
