# Self-review

## Correctness — PASS

The exact-threshold claim is proved in two directions: first-divergence of retained run counts forces at least one deleted symbol at an earlier run plus deletion of every intervening symbol to a later equal-letter run; conversely, deleting an intervening segment and choosing which adjacent equal-letter run loses one symbol gives a collision at the claimed threshold, which extends to every larger admissible deletion count. Polynomial smoothing is coefficientwise and terminates at positive near-equal run lengths. Periodic symbols ensure each repeated-symbol separation costs at least \(q\) deletions and attain the upper bound for \(t<q\). The edge cases \(r=1\), \(r=n\), and \(t=n-1\) are covered. Independent finite enumeration supports the exact domain but is not an infinite proof.

## Originality — PASS, with explicit residual risk

Li–Wang–Fu (arXiv:2601.06493, 2026) prove balanced extremality for divisible run counts and only an inflated-length bound in their Corollary 15 for nondivisible counts; they identify the latter extremal problem as open. Liron–Langberg (arXiv:1202.1644, Section VII) already establish the deletion-pattern upper bound and discuss collisions, but not the all-word equality threshold or the short-deletion high-alphabet extremum. Searches across published findings and relevant literature, including collision, pattern, run-balance, and alias formulations, did not identify the stated all-parameter theorem. Mercier–Khabbazian–Bhargava (DOI:10.1109/TIT.2008.924730) offer older small-deletion formulas; their full text was unavailable through open sources and authorized institutional access at review time. That is a specific residual priority risk, not evidence of novelty.

## Mathematical value — PASS

The work converts a naturally occurring but sometimes loose counting bound into an exact characterization of its equality range, with a structural first-collision invariant computable directly from the runs. It also answers an infinite, genuinely nondivisible subfamily of a concrete open extremal problem for all \(q\ge t+1\), including arbitrarily many repeated runs; the uniform alphabet threshold cannot be reduced. For instance, the exact \(18\) replaces the inflated bound \(20\) at \((n,r,t,q)=(10,4,3,4)\). This is more than a numerical recomputation or a reformulation of the original balanced divisible theorem.

## Remaining scientific limitations

The maximum for \(q\le t\) generally remains undetermined. Not all maximizers are classified. Older inaccessible full text leaves priority uncertainty, and no independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
