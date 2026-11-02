# Scientific review — Two-site memory placement on a weighted ten-state ring

## Correctness: PASS

The claim is quantified over all positive length-one and length-three transition rates and all unordered pairs of distinct sites. The uniform stationary law follows from symmetric rates; irreducibility follows from the length-one edges. For each pair, the integrated equilibrium autocovariance is the quadratic form of the inverse of the graph Laplacian restricted to constants' orthogonal complement. The proof derives its exact normalization by Fourier eigenvectors and the rank-one-regularized Green matrix. Five explicit rational functions exhaust all pair geometries. Every denominator is positive, and ten exact pairwise differences factor into positive-coefficient numerators or factors with only the three stated positive crossover roots. Thus the exhaustive global rankings follow from algebra, not parameter samples. The included standalone checker independently reproduces all rational forms and pairwise identities; finite spectral samples are supplemental.

## Originality: PASS (best-knowledge, with stated risk)

Chen and Limmer (2026), arXiv:2608.23764, supply the general integrated-autocovariance susceptibility and the ten-state first/third-neighbor ring with a two-site observable. The supporting material inspected (notably Sections II–IV and equations S.39–S.75) does not provide the weighted homogeneous-ring all-pair placement order, its exact three rate-ratio thresholds or the sharp readout optimum. The general circulant resistance-distance method of Zhang and Yang (2007), DOI:10.1002/qua.21068, is prior mathematical infrastructure; its publisher abstract does not assert the present parameter-dependent ordering. Separate published research-record searches for the precise network, alternative Green/resistance formulations, autocorrelation readout and placement extremality surfaced no statement implying the complete classification. In particular, general Green-kernel identities require a separate sign and crossover analysis to establish this ordering. **Limitation:** the complete Zhang–Yang paper was inaccessible through available lawful routes, so a hidden weighted-graph special case cannot be excluded; general spectral formulae and unlocated stronger results remain subsumption risks. This is a qualified original-claim assessment, not a uniqueness certificate.

## Value: PASS

The motivating 2026 model directly uses a ten-state ring with ±1/±3 links and a two-site binary output to analyze a thermodynamic lag-error bound. Holding output mean and variance fixed, the current theorem gives the complete geometry-dependent memory susceptibility at every relative edge rate. It identifies which readout placement maximizes or minimizes the observable's memory and two otherwise hidden secondary ranking reversals. These are sharp, model-specific design distinctions that the general susceptibility identity alone does not report. Their significance is restricted to this actual test-network topology and stationary memory: the result does not imply guaranteed error or dissipation improvements for arbitrary input protocols.

## Closest literature and limitations

- Chen and Limmer, *Entropy Production Bounds the Accuracy of Computation in Markov Networks*, arXiv:2608.23764 (posted 2026-08-24), especially supporting Sections II–IV, establishes the susceptibility and graph topology but not the proved geometry ranking.
- Zhang and Yang, *Resistance distance and Kirchhoff index in circulant graphs*, DOI:10.1002/qua.21068 (2007), establishes general spectral resistance methodology; full text was not accessible and remains a residual originality risk.
- MathWorld, *Resistance Distance*, records the general Green-matrix/effective-resistance identity.

All comparisons concern the actual claim and its logical implications. The result is a conditional mathematical statement for a specified homogeneous ten-state network, not for arbitrary finite Markov networks or arbitrary observables.

Self-review: passed. Independent audit: not yet performed.
