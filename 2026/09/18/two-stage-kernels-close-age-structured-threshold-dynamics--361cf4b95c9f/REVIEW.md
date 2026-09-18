# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

PASS.

The constructed survival-weighted reproductive kernel
\[
K(a)=\frac{r_1r_2}{r_2-r_1}(e^{-r_1a}-e^{-r_2a})
\]
is a normalized two-stage hypoexponential density. With \(r_1>\|\mu\|_\infty\), the fertility \(\beta=e^M K\) is bounded and strictly positive for positive age, so it satisfies the source model's normalization and has noncompact support.

The auxiliary first-stage weight \(\beta_1(a)=r_1e^{M(a)-r_1a}\) gives exact moment equations
\[
X'=r_1(f(Y)-X),\qquad Y'=r_2(X-Y).
\]
The identities follow from \(\beta_1'-\mu\beta_1=-r_1\beta_1\), \(\beta'-\mu\beta=r_2(\beta_1-\beta)\), and the model boundary condition. They are also consistent with the standard two-stage linear-chain representation.

Eliminating X yields
\[
Y''+(r_1+r_2)Y'=r_1r_2(f(Y)-Y),
\]
with strict Lyapunov function
\[
E=\frac12(Y')^2+r_1r_2\int_0^Y(s-f(s))\,ds,
\qquad
E'=-(r_1+r_2)(Y')^2.
\]
The source assumption \(\limsup f(y)/y<1\) makes the potential coercive. LaSalle therefore restricts every omega-limit set to the three fixed points of f. The Jacobian determinant is \(r_1r_2(1-f'(\kappa))\): the lower and upper equilibria are sinks and the intermediate one is a saddle.

The characteristic formula for the transport equation transfers convergence of the birth signal to L1 convergence of the full age density because mortality is uniformly bounded below. The planar stable manifold at the saddle is unordered: its local tangent has opposite-sign components, while strong cooperativity would preserve strict ordering of two ordered global-stable-manifold points until they enter the local stable manifold, which is impossible. Hence a strictly increasing moment curve from a source-type monotone family intersects the saddle stable manifold at most once. Together with continuity and the two sink basins, this gives the stated sharp alternative and convergence of the threshold solution to the intermediate equilibrium.

Adversarial checks included the unequal-rate case, the equal-rate Erlang-2 limit, the possibility of arbitrary admissible age-dependent mortality, and the distinction between moment convergence and full L1 convergence. No periodic orbit is compatible with the strict mechanical energy unless it is an equilibrium.

## Originality

PASS, to the best of our knowledge.

The primary source, Griette--Herrera (2026), was inspected in full-text HTML. Its Theorems 1.2 and 1.3 establish a unique threshold for compactly supported fertility and for a noncompact eventually-constant fertility/mortality class, respectively, but do not identify the threshold solution's limit. The paper explicitly states that describing threshold-solution asymptotics remains open and notes that oscillatory or periodic behavior can occur in related age-structured models. The source contains no Erlang, hypoexponential, or linear-chain treatment of this question.

Finite-dimensional reduction by gamma/Erlang or phase-type kernels is classical and is excluded from the novelty claim. Gyllenberg's review describes Gurtin--MacCamy reductions for gamma-type fertility and connects them to the linear-chain trick; Metz--Diekmann and later Diekmann--Gyllenberg--Metz develop the general finite-dimensional representation theory. Searches for the 2026 source together with Erlang, gamma, hypoexponential, two-stage, stable-manifold, and intermediate-equilibrium threshold terminology did not locate a prior statement of the theorem recorded here.

The most important residual risk is M. E. Gurtin and R. C. MacCamy, *Some simple models for nonlinear age-dependent population dynamics* (1979), DOI 10.1016/0025-5564(79)90049-X. Its accessible abstract and indexed text say that certain age-structured models reduce to ODE systems and that periodic solutions are impossible in many cases. The accessible model description uses mortality and maternity depending on total population, rather than the 2026 boundary feedback \(u(t,0)=f(\int\beta u)\). The full 1979 article was not independently inspected, so an unrecognized equivalent special case remains possible. Modern reviews were inspected specifically to assess this risk and confirm the classical status of the reduction technology.

The originality claim is therefore limited to the source-specific global theorem: in the 2026 bistable boundary-feedback model, a broad explicit noncompact two-stage reproductive class admits a damped-gradient reduction that completely determines all PDE omega-limits and forces every nontrivial monotone-family threshold solution to converge to the intermediate equilibrium.

## Value

PASS.

The source paper identifies threshold-solution asymptotics as an open problem and emphasizes that noncompact fertility is the technically harder regime. The present result gives a full answer for an explicit infinite-support family outside the source's eventually-constant class, and it classifies every initial datum rather than only a one-parameter family. It also isolates a concrete structural reason persistent threshold oscillation is impossible: a two-stage reproductive kernel collapses the renewal memory to a damped one-degree-of-freedom mechanical system with strictly decreasing energy.

The result distinguishes the part of the difficulty caused by genuinely higher/infinite-dimensional reproductive memory from that caused merely by noncompact support. This provides a tractable benchmark for testing broader conjectures about the separatrix and threshold dynamics.

## Sources checked

- Q. Griette and F. Herrera, *Sharp Threshold Dynamics for a Bistable Age-Structured Population Model*, Journal of Dynamics and Differential Equations (2026), DOI 10.1007/s10884-026-10527-w:
  https://doi.org/10.1007/s10884-026-10527-w
- M. Gyllenberg, *Mathematical aspects of physiologically structured populations: the contributions of J. A. J. Metz*, Journal of Biological Dynamics (2007), DOI 10.1080/17513750601032737:
  https://doi.org/10.1080/17513750601032737
- J. A. J. Metz and O. Diekmann, *Exact finite-dimensional representations of models for physiologically structured populations. I. The abstract foundations of linear chain trickery* (1991):
  https://ir.cwi.nl/pub/1559
- O. Diekmann, M. Gyllenberg, and J. A. J. Metz, *Finite dimensional state representation of physiologically structured populations*, Journal of Mathematical Biology 80 (2020), DOI 10.1007/s00285-019-01454-0:
  https://doi.org/10.1007/s00285-019-01454-0
- M. E. Gurtin and R. C. MacCamy, *Some simple models for nonlinear age-dependent population dynamics*, Mathematical Biosciences 43 (1979), DOI 10.1016/0025-5564(79)90049-X. Full text was not independently inspected; accessible abstract/indexed text and later reviews were checked:
  https://doi.org/10.1016/0025-5564(79)90049-X

## Limitations retained

The result does not address arbitrary noncompact fertility, higher-stage phase-type kernels, or kernels capable of genuinely delay-like oscillatory dynamics. The sufficient rate condition is stronger than necessary and is imposed to ensure bounded fertility. The stable-manifold separatrix is characterized dynamically but not in closed form. No claim is made that the classical finite-dimensional reduction itself is new.
