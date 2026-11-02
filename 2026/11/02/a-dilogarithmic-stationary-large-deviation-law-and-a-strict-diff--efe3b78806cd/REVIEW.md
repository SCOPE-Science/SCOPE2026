# Scientific review

## Correctness — PASS
The exact Gaussian mixture from independent Brownian increments and exponential reset intervals gives the stationary transform from [2]; the proof checks the contraction hypothesis, product domain, and factor \(\lambda s/D\) in the rare-position normalization. The mesh parameter is \(-\log(1-s)\); the limiting scaled cumulant function is half the dilogarithm. Its derivative maps the open tilt domain onto the whole real line, allowing a full LDP with explicit exponential tightness and tilting-based lower bounds. The effective Itô stationary zero-flux density has a different logarithmic large-deviation rate. The derivative comparison reduces to a scalar strictly positive function whose derivative has proved sign. Taylor inversion and boundary evaluation of the dilogarithm give the sixth-order and distant asymptotics. Finite numerical checks (41) support arithmetic, not proof of any infinite-dimensional or asymptotic statement.

## Originality — PASS (best knowledge, not certified)
Galla [1], in the fast-weak-reset regime, supplies the effective Itô model and stationary density but no stationary rare-scale rate comparison. Tal-Friedman–Roichman–Reuveni [2] supplies the exact partial-reset stationary transform; the product is explicitly prior, and its fixed-intensity weak-reset Gaussian limit does not state the two-model strict large-deviation comparison. Di Bello et al. [3] derive fixed-parameter far tails and time-dependent large deviations but not this joint weak-reset stationary-scale statement. A prior related investigation of positive linear drift and partial resetting gives fixed-reset stationary algebraic-tail exponent comparisons, but those fixed-positive-drift statements do not imply the zero-drift dilogarithmic scaling or the global strict rate gap. Actual mathematical-record semantic searches did not identify a dominating result; absence from search results alone is not a novelty proof. Residual risk includes a general transform-based LDP or general small-jump WKB comparison unlocated in the checked literature.

## Value — PASS
A natural operational question is whether the Gaussian-noise approximation to frequent tiny reset events controls statistically rare stationary displacements. The theorem produces **two exact nonquadratic rates**, proves they are strictly ordered for every nonzero scaled displacement, identifies their first difference only at sixth order, and finds distinct large-position growth (linear versus logarithmic). The result separates genuine global rate-function failure from agreement of typical Gaussian behavior and stationary second moments. This is a substantive boundary on the approximation, not a restatement of the pre-existing transform.

## Closest literature and remaining limits
[1] Tobias Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635v1 (2026-02-25), main Eq. (4)-(5), supplement S1.1.

[2] Tal-Friedman, Roichman and Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363, Sec. II Eq. (5).

[3] Di Bello et al., *Partial versus total resetting for Lévy flights in d dimensions*, arXiv:2501.01139, stationary tails and long-time deviation sections.

The statement does not imply finite-s density ratios, first-passage control, or results for nonconstant reset amplitudes. Only the specified stationary model is proved. Originality is best-knowledge and an independent priority audit is still needed.

Self-review: passed. Independent audit: not yet performed.
