# Independent mathematical audit

## correctness

PASS

With y_t=v_t/G² and s=1-beta2, the recurrence is y_t=y_{t-1}-s sign(y_{t-1}-1). Starting from zero, it advances by exactly s until it either lands on one or first overshoots. Integer reciprocal 1/s gives exact hitting and then sign zero freezes the state. Otherwise the first overshoot is exactly one step above the last subunit lattice point, and the next step returns to that point, forcing a two-cycle. The first moment and Adam comparison are elementary closed recurrences. The exact verifier checks locking cases, nonlocking cycles, cycle width and the reported parameter grid.

## originality

PASS

The defining Yogi recurrence is an additive fixed-magnitude sign update, and the submitted constant-gradient classification follows by solving that scalar lattice dynamics exactly. Targeted literature and Resultary searches did not surface a prior finite-lock-versus-two-cycle theorem. The source itself was not materially reread in complete primary full text during this run, so an implementation-note or source-version overlap remains a residual originality risk.

## value

PASS

Yogi's defining design choice is an additive sign-controlled second moment. The theorem exposes a qualitative arithmetic consequence of exactly that mechanism—finite lock versus permanent oscillation—and quantifies the oscillation, making it a useful diagnostic rather than a routine one-step calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
