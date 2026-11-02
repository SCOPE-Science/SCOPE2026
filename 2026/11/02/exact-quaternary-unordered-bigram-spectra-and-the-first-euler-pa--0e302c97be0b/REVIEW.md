# Scientific review: quaternary unordered-bigram spectra

## Correctness

**PASS.** A ten-coordinate unordered adjacent-pair profile is realized by a linear four-letter word if and only if its associated undirected looped multigraph admits an Euler trail. The proof separately enumerates one-, two-, three- and four-vertex connected supports, and subtracts only the four-odd-degree profiles in the four-active-vertex case. The parity fiber has exactly eight subgraphs of \(K_4\): three matchings, four stars and the complete graph. For matchings, the required even-multiplicity connecting edge is explicitly enforced. The resulting rational function has reduced denominator \((1-z)^{10}(1+z)^4\), nonzero values at both singularities, and the stated asymptotics. Standalone literal-word and independent integer-profile checks match twelve coefficients; finite checks support but do not replace the proof. Boundary \(m\ge1\) and loop degree two are explicit.

## Originality

**PASS, subject to the listed unindexed-specialization risk.** Ye--Elishco's length-limited substring composition model gives a motivating broader readout framework but no exact isolated length-two quaternary image count. Gabrys--Milenkovic retain ordered factors, Gupta--Mahdavifar use all substring lengths over a binary alphabet, and the exact published binary two-multispectrum result is alphabet- and orientation-distinct. Jacquet--Knessl--Szpankowski count cyclic directed Markov types, not undirected open Euler trails. Searches of adjacent-composition, graph-Euler, exact generating-function and initial coefficient aliases did not locate the present rational spectrum. The general Euler-trail theorem itself is not claimed as new. Potential coverage by an older labeled-looped-multigraph table remains a residual risk, not a checked absence.

## Mathematical value

**PASS.** The four-letter alphabet is the smallest where connected unordered-bigram multigraphs can have four odd vertices and hence a genuine parity obstruction to realizability. The result resolves the full all-length observation-space cardinality at that threshold, identifies an exact period-two law and the limiting achievable fraction \(7/8\), and gives the exact largest zero-error code size under a natural limited-composition observation model. The contribution is the motivated all-length classification/enumeration, not a routine finite instance or a restatement of Euler's theorem.

## Literature and limitations

Compared in detail with Z. Ye and O. Elishco (arXiv:2208.14963, Section VIII); R. Gabrys and O. Milenkovic (arXiv:1804.04548, Sections I--II); U. Gupta and H. Mahdavifar (arXiv:2201.09955, Sections I--II); the published exact binary two-multispectrum RESULT.md; and P. Jacquet, C. Knessl and W. Szpankowski (2010, accessible abstract only). This work does not determine individual observation-class sizes, noisy recovery, or larger-alphabet counts. Independently qualified originality remains to be assessed.

Self-review: passed. Independent audit: not yet performed.
