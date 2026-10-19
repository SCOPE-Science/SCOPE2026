# Scientific assessment

**Correctness — PASS.** The proof explicitly derives the spectral covariance and whitened source-ball operator norm; the worst-case source vector is attained along an eigenvector. The noncentral chi-square CDF is strictly decreasing in its noncentrality parameter, so the inverse CDF gives the unique minimum deterministic radius in the specified ellipsoid family. The fixed-step singular-value asymptotics give the half-order threshold and establish that the normwise sufficient radius diverges. A standalone numerical program checks the identities and selected boundary cases.

**Originality — PASS with residual bibliographic risk.** Abhishek–Holman (2026, arXiv:2610.00882v1, Theorem 3.6) already derive a valid central-chi-square-plus-bias confidence ellipsoid; their §3.3–3.6 was inspected, and that result is not claimed anew. The present mathematical contribution is the exact source-ball minimax calibration *within the covariance-aligned ellipsoid family*, plus the singular-spectrum half-order stability threshold and unbounded gap against the normwise bound. Classical noncentral-chi-square laws and Gaussian confidence-ball theory are prior tools. Older bounded-normal-mean and general Gaussian-ball works pose a limited bibliographic equivalence risk; no claim of global optimality among arbitrary confidence sets is made.

**Value — PASS.** The exact spectral calibration matters where singular directions have vanishing propagated variance. For smooth source classes it prevents arbitrary inflation from bounding Euclidean bias and inverse covariance separately; the \(\nu=1/2\) phase boundary precisely identifies when the normalized bias remains bounded. This is an interpretable benchmark for uncertainty calibration of fixed-step regularization, although exact full covariance may be computationally expensive.

**Closest sources:** Abhishek and Holman, arXiv:2610.00882v1, §§3.3–3.6; Baraud (2004), *Confidence balls in Gaussian regression*; Stark (1992), *Affine minimax confidence intervals for a bounded normal mean*. The latter two are related Gaussian-confidence-set theory, not known to treat the stated Landweber spectral degeneration. No independent literature audit has been performed.

**Limits:** The source ball, deterministic iteration, Gaussian noise, exact covariance, full column rank, and fixed covariance-shaped confidence ellipsoid are essential. Randomized approximate covariance, adaptive stopping, and unrestricted confidence-set minimaxity are outside scope.

Self-review: passed. Independent audit: not yet performed.
