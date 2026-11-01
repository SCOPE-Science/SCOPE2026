# Mathematical review: two-vertex rare-event phase transition

## Correctness — PASS

The object is the Euclidean unit disc with independent uniform area sampling and a radius-\(R\) ball-convex hull, \(R\ge1\). The event of exactly two ball-extreme sample points equals the union of disjoint (up to measure zero) events that a particular pair's ball-spindle contains the other sample points. Conditioning on the pair yields the established all-sample-size moment integral. The half-distance density and the spindle-area formula have the normalization shown in the cited 2026 primary source.

The new proof analyzes the endpoint \(\ell\uparrow1\) in three distinct regimes. For fixed \(R>1\), the half-distance density has a \((1-\ell)^{3/2}\) zero while the area has a nonzero first derivative, giving \(n^{-1/2}q_R^n\) after the \(\binom n2\) factor. For \(R=1\), the normalized area deficit is linear in \(\arccos\ell\), and an analytic inverse-series computation yields the stated \(n^{-3}\) expansion with rational factorial denominators. For \(R=1+\kappa/n^2\), the rescaled angle has a dominating integrable \(t^4e^{-t/\pi}\) envelope; dominated convergence supplies the explicit crossover, and Gaussian Laplace asymptotics supplies its large-parameter limit. Positivity, boundaries, and quantifiers are explicit. A standalone verifier confirms the relevant local series and selected convergences, including known exact small-sample values. Finite tests are not used as infinite proofs.

## Originality — PASS, with a precise inherited-formula boundary

The strongest predecessor is Bakó-Szabó–Besau–Fodor, arXiv:2608.29975v1 (2026-08-30). Its Equations (3.4), (4.10), (4.11) and Corollary 4.4 already give the **full all-\(n\) two-vertex moment integral**. The integral and the known probabilities for \(n=3,4\) are unconditionally treated as prior work. The candidate is restricted to the explicit sharp fixed-radius rare-event asymptotics, the nontrivial two-term critical expansion, and particularly the joint scale \(R-1\asymp n^{-2}\) with its crossover function; these are not the same statement as a moment identity and are not presented or worked out in the inspected primary text. It is acknowledged that the prior exact moment representation supplies their starting point and that the new conclusions can be derived from it by additional endpoint analysis.

Marynych–Molchanov (2022) prove convergence of the entire random face vector and moments, but no rate for the vanishing two-vertex probability or varying-radius crossover is identified in the inspected full text. Fodor–Montenegro Pinzón (2024) and Fodor–Papvári (2025/2026) address expected vertex counts and related asymptotic expansions. The 2014 Fodor–Kevei–Vígh article was not accessible in full: available primary abstract and the later full-text citation concern expectation rather than this rare-event phase. Residual historical-priority uncertainty is real; no independent-priority certification is claimed.

## Mathematical value — PASS

This is a natural rare event within a distributional model whose limiting expected vertex count is nonzero. The distinction between polynomial rarity at the geometry-matched radius and exponential rarity at any larger fixed hull radius is structural rather than a numerical increment. The exact \(n^{-2}\) crossover identifies the boundary layer that neither fixed-radius asymptotic alone describes and gives an explicit monotone function connecting the regimes. The second critical term and its reproducible coefficients make the statement quantitative. It does not claim a solution for arbitrary source bodies or for the full vertex distribution.

## Verification and unresolved risks

The numerical and symbolic checker completed 32 stated tests. The proof depends on the standard pair-distance density, the established Efron–Buchta identity, and endpoint Laplace/dominated-convergence arguments reconstructed in RESULT.md. The closest earlier all-\(n\) integral is sufficiently strong that future historical work might discover the same asymptotic phase law in older material. The primary 2014 paper was not read in full; the external mathematical audit is not performed. The claim makes no assertion of independent validation.

Self-review: passed. Independent audit: not yet performed.
