# Self-review

## Correctness — PASS
The identity and doubling inverse branches give an exact four-dimensional invariant space of piecewise-affine signed densities. The starting signed density representing \(X_0\) lies in that space. Exact matrix integration gives all lags; direct symbolic matrix elimination yields the stated rational covariance transform, and the explicitly factored eigenvalues give the near-identity crossover. The checker verifies 259 finite, exact-rational cases. The analytic proof supplies the infinite conclusions. The stationary density is independently documented in the primary source.

## Originality — PASS within inspected sources
The 2021 primary paper and 2023 open-access thesis analyze existence and explicit stationary density for this random map. The thesis' full Section 4.4 was inspected, including definitions (4.5), density (4.6), proof, and handoff to a different map in Section 4.5. It does not report the all-lag coordinate covariance, the affine-density four-state transfer formula, or the singular crossover \(e^{-2u/3}/48\). Searches comparing the specific map, covariance rationality, and near-identity crossover with available published mathematical records found related but non-covering work on random expanding circle maps and covariance spectra. The finite-state *constant-density* computation in the source cannot by itself evaluate the coordinate two-time correlation, which needs linear-density information. Residual risk: an alternate exact autocovariance calculation elsewhere may exist and requires independent publication-priority checking.

## Mathematical value — PASS
The source presents a random system whose stationary density exists for every parameter below the deterministic identity endpoint, but the density does not quantify temporal relaxation. The exact covariance identifies three distinct dynamical spectral scales for an original, physically measured coordinate, while its near-endpoint crossover gives a sharp slowing constant \(2/3\) and the selected limiting variance \(1/48\). Both the full sequence and singular scaling answer natural quantitative questions for the motivating model; the result is not a re-expression of the known density formula.

## Scope and limitations
Stationary, annealed coordinate covariance only; no general-observable/quenched mixing assertion and no uniqueness of the invariant law at the deterministic boundary. Literature-search incompleteness remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
