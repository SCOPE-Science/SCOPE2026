# Independent mathematical audit — Zero-residual false positives in projected certification of constrained extremal eigenpairs

Audit date: 2026-10-01 (UTC) UTC
Disposition: passed

## Correctness
for H=diag(0,0,M), A=(1,0,0), and positive penalty rho, the constrained maximum is M on e3 while e2 is a feasible non-dominant eigenvector. At e2 the penalized eigen-residual, projected feasibility residual, projected KKT residual, and repeated outer Rayleigh change are all exactly zero, while the extremal error equals M. A nearby feasible vector with e3 component delta has residual M delta sqrt(1-delta squared) and error tending to M. Independent numerical algebra at M=7, rho=0.3 reproduced these identities.

## Originality
the primary Wang–Xia paper was inspected through its full HTML text. Its projected certification explicitly accepts when the four residual tests pass, while its algorithm permits an arbitrary unit start; it does not include an extremal-index enclosure in the stopping test. Resultary searches found the present counterexample and later follow-up work but no earlier source stating this zero-residual PSM failure.

### equivalent_formulations
The exact PSM-specific zero-residual false certificate is the pertinent equivalent statement.

Searches: Resultary: PSM projected certification residual extremal eigenpair zero residual false positive; Wang–Xia arXiv:2609.18538; Split–Merge arXiv:2501.15131

Evidence: The primary PSM full text was inspected at its projected residual definitions and Algorithm 1; the counterexample shows those tests certify stationarity but not the requested spectral index.

### broader_coverage
General prior principles motivate the failure but do not cover the specific interface/certificate claim.

Searches: Parlett Lanczos misconvergence; van Dorsselaer–Hochstenbach–van der Vorst 2001; Resultary PSM residual search

Evidence: Classical literature says small Ritz residual need not identify an extreme eigenvalue, but it does not instantiate the PSM projected stopping suite or the penalty-duality repair.

### exact_database_or_table
Database/table comparison is specifically inapplicable.

Searches: Resultary constrained eigenvalue certification

Evidence: No exact database/table is relevant; the counterexample is symbolic for every M≥1.

### claim_vs_prior_implication
The PSM-specific statement is not itself stated by the prior sources, although it uses a classical spectral-index principle.

Searches: Wang–Xia Algorithm 1 and equations defining four stopping tests; Split–Merge dominant-overlap condition

Evidence: The source algorithm permits an arbitrary unit initial vector, while the inner convergence guarantee assumes dominant overlap; the e2 construction exploits that documented gap.

### Source inspections
- **Wang and Xia, The Projected Hessian Quantification Theorem: An Exact Duality for Constrained Eigenvalues** — Primary full HTML inspected, especially Sections 4.1–4.4: equations (27), (33), (34) and Algorithm 1 show the residual acceptance suite and arbitrary unit initialization. Assessment: Compared against the final statement and implication scope.
- **Resultary search** — Searched PSM certification, residual, extremal index, and false-positive formulations; no prior covering result was found. Assessment: Compared against the final statement and implication scope.

## Scientific value
an exact counterexample to the stopping certificate of a newly proposed extremal-eigenpair method is a motivated boundary result. The accompanying extremality-bracket repair isolates what the residual suite does and does not certify.

## Reproducibility
Independent algebra at M=7 and rho=0.3 gives zero inner and projected KKT residuals at e2, constrained-value error 7, and for delta=1e-8 residual 6.999999999999999e-8, matching M delta sqrt(1-delta squared).

## Limitations and residual risks
The exact trajectory uses an initialization orthogonal to the desired dominant eigenvector, a measure-zero event under an absolutely continuous random start. The result establishes deterministic certification failure and a residual-versus-extremality obstruction; it does not dispute projected-Hessian penalty duality or prove positive-probability failure under randomized initialization.
- The exact bad initialization is nongeneric under randomized starts.
- A future revision of the source method could add a dominance certificate and remove this failure mode.
