# Scientific review

## Correctness — PASS

The claim covers every integer \(n\ge4\) and every symmetric, nonnegative stochastic chain supported on the specified cycle-plus-antipodal graph. The proof derives the exact Fourier spectrum; the three active modes carry strictly positive dual multipliers which cancel both optimization variables, yielding a global lower bound. The exhibited chain is feasible, and **all** remaining Fourier modes are bounded analytically, including the even/odd endpoints. Positivity of the holding probabilities, the endpoint case \(n=4\), and uniqueness within the invariant subclass are established. Computational checks support, but do not replace, the infinite-family inequalities.

## Originality — PASS, with residual risks

The 2004 Boyd–Diaconis–Xiao framework establishes the convex FMMC problem. The 2005 symmetry analysis gives representation-theoretic tools. The 2009 Boyd–Diaconis–Parrilo–Xiao full paper establishes symmetry reduction and gives explicit results for edge-transitive graphs, cycles, Cartesian products, complete bipartite graphs and wheels. The present family with \(n\ge4\) has distinct cycle and antipodal edge orbits, is not the Cartesian prism, and does not have its claimed two-orbit parity formulas or dual certificate in the inspected relevant primary text. The edge-transitive \(n=3\) case is expressly excluded from the new claim. Text searches for Möbius ladders, Wagner graphs, circulant versions and equivalent Fourier-optimality formulations identified no stronger coverage. This supports originality but does not prove a complete census of all mathematical literature; specialised or unindexed papers remain possible.

## Value — PASS

The graph is a standard cycle-plus-antipodal network with two independently adjustable natural link types. Optimizing SLEM addresses convergence of reversible uniform-stationary Markov walks and symmetric consensus schemes. The complete family has a sharp odd/even dichotomy: equal-edge walks are periodic when \(n\) is odd, and on the even subfamily their asymptotic spectral gap is a factor \(6\) below the exact optimum. The result is a structural edge-weight design with global optimality, not merely a numerical example or a reparameterization of one-edge-transitive results.

## Limits and evidence

Checked primary materials: Boyd–Diaconis–Xiao, *SIAM Review* 46 (2004), DOI 10.1137/S0036144503423264; Boyd–Diaconis–Parrilo–Xiao, *Internet Mathematics* 2 (2005), DOI 10.1080/15427951.2005.10129100; Boyd–Diaconis–Parrilo–Xiao, *SIAM Journal on Optimization* 20 (2009), DOI 10.1137/070689413. Their general methods remain crucial precursors. The result is not independently audited; arbitrary non-invariant optimizer uniqueness and direct total-variation mixing-time optimality are not claimed. Earliest exactly day-dated source used is 2004-10-29; earlier reports exist with month-only evidence.

Self-review: passed. Independent audit: not yet performed.
