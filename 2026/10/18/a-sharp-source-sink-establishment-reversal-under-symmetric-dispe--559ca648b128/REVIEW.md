# Scientific review

**Correctness — PASS.** Poisson thinning yields the exact least-fixed-point equations, whose nontrivial zero-dispersal branch is differentiable because \(rq<1\) and \(s<1\). Direct implicit differentiation gives the sharp sign test. A strictly negative spectral derivative and standard multitype branching extinction criteria give the unique high-dispersal collapse boundary, while a scalar convexity argument proves the parameter band is nonempty for all \(r>1\). The exact example and a standalone numerical implementation provide separate finite checks, not substitutes for the algebraic proof.

**Originality — PASS, with residual risk.** The closely related Bansaye–Lambert source–sink paper (arXiv:1111.2535, sections 1–3 and Appendix B) studies the same basic lifecycle, but focuses on persistence thresholds, growth rates, and ancestry rather than the uniform-founder low-dispersal extinction derivative. Tomasini–Peischl (2018, model and discussion) and Czuppon et al. (2021, model and equations 4–8) already analyze multi-type establishment and migration nonmonotonicity; the qualitative phenomenon and generic Poisson fixed points are **not** claimed as new. Their alternative habitat-selection/migration life cycles and objectives do not state the joint exact \(s>rq\) criterion, universal nonempty band, and continuously decreasing growth contrast. General theory could imply a specialization not stated explicitly; an unindexed exact result remains possible.

**Value — PASS.** Comparing founder establishment with Perron growth addresses an ecologically motivated planning tradeoff. The sharp sign condition and universal existence of a beneficial-then-fatal dispersal interval for any viable source are structural conclusions, not an arbitrary numerical example or routine reparameterization of a known table.

**Limits.** Only the stated two-patch Poisson offspring-then-dispersal model with uniform founder locations is covered. The location and uniqueness of the interior optimum are not determined. No independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
