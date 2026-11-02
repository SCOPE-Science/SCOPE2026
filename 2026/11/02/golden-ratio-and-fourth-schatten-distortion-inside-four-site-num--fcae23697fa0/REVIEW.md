# Scientific review

## Correctness — PASS

The claim concerns all nonnegative 4x4 one-step nilpotent weighted shifts with positive outer weights. The independent full-shadow invariants \(S=x+y+z\) and \(P=xz\) follow from the tridiagonal characteristic polynomial and the classical Haar shadow moment-generating identity; the first two nonzero radial moments recover both. The entire fiber is the compact interval \(2\sqrt P\le v=x+z\le S\). The squared norm is the maximum of one increasing and one decreasing function, so its minimizer either occurs at the left endpoint or at the unique crossing; the maximum is at the right endpoint. The fourth Schatten power is a strictly convex quadratic, giving exact minima and maxima. Rescaling by \(r=S/\sqrt P\) reduces the global sharp norm quotient to a monotone two-branch radical function peaking uniquely at \(r=3\), and the fourth-power Schatten quotient to a rational function peaking uniquely at \(r=2+\sqrt2\). All branch seams and the singular boundary \(S=2\sqrt P\) were checked. The exact equality witnesses attain both constants in potentially distinct fibers. The deterministic verifier passed its finite supplement, but it is not a proof of universal quantifiers.

## Originality — PASS (best knowledge)

Dunkl et al. (arXiv:1010.4189, 2010), Sections V, VI and VIII, are stronger prior input for general shadow equivalence, rotational symmetry, the same-shadow direct-sum construction and hidden rank/nilpotence. The determinant reduction and the observation that shadow does not recover nilpotency are not claimed as new. Johnson (arXiv:2610.29675, first submitted 2026-10-21), studies rigidity specifically for 3x3 matrices. Nearby research records treat three-level shadow singular-value fibers, four-site resolvent Schatten rearrangements, and numerical-radius/Schatten inequalities for shifts; they do not entail a global golden-ratio norm discrepancy and the distinct fourth-Schatten optimum for the same entire shadow in this four-site class. Search and primary text scrutiny found no equivalent exact pair, while the possibility of an unstated corollary or independent earlier derivation remains.

## Mathematical value — PASS

The new sharp constants quantify precisely how much matrix norm information is destroyed by preserving an entire probability distribution rather than merely a numerical range, within the first natural four-site path with two independent shadow invariants. The unexpectedly different maximizing fibers, \(r=3\) and \(r=2+\sqrt2\), demonstrate genuinely different spectral sensitivity of the operator norm and Schatten-four norm. Every fiber's full attainable intervals, including endpoint allocations and boundary transitions, are given rather than isolated examples. This is a natural complete constrained classification, not a randomly selected numerical value.

## Closest sources and limitations

- Dunkl, Gawron, Holbrook, Puchała, Życzkowski, *Numerical shadows: measures and densities on the numerical range*, arXiv:1010.4189; full 40-page text inspected, especially general equality theorem and Section VIII, Remark 8.7 (direct sums and non-rigidity).
- Dylan Johnson, *Numerical Shadow Rigidity for 3x3 Matrices*, arXiv:2610.29675v1, published 2026-10-21; full HTML text inspected; dimensions differ.
- Related finite nilpotent weighted-shift records concern Schatten norms of resolvents or generalized numerical radii, not the norm ratio within identical full shadow measures.

Bounds are confined to the stated four-site weighted-shift class and do not generalize to all matrices sharing a shadow. Independent validation and unknown prior equivalences remain residual risks.

Self-review: passed. Independent audit: not yet performed.
