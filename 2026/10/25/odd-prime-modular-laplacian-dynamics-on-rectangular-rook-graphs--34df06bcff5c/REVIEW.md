# Self-review

## Correctness — PASS

The signed graph-Laplacian formula and the identities \(P^2=aP\), \(Q^2=bQ\) reconstruct the dynamics. Tensor eigenbases establish the completely nondivisible case. If one dimension is divisible by the odd prime, the rank-one square-zero all-ones matrix creates size-two Jordan blocks and the sharp depth-two bound. If both dimensions are divisible, \(L^2=2J_m\otimes J_n\) has rank one and \(L^3=0\); a row/column-sum argument independently yields \(\operatorname{rank}L=m+n-2\), proving one size-three block and exact convergence counts. The canonical nilpotent-plus-invertible splitting, \(\dim\ker(L^t-I)\) and Möbius inversion establish every joint depth/period count. The bundled verifier checks these formulas by a separately constructed matrix and complete small-state enumeration. Finite tests are corroboration only.

## Originality — PASS, qualified

The closest inspected graph-specific source is Ducey, Gerhard and Watson (2015), which studies square rook-graph Laplacian Smith and critical groups and points to earlier rectangular integer Smith work. Those **two-sided equivalence** invariants do not classify the powers of the modular Laplacian under **similarity**. Moreno, Bollman and Aviño-Díaz (2006) supply general finite-field linear-dynamical methods, not an explicit all-size rook census. Peeters (2002), Theorem 3.4, already determines ranks of powers of a shifted adjacency matrix of the **square** Hamming graph when the field characteristic divides its alphabet size; in its two-coordinate specialization it covers the nilpotency-rank subcase for equal divisible dimensions. The asserted original extension concerns all unequal rectangular boards, the mixed-residue nonzero Jordan cases, and the complete simultaneous depth-period formulas, not the known square power-rank calculation. An inspected published prime-power modular lattice-kernel dilation has different translation geometry and does not imply the rectangular census. Accessible previous binary-parity work on complete-graph Cartesian products does not cover the odd-prime case. Searches did not find an equivalent statement, but hidden historical equivalences are still possible; not all cited older Smith papers were read in full.

## Mathematical value — PASS

The exact modular attractor phase diagram distinguishes sharp depths one, two and three by arithmetic divisibility, identifies the size-independent fraction \(1-1/p\) requiring the full three-step extinction when both dimensions vanish modulo \(p\), and counts every primitive orbit and transient stratum. This gives a complete natural family classification rather than a single experimental exception.

## Limitations and closest literature

No claim is made for general graphs, composite moduli, sequential chip-firing or all published history. The finite-field tools are classical; the asserted addition is the explicit complete dynamical census for rectangular rook Laplacians in odd prime characteristic. General linear methods can potentially reproduce it with further parameter-specific work. Independent external review remains open.

Self-review: passed. Independent audit: not yet performed.
