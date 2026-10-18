# Independent mathematical audit

## correctness

PASS

The final claim fixes nonnegative n-by-n cell probabilities, uniform 1/n row and column margins, and only n+1 diagonal prefix values k²/n². For each i<j, comparing the copula upper envelope and Bertino lower bound gives n²[C(i/n,j/n)-C(j/n,i/n)]≤F_ij=min(h_i,h_j)-max(0,H_ij-n(j-i)), with h_k=k(n-k) and H_ij=max_{i≤k≤j}h_k. Linear interpolation of the prescribed diagonal knots is admissible and the published upper/Bertino splice attains all F_ij simultaneously; this is a genuine copula, so its cell masses give a feasible table. Centering at spacing d yields G_n(d)=(n²-L²)/4-max(0,floor(n²/4)-nd), with L=d+((n-d) mod 2); G rises before its threshold and falls after, yielding the eight residue coefficients and equality at 8|n. Independent exact integer interval tests for 2≤n<130 and seven feasible simultaneous-attainment LPs for n=2..8 agree. Those checks do not prove the infinite case; the interpolation/splice and centered threshold arguments do.

## originality

PASS

The earlier full-diagonal copula theorem supplies crucial envelope/splice machinery and the continuous 15/64 benchmark, which are credited rather than claimed. Material comparison of its actual hypotheses with the finite-knot feasible class and the integer maximization supports a distinct new exact theorem on every finite grid. The published discrete-copula geometry and a Resultary search for equivalent matrix formulations disclosed no dominating finite-knot law. Absence from search is not novelty proof; a concise corollary implicit in full-diagonal machinery remains the main priority risk.

## value

PASS

Exact grid-point asymmetry under independence-matching diagonal observations is a natural partial-identification problem for discretized copulas. The finite-knot constraints are demonstrably weaker than knowing an entire continuous diagonal. The sharp sample-grid oscillation, its exact period-eight arithmetic, and one joint extremizer for all oriented comparisons quantify a meaningful finite-resolution phenomenon. This is not merely another statement of the established continuous 15/64 example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
