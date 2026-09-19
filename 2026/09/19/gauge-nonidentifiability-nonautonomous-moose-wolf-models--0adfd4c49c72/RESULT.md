# Exact gauge non-identifiability in non-autonomous Moose–Wolf models

## Result

Consider the two dimensionless non-autonomous prey–predator models in Singh and Kumari, arXiv:2609.20793v1. In both models the prey intrinsic growth rate \(\alpha(\tau)\) and predator death rate \(\delta(\tau)\) are unknown functions, while \(a,b,c\) are unknown constants.

The paper first verifies global identifiability after replacing \(\alpha(\tau)\) and \(\delta(\tau)\) by constants, and then argues that the time-dependent model has no structural redundancy because one may freeze the forcing values at a fixed time. That implication does not hold. For the stated non-autonomous models there is an explicit three-parameter family of exactly indistinguishable constant parameters and time-dependent functions, even under perfect continuous observation of both populations.

Throughout, let \(I\) be a compact time interval, let \(x,y\in C^1(I)\) be positive, and assume \(x(\tau)\ne 1\) on \(I\). The last assumption only avoids division by the theta-logistic factor \(1-x^4\); at \(x=1\), \(\alpha\) drops out of the prey equation and identifiability is not improved.

### Holling type-II response

The model is
\[
x'=\alpha(\tau)x(1-x^4)-\frac{axy}{b+x},
\qquad
y'=\frac{cxy}{b+x}-\delta(\tau)y.
\]

Suppose \((a,b,c,\alpha,\delta)\) generates a trajectory \((x,y)\). For any alternative constants \(A,B,C\) for which \(B+x(\tau)\ne0\), define
\[
\boxed{
\widetilde\alpha(\tau)
=
\alpha(\tau)
+
\frac{y(\tau)}{1-x(\tau)^4}
\left[
\frac{A}{B+x(\tau)}
-
\frac{a}{b+x(\tau)}
\right]
}
\]
and
\[
\boxed{
\widetilde\delta(\tau)
=
\delta(\tau)
+
x(\tau)
\left[
\frac{C}{B+x(\tau)}
-
\frac{c}{b+x(\tau)}
\right].
}
\]

Then the same functions \(x(\tau),y(\tau)\) satisfy
\[
x'=\widetilde\alpha(\tau)x(1-x^4)-\frac{Axy}{B+x},
\qquad
y'=\frac{Cxy}{B+x}-\widetilde\delta(\tau)y
\]
identically on \(I\). Thus \((a,b,c)\) are not structurally identifiable when \(\alpha,\delta\) are unrestricted unknown functions.

