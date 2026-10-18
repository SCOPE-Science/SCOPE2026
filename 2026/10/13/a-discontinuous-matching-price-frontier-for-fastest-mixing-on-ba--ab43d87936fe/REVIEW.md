# Independent mathematical audit

## correctness

PASS

For K_{n,n}, n≥3, with price t on one perfect matching and price 1 otherwise, projection-trace Rayleigh bounds valid for all asymmetric edge weights give λ2≤min{B/(n−1),[2(n−1)A+(n−2)B]/[n(n−1)]}, where tA+B=1. The piecewise-linear envelope maximizes at a=b when t<2(n−1)/(n−2), at A=0 when t>threshold, and over a full interval at equality. Exact block spectrum for orbit-constant weights is 0,2d,nb,2a+(n−2)b with multiplicities 1,1,n−1,n−1. Equality in the second trace bound forces the whole antisymmetric zero-sum space into the λ2 eigenspace; comparison of the two Laplacian blocks forces offmatching weights equal and the diagonal equal, ruling out asymmetric optima. Independent exact rational eigen/projection and threshold checks agree. The optimization is continuous-time Laplacian, not discrete-time SLEM.

## originality

PASS

The ancestor Sun–Boyd–Xiao–Diaconis 2006 supplies general priced continuous-time SDP and dual; it does not display the distinguished-matching K_{n,n} all-size full optimal-face classification or the edge-rate discontinuity in reviewed sections. Boyd–Diaconis–Parrilo–Xiao discrete-time SLEM examples and crown-graph fixed-weight Laplacian spectrum have different objectives or lack price optimization.

## value

PASS

A common optimization problem—select conductances on a symmetric bipartite network when a predefined set of links is expensive—has an exact discontinuous structural phase boundary in the unique optimal design. Proving the entire face and excluding asymmetric choices yields a reusable global certificate and a decision rule without numerical semidefinite optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
