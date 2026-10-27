# Scientific review

## Correctness

**PASS.** The claim is a complete equilibrium classification for a precisely specified continuous-time, flow-regulated SIS model on \(K_{m,n}\). At stationarity and positive total load, every load is positive and every infection probability is strictly below one. The sum-of-edge-squares identity forces \(\beta_i/(1-x_i)\) to be constant throughout any connected undirected graph. On a complete bipartite graph, the strict monotonicity of \(x/(1-x)^2\) then forces within-part symmetry. The resulting two equations reduce to explicit infection odds, and conserving total load gives a single positive parameter exactly above the stated critical load. Back-substitution proves existence, and the preceding forced reductions prove uniqueness; boundary states have also been excluded. The separate Jacobian computation supports only the stated local properties of the disease-free equilibrium. The standard-library checker confirms the full equations for 128 exactly rational and 972 floating-point positive cases and 363 disease-free cases.

## Originality

**PASS, with a bibliographic residual risk.** Punzo (2022) introduces the precise coupled equations and already proves total-load conservation and a general spectral threshold. It provides a special exact regular-graph equilibrium and otherwise approximations, not the class-by-class exact formula for irregular complete bicliques. The equal-part case and generic epidemic threshold are explicitly excluded from any novelty claim. The opposite ordering itself is a consequence of the source model's general stationary-load identity; the new result computes the actual classwise levels on unequal bicliques rather than first establishing an anti-correlation principle. Mei et al. (2017) use a fixed scalar infection rate rather than an endogenous load vector, while Meloni et al. (2009) use packet-routing infection mechanisms. Read portions of the primary full texts, searches for the same model and equivalent formulae, and relevant indexed research descriptions yielded no stronger covering claim. Search failure is not proof of universal originality; a previously unindexed exact reduction is possible.

## Mathematical value

**PASS.** The exact steady-state solution closes a natural gap in the source model: heterogeneity in node degrees usually obstructs the source's explicit endemic formula. Unequal bicliques, including arbitrarily large star-like networks, are a fundamental nonregular test family. The theorem gives exact per-community infection and load levels for all positive parameters, forces symmetry without presupposing it, and makes the structurally implied opposing risk–load ordering quantitative. These exact classwise values matter in interpreting flow-regulated network contagion and cannot be obtained by merely substituting the regular-graph solution.

## Closest sources and limitations

- G. Punzo, *An SIS network model with flow driven infection rates*, Automatica 137 (2022), 110107. Sections 2–5 and Appendix were inspected in the lawful open full text. Its regular-graph exact solution applies to \(m=n\), not to \(m\ne n\).
- W. Mei, S. Mohagheghi, S. Zampieri and F. Bullo, *On the Dynamics of Deterministic Epidemic Propagation over Networks*, 2017, arXiv:1701.03137. Its Section 4 studies fixed-rate SIS rather than the coupled flow law.
- S. Meloni, A. Arenas and Y. Moreno, *Traffic-driven epidemic spreading in finite-size scale-free networks*, PNAS 106 (2009). The inspected full text instead concerns packet movement and scale-free traffic.

The result does not prove global attraction of the positive equilibrium, describe stochastic SIS extinction, or extend to directed/weighted networks. The independent audit is not performed. Equivalent formulations in unpublished or unindexed literature cannot be ruled out solely by database searches.

Self-review: passed. Independent audit: not yet performed.
