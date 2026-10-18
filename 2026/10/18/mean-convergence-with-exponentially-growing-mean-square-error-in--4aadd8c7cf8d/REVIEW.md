# Scientific review

**Correctness — PASS.** The state matrices are reconstructed exactly from the one-worker algorithm with independent Bernoulli compressor. A rational positive-definite subeigenmatrix gives a \(13/10\) lower energy factor for full feedback, a separate rational Lyapunov equation proves decay of the first moment, and another positive-definite Lyapunov equation proves mean-square decay when feedback is halved. A deterministic inequality transfers augmented-state energy growth to the maximum iterate second moment. All matrix claims have executable exact-rational certificates; no finite simulation is extrapolated as proof.

**Originality — PASS, conditional on the explicitly recorded residual bibliographic risk.** The EControl source already observes instability at full feedback for a different initialization and a deterministic Top-1 compressor, so neither generic feedback instability nor the need to tune feedback is claimed new. The examined source does not give the present standard-initialization scalar half-dropout first-versus-second-moment separation or the exact same-step feedback recovery. Closest EControl-adjacent records treat classic error feedback or other estimator recursions. Searches are not a uniqueness proof; equivalent uncatalogued derivations remain possible.

**Value — PASS.** The exact counterexample exposes a nontrivial stability diagnostic: an apparently converging expected optimization iterate can conceal explosive second moments even with a noiseless, strongly convex one-dimensional objective and conventional stored-gradient initialization. The feedback comparison quantifies a stabilizing design decision with an explicit rational certificate. This is not an extension of the source's small-step guarantees and is not a universal instability assertion.

**Limitations and closest literature.** Gao–Islamov–Stich, arXiv:2311.05645v1, Algorithm 2 and Appendix C; classical Bernoulli error-feedback stability and scalar EF21 published-finding corpus results use different state updates. No independent audit is represented.

Self-review: passed. Independent audit: not yet performed.
