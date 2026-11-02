# Scientific review: exact ternary ordered-bigram multispectrum counts

## Correctness — PASS

The theorem applies to every length-\(m+1\) ternary word with \(m\ge1\). The exact directed Eulerian trail criterion handles weak connectivity of active vertices and distinguishes zero degree imbalance from six ordered unit-imbalance vectors. Three separate balanced support cases and the precise exceptional disconnected endpoint case are enumerated without double counting. The resulting rational function was expanded and its first ten coefficients checked both by literal enumeration of words and enumeration of admissible arc matrices. The formal-series pole analysis proves the quasipolynomial and asymptotic statements. The standalone verifier checks 265,716 words and all integer nine-vector candidates through total degree ten; finite verification is corroborative, not an all-length proof. One-letter words are explicitly outside the series.

## Originality — PASS, subject to the stated residual risk

The closest checked work studies general substring reconstruction, multistring reconstruction, and equality of substring *sets*; these do not state or imply an exact generating function for all ternary ordered-bigram *multisets*. A closely related exact **binary** bigram-multispectrum classification counts a different alphabet domain and does not imply the ternary three-by-three Eulerian-flow enumeration. A ternary window-two DNA-profile result concerns realizable rankings and shortest realizing length, not the number of realizable integer profiles of each total weight. The all-length coefficient sequence and polynomial-degree-six constant were not identified in the checked comparisons. Residual risk: older work on directed multigraph flows, Eulerian matrix enumeration, or genomic two-gram spectra might contain an equivalent algebraic specialization.

## Mathematical value — PASS

The alphabet-three case is the first genuinely three-cycle setting, unlike the binary two-vertex graph. The theorem solves the exact number of distinguishable observations for a basic lossless overlapping-bigram sequencing model, across every source length, and exhibits nontrivial six-period quasipolynomial fluctuations and a sharp degree-six growth coefficient. The structural Eulerian-flow decomposition and explicit connectivity correction offer reusable test instances for sequence reconstruction, not an arbitrary isolated small-length census.

## Closest literature and limits

Marcovich–Yaakobi, arXiv:1912.11108; Yehezkeally–Marcovich–Yaakobi, arXiv:2108.11725; Bernardini–Conte–Gabory et al., *On Strings Having the Same Length-\(k\) Substrings* (2022 conference version, expanded journal version https://link.springer.com/article/10.1007/s00224-025-10240-z). The binary exact multispectrum result and the ternary DNA ranking result are distinct specializations, not asserted as independent proofs of the current formula. This theorem neither calculates individual fiber cardinalities nor handles larger alphabets or reads of length greater than two. The sources inspected may not exhaust work under equivalent Eulerian-flow terminology.

Self-review: passed. Independent audit: not yet performed.
