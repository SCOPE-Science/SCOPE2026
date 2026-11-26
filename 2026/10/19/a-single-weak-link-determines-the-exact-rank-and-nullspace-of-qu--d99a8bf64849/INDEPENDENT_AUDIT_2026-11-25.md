# Independent mathematical audit

## correctness

PASS

The Cesàro mean is the sum of the Schur squares of the projectors onto distinct eigenspaces. For g≠1, the two endpoint values determine an eigenvector by the interior three-term recurrence. An eigenspace of dimension two would make both linear endpoint constraints identically zero; their coefficients include 1+g u_(n−2) and u_(n−2)+g, so g²=1, impossible also at g=0. Thus simple eigenvectors have definite reversal parity and their squared amplitudes lie in the q-dimensional symmetric subspace. The diagonal moments lie in their span. Independently checked the determinant on the lifted integer line: 2k<n forces zero winding, so the unit-coupling baseline is binom(2k,k). From representative r the distances to cross a lift of the distinguished bond on the two routes are r+1 and n−r. A 2k-step return cannot use it when k≤r. For r≤q−2 and k=r+1 the shorter route is unique and the only such walk immediately retraces, contributing g² instead of 1. This proves the same triangular defect identity even at g=0 (those walks have weight zero) and g=1. Subtracting the binomial multiples of the ones column and expanding in the last row gives the signed power. Its invertibility for g≠1 saturates the upper bound, giving the full reversal-antisymmetric kernel. At g=1 the verified Godsil formulas give positive definiteness at odd order and exactly the antipodal-antisymmetric kernel at even order; the all-ones summand annihilates that subspace. The frozen Fraction and NumPy verification code was inspected, not executed; its finite tolerance tests do not prove ranks for arbitrarily small |g−1|.

## originality

PASS

The distinct result is the one-bond even-moment determinant and the resulting all-weight classification, particularly even-order nonunit cycles. Credit the known unweighted cycle and path cases. For odd cycles a prior endpoint-potential theorem also implies the nonunit positive-weight rank lower bound after reflection folding and establishing simplicity; the present determinant is a different certificate and covers both parities. The closest previous cycle certificate uses a site potential and odd moments, not a changed edge.

## value

PASS

A single edge variation is a natural symmetry-breaking experiment for average mixing. Rank alone would miss the even-order switch from antipodal to bond-reflection antisymmetry. The exact moment determinant certifies rank even for arbitrarily weak defects, where numerical rank and degeneracy grouping become unreliable, and identifies the algebraic vanishing order at the unperturbed cycle. This remains useful beyond rederiving the known path and cycle cases or the folded odd-rank lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
