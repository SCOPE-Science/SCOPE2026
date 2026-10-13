# Review

## Correctness — PASS

The claim is an exact characterization for strictly positive two-by-two kernels, exactly uniform marginals, all positive starting scaling vectors and fixed nonnegative relaxation. The logarithmic ratio reduction gives an exact log-cosh conditional objective. Strict convexity and coercivity establish uniqueness and compactness; strict coordinate descent proves convergence, while the endpoint invariant and supercritical ascent prove sharpness. The mean-log scalar recurrence separately establishes convergence of the unnormalized coupling. A Schur test supplies the eventual geometric rate. The attached standard-library verifier rederives updates and checks these identities on randomized kernels, but finite tests are not used as an infinite proof.

## Originality — PASS (self-review)

The full primary texts of Thibault et al., arXiv:1711.01851, §§4.1–4.3, and Lehmann et al., arXiv:2012.12562, §§1–3, were examined, including their stated fixed-relaxation updates and global-convergence theorems. The former proves adaptive Lyapunov-controlled convergence; the latter proves only the data-dependent global sufficient interval \(0<\omega<2/(1+\Lambda(K))\), while its \(0<\omega<2\) result is local. Neither inspected statement covers the sharp all-start fixed-parameter interval for the balanced two-by-two class or the exact endpoint first integral. Targeted searches for two-by-two balanced scaling, its log-cosh equivalence, and a stronger global overrelaxation theorem identified no decisive prior coverage. Absence from indexing is not proof of priority; unindexed specialized literature and alternate convex-coordinate terminology remain residual risks.

## Value — PASS

For a well-defined and standard small transport-scaling test problem, the theorem closes the distinction between local and global stability all the way to the sharp endpoint. The improvement over the general global sufficient range can be arbitrarily large near the ill-conditioned limit where \(\Lambda(K)\to1\), yet requires no adaptive line search. The result also identifies a conservation mechanism precisely at the instability boundary and shows that convergence concerns the actual coupling, not merely projective coordinates. It is a sharp structural benchmark, not a claim about high-dimensional optimal transport.

## Residual scope and priority risk

The theorem is only for uniform two-by-two margins, positive kernels, fixed real nonnegative relaxation and exact arithmetic. General initializations are allowed but no uniform global contraction rate is asserted. Priority risk persists if an unindexed theorem on symmetric two-state iterative proportional fitting or nonlinear successive overrelaxation already contains the result.

Self-review: passed. Independent audit: not yet performed.
