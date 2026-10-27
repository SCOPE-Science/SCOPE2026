# Scientific review

**Correctness — PASS.** The proof uses the exact mixed transition likelihood, an independent-uniform record-minimum coupling, the independence of insertion ranks, a square-summable bound on successive minima, and a bounded-increment score martingale CLT. The observed curvature controls the Taylor remainder and the interior likelihood maximizer. Endpoint Fisher information follows by a dominated rescaled density integral; its atom vanishes. The standalone exact-arithmetic checker confirms 111 finite instances, without being used as an infinite proof.

**Originality — PASS, qualified.** Yoshida (arXiv:2604.22637v1, Sections 2–4) derives the process law, its jump-count generating function, and state-function martingales, but does not derive the parameter likelihood, Fisher information growth, LAN, efficient MLE, or the sharp ratio of whole-path to endpoint information. The 1999 continuous-time staircase has a different transition time model. Searches of relevant mathematical records and literature found no direct statement of this four-part discrete-time inference result. A general record-process inference theorem might imply some or all of it; that is a residual risk, not an established coverage claim.

**Value — PASS.** The natural inference question for the paper's unknown jump-probability parameter has an atypically slow \(\sqrt{\log n}\) effective rate even though \(n\) states are observed. The logarithmic information gain of the complete trajectory relative to a terminal observation is a concrete, nontrivial statistical distinction. The theorem supplies a workable efficient estimator and a likelihood-based explanation for the effective sample size, rather than another marginal or generating-function identity.

**Limitations.** Fixed interior \(p\); full noiseless observations; first-order pointwise LAN and efficiency only. Potential implicit coverage in general record inference remains to be checked by independent experts.

Self-review: passed. Independent audit: not yet performed.
