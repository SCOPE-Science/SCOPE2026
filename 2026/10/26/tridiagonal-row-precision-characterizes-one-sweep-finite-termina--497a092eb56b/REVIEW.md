# Scientific review

## Correctness — PASS

The proof first establishes the exact rank-loss criterion for each oblique row projection; reaching rank zero in precisely \(n\) updates forces each new direction to preserve *all* previous row equations. These constraints coincide with the chained Gram identities. A backward bidiagonal factorization of a symmetric positive-definite tridiagonal precision matrix gives the converse. In three dimensions an exact Schur-complement calculation gives the Euclidean operator norm, with strict inequality proved by positive definiteness. The numerical checker uses exact rational arithmetic and is supportive, not a replacement for these arguments.

## Originality — PASS, subject to priority limits

The 2021 KO paper supplies the update and asymptotic convergence and illustrates finite solution of two-row examples; it does not establish the all-dimension first-sweep if-and-only-if in terms of tridiagonal precision or the exact three-row partial-correlation norm. The greedy oblique variants use other row selection rules. The accumulated-history PLSS solver is a more powerful direct-projection algorithm, but its general finite-termination property does not entail when **one-previous-row** KO terminates. Published-record and own-claim comparisons found no covering statement. Unindexed specialized identities and partially inaccessible prior full texts are residual risks.

## Value — PASS

The exact boundary separates the matrices on which minimal one-row memory is algebraically sufficient for finite solution from matrices on which it is not. The criterion is practical to recognize through tridiagonal precision/Markov row structure, includes dense correlated systems of all orders, and quantifies the first nontrivial obstruction by a sharp conditional correlation. It is a structural characterization, not an arbitrary numerical slice.

## Limits

The claim is limited to exact arithmetic, a single fixed ordered sweep, no skipped updates, and invertible square real systems; the three-row formula is the Euclidean operator norm, not an asymptotic rate. Unsearched and inaccessible literature may affect publication priority. Independent validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
