# Scientific review: first homology of rook neighborhoods

## Correctness — PASS
The result concerns the open neighborhood complex for every pair of integers \(m,n\ge3\), with no finite-range extrapolation. A complete 1-skeleton gives a unique normalization of each 1-cocycle by a coboundary. The proof exhausts the root, row, column, and mixed triangle types, thereby bounding normalized cocycles by parameters \(t_{ij}\), \(p_{j\ell}\), and \(q_{ik}\), with a crucial relation between opposite corners. Explicit cocycles realize all permitted parameters for **arbitrary abelian coefficients**, distinguishing the free cases from order-two torsion. The universal coefficient theorem then identifies integral homology. The executable checks explicit generators and first mod-prime Betti numbers on seven finite boards; exact integer Smith calculations on three boards offer additional consistency evidence. The all-parameter statement is proved symbolically, not inferred from computations.

## Originality — PASS, with residual risk
The closest full-text results are the exact four-by-four calculation, which supplies one previously known special case, and an all-parameter rook-neighborhood result proving higher homology and the row-column cofiber but explicitly **not** first homology. Neither supplies the new low-width/free-versus-torsion threshold; the higher-homology statement alone does not determine the integral connecting maps needed for \(H_1\). The literature on small-degree graphs excludes the general rook family, and generic fundamental-group correspondences do not compute its explicit first homology. The different width-two family is outside the hypotheses, while closed-neighborhood, three-cut, clique, and independence complexes have different face conditions. Searches included rook/Hamming/line-graph aliases and integrality/torsion variations. An unindexed equivalent result remains possible.

## Mathematical value — PASS
A complete integral first-homology classification is a natural invariant of the Lovász neighborhood complex for the entire rectangular rook-graph family. The sharp parameter-dependent transition \(\mathbb Z^2\to\mathbb Z\to\mathbb Z/2\mathbb Z\) separates free cycles from genuine torsion, is not implied by the previously determined high-degree homology, and offers a reusable cohomological method rather than a one-board computation. The four-by-four case is explicitly credited as prior work.

## Scope and integrity
No claim is made about \(\pi_1\), complete homotopy type, higher integral homology, or width-one/two rook graphs. Finite checks are not a substitute for the algebraic argument. The finding has undergone self-review only; no independent mathematical validation or audit has occurred.

Self-review: passed. Independent audit: not yet performed.
