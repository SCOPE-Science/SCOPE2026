# Self-review

## Correctness — PASS

The exact two-period matrix has trace \(T_0-(a+b)^2\delta^2\) and determinant \(U_0-4a^2b^2\delta^2\). For unequal habitat multipliers, the amplitude-independent characteristic polynomial at \(K=4a^2b^2/(a+b)^2\) is negative for every allowed \(m\), so the Perron eigenvalue stays strictly above \(K\) and its derivative with respect to squared amplitude is negative. Equal habitat multipliers give exact equality. For \(ab<1\), the second eigenvalue stays below one, making the sign of the characteristic polynomial at one a necessary-and-sufficient invasion classification. A rational counterfactual verifies crossing of the threshold without numerical rounding. The standard-library checker confirms exact identities and illustrative finite instances. The proof applies to all strictly positive multipliers and admissible symmetric dispersal rates as written; nothing is inferred from simulation alone.

## Originality — PASS within inspected literature, with priority risk

The 2012 Watson article and the 2014 Snyder article already describe the harmful effects of varying connectivity and cannot be credited as new qualitative insights. Snyder's full accessible text treats small iid perturbations and biophysical simulations rather than the all-amplitude, period-two, two-patch classification. The full arXiv text of Schreiber and Li addresses temporally varying habitat fitness and fixed dispersal phenotypes, which does not imply the claim here by simple substitution. The 2023 review reports effects of both signs in other covariance regimes, without an all-amplitude result for this fixed matrix family. Targeted published-literature searches and comparisons with available mathematical research statements found no statement implying the precise result. The full text/appendix of Watson (2012) could not be inspected and could contain an unrecognized dominating argument; the claim is thus historically provisional, not an independently certified discovery.

## Value — PASS

The all-parameter finite-amplitude inequality solves a motivated uncertainty in two-patch source–sink population projections: whether a time-averaged migration estimate correctly determines invasion. The explicit algebraic boundary and exact reversal example answer a precise, natural question not settled by a small-noise penalty, and identify cases where deterministic constant-dispersal projections forecast growth but an equal-mean periodic dispersal pattern declines. A two-patch population with two temporal phases is a minimal interpretable benchmark; arbitrary extension to many habitats is neither claimed nor needed for the exact benchmark's use.

## Remaining scientific limitations

Only symmetric, post-reproductive movement with no density feedback or temporally fluctuating habitat quality is considered. General connectivity matrices may behave differently. Literature priority, especially relative to the inaccessible mathematical sections of Watson (2012), requires independent examination.

Self-review: passed. Independent audit: not yet performed.
