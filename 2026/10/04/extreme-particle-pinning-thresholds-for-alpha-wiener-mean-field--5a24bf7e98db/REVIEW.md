# Same-model review

## Correctness
PASS. In the stated equal-weight, zero-common-noise specialization, subtracting the ensemble average from each particle cancels the shared mean and leaves an exactly solvable linear SDE. The variation-of-constants kernel is the \(\alpha\)-Wiener kernel, so at each fixed time the residual vector is exactly a centered iid-Gaussian sample multiplied by \(\sigma\sqrt{v_\alpha(t)}\). The maximum differs from the ordinary iid absolute-Gaussian maximum by at most \(|\bar Z_n|\), which is negligible both on the \(\sqrt{\log n}\) scale and on the Gumbel \(1/b_n\) scale. The closed form and three endpoint equivalents for \(v_\alpha\) follow by direct integration.

Risk: the theorem is deliberately restricted to a chosen time and to the exact Gaussian specialization. No inference is made about continuous-time suprema or general weighted systems.

## Originality
PASS. The closest source, DOI:10.1017/jpr.2025.10032, contains the exact residual representation and \(\alpha\)-Wiener example but explicitly leaves the dependence of convergence rate on the interaction function for future study; it separately leaves its pointwise spatial convergence rate for future work. Full-text inspection found no theorem for the maximum particle deviation, no \(\log n\) terminal window, and no Gumbel law. Barczy–Pap's arXiv:0810.3070 covers endpoint behavior of a single \(\alpha\)-Wiener bridge, while the earlier pinned-particle paper DOI:10.1088/1751-8121/ac2715 treats the one-segment mean-field limit and Del Moral–Rio DOI:10.1214/10-AAP716 supplies broad concentration machinery. None of the inspected statements implies the exact growing-ensemble thresholds or the centered-Gaussian maximum law.

Residual risk: extreme-value statements may exist under different terminology in literature not surfaced by the targeted searches. The accepted claim avoids treating the classical Gaussian maximum theorem or single-bridge endpoint asymptotics as novel; novelty is confined to their exact combination with this finite-\(n\) centered particle representation and the resulting joint terminal-window phase diagram.

## Value
PASS. The source explicitly identifies convergence-rate analysis as an open direction. Pointwise pinning of each particle does not answer whether an entire growing ensemble is simultaneously close to its average. The theorem gives an exact and interpretable answer: a \(\log n\) extreme-value penalty changes the required approach to the terminal time, with a genuine three-regime phase transition at \(\alpha=1/2\). The Gumbel refinement quantifies residual all-particle risk beyond first order.

Risk: the value is specific rather than universal; extending the threshold to weighted, correlated, or non-Gaussian systems remains open.

Same-model review: passed. Independent audit: not yet performed.
