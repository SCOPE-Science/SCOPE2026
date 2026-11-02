# Scientific review of the two-anchor cycle-coherence theorem

## Correctness — PASS

The claim is the exact weak-frequency-heterogeneity coefficient and its all-cycle-size optimal two-pin geometry, plus persistence of the strict optimizer at sufficiently small nonzero disorder. The nonlinear local equilibrium follows from a strictly positive grounded Laplacian and the analytic implicit-function theorem. The complex order parameter produces the mean-centered projector \(P=I-\boldsymbol1\boldsymbol1^{\mathsf T}/M\), giving \(\operatorname{tr}(L_g^{-1}PL_g^{-1})\) after averaging over independent unit-variance quenched frequencies. The exact Dirichlet Green kernel yields two checked fourth- and fifth-degree polynomial sums. Their combination is strictly concave in the arc product \(y=\ell(M-\ell)\), forcing global minimizers to be either adjacent or maximally separated. Endpoint comparison proves the unique threshold between \(N=6\) and \(N=7\). Uniformity of the even Taylor remainder at each fixed graph size transfers the strict leading comparison to actual weak-disorder expected coherence. The 355 independent deterministic checks include matrix inverses, symbolic identities, cycle enumeration, and local nonlinear equilibrium regression.

**Limits.** The theorem makes no claim for general fixed disorder, finite-rate resetting, arbitrary graphs, or globally selected nonlinear attractors. Numerical regression supports but does not prove the infinite family.

## Originality — PASS, qualified

The closest paper, Paramero-Arias and Riascos, arXiv:2610.21842 (2026-10-15), explicitly supplies the grounded-Laplacian reduction and the unpinned mean-centered order-parameter quadratic (its stationary linear expression, Eq. (29)); these are credited. The new component is the complete explicit cycle optimization, including the finite-size *adjacent-to-balanced* inversion at exactly \(N=7\) and transfer to the locally stable nonlinear model at small disorder. An operator expression for all graphs is not the same statement as a sharp global optimum over all two-anchor placements.

Fitch and Leonard (arXiv:1407.1569), Patterson, McGlohon and Dyagilev (arXiv:1412.6595), and Patterson, Yi and Zhang (arXiv:1708.06873) obtain even-spacing results for time-white-noise leader-following objectives involving \(\operatorname{tr}(L_g^{-1})\). Those results do not imply the present mean-centered *quenched-frequency* \(\operatorname{tr}(L_g^{-1}PL_g^{-1})\) criterion. Targeted public mathematical-literature searches by object, observable, graph geometry, and source identifiers returned no equivalent claim; negative search results are not treated as proof of novelty.

**Residual risk.** A broader unlocated theorem on relative-phase pin-placement optimization might cover the conclusion. The general source Eq. (29) does imply the correct objective when specialized, but the explicit all-size minimizer and its size-six/size-seven inversion require the additional polynomial optimization given here. Independent originality review has not occurred.

## Value — PASS

The distinction between phase agreement *within the unreset population* and tracking the pin phase is physically motivated by the actual Kuramoto subpopulation order parameter, not by an arbitrary norm. The theorem completely determines the globally optimal location of a fixed pair of permanently reset nodes for every finite cycle size in a well-defined weak-disorder regime. Contrary to the standard evenly spaced leader heuristic, adjacent pins give better internal coherence on three nontrivial small graph sizes; balanced pins take over sharply at seven vertices. The derivation isolates the mathematical cause: subtraction of the subpopulation's collective phase mode. The classification can guide small-ring pin-placement experiments and prevent transfer of fixed-reference tracking conclusions to an order-parameter objective without a new proof. It is not presented as a universal graph-design theorem.

## Sources and limitations

The four arXiv papers named above were compared at the level of objective, assumptions, implication, and exact result, not just overlapping words or titles. The relevant source material included the 2026 paper's linearized model and order-parameter equations, and the earlier papers' cycle leader-optimality and trace-of-inverse performance derivations. The reproducibility file checks the supplied coefficient rather than replacing the analytical proof. No external mathematical validation or publication-priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
