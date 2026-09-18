# Exact gauge family defeats structural identifiability in the time-varying Moose–Wolf models

## Result

Singh and Kumari, arXiv:2609.20793v1, study two non-autonomous predator–prey systems in which the prey growth rate and predator natural-death rate are unknown functions of time while three interaction coefficients are estimated as constants. Their structural-identifiability check replaces the two unknown functions by constants, establishes identifiability for that autonomous surrogate, and then argues that the time-varying model has no structural redundancy.

For the non-autonomous differential equations themselves, there is instead an explicit parameter–function gauge. Even perfect continuous observation of both state variables does not identify the three constant interaction coefficients unless additional information or restrictions are imposed on the time-varying rates.

Throughout, let \(I\) be an interval and suppose
\[
x,y\in C^1(I),\qquad x(t)>0,\quad y(t)>0,\quad x(t)^4\ne 1
\]
for every \(t\in I\).

### Holling type-II model

Consider
\[
\dot x=\alpha(t)x(1-x^4)-\frac{Axy}{B+x},
\qquad
\dot y=\frac{Cxy}{B+x}-\delta(t)y,
\]
where \(A,B,C>0\) are constants.

For **every** choice \(A,B,C>0\), define
\[
\boxed{
\alpha_{A,B}(t)
=
\frac{\dot x(t)/x(t)+A\,y(t)/(B+x(t))}
     {1-x(t)^4}
}
\]
and
\[
\boxed{
\delta_{B,C}(t)
=
\frac{C\,x(t)}{B+x(t)}
-\frac{\dot y(t)}{y(t)}.
}
\]

Then the prescribed trajectory \((x(t),y(t))\) is an exact solution of the model with constants \((A,B,C)\) and time-varying rates \((\alpha_{A,B},\delta_{B,C})\).

Hence the map from
\[
(A,B,C,\alpha(\cdot),\delta(\cdot))
\]
to the fully observed state trajectory is not injective. The ambiguity contains a three-parameter continuum in the constant coefficients alone.

### Ratio-dependent model

For
\[
\dot x=\alpha(t)x(1-x^4)-\frac{Axy}{By+x},
\qquad
\dot y=\frac{Cxy}{By+x}-\delta(t)y,
\]
the analogous exact family is
\[
\boxed{
\alpha_{A,B}(t)
=
\frac{\dot x(t)/x(t)+A\,y(t)/(B\,y(t)+x(t))}
     {1-x(t)^4},
}
\]
\[
\boxed{
\delta_{B,C}(t)
=
\frac{C\,x(t)}{B\,y(t)+x(t)}
-\frac{\dot y(t)}{y(t)}.
}
\]

Again, every positive constant triple \(A,B,C\) can be paired with reconstructed time-dependent rates that reproduce exactly the same observed trajectory.

## Proof

Divide the prey equation by \(x>0\) and the predator equation by \(y>0\). In the Holling case this gives
\[
\frac{\dot x}{x}
=
\alpha(t)(1-x^4)-\frac{Ay}{B+x},
\qquad
\frac{\dot y}{y}
=
\frac{Cx}{B+x}-\delta(t).
\]
Solving these two scalar equations pointwise for \(\alpha(t)\) and \(\delta(t)\) yields the boxed formulas. Substitution recovers the prescribed \(\dot x,\dot y\) identically.

The ratio-dependent calculation is identical after replacing \(B+x\) by \(By+x\).

No numerical approximation or local linearization is used.

## Positivity and admissible parameter restrictions

The ambiguity is not merely an artifact of permitting pathological signs.

On a compact interval with positive \(x,y\), the factors
\[
\frac{x}{B+x}
\quad\text{and}\quad
\frac{x}{By+x}
\]
have positive minima. Therefore, for every fixed \(B>0\), choosing \(C\) sufficiently large makes the reconstructed \(\delta(t)\) strictly positive on the whole interval.

If \(x<1\) on a compact interval, then \(1-x^4\) is positive and bounded away from zero. If positivity of \(\alpha\) is additionally imposed, choosing \(A\) sufficiently large makes the numerator of \(\alpha_{A,B}\) positive. More generally, around any admissible representation whose rate functions stay a positive distance from a sign boundary, sufficiently small changes in the constants preserve admissibility by continuity.

A nondegenerate bound on a constant coefficient does not restore structural uniqueness by itself. Two different admissible values inside such a bound can be offset exactly by the corresponding time-dependent rate.

## Why the autonomous identifiability check does not transfer

