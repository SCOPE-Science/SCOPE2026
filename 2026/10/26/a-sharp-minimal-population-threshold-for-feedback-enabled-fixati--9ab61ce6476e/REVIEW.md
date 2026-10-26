# Review: A sharp minimal-population threshold for feedback-enabled fixation

## Correctness — PASS

The fixed-environment probabilities follow from the birth–death recurrence. The two-state transient calculation proves the \(N=2\) impossibility statement. For \(N=3\), the backward-equation matrix is a nonsingular M-matrix; elimination yields the exact sign criterion and positive-root threshold. The included script reproduces the representative rational example with exact arithmetic. The proof does not infer a universal result from finite computation.

## Originality — PASS

The closest inspected primary literature studies environmental switching independent of mutant count. The 2014 fixation theory and the 2017 fluctuating-carrying-capacity model do not contain the state-conditioned switching generator or the exact threshold proved here. Targeted searches did not identify an equivalent result, but this is not proof that all related literature has been found.

## Value — PASS

The result gives a sharp minimal population-size boundary and an exact switching-rate criterion for a biologically interpretable feedback mechanism: the environment switches more rapidly toward the state with the lower death-to-birth ratio at each transient mutant count. The example shows that this can outweigh unfavorable selection in both frozen environments. The conclusion is a mathematical benchmark, not a calibrated biological prediction.

## Closest literature and limitations

P. Ashcroft, P. M. Altrock, and T. Galla, “Fixation in finite populations evolving in fluctuating environments” (2014), https://arxiv.org/abs/1406.5619. Their environment is independent of population state. K. Wienand, E. Frey, and M. Mobilia, “Evolution of a Fluctuating Population in a Randomly Switching Environment” (2017), https://arxiv.org/abs/1708.08841, couples population size and demographic noise but retains exogenous environmental switching. Broader literature on endogenous switching remains a residual risk; the theorem applies only to the stated rate family and initial condition.

Self-review: passed. Independent audit: not yet performed.
