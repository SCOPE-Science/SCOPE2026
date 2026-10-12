# Review

## Correctness

PASS. The first Adam-GC step with zero moments reduces exactly to \(\Delta w_i=-\alpha h_i/(|h_i|+\varepsilon)\). Splitting a centered gradient into positive and negative masses gives a sharp signed-sum bound via concavity, and the explicit one-versus-\(d-1\) family approaches it. The official final-delta centralization has zero component sum identically.

Risk: the sharp envelope is a first-step statement and excludes weight decay.

## Originality

PASS. The defining paper proves the affine weight constraint for projected SGD/SGDM, not for its coordinatewise-preconditioned Adam update. The official repository already recognizes that adaptive methods benefit from preserving weight mean and provides GC2, while later Moment Centralization forces zero-mean first moments. Those broader observations and repairs are treated as prior. The inspected sources do not give the exact Adam-GC first-step mean drift, the \(d=2\) exception, or the sharp \(\alpha(d-2)/d\) supremum.

Residual risk: an equivalent compact extremal calculation may exist in unindexed implementation discussions.

## Value

PASS. Weight-space constraint preservation is a central theoretical rationale for Gradient Centralization, and Adam is a primary advertised embedding. The sharp envelope quantifies precisely where that rationale stops transferring through adaptive preconditioning and explains the repository's final-update centralization as an exact invariant-restoring repair.

Self-review: passed. Independent audit: not yet performed.
