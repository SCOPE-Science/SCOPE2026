# Scientific review — full-path equivalence and optimal finite-edit cost

## Correctness — PASS
The proof reconstructs the inclusion-induced parity model and quantifies precisely the independent coefficient rows. Conditional means are \(b_n=(1-2p)^{2^{M_n}}\); the geometric occupancy calculation proves summability without an unjustified uniform-in-path bound. The full conditional product density converges in \(L^2\) with strictly positive logarithmic limit, yielding two-sided equivalence after integrating over the common walk. Each coordinate of any shared-walk coupling has mismatch probability at least \(|b_n|/2\); a common-uniform coupling attains all such bounds simultaneously. Endpoint and asymptotic claims follow by explicit arguments. The finite checker passed 64 exact rational checks, not an infinite certification.

## Originality — PASS, with documented risk
Hamza–Tournier (arXiv:2610.01658v1), read through its theorem and appendix, provides exactly the coefficient representation, quenched and annealed Brownian convergence, and a related subexponential binomial estimate. The original 2015 bootstrap-walk paper (arXiv:1508.02840v2) was also inspected. The earlier general-bootstrap work (arXiv:2010.16000v2) concerns deterministic transformations, diffusion limits, and ergodicity. Their statements do not imply equivalence of whole unscaled paths or the sharp minimal Hamming coupling cost. Targeted indexed research comparisons yielded adjacent but distinct dependence or Bernoulli TV phenomena. General product-measure equivalence and maximal-coupling principles are standard; the original claim is the precise model-specific path-level classification, constant and endpoint behavior. A possible older presentation under finitary coupling terminology remains a priority risk.

## Value — PASS
The distinction between almost-sure quenched singularity and annealed equivalence is a substantive strengthening in kind over diffusion convergence. The coupling theorem quantifies exactly how many increments of an independent reference must be changed while preserving the driving walk, and its logarithmic endpoint divergence captures a natural boundary of the model. The claim is deliberately restricted to independent coefficient rows, where it is both complete and motivated.

## Closest literature and limitations
- Hamza and Tournier (2026), *Are random random walks normal?*, arXiv:2610.01658v1, Sections 2–3 and Appendix B.
- Collevecchio, Hamza, Shi and Williams (2020/2021), *Limit theorems and ergodicity for general bootstrap random walks*, arXiv:2010.16000v2.
- Unknown earlier literature under path-space quasi-invariance terminology might overlap; the 2015 *Bootstrap Random Walks* preprint was inspected in full HTML and treats deterministic bootstrap constructions. The proof does not extend to coefficient arrays with temporal dependence.

Self-review: passed. Independent audit: not yet performed.
