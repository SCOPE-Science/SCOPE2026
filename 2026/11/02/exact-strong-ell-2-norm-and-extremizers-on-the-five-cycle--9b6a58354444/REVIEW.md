# Scientific review

## Correctness — PASS
The finite-ball representation is exact for the five-cycle. Independent row selection reduces the nonlinear \(\ell^2\) norm to 243 finite matrix norms. A standalone rational certificate shows \(\tau I-A^{\mathsf T}A\) positive definite for all 238 nonwinning choices at \(\tau=1463/1000\); the five remaining choices are graph rotations. Their Perron restriction has a characteristic cubic whose root lies strictly above \(\tau\). The positive eigenvector gives active averaging balls and the entire equality class. The proof covers every real input, including zero coordinates and arbitrary signs. No finite sampling is used to infer a statement about an infinite graph family.

## Originality — PASS, with residual priority risk
The October 22, 2014 preprint of Soria–Tradacete studies sharp graph maximal bounds but its inspected scopes and sections do not give this five-cycle strong \(\ell^2\) norm; the 2020 González-Riquelme–Madrid preprint gives strong \(\ell^2\) norms for stars and complete graphs. The closest accessible previous local result concerns the four-cycle and does not imply the five-cycle statement. Published-research semantic searches for the exact fifth-cycle algebraic constant, equivalent spectral formulation, and extremizer geometry found no covering result. Index incompleteness remains a publication-priority risk, not a mathematical proof of novelty.

## Value — PASS
The five-cycle is the smallest noncomplete odd cycle and the first diameter-two odd cycle with three distinct centered ball sizes. Its exact strong-type constant fills a natural gap between the classical complete/star examples and the even four-cycle. The mixed three-scale maximizer and complete classification of alternating two-peak extremizers are structurally informative, not merely a numerical bound for an arbitrary induced subgraph. The finite result does not claim a general cycle theorem.

## Independent verification and limitations
The exhaustive finite certificate is included as `verify_c5.py`, and the proof's determinant and root steps are given in `RESULT.md`. Unindexed equivalent results could exist; general cycles, weights, and other exponents remain outside scope.

Self-review: passed. Independent audit: not yet performed.
