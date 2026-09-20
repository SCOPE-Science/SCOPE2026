# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

For the Holling type-II model, direct substitution of
\[
\widetilde\alpha
=
\alpha+
\frac{y}{1-x^4}
\left(\frac{A}{B+x}-\frac{a}{b+x}\right),
\qquad
\widetilde\delta
=
\delta+x\left(\frac{C}{B+x}-\frac{c}{b+x}\right)
\]
into the equations with constants \((A,B,C)\) cancels exactly to the original equations with constants \((a,b,c)\). The same calculation with \(B\,y+x\) in the denominator proves the ratio-dependent family. No asymptotic or numerical approximation is involved.

The local admissibility statement follows by continuity on a compact interval. If the original constants lie in the interior of their allowed sets and \(\delta\) has a strictly positive margin, sufficiently small changes of \((a,b,c)\) keep the constants admissible and keep the transformed \(\delta\) positive. The source paper does not constrain \(\alpha\) to be positive and reports fitted negative values, so no additional positivity obstruction arises there.

The fixed-time argument in the source paper does not invalidate the gauge. Structural identifiability of an autonomous model exploits the fact that the same parameter values persist over the entire trajectory. In the non-autonomous model, the two unknown functions can vary with time and absorb changes in the three constants exactly.

The repair identities are also exact. With known \(\alpha\), the Holling equation gives \(1/r=x/a+b/a\); the ratio-dependent equation gives \(1/r=x/a+(b/a)y\). The stated generic rank conditions then determine \(a,b\), and known \(\delta\) determines \(c\).

The symbolic artifact verifies all four equation-level cancellations and both repair identities and reports `all_symbolic_checks_passed = True`.

## Originality

**PASS, with a narrow source-specific novelty claim.**

The broad principle is known: time-varying unknown parameters cannot generally be treated as ordinary constant parameters in a structural-identifiability calculation. Martinelli's arXiv:2211.13507 explicitly treats time-varying parameters as unknown inputs and develops general identifiability analysis for them. Villaverde's 2019 review and subsequent unknown-input literature make the same conceptual distinction. Xue, Miao, and Wu also discuss ODE inference with both constant and time-varying coefficients. None of this general theory is claimed as new.

The source-specific claim is that arXiv:2609.20793v1's two displayed non-autonomous Moose–Wolf models possess the explicit three-constant indistinguishability families given in `RESULT.md`. These families directly contradict the paper's stated inference from identifiability of the constant-\(\alpha,\delta\) submodel to absence of redundancy in the time-varying model.

Searches by the source identifier, exact title, Moose–Wolf model terminology, structural identifiability, time-varying parameters, unknown inputs, and equivalent predator–prey terminology found no prior public comment giving this explicit correction. The current SCOPE repository was checked by source identifier and claim family and contained no overlap.

The full literature on every possible predator–prey identifiability model was not exhaustively inspected. General unknown-input identifiability theory is sufficiently established that no broad novelty is claimed. A contemporaneous, unindexed author revision or comment on arXiv:2609.20793 remains the main residual originality risk.

## Value

**PASS.**

The result changes the interpretation of the inverse problem at the structural level. Under the stated non-autonomous ODE model, even perfect continuous observations of both populations cannot uniquely identify the three constants if the two rates are allowed to remain unknown functions. Thus observational density and noise reduction alone cannot resolve the ambiguity.

This is directly relevant to the source paper because simultaneous estimation of the time-dependent rates and constant interaction parameters is one of its main contributions, and structural identifiability is presented as a prerequisite for interpreting that estimation. The explicit gauge also provides a constructive repair principle: independent information or appropriately restricted functional models for the time-dependent rates are needed to identify the constants.

## Limitations

The claim is about the mathematical ODE model with unknown functions \(\alpha(\tau)\) and \(\delta(\tau)\), not about exact injectivity of the paper's particular finite neural-network architecture. If a fixed architecture is declared to be part of the model class, exact structural identifiability must be reanalyzed for that enlarged finite-dimensional parameterization.

The displayed reconstruction excludes \(x=1\) to avoid division by \(1-x^4\). At \(x=1\), the prey equation is independent of \(\alpha\), so the exceptional value does not supply missing information about that function.

The result does not assess practical forecast accuracy, ecological model adequacy, or the usefulness of one regularized representative selected by the training procedure.

## Sources inspected

- arXiv:2609.20793v1, full accessible HTML, including Eqs. (11) and (16), the structural-identifiability argument, the network parameter constraints, and the reported parameter behavior.
- arXiv:2211.13507, accessible full text, including its explicit treatment of time-varying parameters as unknown inputs and construction of indistinguishable transformations.
- Villaverde (2019), *Observability and Structural Identifiability of Nonlinear Biological Systems*, accessible review text on constant parameters, known inputs, and unknown time-varying inputs.
- Xue, Miao, and Wu (2010), accessible full text on estimation and identifiability for ODE models with constant and time-varying coefficients.
- Current SCOPE repository records and recent changes for overlap by source identifier and equivalent terminology.

**Same-model review: passed. Independent audit: not yet performed.**
