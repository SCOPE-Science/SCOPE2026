# Scientific review

## Correctness — PASS

The model explicitly selects the nonsticky diffusion through Brownian time change, so the singular coefficient at the origin has no unresolved gluing ambiguity. Excursion lengths are dominated by scaled Brownian exit times and have exponential moments; the reward is bounded by the excursion length. The first Dirichlet problem gives the known occupation mean. A second Dirichlet problem and two exact Green-monomial integrations give the centered cycle second moment, whose division by the mean cycle duration supplies the stated regenerative central-limit coefficient. Uniform moment bounds justify also the asymptotic variance statement. A standalone verifier passes 158 exact or quadrature-based checks; infinite-parameter validity follows from the proof.

Risk: the result is for the nonsticky continuum diffusion, not every weak solution of a formal singular-coefficient SDE or every discrete sluggish walk.

## Originality — PASS, best-knowledge qualification

The closest 2026 source, arXiv:2610.21962, Section 6.1.2, gives the occupation fraction mean and qualitative concentration but not the exact Gaussian coefficient. The 2018 Brownian additive-functional study concerns Poisson-clock resets; the 2020 run-and-tumble work also uses Poisson clocks and an orientation state; the 2022 occupation-triggered absorption study has a distinct meaning of threshold. Known regenerative central limit and Green-kernel techniques are acknowledged. Relevant exact-formula, alias, reduction and broader-method searches found no already published claim that directly gives the all-real-exponent coefficient or its Brownian reset-location rigidity.

Risk: a generic regenerative-diffusion covariance theorem may imply the formula once the elementary integrals are worked out; comprehensive independent priority assessment has not been performed. This is not evidence of literature-wide uniqueness.

## Value — PASS

The motivating paper predicts a deterministic occupation share and indicates fluctuations on a square-root scale but does not quantify their magnitude. The closed coefficient solves that natural measurement question for every real sluggishness exponent and reset location; the exact Brownian invariance and its strict breakdown under any positive sluggishness are meaningful structural comparisons, not renaming or numerical table entries. The result can calibrate occupation-fluctuation measurements and discriminate ordinary diffusion from space-dependent mobility at fixed reset geometry.

## Closest literature and limits

- arXiv:2610.21962, Section 6.1.2: first-order threshold-reset occupation law (direct source; not second-order coefficient).
- arXiv:1801.09909, Section IV: Poisson-reset Brownian occupation statistics (different stopping mechanism).
- arXiv:2009.01968, Section IV: Poisson-reset run-and-tumble occupation statistics (different motion and stopping).
- arXiv:2205.13989, Sections 3–4: Poisson position reset plus occupation-triggered absorption (different threshold).

The statement is asymptotic as physical time grows at fixed parameters. It excludes discrete lattice corrections, nonsymmetric domain endpoints, and alternative behavior at the mobility singularity.

Self-review: passed. Independent audit: not yet performed.
