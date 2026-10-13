# Scientific review

## Correctness — PASS

The simultaneous averaged-row update is reconstructed in the orthonormal bisector basis, with independent centered minibatch sign variable of variance \(1/q\). The diagonal covariance recurrence closes exactly and is a nonnegative symmetric two-by-two matrix with positive Perron vector; every nonzero deterministic error has nonzero projection on that vector. The determinant of \(I-T_q\), the positive-definiteness inequalities, and the upper-root exclusion prove necessity, sufficiency, and behavior at equality. A separate exact conditional-square computation gives the strict one-step gap. The fastest-relaxation claim follows from a simple largest eigenvalue, strictly positive second derivative and opposite endpoint derivative signs; its high-coherence expansion follows by the rescaled eigenvalue derivative equation. The embedded checker passes 1,220 tests. Finite checks do not replace the analytic proof.

## Originality — PASS, with residual priority risk

The defining averaged-Kaczmarz source [1] contains a one-step spectral error bound and a parameter choice minimizing that bound, but not the exact two-row long-horizon Perron factor nor an above-bound transient-growth regime. The cited broader sketch-and-project study [2] likewise optimizes rate guarantees; the related sparse averaging study [3] has a different state update and guarantee; the classical exact-MSE study [4] treats single-row Kaczmarz. Previously indexed coherence, cyclic bias, and delayed Gauss-Seidel results concern different sampling/update rules. Neither the already-known one-step inequality nor those neighboring results implies the stated long-horizon covariance threshold. An equivalent unindexed specialized calculation remains a real residual risk. Source [4]'s full PDF could not be inspected; its abstract was examined, so whole-document noncoverage is not asserted.

## Value — PASS

The exact gap between uniform one-step decrease and long-term convergence identifies a meaningful limitation of conservative relaxation rules for a published parallel solver. The rational witness exhibits a genuine positive first-step mean-square spike while every nonzero initial error ultimately decays; the unique rate-optimal relaxation and its near-coherent asymptotic identify a concrete tuning tradeoff. This is restricted to a natural exact two-row model, not presented as a general algorithmic speedup or new method.

## Limits and literature

The conclusion assumes two normalized independent rows, noiseless consistency, fixed independent uniform minibatches and constant relaxation. See the named comparisons and residual priority risks in `AUDIT.json`. Independent validation of the work is absent.

Self-review: passed. Independent audit: not yet performed.
