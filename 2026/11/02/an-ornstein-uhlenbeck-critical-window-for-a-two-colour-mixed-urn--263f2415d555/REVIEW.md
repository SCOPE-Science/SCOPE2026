# Scientific review

## Correctness — PASS

The object is a balanced, independent-rule-choice urn with one fixed mixing probability within each triangular-array row. The increment is exactly \(R_jS_j\), where \(R_j\in\{-2,4\}\), the conditional sign mean is \(U_{j-1}/(4j)\), and the regression coefficient is \(\alpha_N=1/2-\tau/\log N\). The exact conditional variance and scalar second-moment recursion follow algebraically. Martingale renormalization by the gamma product produces the predictable bracket \(12\Gamma(3/2)^2\int_0^t e^{2\tau u}\,du\); the dependent correction is summably bounded by the second-moment estimate, and bounded jumps give the Lindeberg condition. A martingale functional limit, the convergent gamma-product multiplier, and a Doob bound at logarithmic time zero establish the stated Ornstein–Uhlenbeck path law. The separate exact moment recurrence yields the variance profile and the critical harmonic identity. The packaged standard-library checker replayed 2,917 exact and 56 supplementary numerical checks; those checks alone cannot establish the functional limit.

**Risk:** Only fixed \(\tau\), equal initial masses, and the specified four-ball balanced rules are proved. The proof relies on the standard martingale functional central limit theorem but checks its Lindeberg and bracket conditions explicitly.

## Originality — PASS, subject to historical priority

The May 2026 motivating paper by Shi, Yin and Miao proves a fixed-parameter, noncritical central limit theorem for this mixed urn. Zhang's broad stochastic-approximation theorems prove fixed-drift critical and Gaussian-process approximations, but their stated hypotheses do not supply the uniform triangular-row limit as the drift approaches the boundary at rate \(1/\log N\). Classical work by Janson and by Bai, Hu and Zhang establishes relevant urn Gaussian theory; where full-text material was unavailable no whole-paper noncoverage assertion is made. The already known exactly-critical Brownian logarithmic-time limit is precisely the \(\tau=0\) case; it is explicitly excluded from the novel contribution. The distinct claim is the parameter-indexed entire critical-window process, nonzero Ornstein–Uhlenbeck drift and interpolating second-moment law, neither a fixed-parameter limit nor a substitution into one. Relevant mathematical-record and exact/alias literature searches revealed no direct identical or stronger critical-window theorem.

**Risk:** General earlier Gaussian approximations may be adaptable to this triangular array and could affect priority; the full texts of some broadly relevant older articles were not accessible. Search nonhits are not proof of novelty.

## Mathematical value — PASS

In a mixed reinforcement mechanism, the eigenvalue crosses the \(1/2\) fluctuation boundary. Tuning by \(1/\log N\) is uniquely motivated by the response factor \(k^{\alpha_N-1/2}=\exp(-\tau\log k/\log N)\), which stays nontrivial throughout logarithmic time. The result separates the critical Brownian limit from a continuum of negatively or positively correlated OU-type drift profiles and quantifies the variance amplification/suppression across the boundary. This gives a natural finite-size phase window, not an arbitrary parameter slice or an isolated computation.

**Risk:** The result concerns a particular balanced urn and is not a general generalized-urn critical-window classification.

## Closest literature and limits

- Shi, Yin and Miao (2026), arXiv:2605.26669v1: fixed-mixture Bernoulli mixed urn, with a fixed-parameter noncritical CLT.
- Zhang (2016), arXiv:1602.05708: fixed-regression stochastic-approximation CLT and Gaussian-process approximation, including an exact critical case.
- Janson (2004), DOI:10.1016/j.spa.2003.12.002: general generalized-urn functional limits; available abstract alone cannot exclude indirect coverage.
- Bai, Hu and Zhang (2002), DOI:10.1214/aoap/1037125857: Gaussian approximations for homogeneous and nonhomogeneous generalized Friedman urns; incomplete full-text comparison remains a priority risk.
- Roy, Takei and Tanemura (2024), arXiv:2403.02881: triangular-array elephant walk based on memory truncation, a different triangular mechanism.

Self-review: passed. Independent audit: not yet performed.