Equivalently, from a perfectly known trajectory one may choose \(A,B,C\) first and reconstruct
\[
\widetilde\alpha(\tau)
=
\frac{x'(\tau)/x(\tau)+A\,y(\tau)/(B+x(\tau))}
{1-x(\tau)^4},
\]
\[
\widetilde\delta(\tau)
=
\frac{C\,x(\tau)}{B+x(\tau)}
-
\frac{y'(\tau)}{y(\tau)}.
\]

### Ratio-dependent response

The second model is
\[
x'=\alpha(\tau)x(1-x^4)-\frac{axy}{by+x},
\qquad
y'=\frac{cxy}{by+x}-\delta(\tau)y.
\]

The corresponding exact gauge family is
\[
\boxed{
\widetilde\alpha(\tau)
=
\alpha(\tau)
+
\frac{y(\tau)}{1-x(\tau)^4}
\left[
\frac{A}{B\,y(\tau)+x(\tau)}
-
\frac{a}{b\,y(\tau)+x(\tau)}
\right]
}
\]
and
\[
\boxed{
\widetilde\delta(\tau)
=
\delta(\tau)
+
x(\tau)
\left[
\frac{C}{B\,y(\tau)+x(\tau)}
-
\frac{c}{b\,y(\tau)+x(\tau)}
\right].
}
\]

Again, these substitutions leave the observed trajectory exactly unchanged for every admissible triple \((A,B,C)\).

## Local non-identifiability survives the stated positivity constraints

The training parameterization in arXiv:2609.20793v1 constrains \(a\) to an open bounded interval after a sigmoid transformation, constrains \(b,c>0\), and enforces \(\delta(\tau)>0\) by a softplus output. It does not enforce positivity of \(\alpha(\tau)\), and the reported fitted \(\alpha\) in fact takes both signs.

Assume a representation lies in the interior of the allowed constant-parameter region and
\[
\inf_{\tau\in I}\delta(\tau)>0.
\]
Because the gauge formulas depend continuously on \((A,B,C)\), every sufficiently small change of the three constants preserves the constant-parameter constraints and preserves \(\widetilde\delta>0\). Therefore the ambiguity is local as well as global: there is an open continuum of admissible constant triples producing exactly the same full-state trajectory after compensating changes in the two time-dependent rates.

This conclusion is stronger than practical ill-conditioning. It persists with noiseless, arbitrarily dense, full-state observations.

## Why freezing the functions at one time does not transfer autonomous identifiability

The autonomous calculation in the source paper may be valid for the autonomous submodel in which \(\alpha\) and \(\delta\) are constants over the whole observation interval. Its conclusion does not transfer pointwise to the non-autonomous model.

Autonomous structural identifiability uses the temporal constraint that the same scalar parameters govern the trajectory at every time. Replacing an unknown function by its value at one time removes precisely the functional degrees of freedom that can absorb changes in \(a,b,c\). The displayed gauge families show that these compensations can be made coherently over the whole interval, so pointwise freezing cannot rule them out.

In the language of the identifiability literature, unknown time-varying parameters are unknown inputs rather than constant parameters. General methods for time-varying-parameter identifiability therefore analyze them as such.

## A simple way to break part of the gauge

The obstruction also shows what additional information is needed.

For the Holling model, if \(\alpha(\tau)\) is independently known, then
\[
r(\tau)
=
\frac{\alpha(\tau)(1-x(\tau)^4)-x'(\tau)/x(\tau)}
{y(\tau)}
=
\frac{a}{b+x(\tau)}.
\]
Hence
\[
\frac1{r(\tau)}=\frac{x(\tau)}a+\frac ba.
\]
Two times with distinct \(x\)-values determine \(a\) and \(b\) generically. If \(\delta\) is also known at one time with \(x>0\), then
\[
c=
\left(\frac{y'}y+\delta\right)\frac{b+x}{x}
\]
determines \(c\).

For the ratio-dependent model, known \(\alpha\) gives
\[
r(\tau)=\frac{a}{b\,y(\tau)+x(\tau)},
\qquad
\frac1{r(\tau)}
=
\frac{x(\tau)}a+\frac b a\,y(\tau).
\]
Two times for which the vectors \((x,y)\) are linearly independent determine \(a,b\) generically; known \(\delta\) then determines \(c\).

Thus independent information about the time-varying rates, or a finite-dimensional functional parameterization whose identifiability is analyzed together with the constants, can remove the gauge. Merely increasing the temporal resolution of \(x,y\) cannot.

## Relation to the source paper

The source paper explicitly states that \(\alpha^*(\tau)\) and \(\delta^*(\tau)\) are time-dependent and uses separate neural subnetworks to estimate them. It nevertheless performs structural identifiability after replacing them by constants and then argues from a fixed-time freezing step that the non-autonomous structure has no redundancy.

The exact families above contradict that structural conclusion for the mathematical model with unrestricted time-dependent rates. They do not imply that the reported neural-network fit cannot select one particular parameter set. A finite neural architecture, parameter bounds, initialization, optimization, and implicit or explicit regularization can select representatives from a structurally non-unique family. Such selection is not structural identifiability of the underlying non-autonomous ODE model.

## Verification

`artifacts/verify_gauge.py` symbolically substitutes both gauge transformations into both source equations and verifies that all four residual differences simplify identically to zero. It also verifies the affine identities used in the simple known-\(\alpha\) repair. The accompanying output reports
`all_symbolic_checks_passed = True`.

## Originality scope

General structural-identifiability theory for ODEs with unknown time-varying parameters is prior work. In particular, Martinelli treats time-varying parameters as unknown inputs and develops general identifiability tests; Villaverde and coauthors likewise distinguish constant parameters from unknown time-varying inputs. Those general facts are not claimed as new.

The novelty claim is deliberately source-specific: for the two non-autonomous Moose–Wolf models of arXiv:2609.20793v1, the explicit three-constant gauge families above give a direct obstruction to the paper's stated transfer from autonomous to time-varying structural identifiability, and they show that the ambiguity survives the positivity/bound constraints locally.

No prior SCOPE record or publicly indexed comment making this specific correction was found. A contemporaneous or not-yet-indexed author revision or comment remains a residual originality risk.

## Limitations

The result concerns structural identifiability of the ODE model when \(\alpha(\tau)\) and \(\delta(\tau)\) are treated as unknown functions. It does not establish non-identifiability of a particular fixed finite neural-network architecture considered as part of an enlarged finite-dimensional parameterization; that would require a separate architecture-specific analysis.

The formulas assume \(x,y>0\), denominators nonzero, and \(x\ne1\) on the interval used for the displayed reconstruction. These conditions cover the generic positive regime. The exceptional surface \(x=1\) does not restore dependence on \(\alpha\); rather, the prey equation loses \(\alpha\) at that instant.

No claim is made about forecasting accuracy, ecological validity, or whether a particular regularized fit is practically useful.

## References

1. A. Singh and N. Kumari, *A physics-informed inverse modeling framework for Moose–Wolf dynamics from limited & noisy data in Isle Royale National Park*, arXiv:2609.20793v1 (2026). https://arxiv.org/abs/2609.20793
2. A. Martinelli, *Identifiability of nonlinear ODE Models with Time-Varying Parameters: the General Analytical Solution and Applications in Viral Dynamics*, arXiv:2211.13507 (2022). https://arxiv.org/abs/2211.13507
3. A. F. Villaverde, *Observability and Structural Identifiability of Nonlinear Biological Systems*, Complexity 2019, 8497093 (2019). https://doi.org/10.1155/2019/8497093
4. H. Xue, H. Miao, and H. Wu, *Sieve Estimation of Constant and Time-Varying Coefficients in Nonlinear Ordinary Differential Equation Models by Considering Both Numerical Error and Measurement Error*, Annals of Statistics 38 (2010), 2351–2387. https://doi.org/10.1214/09-AOS784
