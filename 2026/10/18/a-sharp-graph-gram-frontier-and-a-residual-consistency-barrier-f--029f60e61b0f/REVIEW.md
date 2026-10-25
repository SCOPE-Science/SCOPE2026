# Independent mathematical audit

## correctness

PASS

The normalization A^T A=A1^T(I+Y^T Y)A1 and positive definiteness reduce the spectrum to a Rayleigh ratio. The completed-square identity and ||Yv||/||v|| differing from ||Wv||/||v|| by at most epsilon prove both spectral bounds. A diagonal 2x2 witness attains both endpoints simultaneously. SPD similarity yields the G-energy Richardson factor and balancing the endpoints gives tau*=2/(2+epsilon^2). For residual consistency, choose r2=u and r1=-Y^T u; then A^T r=0 but the W correction is nonzero whenever W!=Y. The scalar inconsistent example has z(e)h(e)<0, so the quadratic objective strictly increases for every tau>0. Numerical tests are corroborative only.

## originality

PASS

The row-splitting construction and least-squares column-space consistency are acknowledged prior work. Full-text comparison did not identify the exact sharp phi^4 error-only envelope, simultaneous endpoint witness, minimax step, or the matched true-gradient/residual-channel counterexample. Equivalent classical graph-subspace or shear-matrix results remain a meaningful risk.

## value

PASS

Row splitting creates a concrete design choice: using an approximate factor with the true normal residual has a dimension-independent sharp spectral guarantee, while inserting the same inaccurate factor inside the residual can destroy least-squares stationarity and produce ascent even for arbitrarily small error. The simultaneous extremizer and exact minimax step make the error bound operational rather than merely sufficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
