# Mathematical review

**Correctness — PASS.** The variance reduction follows from Brownian covariance and an explicitly differentiated bivariate Gaussian density. The single-crossing argument is an analytic strict inequality between two tilted means, with signs established at both ends. The small-band cubic term and large-band sharp constant have integrable dominated-convergence bounds. `verify.py` passed 42 finite numerical checks; no infinite claim is inferred from these tests.

**Originality — PASS, subject to the named priority risk.** Fischer and Glynn (arXiv:2610.24668v1, equation (4), Table 1) give the Brownian occupation functional and numerical second moments, which are acknowledged as prior work. The new mathematical conclusion is the *unique* variance peak and its exact integral characterization, accompanied by sharp asymptotics at both coverage extremes. Plackett's Gaussian-corner formula is old and not claimed. The complete historical Ehrhardt–Majumdar–Bray text was unavailable, and an equivalent prior occupation analysis remains possible.

**Mathematical value — PASS.** The global maximum gives a natural, exact worst-instability nominal confidence level for the limiting coverage statistic. The asymptotic constants explain high- and low-coverage dispersion scales beyond the motivating numerical table, and the reduction gives a simple reproducible quadrature. No claim is made about the finite-sample statistic, its full distribution, or its quantiles.

**Closest prior literature.** Fischer–Glynn (2026); Plackett (1954); Ehrhardt–Majumdar–Bray (2003, abstract inspected, full text not available). The same original claim and limitations appear in the accompanying result and structured record.

Self-review: passed. Independent audit: not yet performed.
