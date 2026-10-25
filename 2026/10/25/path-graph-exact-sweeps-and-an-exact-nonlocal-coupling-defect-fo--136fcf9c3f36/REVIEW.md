# Review of the path-graph RCGLS finite-sweep theorem

**Correctness — PASS.** The precise algorithm is the one-predecessor \(H\)-conjugacy projection and exact line search of the referenced RCGLS Algorithm 1, on singleton sketches with nonzero coefficients. The normalized search directions form a unit-triangular basis. The projection-product rank lemma yields necessary as well as sufficient conditions for one-sweep exactness; the support induction yields exactly tridiagonal \(H\). A separate direct computation proves the exact three-coordinate energy factor, and the included checker tests the rational witness and random full-rank matrices. Zero-gradient special branches and finite-precision effects are outside scope.

**Originality — PASS, with residual risk.** The authors' Algorithm 1, its general expectation theorem, classic fully conjugate line-search theory, and generic CG short-recurrence explanations were compared against this statement. The assessed addition is the exact one-pass path graph classification and sharp three-dimensional nonlocal-coupling defect. A prior two-dimensional RCGLS stopping-time analysis is a different result. General conjugate-direction facts are credited; literature coverage is not claimed exhaustive.

**Mathematical value — PASS.** This structural characterization distinguishes graph orders requiring only adjacent conjugation from those retaining uncorrected long-range coupling. The exact final-step ratio and order-sensitive family identify a numerical reason to order sparse normal-matrix columns along paths. The conclusion is useful independently of a general IID convergence rate, but only in exact arithmetic and on generic prescribed sweeps.

**Closest literature.** Zeng–Cai–Han–Xie, arXiv:2605.25034, Algorithm 1 and Theorem 2.4; classic conjugate-directions finite termination; short-recurrence explanations for Krylov CG. Remaining risks include equivalent incomplete-Gram–Schmidt formulations in earlier literature and zero-sketch branches not covered here.

Self-review: passed. Independent audit: not yet performed.
