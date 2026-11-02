# Scientific review: terminal-sibling clustering covariance

## Correctness (PASS)

The exact recursive-tree attachment mechanism defines the two random variables without approximations. Rooted terminal vertices, rather than graph-degree-one vertices, are explicitly counted. The conditional increment identities (2)--(3) in `RESULT.md` are verified by considering the two disjoint choices: an existing nonterminal parent, or a terminal parent whose own parent loses one terminal child. The term \(6F_{n,3}\) in the squared pair-count increment is essential and is included. The factorial-moment recursion and induction establish \(\mathbb EF_{n,r}=n/(r+1)!\) on the stated ranges. The triangular second-moment recursion has the indicated initial values and uniquely yields the displayed polynomials, hence the covariance matrix for every \(n\ge5\). The independent exact enumerator and recurrence checker passed 5,017 assertions. Finite checks are supplementary; the proof does not extrapolate from tests.

## Originality (PASS, subject to independent priority review)

The closest study, Hartle and Krapivsky (arXiv:2511.04085), gives the asymptotic one-vertex leaf-degree distribution, its descending factorial moments, and a separate full distribution for the total number of graph leaves. Those first-moment formulas do not imply the finite covariance of the aggregate unordered sibling-pair count. Hartle and Krapivsky (arXiv:2602.01021) give additional asymptotic degree/leaf-degree marginals in recursive trees and selected second-order counts in preferential attachment, but not the asserted pair-count variance. Stepanyants et al. (arXiv:2608.04303) establish rank/layer marginal laws and self-averaging bounds, not this statistic. Gopaladesikan--Mahmoud--Ward (DOI 10.1007/s11009-013-9333-z) treat subtree motifs on the fringe, not all pairs of current terminal children of arbitrary high-degree vertices. Literature and mathematical-record searches found no explicit covering \(59/180\) or \(1/8\) coefficient for the same observable. Residual risk: a broader result on additive functionals, motifs, or exchangeable tree growth might imply the exact covariance indirectly; the literature search is not a novelty proof.

## Mathematical value (PASS)

The number of unordered terminal-sibling pairs measures how the tree's terminal population clusters under parents. Unlike a one-vertex leaf-degree marginal, its variance requires two-parent dependencies and sibling overlap. The full, sharp, finite-size covariance and nonzero correlation quantify how peripheral abundance and clustering cofluctuate; the proof identifies a finite hierarchy of terminal-child factorial moments that closes these global fluctuations. The exact formulas give a nondegenerate baseline for random genealogical/attachment tree comparisons and show \(L^2\) concentration with known constants. This is a natural second-order structural invariant, not a numerical fit or an arbitrary finite slice. No central limit theorem is claimed.

## Scope and residual risk

Uniform rooted recursive trees only; \(n\ge5\) for the complete covariance formula. The defined terminal-child statistic differs in finite size from graph-degree-one leaf statistics when the root has degree one. Historical priority, a Gaussian limit, and the full distribution of the pair count are not established here.

Self-review: passed. Independent audit: not yet performed.
