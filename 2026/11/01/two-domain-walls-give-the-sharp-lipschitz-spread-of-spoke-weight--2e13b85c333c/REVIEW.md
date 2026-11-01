# Scientific review: spoke-weighted wheel variance

## Correctness

PASS. The hub-normalized quadratic form has strictly positive Hessian. A tight-constraint component argument proves the four possible vertex levels for intermediate spoke lengths, which is the essential nonlinear-polytope step. An exact one-class quadratic comparison excludes single-sign extremizers. For two-sign configurations, the variance decomposes into a penalty per bridge and an exact squared-mean term. The odd-rim extra-bridge comparison is proved for both large and small \((n+1)(2t-1)\), with the small-parameter case controlled by integral sign parity. At the unit-spoke endpoint the zero-level classification follows by a separate integer extreme-point argument. Exact-rational tests cover 45 finite parameter instances and the asserted algebraic inequalities. The major limitation is that this proof concerns uniform rim weights and a common spoke length.

## Originality

PASS with residual priority risk. The 1998 foundational paper [1] defines spread and proves integral optimizer structure for unweighted graph metrics; the 2009 source [2] develops random-graph and random-edge-length estimates; the 2017 source [3] analyzes variance-optimal functions and cycles. Inspected material does not yield the deterministic sharp weighted wheel formula. Related public mathematical records on wheel negative type, weighted wheel heat flow, and wheel symmetric-edge-polytope ellipsoids optimize different functionals; their statements do not imply the sharp centered one-Lipschitz variance here. Searches for weighted-wheel spread, coned-cycle variance, and the explicit two-interface formula returned no covering result. A differently named or inaccessible earlier exact treatment remains possible; searches cannot prove novelty.

## Value

PASS. Wheels are a basic symmetric family of graph metrics. Varying only the spoke length is a natural geometric deformation: at \(t=1/2\), rim edges become active as shortest-path constraints. The theorem identifies the exact variance cost of this activation, its strict parity-sensitive derivative jump, and every optimizer's transition from freely interlaced signs to two mandatory interfaces. This is a structural sharp inequality for an entire two-parameter infinite metric family, not a standalone numerical example.

## Closest literature and limitations

[1] Alon–Boppana–Spencer (1998), Section 2.1, general finite-graph extremizer structure. [2] Addario-Berry–Janson–McDiarmid, arXiv:0902.1156, introduction and Section 7, random weighted graph bounds. [3] Yancey, arXiv:1705.09725, introduction and cycle/extremizer sections. The result is restricted to real observables, uniform vertex measure, cyclic rims of size at least four, and spoke lengths at most the rim length. It has no independent mathematical review.

Self-review: passed. Independent audit: not yet performed.
