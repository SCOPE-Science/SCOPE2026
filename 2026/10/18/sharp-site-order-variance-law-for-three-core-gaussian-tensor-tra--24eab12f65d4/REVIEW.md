# Mathematical review

## Correctness — PASS
The proof uses a correctly normalized isotropic Gaussian tensor-train vector. Conditional Gaussian quadratic-form moments and explicit Wishart moments yield the displayed exact variance. The exchange identity has a nonpositive sign for moving higher purity inward, and the positive-polynomial factorization verifies the sharp \(\chi\) ratio. A rank-one factor and two normalized-identity factors establish sharpness as the common local dimension increases. The symbolic factorization and direct Monte Carlo sketches were recomputed; finite testing alone is not the proof.

## Originality — PASS, with residual risk
The 2026 Camaño–Epperly–Meyer–Tropp paper already supplies the complete Gaussian tensor-train fourth moment, and the 2026 Bujanović–Kressner–Olić paper supplies moment and tail analysis; both facts are acknowledged, not asserted to be new. The full accessible versions were examined at the relevant definitions, trace-estimation and moment sections. Neither expresses or proves the all-permutation optimal central-purity rule, the strict swap law or the sharp factor-\(\chi\) variance penalty. The new mathematical contribution is that integrated rearrangement-and-optimality theorem, not a claim to discover the underlying fourth moment. A specialized earlier rearrangement result may have been overlooked.

## Value — PASS
Tensor-train probes distinguish endpoint and interior Gaussian cores, so permuting otherwise isospectral Kronecker factors changes estimator variance. An exact ordering rule needs only trace and Frobenius norm of three factors and can prevent a variance penalty approaching the bond dimension; this is a nontrivial, structurally motivated benchmark for mode ordering. The result is restricted to three cores and proves no wall-clock gain.

## Prior work and limitations
Primary sources: arXiv:2606.15350v1, Definition 1.1, Theorem 4.3, §§3.3 and 4.5; arXiv:2606.15679v1, Definition 1 and §§3–4. Broader tensor-probability equivalents have not been eliminated exhaustively. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
