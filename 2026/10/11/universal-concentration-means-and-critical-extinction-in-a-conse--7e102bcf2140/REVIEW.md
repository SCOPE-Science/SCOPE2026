# Scientific assessment: exact means and critical extinction

## Correctness — PASS

For the given positive four-species system, differentiation of \(\Phi=\log x-(1+p)y/q-[\,(1+p)/q+1/s\,]z\) yields **exactly** \(\dot\Phi=C-r-Dx\); mass conservation and the two linear balances give the four time-average coordinates with bounded endpoint corrections. The lower-barrier argument for \(\Phi\) proves eventual positivity of \(x\) when \(C>r\), so no undocumented recurrence assumption is needed. At \(C=r\), the comparison \(\dot x\le-x^2\), stable convolution kernels, and dominated convergence imply both asymptotic ratios and the universal inverse-time coefficient. The logarithmic integral limit follows from the same exact identity. The symbolic checker in the deliverable returns \(\texttt{CHECK_OK}\). These arguments do not rely on finite numerical experiments as substitutes for proof.

## Originality — PASS with bounded residual risk

The closest work is Boros–Hofbauer, arXiv:2202.11034v2, Equation (8) and Theorem 14. Its full text was inspected: it establishes the equilibrium, existence of multiple cycles, and permanence, but the inspected analysis does not state the exact invariant-measure barycenter, all-trajectory \(O(T^{-1})\) mean vector, or critical \(t^{-1}\) and logarithmic-integral asymptotics. The definitions and relevant introduction of Joshi–Craciun, *Foundations of static and dynamic absolute concentration robustness*, were also inspected; their pointwise dynamic ACR differs from time-averaged concentrations on nonconstant cycles. Additional searches compared time-average invariants, mass-action oscillator aliases, published-finding corpus records, and prior claims; no result covering the full theorem was identified. Closest cross-model published-finding corpus results concern other flows' stationary moments and do not imply this specific formula. A literature search does not certify absolute novelty; unindexed general chemical-kinetic averaging results remain a possible priority risk.

## Value — PASS

The source proves this chemically motivated mass-conserving system can exhibit **three coexisting recurrent choices** (a stable equilibrium and two different-stability cycles). It is therefore meaningful—not simply an equilibrium calculation—that all observable species **time means** coincide exactly for those regimes, with finite-time errors reduced to explicit endpoints. The same analytic mechanism gives a sharp structural transition at the natural total-mass boundary: a universal \(t^{-1}\) extinction profile and a finite logarithmically centered cumulative output. Those two linked results constrain data interpretation for an entire parameter family, independent of the unknown cycle periods and basins.

## Scope and residual limitations

The theorem concerns deterministic positive solutions of the specified four-component ODE and the full conserved total \(C\), not individual long-time pointwise convergence above threshold. The \(O(T^{-1})\) constant can depend on the initial point; compact-support assumptions on invariant measures exclude boundary measures. The source's cycle coexistence is cited, not reproved or claimed novel. Broader unpublished and nonindexed results were not exhaustively excluded.

Same-model review: passed. Independent audit: not yet performed.
