# Scientific review

## Correctness — PASS

For every integer \(n\ge3\), the exact sine/Chebyshev marker recurrence reaches the negative vertical ray at time \(n^2-n\), then returns to the positive vertical ray at time \(n^2\), with no earlier positive vertical-ray return. The established rotation number \((n-1)/n^2\) turns these rays into a \(n^2\)-sector partition with exactly \(n\) consecutive negative sectors. Invariance and transitivity force equal sector masses; exact cyclic-block intersections give all multi-time laws and the sharp lag classes. Algebraic and modular checks in `check.py` reproduce independent finite cases. The proof, rather than numerical evidence, handles infinitely many \(n\) and lags.

## Originality — PASS, subject to priority limitations

Lagarias–Rains Part I gives the periodic cosine family, rotation number and general sector dynamics. Those results are not new. Part II concerns invariant circles and related symbolic families. Neither inspected full text states the complete invariant-measure-independent strict-negative sign law, lag-one independence, lag-two exclusion, or the exact general lag-overlap classification. The extra boundary-orbit calculation identifying the specific \(n\)-sector block is the differentiating step, followed by finite cyclic geometry. The earlier Beardon–Bullett–Rippon (1995) paper and general rotational coding remain priority risks; its full text was unavailable, so coverage is not ruled out by an abstract.

## Mathematical value — PASS

A full, parameter-indexed statistical classification of a natural sign sensor is motivated by the map's exceptional \(n^2\)-periodic dynamics. It applies to **every** invariant law avoiding the boundary orbit, not just a specially normalized density. The counterintuitive uniform pattern—adjacent rare events independent, two-step co-occurrence impossible, and an \(n+1\)-step strong positive echo—shows how a deterministic periodic process can hide dependence at its nearest lag. Its exact higher-order cylinder law provides a quantitative invariant of the entire family, beyond an isolated finite word computation.

## Scope and closest literature

J. C. Lagarias and E. Rains, *Dynamics of a family of piecewise-linear area-preserving plane maps I. Rational rotation numbers*, arXiv:math/0301294 (2003), provides the original two-branch system, periodic family and rotation-number formula. Their Part II, arXiv:math/0303007 (2003), treats invariant circles and symbolic orbit families. A. F. Beardon, S. R. Bullett and P. J. Rippon, *Periodic orbits of difference equations* (1995), precedes these constructions; full-text access was not obtained. No claim of independent priority, mixing, or an uncited pre-existing periodicity theorem is made.

Self-review: passed. Independent audit: not yet performed.
