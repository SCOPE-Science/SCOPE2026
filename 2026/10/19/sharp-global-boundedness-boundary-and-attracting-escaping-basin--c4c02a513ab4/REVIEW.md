# Scientific assessment

## Correctness

**PASS.** The one-step forcing norm is at most \(3\), giving a direct absorbing bound for \(0<T<2\) and a strict exterior growth bound for \(T>2\). The delicate endpoint is independently resolved: at \(T=2\) the bias cancels in the second iterate, and dominant diagonal coupling forces every sufficiently large coordinate inward by at least \(53/25\) every two steps. That establishes an actual compact absorbing set rather than extrapolating an experiment. At \(T=9/4\), \(\alpha=1/4\), the fixed-point contraction and Jacobian row-sum inequalities are rational and strict; the attracting square and disjoint open escape region follow. The normalized escape limit is an absolutely convergent geometric series. The finite verification program checks constants and trajectories but is not substituted for those proofs.

## Originality

**PASS, with residual historical risk.** The 2023 originating article [1] was read through its defining equations, equilibrium stability treatment, numerical bifurcations, conclusions and appendices. It does not supply the all-initial global boundary, the nonlinear neutral-step argument, or a certified fixed-point/escape coexistence witness. The article's numerically observed finite-orbit attractors are not an implication of boundedness on the whole plane. General bounded-forcing affine estimates address strict steps but become neutral and inconclusive at \(T=2\), whereas the present endpoint proof uses the signed structure of the coupled saturating activation. Searches for alternate names (saturating neural Euler map, two-cell tanh map, absorbing set, escape basin, timestep instability) located no identical theorem. Results about different neural maps or generic numerical integrators do not contain the specific endpoint and basin statements. Exact historical priority cannot be guaranteed against unindexed or differently phrased results.

## Mathematical value

**PASS.** The step parameter is central to the paper's proposed digital-neuron dynamics. The source reports bounded spiking and chaotic patterns at steps exceeding two for selected initial conditions; therefore whether such behavior is globally bounded is a natural interpretive question, not an arbitrary parameter slice. The theorem supplies the sharp all-initial threshold, resolves its noncontractive critical endpoint using an original two-step mechanism, and proves simultaneous positive-size attraction and escape basins with fully explicit constants. It establishes a global limitation of finite-initial-condition bifurcation diagrams without claiming those diagrams are wrong or that the outer escape region occupies the whole plane. No broader chaos theorem is asserted.

## Prior work and limits

[1] A. Buscarino, C. Famoso, L. Fortuna, *Bifurcations in a new two-cell spiking map: a numerical and experimental study*, Nonlinear Dynamics 111 (2023), 20361–20375, DOI 10.1007/s11071-023-08897-7.

The result applies to deterministic real iterations at the source paper's fixed coupling parameters. It does not characterize basins inside the sufficient escape radius, noisy neuron models, or hardware-quantized recurrence. The exterior threshold is an explicit sufficient radius, not an optimal one. Priority risk remains for general results on diagonally dominant saturated Euler recurrences not found in the investigated literature.

Self-review: passed. Independent audit: not yet performed.
