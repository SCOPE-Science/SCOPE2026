# Scientific review: effective-assortativity barrier

## Correctness — PASS

The precise reduced equations follow algebraically from Eqs. (15)–(16) of Landry and Restrepo. For \(u<1\), the derivative of \(h_{u,v}(z)=z/(1-z)-uz-vz^2\) has an explicit global minimum whose zero is exactly the stated cubic threshold. For \(u\ge1\), strict convexity of \(1/(1-z)-u-vz\) ensures uniqueness at nonnegative pressure. The proof explicitly handles zero-pressure and boundary equilibria, and the constructive converse keeps every original parameter admissible. A rational witness and standalone exact-arithmetic checks independently test the key reduction.

## Originality — PASS, subject to literature risk

The motivating paper [1] numerically maps asymmetric and stable equilibria of the exact source equations, and its full-text Section III treats particular parameter slices using interval root finding; it does not state the universal effective-strength exclusion-and-attainability boundary. Its reproduction code [2] similarly supplies parameter scans, not this closed analytic barrier. A newer collective-decision paper [3] concerns different dynamical equations, and therefore its symmetry-breaking results do not directly subsume the theorem. Targeted searches for the same reduced equations, algebraic monotonicity obstruction, and bifurcation thresholds found no covering published claim; equivalence in unindexed specialist bifurcation literature remains possible. General fold calculus alone is not represented as novel.

## Value — PASS

The original problem is to determine when an even-sized pair of social groups can retain different stationary opinions under higher-order interactions. A single sharp inequality in the physically meaningful products \(be\) and \(cf\) excludes *all* asymmetric equilibria, including unstable ones, for an infinite family of parameter choices. A constructive converse establishes that the boundary is not merely an overly conservative sufficient condition. It explains why triangle assortativity has a qualitative effect in the published numerical phase diagrams and separates stationary asymmetry from its stability.

## Limits and residual risks

The sharpness quantifier ranges over parameter quadruples with specified products; it is not pointwise sufficiency for each quadruple. The witness is a saddle. Only the equal-sized deterministic mean-field model and admissible nonnegative assortativities are covered. An unindexed equivalent normal-form argument may exist; independent expert replication and literature validation have not occurred.

Self-review: passed. Independent audit: not yet performed.

## Sources

[1] Landry and Restrepo, arXiv:2302.13967, Eqs. (15)–(16), Figs. 3–5, Appendix C; doi:10.1103/PhysRevE.108.034311.
[2] https://github.com/nwlandry/opinion-disparity-in-hypergraphs.
[3] *Symmetry breaking in collective decision-making through higher-order interactions*, *npj Complexity* (2026).
