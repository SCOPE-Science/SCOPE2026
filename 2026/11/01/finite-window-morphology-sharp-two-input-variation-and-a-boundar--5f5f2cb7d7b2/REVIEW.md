# Scientific review: finite-window morphology and weighted variation

## Correctness

**PASS.** The result applies to every finite path length, every integer window radius in the stated range, arbitrary real input pairs, and strictly positive edge weights. Each generic min/max filter has nondecreasing optimizing-coordinate indices, so its selector linearization transports each input variation jump to at most one output edge. The possible crossings are exactly those listed: inactive edges have identical neighboring windows, while every crossing in an active edge's radius band is realized by placing successive smallest values at a disappearing left endpoint or newly appearing right endpoint. Exact step perturbations attain each weight ratio. Piecewise-linear integration proves the global two-input inequality. Active-edge connectivity proves the weight classification. The independent finite checker supports, but does not replace, this analytic proof.

## Originality

**PASS under the accessible-evidence comparison, with residual risk.** The primary 2007 Anguelov–Rohwer full text treats variation preservation of one input and its residual, not the two-input weighted Lipschitz modulus. A directly related earlier 2002 abstract likewise states single-input variation decomposition. Existing finite cyclic dilation and running-median sensitivity results concern different boundary and/or filter families and do not imply the path-specific weighted transition. A 2005 LULU book chapter and the 2002 full article could not be read in full and may contain an implicit equivalent statement; this remains an explicit uncertainty, not a claim of exhaustive uniqueness.

## Mathematical value

**PASS.** The stability of nonlinear morphology under *differences of two noisy signals* is distinct from the familiar assertion that filtering decreases variation of one signal. The exact attained coefficient characterizes allowable inhomogeneous edge penalties, identifies a non-obvious near-global-window overlap transition, and gives an all-depth stability guarantee for arbitrary erosion/dilation cascades under uniform weights. These address interpretable filter robustness and design questions rather than an arbitrary finite parameter table.

## Boundaries of the result

The exact formula applies to centered integer-radius sliding min/max on finite paths with truncated windows; it does not cover general neighborhoods, cycles, multidimensional image grids, weighted order statistics, or other filter boundaries. The cascade result is unweighted unless every stage individually satisfies the weighted criterion. Day-resolved source metadata identify the accessible 2005 book-chapter publication and the 2007 arXiv text; a still older 2002 reference has only year-level date evidence in the accessible material.

Self-review: passed. Independent audit: not yet performed.
