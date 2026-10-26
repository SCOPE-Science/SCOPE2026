# Review of A source-term compatibility condition for compact aquifer wetting fronts

## Correctness

**PASS.** Under the stated full-line distributional interpretation, test functions supported inside a dry open cylinder eliminate every term except \(N(t)/n\). Since \(n>0\), the necessary condition is exactly \(N=0\) almost everywhere on the interval. The argument uses the equation and source definition printed in Bartlett–Porporato (2018), plus their zero extension beyond the wetting fronts. It does not infer a global statement from numerical experiments.

## Originality and overlap

**PASS, narrowly scoped.** The claim is not offered as a new general porous-medium theorem. It identifies the compatibility condition for the specific Boussinesq equation with additive time-only source and the paper's compactly supported zero extension. The closest general literature inspected concerns unforced finite propagation or sources that vanish with the state; neither directly supplies this model-specific qualification. The public literature search found no directly equivalent statement for this exact aquifer formula. The nearest related published material concerns different model classes and does not imply this condition.

## Value

**PASS.** The distinction matters because the paper explicitly motivates \(N(t)\) by recharge and other time-varying source/sink fluxes. A reader using a finite wetting-front profile with nonzero uniform recharge needs to know whether the PDE applies on dry ground or only on the saturated set. The result supplies that exact boundary of validity and a concrete modeling repair: state the wet-domain convention or localize the source.

## Closest literature and residual risk

The primary source is Bartlett and Porporato (2018), especially its governing equation, source/sink definition, exact profile, and wetting-front discussion. Troch et al. (2013) provides background on exact Boussinesq solutions and recharge limitations. The principal residual risk is interpretive: if the authors intended the equation only on the wet set, the issue is a missing domain/source qualification rather than a contradiction to the interior formula. This finding states that limitation explicitly.

Self-review: passed. Independent audit: not yet performed.
