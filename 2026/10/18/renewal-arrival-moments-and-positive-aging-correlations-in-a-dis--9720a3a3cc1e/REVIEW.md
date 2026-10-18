# Scientific review

**Correctness — PASS.** The renewal generating function is derived directly from the interarrival PGF. The Stieltjes inversion is valid because the fractional transform is analytic off the nonpositive axis, is \(O(|s|^{-1})\) at infinity, and is \(O(|s|^{-q})\) near zero with \(0<q<1\). The jump density is positive and normalized; all finite differences are strictly signed. Regeneration gives the exact covariance, and Laplace scaling gives the asymptotic. A separate executable performs 436 finite consistency checks but is not treated as proof of infinite claims.

**Originality — PASS, subject to literature risks.** The closest full-text source [1] states the waiting PGF and explicitly proposes correlation analysis for later work, but does not show the renewal-epoch mixing measure or covariance profile. [2] studies related but different count and time-change observables. [3] supplies general discrete complete-monotonicity technology, and [4] classical renewal regeneration. Published research-record comparisons did not surface this exact combination. A differently named earlier renewal-sequence moment theorem might subsume the spectral component, so uniqueness is not guaranteed.

**Value — PASS.** The finding supplies a nontrivial positive spectral representation and strict finite-time dependence together with an exact asymptotic aging profile for a newly studied renewal model. This identifies a mathematically meaningful form of persistent dependence without incorrectly assuming stationarity.

**Limits.** The result is restricted to renewal-epoch indicators and the stated fractional family; stationary spectral long-range dependence and the covariance of accumulated event counts are not established. No independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.

References: [1] N. Yoshida (2026), arXiv:2605.03664; [2] A. Pachon, F. Polito and C. Ricciuti, *On discrete-time semi-Markov processes*; [3] R. A. C. Ferreira, *Complete monotonicity of discrete equations and related results*; [4] R. G. Gallager, *Discrete Stochastic Processes*, Chapter 4.
