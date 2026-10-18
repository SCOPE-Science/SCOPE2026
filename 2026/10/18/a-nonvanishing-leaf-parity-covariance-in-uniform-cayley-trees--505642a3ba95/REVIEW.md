# Scientific review

## Correctness

**PASS.** Leaf deletion conditional on a specified vertex being a leaf is uniform over smaller labeled trees and uniform attachments, producing the exact covariance reduction. The distance-between-two-vertices distribution follows by fixing the connecting path and applying the classical labeled-forest completion formula. Alternating the exact path distribution and applying the exponential Taylor-remainder integral gives the expansion of the root parity-class mean to the order needed for the limiting \(1/(8e)\) covariance. The conditional two-word bipartite Prüfer encoding independently corroborates the finite moments. The standalone finite checks use exhaustive Prüfer enumeration through seven vertices and exact rational arithmetic. The asymptotic assertion is proved analytically; finite tests do not establish it.

## Originality

**PASS on available inspected evidence, subject to historical-priority uncertainty.** Contat (2021, arXiv:2103.03800) studies the marginal even-height class and the greedy independent set. Hladký–Nachmias–Tran (2017, arXiv:1711.09788) study local uniform-spanning-tree degree frequencies, including leaves. Dong–Ge (2021, arXiv:2103.05294) study prescribed spanning forests in complete bipartite graphs. No inspected statement among these presents the precise two-statistic leaf/parity covariance or the nonzero \(1/(8e)\) constant. Classical leaf indicators, tree enumeration, and bipartite Prüfer encoding are not claimed as original. Explicit joint tree-statistic identities elsewhere in the historical literature may implicitly yield this calculation; the source comparison is not an exhaustive proof of priority.

## Value

**PASS.** The root's even-distance class is the statistic appearing in a nontrivial distributional identity for Cayley trees; leaves are the canonical local degree statistic. Their joint dependence is not fixed by either marginal result. The exact covariance reduction and its small, strictly positive constant reveal a second-order coupling between a global parity statistic and a local count even though both fluctuate on square-root scales. The conditional occupancy representation gives a transparent finite-size interpretation. No general theorem beyond this motivated pair is asserted.

## Limits and closest literature

The full sign of the finite-size covariance for every order is not proved, though its eventual positivity follows from the limit. The source's greedy independent set is only marginally equidistributed with the even-distance class: the calculation concerns the latter on the same tree as its leaves, not the greedy set and leaves. Highly relevant texts inspected: Contat (https://arxiv.org/abs/2103.03800), Dong–Ge (https://arxiv.org/html/2103.05294v2), and Hladký–Nachmias–Tran (https://arxiv.org/html/1711.09788v3). Earlier implicit coverage remains possible.

Self-review: passed. Independent audit: not yet performed.
