# Scientific review

## Correctness — PASS

The Poisson score information factorization and exact determinant are derived from independent mean-gradient rows, not inferred from simulation. At fixed total exposure the exposure product has its unique maximum at equal allocations. The D- and c-objective logarithmic derivatives are strictly decreasing over every positive spacing and have opposite endpoint signs, establishing unique global maxima and the strict separator \(t_C<1<t_D\). Implicit background monotonicity and the positive Lambert \(W\) asymptotic are reconstructed with all boundary assumptions. The standard-library verification checks 16,105 independent numerical or exact-arithmetic assertions. These finite checks are not substituted for the continuum proof.

## Originality — PASS, qualified by priority risk

Guestrin–Krause–Singh (2005, https://doi.org/10.1145/1102351.1102385) concern covariance-based Gaussian-process mutual-information placement, not nuisance-parameter Poisson determinants. Jones–Goldstein–Jonathan–Randell (2015, https://www.lancaster.ac.uk/~jonathan/JGJR15_OptDsg.pdf) explicitly describe Gaussian atmospheric plumes and optimal environmental sensing, but in a Gaussian-data Bayesian design setting. Gallatin–Berglund (2012, https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=910609) analytically optimize Poisson localization for a known Gaussian intensity profile, without the two positive unknown nuisances; their one-parameter result cannot by itself imply the full determinant optimum. Battistelli et al. (2015, university open-access PDF cited in RESULT.md) concern PDE/Kalman source reconstruction, not this symmetric static three-count optimization. Direct published-finding corpus and open-literature searches using Gaussian source, Poisson Fisher, background, D-optimality and three-site variants found no equivalent analytic classification. The closest topical plume information source, Ristic–Gunatilaka–Gailis (2015, https://doi.org/10.1016/j.inffus.2014.10.007), uses binary sensors; its full manuscript was inaccessible and remains an explicit historical-priority risk. The claim of originality is best-knowledge, not independently verified.

## Value — PASS

The result is an exact and natural design tradeoff rather than a bare finite calculation: optimizing joint source localization, strength and ambient counts always requires a wider transect than center localization after equal exposure allocation, and the full-parameter spacing diverges as background vanishes while center-only spacing remains bounded. The all-positive-background classification and asymptotics identify when changing the scientific objective radically changes hardware placement. No unrestricted optimality, field validation or non-Gaussian transport prediction is claimed.

## Verification and limitations

The six-file statement is accompanied by a runnable deterministic standard-library checker. It verifies the stated finite examples and matrix algebra while the analytic inequalities carry the uncountable domain. The expected successful output is `VERIFY_OK assertions=16105`. The comparison with the unavailable binary-sensor manuscript and possibly uncatalogued equivalent formulations is an unresolved historical limitation; independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
