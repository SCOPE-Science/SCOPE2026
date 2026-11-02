# Scientific review

## Correctness — PASS

The finite theorem is a precise statement for \(m\ge3\), the extended binary Hamming code \(\operatorname{RM}_2(m-2,m)\), and uniform sampling with replacement of generator column indices. Its complete proof derives the Reed–Muller duality by orthogonality and dimensions, uses the dual-matroid rank identity to equate spanning subsets with complementary affine-independent point sets, and counts these exactly by affine-span growth. Separately derived coupon-collector waiting times give the rational expectation. The CDF's convergent product and geometric tail bound justify both distributional convergence and first-moment convergence. A split-tail dominated-convergence argument gives the sharp coefficient of the expected-sampling overhead. The link to the classical binary-rank constant is independently justified by rank-by-rank waiting probabilities.

A standalone standard-library verifier enumerates all subsets for \(m=3,4\), including all \(65{,}536\) dual-rank identities for \(m=4\), and checks the exact rational CDF and expectation for \(m=3,\ldots,12\). These tests agree with independent absorbing-state sampling recurrences. The infinite-family result depends on the written proof, not on extrapolation from the tests.

## Originality — PASS, with residual priority risk

The closest published formulas are the general coverage-depth duality of Bertuzzo–Ravagnani–Yaakobi and their exact analyses of ordinary Hamming and first-order Reed–Muller codes. Their unextended Hamming family is not this length-\(2^m\) extended family, and their general duality requires additional affine-set enumeration to specialize. Gross and collaborators investigate first-order Reed–Muller optimality and random-code ensembles, not the exact deterministic high-rate extended-Hamming stopping law. Wang–Yaakobi provides general bounds but no such exact deterministic limit. An accessible prior-result search did not identify a theorem containing both this CDF and sharp asymptotic coefficient. The random-matrix distribution and Erdős–Borwein constant themselves are known, and are not claimed as original.

Residual priority risks: an unindexed affine-matroid independence polynomial or an implicit specialization of known code-enumerator formulas may prove substantially equivalent. The accessible rendition of arXiv:2610.07370 is an extracted text representation rather than the publisher's original typeset full text. These are priority limitations, not gaps in the internally proved algebra.

## Value — PASS

The problem is motivated by DNA-storage sampling cost, where the number of distinct encoded symbols required for recovery differs from the classical MDS coupon collector. The extended Hamming code is the canonical length-\(2^m\), redundancy-\(m+1\), distance-four binary code. A complete finite sampling distribution and an exact independent-set census make the comparison reproducible. The deterministic full-rank delay unexpectedly shares the classical random-binary-matrix limit; the sharp \(2^m/m\) correction quantifies this relation and identifies the precise nonzero leading coefficient. The contribution is a nontrivial asymptotic and structural synthesis, not a claim of code optimality or a new formula for the known constant.

Self-review: passed. Independent audit: not yet performed.
