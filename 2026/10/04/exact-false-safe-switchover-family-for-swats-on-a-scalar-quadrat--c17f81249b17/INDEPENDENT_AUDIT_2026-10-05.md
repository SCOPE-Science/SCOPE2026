# Independent mathematical audit

## correctness

PASS

Reconstruction from the primary SWATS equations gives the displayed first and second Adam-phase steps exactly. Substituting the proposed \(x_0\) and \(\varepsilon\) yields \(p_1=-qx_0\), \(p_2=-qx_1\), hence \(\gamma_1=\gamma_2=q\) and \(\lambda_2/(1-b^2)=q\). The source criterion is checked for \(k>1\), so it fires at step 2. With \(\beta_1=0\), the switched phase is ordinary scalar gradient descent with multiplier \(1-q\), whose modulus exceeds one. A fresh independent numerical replay over multiple interior \(b\) values reproduced the exact identities to floating-point tolerance; the infinite family is established algebraically, not by the replay.

## originality

PASS

The defining paper supplies the projection estimator and stationarity trigger but not a post-switch stability theorem or a scalar family accepting arbitrarily unstable rates. Fresh Resultary and public searches using SWATS, scalar quadratic, false switch, instability, convergence, and \(\beta_1=0\) aliases returned the defining paper and unrelated optimizer-stability work, not an implication-equivalent SWATS counterexample.

## value

PASS

SWATS is designed to learn both when to switch and what SGD rate to use. Showing that perfect stationarity can certify an arbitrarily unstable scalar rate isolates a structural mismatch between temporal agreement and dynamical safety and directly motivates a curvature- or magnitude-sensitive safeguard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
