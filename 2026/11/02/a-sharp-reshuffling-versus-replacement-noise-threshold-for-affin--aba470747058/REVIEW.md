# Scientific review: sharp reshuffling noise crossover in affine stochastic extragradient

## Correctness — PASS

The result is reconstructed directly from the two evaluations per same-sample stage in Algorithm 1 of Emmanouilidis–Vidal–Loizou (2024). The stage has exactly the affine form \(Mz+\epsilon d\). Orthogonal reduction of an invertible skew matrix makes the linear map a strict planar similarity, with squared multiplier \(r_j^2\), and yields the squared paired innovation factor \(h_j\). Independent centered random signs give exact geometric sums at each finite epoch. The stated universal ordering follows from the *necessary and sufficient* sign identity \(h_j-1-r_j^2=2(\kappa t_j^2-1)\). The strict-stability and threshold intervals overlap nontrivially precisely when \(\kappa>1\). The accompanying exact rational checker independently enumerates 32 finite-horizon expectations using the original stage evaluations; these finite checks are not offered as infinite-dimensional proof.

## Originality — PASS, with residual priority risk

The closest motivating full text, arXiv:2403.07148, analyzes SEG-RR and derives convergence bounds but does not give this exact modal comparison of stationary and finite-epoch second moments with independent sampling. De Sa (2020) establishes a distinct counterexample to universal reshuffling superiority; generic negative conclusions are therefore old and not claimed. Chae–Yun–Kim (arXiv:2501.00511, Theorem 4.1 and Appendix H.1) give divergent SEG samples with component-dependent bilinear linear parts, while here every sampled step strictly contracts and the precise surviving difference is noninterpolation noise. Related deterministic normal-extragradient polynomial optimization likewise does not contain this affine sampling comparison. The exact spectral crossover and complete two-component family are not implied by the inspected sources. The possibility of an earlier equivalent stationary-variance calculation in random affine iterations remains a residual risk. Priority requires independent verification.

## Mathematical value — PASS

Epoch reshuffling is used expressly to reduce the error of stochastic variational-inequality methods. This theorem identifies **when that mechanism reverses its sign even though the numerical method itself remains contractive**, and does so with a sharp necessary-and-sufficient matrix-spectral test, explicit finite-epoch constants and a stable rational counterexample. The contrast is not based on an arbitrary isolated parameter: the entire contractive step range is classified, with a transition at the source-recommended step ratio's half-frequency mark. It is relevant to choosing step sizes when persistent component offsets remain at the averaged solution. It does not claim new general shuffling failures, general nonlinear guarantees, or independent validation.

## Closest literature and limitations

- Emmanouilidis–Vidal–Loizou, arXiv:2403.07148, Algorithm 1, affine Theorem 2.2, Appendix B.2: source algorithm and nonsharp convergence analysis.
- De Sa, *Random Reshuffling is Not Always Better*, NeurIPS 2020: established warning about reshuffling in a different matrix-product context.
- Chae–Yun–Kim, arXiv:2501.00511, Theorem 4.1 / Appendix H.1: SEG divergence under different component matrices and without the present stationary-crossover law.

The theorem is finite-dimensional, skew-affine, exactly two-component and uses independent fair permutations of each epoch. Generalized sampling or nonlinear mappings need separate work. Earlier equivalences remain possible; mathematical priority is not externally certified.

Self-review: passed. Independent audit: not yet performed.
