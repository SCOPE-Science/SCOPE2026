# Review: exact rank-one BLOKS spectral-degree separation

## Correctness — PASS
The rank-one projector calculation derives the two-eigenvalue unpreconditioned normal matrix, and explicit block matrices derive the positive diagonal preconditioner. Secular interlacing produces \(q\) distinct active roots; the exact Jensen bound excludes the inactive scalar eigenvalue. A nonzero overlap of \(b=e_1+e_2\) with every active eigenspace proves the zero-start exact PCG grade \(q+1\). Direct rational calculations verify the homogeneous companion spectrum. The separate executable carries finite exact consistency checks; its results are not substituted for the arbitrary-dimension argument.

## Originality — PASS under accessible-source comparison
The source preprint [1] defines the block construction and supplies numerical evaluation. The inspected main-text portions do not establish the sharp arbitrary-block Krylov-degree example. The relevant general block-Jacobi papers [2,3] address conditioning, and no direct logical implication giving the specified Nyström block formula plus this right-hand-side polynomial degree was found in the accessible material. General rank-one secular theory and polynomial CG termination are classical proof ingredients, not claimed discoveries. Historical-priority risk remains from incompletely examined appendices and specialist conditioning literature; this is not an independent or exhaustive literature certification.

## Mathematical value — PASS
The exact number of CG steps is a natural invariant of an SPD kernel normal equation and chosen right-hand side. The result supplies a structural benchmark of a recently proposed preconditioning prescription: blockwise variation splits a two-point spectrum into \(q+1\) distinct levels despite a bounded input condition number, whereas a same-spectrum homogeneous block alignment leaves only three levels. It identifies a mechanism to test against and does not confuse exact iteration counts with practical finite-tolerance cost.

## Scientific limits
The example uses the full-landmark, completely observed, two-coordinate block specialization and exact arithmetic. It does not prove a failure of the source's random sparse-sketch implementation, wall-clock advantage, fixed-error convergence behavior, or generalization to all kernel datasets. Some relevant full texts were unavailable or incompletely read.

Self-review: passed. Independent audit: not yet performed.
