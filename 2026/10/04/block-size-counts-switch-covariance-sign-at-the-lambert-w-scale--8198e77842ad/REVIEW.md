# Review

## Correctness

PASS. Marking one \(r\)-block gives a bijection with a choice of \(r\) labels and an arbitrary partition of the remaining labels, and under that bijection the total block count is exactly \(1+K_{n-r}\). This proves the Palm identity and covariance formula without approximation.

The covariance bracket is strictly decreasing because Bell numbers are a strict log-convex moment sequence. The threshold asymptotic follows from the standard Bell-ratio estimate and explicit differentiation of \(n/\alpha_n\). The finite enumerator and independent Bell-ratio checker reproduce all displayed finite identities.

## Originality

PASS, with an explicit implicit-generating-function risk. Chern--Diaconis--Kane--Rhoades prove that total block count and fixed-size block counts belong to an algebra closed under products, so their general theorem implies that a mixed moment must have a shifted-Bell expression. Their inspected full text gives the separate first moments but not the marked-block Palm law, the explicit covariance formula, or its one-switch sign geometry.

Timashev's paper is directly relevant because it conditions fixed-size block counts on a known number of blocks. Only abstract-level material was accessible in the inspected source, so an equivalent covariance identity there remains a residual risk.

Sachkov's earlier marked-partition paper verifies primary \(60C05\) ownership of this probabilistic set-partition setting but does not state the accepted block-size phase law in the accessible material.

## Value

PASS. Total block count and the block-size profile are the two canonical summaries of a random set partition. The theorem gives a finite exact Palm relation and converts it into a qualitative phase diagram: small block counts move with total richness, large block counts move against it, and the sign switch occurs at the natural Lambert-\(W\) block-size scale.

This dependence feature is invisible from separate marginal asymptotics and the marked-component identity is reusable for mixed moments.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK partitions_enumerated=26442 mean_checks=45 palm_checks=420 covariance_checks=45 monotone_checks=299 threshold_checks=299 asymptotic_sanity_checks=7`.
