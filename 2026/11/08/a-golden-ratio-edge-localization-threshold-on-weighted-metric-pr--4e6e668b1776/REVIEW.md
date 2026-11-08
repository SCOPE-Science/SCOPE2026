# Scientific review — weighted metric prism embedding

## Correctness (PASS)

The claim concerns all integers \(n\ge3\) and every positive rung length \(h\), with unit rail edges, standard metric-graph continuity, unnormalized arclength mean zero, and real first-order derivative energy. The analytical proof determines the centered Poisson representer, obtains the exact edgewise evaluation-diagonal quadratic from the weighted vertex Laplacian, and checks the spectral constants separately for rung and rail edges. Both quadratic coefficients are strictly positive; the difference of their midpoint values is strictly increasing with rung length. The monotonicity proof uses two explicit Fourier modes with \(1-\cos(2\pi k/n)\ge1\). The unique crossover, edge classification, rank monotonicity, golden-ratio limit, first correction, and equality functions follow without extrapolation from experiments. A a separately formulated refined-graph Poisson solver reproduced the closed diagonal at 60 rational test evaluations; the universal proof does not rely on those finite cases.

## Originality (PASS, with bibliographic risk)

The underlying Green-function/effective-resistance identities are standard, as detailed by Baker–Faber (arXiv:math/0407428, §§3–6). Cinkir's 2015 open-ladder article (arXiv:1503.06353, §§1–2) concerns unit edges and nonperiodic ends; Cinkir's 2017 complete prism analysis (arXiv:1704.03429, §§1–3) concerns the equilateral prism and computes discrete vertex resistances and its Kirchhoff index. Usman's 2018 article (doi:10.1186/s13660-018-1872-y, §§1–2) establishes general Sobolev-type inequalities without this sharp endpoint or localization result. These works provide methods and special cases, not the weighted continuous embedding optimization and strict one-threshold/golden-ratio classification. Searches for weighted circular-ladder/prism sharp Sobolev evaluations, metric-graph Green diagonals, and equivalent sharp resistance formulations did not reveal a stronger covering statement. The same problem may be implicit in a more general unindexed weighted-graph treatment; a negative search cannot eliminate that risk.

## Value (PASS)

The precise question is the sharp uniform control of point evaluation by energy on an entire natural one-parameter family of cyclic metric networks. Its answer distinguishes the geometry of rail and rung observations, shows a unique length-driven change of all extremizer locations, and proves that the critical rung length decreases strictly with circumference to an explicit golden-ratio limit with the first finite-size term. The exact quadratic deficit controls displacement from every midpoint and the suboptimality of the competing edge orbit. The dimension-four cube tie and the unexpectedly elementary sharp branch in the rung-dominant regime supply structural checks and useful benchmarks for weighted quantum-graph interpolation. No claim is made about irregular weights or higher-order energies.

## Closest literature and limits

The most direct prior comparison is the full arXiv text of Cinkir (2017), which explicitly imposes edge length one and analyzes vertex resistances/Kirchhoff indices; the new claim depends on continuously variable rung lengths and continuum interior-point evaluation. Baker–Faber's general metric-graph calculus is an antecedent rather than novelty. The exact result remains conditional on the stated uniform-rung/rail structure, and publication priority is subject to further independent bibliographic review.

Self-review: passed. Independent audit: not yet performed.
