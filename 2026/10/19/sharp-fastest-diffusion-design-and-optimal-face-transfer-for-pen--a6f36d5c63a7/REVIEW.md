# Scientific review

## Correctness — PASS

The projection identity \(P_{ii}=k/n\) and constant edge Fiedler leverage \(k\mu/m\) follow from vertex and edge transitivity. Lifted base Fiedler modes yield a sharp global Rayleigh-budget inequality for **all** independent edge allocations. The uniform construction attains equality; the quadratic spectral branch gives the gap and equality in the projector certificate fixes every pendant rate. The remaining optimum is exactly the base graph's fixed-sum optimal face. A Fourier imaginary-part argument proves cycle uniqueness, and the full zero-sum Fiedler space proves clique uniqueness. A finite test program passed 4209 checks; it is not a universal proof.

## Originality — PASS, with risks

Sun–Boyd–Xiao–Diaconis's 2006 FMMP theory (DOI `10.1137/S0036144504443821`) gives the broad convex framework and primal/dual conditions; Barik–Pati–Sarma's 2007 corona paper (DOI `10.1137/050624029`) gives unweighted corona spectral transformations; Olesker-Taylor–Zanetti's later work gives qualitative mixing bounds. Their inspected texts do not state the present exact priced-corona optimum or the all-optimizer pendant rigidity and optimal-face transfer. Earlier discrete-time sunlet SLEM optimization addresses a different spectral objective under row-stochastic constraints. The general SDP may admit a similar unpublished specialization; equivalent unindexed literature remains a real residual originality risk.

## Value — PASS

The theorem settles a natural family of continuous-time diffusion resource-allocation problems in an invariant-sharp formula and reveals which part of a globally optimal design is forced versus freely inherited from its core. It covers an infinite graph family rather than an arbitrary numerical slice, gives exact budget fractions, and avoids rerunning an SDP for every corona graph.

## Scientific limitations

The base must be connected, vertex- and edge-transitive; all core edges have the same price, and all private leaves have unit price. Only continuous-time symmetric Laplacian diffusion is treated. Not all base-edge optima are claimed unique. Random and exact-rational finite checks cannot establish infinite-family statements, and equivalent unnoticed literature remains possible.

Self-review: passed. Independent audit: not yet performed.
