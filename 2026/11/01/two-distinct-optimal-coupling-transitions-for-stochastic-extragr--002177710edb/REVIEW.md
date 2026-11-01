# Scientific review

## Correctness — PASS

The two-point fixed-marginal coupling polytope is an interval, with the diagonal mass \(q\) uniquely determining the four joint probabilities. The exact matrix update and identity \(M_{uv}^{\top}M_{uv}=g_{uv}I\) show pathwise scalar norm multiplication, so independence across iterations yields the all-horizon expectation without approximation. Both optimizers follow by comparing affine functions of \(q\). The two polynomial factorizations, positive gains, and strict root inequalities cover all boundaries; the strong law is applicable because the logarithmic gains have finite two-point support. A standalone verifier passed 84 exact assertions and finite-horizon enumerations, which are corroboration rather than proof.

## Originality — PASS, qualified

Comparison with Li et al. (arXiv:2107.00464), including its original stochastic bilinear setup, principal results and supplement locations; Gorbunov et al. (arXiv:2111.08611), including its same-sample arbitrary-sampling section and theoretical appendix map; and available abstract of Yoon–Loizou (arXiv:2608.06182), found no direct all-coupling, fixed-marginal arithmetic-versus-logarithmic optimization classification. Existing same/independent SEG bounds are not themselves the pointwise optimizing statements. Related results on generic random products and elementary coupling inequalities are not denied; they remain priority risks. The 2026 source full text was not accessible, so this is a best-knowledge rather than exhaustive publication-priority judgment.

## Value — PASS

Choosing whether to reuse or complement a sample is a real design decision at fixed two-call cost. The strict separation between mean-square and typical-path optimal policies at a nondegenerate stable step gives a genuine caution about optimizing only one stochastic convergence metric. The exact maximal stable step \(3/8\) provides an interpretable policy benchmark and a concrete region where complementary coupling converges in mean square but ordinary shared coupling does not. This is an intentionally minimal, self-contained benchmark; no general algorithmic dominance is asserted.

## Closest literature and limitations

Li et al. (2021/2022) analyze same-sample bilinear SEG with averaging/restarting; Gorbunov et al. (2021/2022) cover same-sample arbitrary sampling and independent-sample variants separately. Yoon–Loizou (2026) is directly about the distinction between same- and independent-sample SEG; full text was not available for a complete implication comparison. Specialized correlation-coupling literature may contain equivalent formulations. Exact correctness is limited to the specified two-slope bilinear game and iid pair sequence.

Self-review: passed. Independent audit: not yet performed.
