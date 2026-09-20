# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The periodic-orbit theorem follows from two independent multiplier identities. Multiplication of \(z'''+az''+bz'+cz=g(z)\) by \(z'\) gives \(\int(z'')^2=b\int(z')^2\). Multiplication by \(z''\), followed by integration by parts, gives \(a\int(z'')^2-c\int(z')^2=\int[-g'(z)](z')^2\). Their combination is exactly the stated weighted-slope identity. No sign or monotonicity assumption on \(g\) is needed for this equality.

The invariant-measure extension was checked separately using generator identities for \(v^2/2,z^2/2,vw,zv,g(z)v,w^2/2\). These give \(\int w^2=b\int v^2\) and then \(\int[-g'(z)]v^2=(ab-c)\int v^2\). If the derivative energy vanishes, invariance confines the support to equilibria, so division is used only for genuinely non-equilibrium states.

The slope-crossing corollary was stress-tested at turning points. If \(-g'-(ab-c)\) has one sign on a nonconstant periodic orbit, its continuous product with \((z')^2\) can integrate to zero only if the factor vanishes wherever \(z'\ne0\). Every interior value of the oscillation range is traversed with nonzero derivative somewhere, so continuity forces the feedback law to be affine with the critical slope across the entire range. This is exactly the exceptional case excluded in the strict statement.

The Goodwin elimination was checked directly: \((D+\beta_1)(D+\beta_2)(D+\beta_3)R=\alpha_1\alpha_2\alpha_3f(R)\), and symbolic expansion verifies \(a_1a_2-a_3=(\beta_1+\beta_2)(\beta_1+\beta_3)(\beta_2+\beta_3)\). The resulting threshold matches the Routh--Hurwitz equality in Chen--Shih (2026). A high-accuracy numerical Goodwin orbit independently satisfies both integral ratios to about \(2\times10^{-11}\).

## Originality

**PASS, to the best of our knowledge.** The review searched exact and synonymous formulations involving third-order scalar feedback, Goodwin oscillators, derivative-weighted or energy-weighted feedback slopes, Routh--Hurwitz/Hopf slope thresholds, secant criteria, periodic-orbit integral identities, and invariant-measure balances.

A direct prior overlap was found and removed from the novelty claim: Forger (2011) derives an exact Goodwin period formula from an inner-product/integration-by-parts identity and Parseval's theorem, together with a minimum-period bound. The present record explicitly treats that period identity and bound as prior art. Chen--Shih (2026) supplies the precise local Hopf slope threshold and Hopf frequency for general degradation rates; those local bifurcation formulas are also credited rather than claimed.

Hastings (1977) was inspected as a primary source. It studies a particular Goodwin system and proves uniqueness/global orbital stability in a parameter regime by comparison and Poincare-map arguments. No inspected portion states the derivative-energy-weighted slope law. Arcak--Sontag (2006) establishes global stability for cyclic sector nonlinearities under secant-type conditions, a different sufficient-stability mechanism.

No inspected source states the general identity \(\int[-g'(z)](z')^2=(ab-c)\int(z')^2\), its compact-invariant-measure version, or the conclusion that every genuinely nonlinear Goodwin cycle must cross the local Hopf slope surface. The main residual risks are Hastings--Tyson--Webster (1977) and Tyson--Othmer (1978), whose complete texts were not inspected, together with older third-order differential-equation literature where the short multiplier identity could appear under different notation. Originality is therefore deliberately qualified.

## Value

**PASS.** The result turns a local linear stability quantity into an exact finite-amplitude constraint. In a third-order feedback oscillator, every periodic orbit must balance its instantaneous nonlinear slope to the same \(ab-c\) that marks the local Hurwitz/Hopf boundary. For Goodwin systems this means a large oscillation, including one coexisting with a locally stable equilibrium, cannot be supported entirely in a region whose repression slope stays on one side of the Hopf threshold. The invariant-measure formulation extends the constraint beyond a single periodic trajectory to arbitrary compact recurrent statistics.

This is useful as a structural obstruction rather than an existence theorem: it can rule out proposed recurrent regimes from slope information alone and provides an exact diagnostic linking nonlinear finite-amplitude behavior to the classical secant/Hopf threshold.

## Scientific limitations

The theorem does not establish existence, uniqueness, or stability of oscillations. The strict slope-crossing statement excludes the degenerate case in which the feedback is affine with the critical slope throughout the oscillation range. Compact support is assumed in the invariant-measure statement. Forger's exact period relation and period lower bound are prior results and are not part of the originality claim. Full-text coverage of all classical biochemical-control and third-order-ODE literature was not possible; Hastings--Tyson--Webster (1977) and Tyson--Othmer (1978) are the most relevant unresolved sources.
