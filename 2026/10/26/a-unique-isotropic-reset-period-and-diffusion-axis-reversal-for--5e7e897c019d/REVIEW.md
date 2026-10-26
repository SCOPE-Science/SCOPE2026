# Scientific review

## Correctness — PASS

The claim is for arbitrary positive-definite planar translational–rotational mobility, deterministic angle resets, and centered long-time spatial covariance. A Schur complement makes the independent angular and translational noises explicit. Itô differentiation of the angular coboundary proves the exact cycle decomposition; angular first and second harmonics give the covariance tensor, not merely its trace. Independence across fixed-period cycles proves exact integer-cycle moments and a central limit theorem. The traceless tensor factorization, strict scalar monotonicity, and unique isotropization follow by elementary algebra with the full stated positivity and alignment conditions. Symbolic, numerical, and independent SDE checks are supplied. No simulation is used as an infinite-time proof.

## Originality — PASS, self-review, with stated risks

The 2026 source introduces the model and derives precisely the mean drift: those are prior results. The new statement is the coupled tensor and the necessary-and-sufficient unique finite-isotropization condition with an axis reversal, plus a universal trace–drift relation. Earlier anisotropic-particle resetting theory assumes independent translational and angular noises and therefore does not itself cover the nonzero coupling mechanism. The complete available arXiv HTML of the 2026 and 2024 papers was read, including the 2024 Section V effective diffusion tensor in Eqs. (63)–(64), which concerns an independent-noise, Poisson-reset model. General renewal-theoretic covariance formulas or a broader unpublished coupled-mobility theory might implicitly imply parts of this theorem. Relevant indexed scientific result descriptions showed no implication-equivalent result; an unsuccessful search does not prove novelty. Independent priority assessment is pending.

## Value — PASS

The motivating work explicitly proposes diffusivity-assisted shape sorting but provides no complete coupled-diffusion optimization principle. A finite reset period that exactly removes directional spreading despite anisotropic instantaneous and long-period mobilities is a natural experimental calibration target; the proved right-angle reversal separates transport *direction* from spatial *dispersion*. The universal monotone trace and drift–dispersion identity quantify the sorting-performance tradeoff without assuming isotropic translational mobility. These are structural all-parameter conclusions, not a single unmotivated evaluation.

## Limitations

The exact isotropy threshold needs nonzero coupling and a rigid alignment condition; most mobility matrices will not meet it. The statement assumes noiseless angular-only periodic resets and no confinement or interactions. General stochastic covariance results might implicitly yield some formulae after nontrivial specialization, and independent priority assessment remains necessary. No independent external validation has been performed.

Self-review: passed. Independent audit: not yet performed.
