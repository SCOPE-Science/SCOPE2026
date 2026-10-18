# Scientific review: a universal Poisson window for clique-bouquet colorings

## Correctness — PASS

In a proper coloring of a hub-joined family of cliques, every non-hub vertex has a clique as its open neighborhood, so it automatically has a singleton witness color. For the hub, the conflict-free property is exactly the existence of a non-hub color used once. Given the hub color, different clique blocks are independent uniformly injective draws from the other \(r=q-1\) colors. The finite inclusion-exclusion formula counts exactly these singleton events. For a fixed set of \(j\) target colors, the probability all are singleton is asymptotic to \((S/r)^j e^{-jS/r}\); collisions of designated target colors within a bounded-size block contribute a lower-order term. Therefore the \(j\)-th factorial moment tends to \(e^{-jc}\), for every fixed \(j\), proving Poisson convergence and the limiting PCF probability. The argument correctly uses the uniform block-size bound \(M\) and \(S/r^2\to0\). The standalone verifier enumerated 423,262 assignments, 21 further proper-coloring cases, 24 finite optimal-palette cases, and critical-window factorial moments; all comparisons passed. Finite tests are not taken as proof of the asymptotic theorem.

## Originality — PASS, with bibliographic uncertainty

Pradhan–Sharma, arXiv:2608.10874v1 (2026-08-11), already establish the minimum proper conflict-free palette for the relevant block graphs; that number is not claimed. Tom–Vailaya, arXiv:2503.19344 (2025), give chromatic-symmetric-function machinery for graphs glued at one vertex, including clique bouquets. Their results encode proper-color frequency statistics, so no independent novelty is claimed for generic finite-palette singleton extraction or the supporting inclusion-exclusion formula. The classical all-singleton-block case is also excluded from the novelty assertion. The claimed contribution is precisely the heterogeneous, bounded-block, **growing-palette Poisson critical window**, proved uniformly without any limiting distribution of block sizes. A broader occupancy theorem might imply the result; priority is not certified. Public mathematical-research-record searches for proper conflict-free coloring, clique bouquets, chromatic symmetric functions and Poisson singleton occupancy revealed adjacent but not matching statements.

## Value — PASS

Proper conflict-free coloring can be understood structurally through singleton witness colors, but a numerical chromatic bound says little about the proportion of proper colorings that are conflict-free when palette size grows. The theorem gives a sharp transition with an explicit nondegenerate limiting probability for arbitrary mixtures of bounded-size peripheral cliques; the limit does not depend on how those clique sizes vary. It is a motivated universal graph-coloring threshold rather than a fixed graph instance or a repackaged color-number deduction. The finite formula and exact optimal-palette examples are supporting checks, not the principal value claim.

## Residual risks and scope

The literature may contain a more general Poisson occupancy theorem that implies the mixed-block limit. The chromatic-symmetric-function of one-vertex clique sums was previously studied, so fixed-palette enumerations should not be treated as independent novelty. This theorem makes no claim for unbounded blocks or noncritical scalings. Independent mathematical and bibliographic checks have not been conducted.

Self-review: passed. Independent audit: not yet performed.
