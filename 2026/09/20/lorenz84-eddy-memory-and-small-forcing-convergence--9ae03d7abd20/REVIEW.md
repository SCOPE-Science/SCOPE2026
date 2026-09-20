# Review: Lorenz-84 eddy-memory law and small-forcing convergence

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The central identity is exact: with \(R=Y^2+Z^2\) and \(U=F-X\), the first Lorenz-84 equation gives \(\dot U=R-aU\). Backward variation of constants on any bounded complete orbit yields the stated positive memory kernel, hence \(X\le F\). If \(G\ne0\), equality would force \(Y=Z=0\) on a past interval, contradicting \(\dot Y=G\).

For a compactly supported invariant probability measure, applying the generator to an arbitrary antiderivative \(H(X)\) yields \(\int h(X)[a(F-X)-R]d\mu=0\) for every continuous \(h\). This is equivalent to \(E[R\mid X]=a(F-X)\). The covariance identity follows by taking \(h=X\), and the variance inequality follows from total variance. The symbolic artifact independently checks the underlying polynomial identities with zero residual.

For \(F<1\), the complex eddy variable \(W=Y+iZ\) satisfies \(\dot W=[(X-1)+ibX]W+G\). The memory barrier gives \(X\le F\), so its homogeneous propagator decays at least as \(e^{-(1-F)t}\) on every bounded complete trajectory. This proves \(|W|\le |G|/(1-F)\) and then the lower bound on \(X\). Comparing two bounded complete trajectories gives the sup-norm estimates
\[
P\le (2M/a)V,\qquad
V\le \sqrt{1+b^2}(M/(1-F))P,
\]
with \(M=|G|/(1-F)\). The stated strict inequality makes their product less than one, forcing the two trajectories to coincide. The exact energy identity and a Young inequality give a bounded absorbing set, so the finite-dimensional flow has a compact global attractor; since bounded complete trajectories are unique, that attractor is a singleton equilibrium and every forward trajectory converges to it.

## Originality

**PASS, to the best of our knowledge.** The checked literature was searched for exact and synonymous formulations involving Lorenz-84 invariant measures, eddy-energy/zonal-flow balances, covariance or conditional-expectation identities, recurrent-set bounds, global attraction, and small nonzero forcing.

- Lorenz (1984) introduces the equations, physical interpretation, and an energy argument establishing boundedness. The present result does not claim that dissipativity is new.
- Pelino and Pasini (2001) explicitly study dissipation, geometry and a mechanism of energy transfer in Lorenz-84. Only the abstract and bibliographic descriptions were accessible; the full equations/theorems were not inspected. This is the strongest prior-coverage risk for an equivalent energy-transfer identity, so novelty is not assigned to the raw scalar or total-energy identities alone.
- Wang, Yu and Wen (2014) was inspected in full accessible text. It develops equilibrium stability, local Hopf bifurcations, numerical phase diagrams and a topological-horseshoe analysis. Searches of that text did not locate invariant-measure, conditional, covariance, or global-stability statements matching the present theorem. It cites Yu (2006) for the simpler \(G=0\) dynamics; Yu's full article was not inspected, so the unforced specialization is not treated as an originality basis.
- Anguiano and Caraballo (2014) prove pullback and uniform attractors and dimension estimates for non-autonomous Lorenz-84 variants. The located statements are attractor-existence results, not the present autonomous stationary conditional law or the explicit small-nonzero-forcing collapse criterion.
- Vissio and Lucarini (2018) explicitly compare invariant measures of Lorenz-84-based models using moments and Wasserstein distance. The open-access article was inspected for this statistical use; no exact conditional eddy-energy identity or the global convergence criterion was located. This makes the exact law directly relevant as a benchmark for such statistical comparisons.
- Recent Lorenz-84 work studies rigorous homoclinics, multistability, detailed attractor geometry and control. No located statement matches the present package.
- Naser, Abdel Aal and Gumah (2026) is the closest current global-stability item found. Its accessible abstract emphasizes attractivity under vanishing forcing terms and asymptotic/exponential stability in unforced forms. The full theorem text was not inspected, so it remains a residual coverage risk; the present nonzero-forcing inequality should not be read as a claim about their inaccessible detailed hypotheses.
- Gallo, Anselmi and Lazzari (2026) use an invariant-measure moment matrix for Lorenz-84 identifiability. The accessible abstract was inspected but the full preprint could not be inspected through the available route. It is the strongest current-literature risk for exact moment relations, although the abstract states an identifiability result rather than the conditional law recorded here.

No checked source stated the combination \(E[R\mid X]=a(F-X)\), its exact covariance/variance consequences, the bounded-complete past-memory representation, the explicit \(F<1\) recurrent slab, or the sufficient nonzero-forcing global-attractor collapse condition.

## Value

**PASS.** The result links the physically interpreted eddy amplitude to the zonal-flow coordinate at both trajectory and invariant-measure levels. The conditional law is stronger than a mean balance and supplies exact diagnostics for numerical invariant measures, reduced models, and system-identification data. The support formula provides a geometric barrier for all compact recurrent dynamics. The small-forcing theorem converts those exact identities into a global uniqueness/convergence statement for nonzero forcing, excluding multistability, cycles and chaos throughout an explicit parameter region rather than only classifying local equilibrium eigenvalues.

## Scientific limitations

The convergence inequality is sufficient rather than necessary and is not claimed sharp. The conditional law assumes compact support. The model is autonomous; seasonal, stochastic and coupled variants are outside the theorem. The full text of Pelino--Pasini (2001), Yu (2006), and Naser--Abdel Aal--Gumah (2026) was not inspected, and the full Gallo--Anselmi--Lazzari (2026) preprint was not accessible through the inspected route. These are the principal identified prior-coverage risks. In particular, the \(G=0\) specialization is not claimed as novel on its own.

## Checked sources

- https://doi.org/10.1111/j.1600-0870.1984.tb00230.x
- https://doi.org/10.1016/S0375-9601(01)00764-2
- https://doi.org/10.1063/1.2953589
- https://doi.org/10.1155/2014/296279
- https://doi.org/10.3934/dcds.2014.34.3901
- https://doi.org/10.5194/npg-25-413-2018
- https://doi.org/10.1137/16M1079956
- https://doi.org/10.1063/5.0287725
- https://doi.org/10.1007/s40324-026-00429-8
- https://arxiv.org/abs/2607.18490
