# Scientific assessment

## Correctness (C): PASS

The claimed domain is all indexed binary prefix-normal words containing exactly seven ones. The gap criterion reduces the original definition to nine explicitly listed linear inequalities in five nonnegative offsets, plus a positive minimum gap and an arbitrary trailing-zero count. Every extremal ray of the resulting pointed five-dimensional rational cone is captured by a four-facet determinant, and the exact computation finds thirteen. Standard half-open triangulation makes the product of all primitive ray denominators a valid coefficient denominator with numerator degree at most 39. Exact integer enumeration of cone points through degree 39 establishes the numerator identity at every required coefficient. Thus the formula holds to infinite length, independently of the supplemental direct word checks at lengths 7–18. The cyclotomic pole calculations prove least quasiperiod 12; the singularity at one gives the leading coefficient. Risk: the argument relies on the familiar cone lattice-point triangulation theorem and on correct interpretation of all gap inequalities, both explicitly stated and independently testable in the included verifier.

## Originality (O): PASS, with residual priority risk

The 2016 source arXiv:1611.09017 states general rationality and explicitly displays fixed-density generating functions for densities at most six, while saying the authors could not compute beyond that range. Its general theorem does not imply the displayed new rational function's coefficients, pole cancellations, exact least quasiperiod or leading asymptotic without new calculation. arXiv:2003.03222 addresses enumeration by Gray codes, not a fixed-density-seven generating-function identity. arXiv:2005.09281 studies weighted generalizations rather than the particular binary fixed-density-seven length count. Direct literature and published-results searches under fixed-density, seven ones, prefix normal and rational generating function aliases yielded no equivalent formula. An unindexed earlier result, including a differently normalized Hilbert-series expression, remains possible. No search exhaustiveness or independent novelty certification is asserted.

## Mathematical value (V): PASS

The motivating paper explicitly stops its exact fixed-density computations at six. The first next case is a natural and motivated finite-rank enumeration problem, not an arbitrary numerical slice. The thirteen-ray Hilbert-series decomposition yields a compact exact function for every length and the least quasiperiod and asymptotic constant, revealing nontrivial cancellation compared with the coarse polyhedral denominator. It is independently usable for coefficient extraction and asymptotic analysis. The work does not claim a general density-uniform theory, and such a downstream result is not required for this exact natural invariant.

## Limits and closest literature

The primary priority comparison is Burcsi–Fici–Lipták–Ruskey–Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017, fixed-density section and gap lemma. Additional material examined: arXiv:2003.03222 and arXiv:2005.09281. Computational witnesses are finite, but all necessary polynomial coefficients are exhaustively checked under a proven degree bound. Independent peer assessment and exhaustive bibliographic indexing remain outstanding.

Self-review: passed. Independent audit: not yet performed.
