# Review

## Correctness

PASS. Conditioning on the minimum of a uniformly sampled pair makes the partner uniform over the upper tail of the finite population. The claimed regression therefore converts exactly into an affine formula for every upper-tail mean. The elementary tail recurrence then forces consecutive spacings to be equal, and the converse follows from the mean of a finite arithmetic progression.

The correlation statement uses the exact simple-random-sampling variance of the pair total and the exact finite-population variance of the first order statistic. The package checker independently enumerates all pairs for a broad finite census using rational arithmetic.

## Originality

PASS, with explicit residual risk from older finite-population and ranked-set-sampling literature. The most relevant inspected primary paper, Takahasi--Futatsuya, proves positive likelihood-ratio dependence and covariance-sign theorems for finite-population order statistics. Its inspected dependence and covariance sections do not state an equal-spacing characterization from conditional regression.

O'Neill gives a stronger modern distributional framework, including a joint order-statistic law and arbitrary finite-population rank mapping. That framework makes the conditional expectation computable, but the inspected full text has no regression or arithmetic-progression characterization. The accepted claim adds a nontrivial inverse step: a single specified regression law forces the unknown population geometry.

Balakrishnan--Charalambides--Papadatos is a genuine residual risk because its sample-size-two results include covariance questions, but only abstract-level material was available for decisive comparison.

## Value

PASS. Equally spaced finite populations are the canonical model behind serial-number and finite-uniform sampling. The theorem gives an intrinsic statistical signature of that geometry: one observable conditional-regression slope is sufficient to characterize equal spacing.

This is more than a marginal-moment identity. It is a finite inverse theorem, and its population-size-free correlation consequence explains why the canonical two-draw model has a stable dependence constant across every population size and affine rescaling.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK populations=967 pair_rows=11430 regression_checks=4043 rigidity_checks=967 max_checks=194 covariance_checks=54 correlation_checks=108`.
