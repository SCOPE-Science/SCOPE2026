# Scientific review: joint Gaussian arrivals and discoveries

## Correctness — PASS

The complete-graph walk admits an exact Markov projection onto graph size and number visited: births add an unvisited vertex at rate \(\beta\), and each move discovers a vertex at rate \(\lambda(N-X)/(N-1)\). The imbalance \(R=(X-1)-\alpha(N-1)\), \(\alpha=\lambda/(\beta+\lambda)\), has the exact contracting drift \(-\lambda R/(N-1)\). Its second-moment bound yields the discovery law of large numbers and the predictable-bracket limits. The martingale functional CLT and a small-time cutoff in the linear integral equation produce two Gaussian stochastic integrals, whose covariance integrals simplify to the stated matrix. The embedded checker independently exercises the finite Markov reduction, generator identities and algebra with 9,369 exact rational checks. The checker is finite corroboration, not an infinite proof.

## Originality — PASS, with access qualifications

The nearest specific source is Demirci–Işlak–Yıldız, arXiv:2110.01083, version 2: it proves fluctuation results under deterministic integer-time vertex births and remarks that random generation times could be treated, but its inspected text does not state the joint Poisson birth/discovery covariance. Videla (2020) studies growing-graph knowledge processes; its full paper was not accessible, so a stronger theorem there remains a live priority risk. Kijima–Shimizu–Shiraga (2025) studies deterministically varying vertex numbers and a different asymptotic regime. Searches of published mathematical result records and prior claims found no statement that dominates this specific joint Gaussian law. A failed search is not proof of universal novelty; conclusions are conditional on these access limits.

## Value — PASS

The 2021 source explicitly motivates Poisson vertex arrivals as a natural model variation. Moving from deterministic births to stochastic births changes not merely a proof technicality but the limiting distribution: birth noise creates a nonzero discovery/birth covariance and a different discovery variance. The exact, simple two-parameter covariance matrix gives quantitative control of these fluctuations and can be used for statistical uncertainty of network exploration. The result concerns a natural stochastic-growth model, not an arbitrary parameter slice.

## Limitations and nearest literature

Fixed strictly positive birth and jump intensities, one walker, no graph deletions, and complete graphs are essential assumptions. No rates of Gaussian approximation are established. The full Videla (2020) text, early versions of arXiv:2110.01083 and any inaccessible broader general limit theorem remain historical-priority risks. Self-review does not constitute independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
