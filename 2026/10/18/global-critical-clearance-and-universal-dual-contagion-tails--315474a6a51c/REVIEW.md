# Scientific review: global critical clearance in two interacting SIS contagions

## Correctness — PASS

The theorem is for the full deterministic symmetric two-SIS equations at precisely \(\tau=\gamma\), \(\alpha=2\gamma_2/\gamma\), with \(\gamma,\gamma_2>0\) and the closed physical triangle. Direct substitution reproduces the polynomial vector field; all three boundary fluxes point inward. The exact identity \(\frac{d}{ds}(u+3v/2)=-v(u+2hv)\) and LaSalle's principle prove convergence of **all** physical states, including boundary initial conditions. For nonzero initial states, elementary ratio ODEs show \(v/Z\to0\) and \(v/Z^2\to1/h\), which in turn give both exact physical-time amplitudes. This avoids approximating the full system by the quasi-steady reduction. The verification program checks symbolic identities and 15 finite-time numerical examples; the latter are consistency tests rather than infinite-time proofs.

## Originality — PASS, with historical-priority risk

The closest same-model article, Hébert-Dufresne, Simon and Kiss (2026; arXiv:2610.05467v1, Appendix 6.2.4), supplies the state equations and **already identifies** both parameter thresholds; that threshold identification is not claimed here. The article's argument classifies the signs of the leading local bifurcation coefficient away from their equality, but does not provide global critical convergence, an exact Lyapunov function, or both asymptotic amplitudes for its original two-dimensional system. The 2019 Hébert-Dufresne–Scarpino–Young work identifies dynamical equivalence and qualitative transition behavior, not this equality-case quantitative theorem. Earlier general critical-exponent theorems are plausible; this review assigns originality to the conjunction of a global all-parameter critical theorem and the recovery-independent doubly infected amplitude, not to the familiar \(t^{-1/2}\) exponent in isolation. No equivalent implication was identified in the inspected primary texts or targeted mathematical comparisons, but priority remains subject to independent literature verification.

## Mathematical value — PASS

The equalities defining the critical boundary leave the sign-of-derivative bifurcation test degenerate. The exact boundary dynamics are therefore a natural analytical question, not an arbitrary parameter slice. The result resolves whether positive equilibria or nontrivial invariant states survive on that boundary and determines the physically observable decay rates separately for singly and doubly infected fractions. The doubly infected fraction has an unexpectedly parameter-independent leading amplitude when the interaction strength is tuned with its clearance rate, giving a quantitatively testable distinction between two classes.

## Closest literature and limitations

The 2026 paper is the closest and supplies the equations as prior work; the 2019 paper establishes the interacting-contagion interpretation. Related critical-relaxation results for distinct epidemic equations do not imply the full two-contagion claim. The theorem is deterministic, well mixed, symmetric, and restricted to the exact critical line; stochastic finite-network extinction and nonsymmetric data are not addressed. A comprehensive historical-priority audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
