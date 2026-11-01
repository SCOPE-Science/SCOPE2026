# Scientific review

## Correctness — PASS

The parameterized ellipse boundary has the exact arclength speed \(a\sqrt{1-\delta\cos^2\theta}\). The antipodal-coordinate change has unit Jacobian, and the separation is exactly \(2a\cos(v/2)\sqrt{1-\delta\sin^2\phi}\). For fixed positive \(\delta\), the diameter has only two isolated nondegenerate maximizers; rescaled local elliptic caps yield the linear coefficient. In the joint limit \(\delta/(\varepsilon/a)\to\lambda<\infty\), the angular boundary weights converge uniformly and dominated convergence yields the crossover integral. Elementary substitutions express it through complete elliptic integrals; their convergent endpoint series imply the logarithmic cusp and justify differentiating the remainder. The exact circle formula and independent numerical quadratures check limiting constants. The proof explicitly distinguishes fixed-shape and double-scaling quantifiers.

## Originality — PASS (provisional priority)

The 1966 oval interpoint-distance article assumes interior-uniform sampling, unlike the independent boundary endpoints here. The 1967 oval chord-length article uses random directional/line chords, not a product arclength law. Mayer and Molchanov (2006) cover circular/spherical sampling within rotationally symmetric maximal-distance asymptotics; this does not imply the noncircular-ellipse coefficient or double scaling. Schrempp (2015) assumes a two-dimensional Lebesgue density at a fixed elliptical shape and derives sample-max limits, rather than a singular boundary law near the circle. The closely ranked mathematical record on sampling laws in ellipses does not imply the near-diameter single-pair crossover or logarithmic singularity. The exact circular law and special-function expansions are acknowledged as prior facts. A broader equivalent formulation may exist and historical priority is not independently certified.

## Value — PASS

For two-point boundary distances, noncircular ellipses exhibit a linear near-diameter tail, whereas circles exhibit a square-root tail. The joint scaling reveals a continuous universal one-parameter transition with an explicit logarithmic derivative singularity at a geometrically distinguished threshold. This is a structural result about instability of an endpoint distribution under loss of isolated diametral pairs; the theorem does not merely compute a fixed integral or offer an arbitrary numeric case. It provides a benchmark for shape-dependent extremal-distance laws without claiming sampling-statistical consequences.

## Closest literature, verification and limits

Primary full-text comparisons: Gečiauskas 1966 (DOI 10.15388/LMJ.1966.19722), Gečiauskas 1967 (DOI 10.15388/LMJ.1967.19983), Mayer–Molchanov 2006 (arXiv:math/0605289), Schrempp 2015 (arXiv:1505.01597), and NIST DLMF §19.12 (elliptic expansions). All primary scientific premises for the new claim were checked from the actual texts and elementary derivations; uncertain historical priority remains a risk. The standalone `check_ellipse.py` executes 15 numerical validations of the exact integral and asymptotic formulas. Numeric verification is not an infinite proof. No independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
