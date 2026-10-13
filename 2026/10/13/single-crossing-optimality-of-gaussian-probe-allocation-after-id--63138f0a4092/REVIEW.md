# Scientific review

## Correctness — PASS

The estimator is unbiased under independent standard real Gaussian probes. Using \(\operatorname{Var}(g^2)=2\) gives its exact MSE. The rank budget exposes consecutive blocks of \(m\) monotonically increasing squared logarithmic eigenvalues as the number of probes grows. Direct subtraction yields \(F_{N+1}-F_N=2H_N/[N(N+1)]\) and \(H_{N+1}-H_N=(N+1)(c_{N+2}-c_{N+1})\ge0\). This proves the single-crossing, global allocation rule and all ties. Exact finite geometric sums yield the sharp spectral threshold. The standalone exact-rational program replays the identities and geometric cases; it is a check, not a proof of infinitely many parameter choices.

## Originality — PASS, with residual risk

The closest literature is Cortinovis and Toni (2026), equations (14)–(15), whose **pointwise** exact MSE and pairwise comparison are essential known inputs. The finding does not claim those formulas as new. The source does not state or prove the one-crossing property across *all* integer allocations, reduction of global one-probe optimality to a *single* adjacent comparison, or the geometric-log-spectrum boundary and exact limiting optimal count. The general pairwise inequality can be applied exhaustively to all allocations; this could reduce the practical novelty, and an equivalent global monotonicity observation might already exist. Hutch++ addresses different worst-case trace-query guarantees, not this exact spectral allocation problem. These comparisons were made at statement/implication level, not on title matching alone.

## Value — PASS

The motivating 2026 article develops a one-probe strategy and an adaptive fallback for slowly decaying spectra. The new global single-crossing criterion completely characterizes, within the paper's idealized model, when *one* probe beats **every** possible larger probe budget. It collapses an unstructured multiway comparison to one adjacent comparison and gives a sharp geometric-spectrum regime and explicit contrasting flat-spectrum regime. The statement is exact for every ordered positive-semidefinite spectrum, including ties and nondivisible budgets; it is not a parameter substitution or one isolated numerical counterexample. It is a theoretical benchmark rather than an immediately computable oracle-free stopping rule.

## Sources and limits

Primary source: Cortinovis and Toni, arXiv:2601.05778 (first public 2026-01-09), published full text DOI 10.1002/nla.70106, Sections 2 and 4. Context: Meyer, Musco, Musco and Woodruff, *Hutch++*, SOSA 2021. Residual originality risk: a similar global allocation rule under alternative deflation or experimental-design terminology. Model limits: ideal eigenpairs, exact quadratic forms, Gaussian probes, and nominal linear matvec costs, not actual randomized Nyström or inexact Lanczos execution time.

Self-review: passed. Independent audit: not yet performed.