The autonomous surrogate replaces \(\alpha(t)\) and \(\delta(t)\) by two scalar constants. Those two numbers must satisfy the ODE at every observation time, so data from different times are coupled through the same unknowns.

Once \(\alpha\) and \(\delta\) are arbitrary unknown functions, that cross-time coupling disappears: the two ODEs can be solved pointwise for the two rate functions after any choice of \(A,B,C\).

Accordingly, evaluating the functions at one time and regarding those two values as fixed numbers does not turn the original non-autonomous inverse problem into the globally autonomous one. At a single time, the state derivatives provide only two scalar relations, while the function values can compensate changes in the constant coefficients exactly.

Thus global identifiability of the frozen autonomous model is not evidence of structural identifiability of the time-varying model.

## Consequence for the inverse problem

At the differential-equation level, full and noiseless observation of both populations identifies only combinations such as
\[
\alpha(t)(1-x^4)-\frac{Ay}{B+x}
\]
or
\[
\alpha(t)(1-x^4)-\frac{Ay}{By+x},
\]
together with the analogous predator combination. It does not uniquely separate the constant interaction parameters from the two unknown rate functions.

Unique ecological parameter recovery therefore requires additional structure, for example independently measured forcing functions, a finite-dimensional parametric law for \(\alpha,\delta\), extra observables tied directly to those rates, or other scientifically justified constraints that break the gauge.

This does **not** imply that a trained predictor cannot fit or forecast the population trajectories. It means that a good state fit, even an exact one, cannot by itself certify unique recovery of the ecological constants and free time-varying rates.

## Compact verification

`artifacts/verify_gauge.py` constructs a smooth positive test trajectory and reconstructs the two rates for two distinct constant triples in both response models. All four reconstructed rate pairs remain positive in that example, while the largest ODE residual over 1001 sample points is
\[
1.39\times 10^{-16},
\]
consistent with floating-point roundoff. This check is supplementary to the exact algebraic proof.

## Relation to prior identifiability theory

The general phenomenon that time-varying parameters must be analyzed as unknown inputs is established in the identifiability literature. In particular, Martinelli develops analytical identifiability methods specifically for nonlinear ODEs with time-varying parameters, and later work uses continuous symmetries to characterize indistinguishable states and parameters. Conrad and Eisenberg likewise emphasize that replacing time-varying quantities by constants can change identifiability properties.

Those general principles are not claimed as new here. The source-specific contribution is the explicit gauge for both Moose–Wolf models in arXiv:2609.20793v1 and the resulting direct contradiction of the paper's inference from its frozen autonomous identifiability calculation to its non-autonomous inverse model.

## Originality status

To the best of our knowledge, no correction, comment, or source-specific note located for arXiv:2609.20793v1 gives these exact indistinguishable families or identifies this structural-identifiability failure. Searches included the exact title and identifier, structural/non-identifiability terminology, time-varying parameter formulations, Holling type-II and ratio-dependent predator–prey formulations, and equivalent unknown-input language.

The source is very recent, so an unindexed author revision or discussion remains the principal residual originality risk.

## Limitations

1. The theorem treats the time-varying rates as functions in the differential-equation model. A fixed finite neural-network architecture defines a smaller function class and need not represent every compensating function exactly. Architecture-restricted identifiability would be a different parametric problem and must be analyzed separately.
2. The formulas require \(x,y>0\). They also require \(x^4\ne1\) to reconstruct \(\alpha\). Contact with the carrying-capacity level \(x=1\) requires a separate compatibility analysis.
3. The theorem does not assess statistical uncertainty, optimization quality, predictive skill, or biological plausibility of every member of the gauge family.
4. The result does not show that the constant-parameter autonomous surrogate is unidentifiable; it shows that identifiability of that surrogate does not carry over to the model with free time-varying rates.

## References

- A. Singh and N. Kumari, *A physics-informed inverse modeling framework for Moose–Wolf dynamics from limited and noisy data in Isle Royale National Park*, arXiv:2609.20793v1 (2026). https://arxiv.org/abs/2609.20793
- A. Martinelli, *Identifiability of nonlinear ODE Models with Time-Varying Parameters: the General Analytical Solution and Applications in Viral Dynamics*, arXiv:2211.13507. https://arxiv.org/abs/2211.13507
- A. Martinelli, *Revisiting the observability and identifiability properties of a popular HIV model*, Journal of Theoretical Biology 584 (2024), 111780. https://doi.org/10.1016/j.jtbi.2024.111780
- J. R. Conrad and M. C. Eisenberg, *Examining the impact of forcing function inputs on structural identifiability*, arXiv:2407.02771. https://arxiv.org/abs/2407.02771
