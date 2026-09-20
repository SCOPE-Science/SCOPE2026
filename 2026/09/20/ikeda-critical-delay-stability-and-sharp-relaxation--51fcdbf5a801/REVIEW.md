# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** At \(\mu=1\), differentiation of
\[
V=\frac12x(t)^2+\frac12\int_{t-h}^{t}x(s)^2\,ds
\]
gives exactly
\[
\dot V=-\frac12(x(t)-\sin x(t-h))^2
-\frac12(x(t-h)^2-\sin^2x(t-h)).
\]
The second defect vanishes only when \(x(t-h)=0\), and then the first forces \(x(t)=0\). Boundedness from \(V\), bounded derivative, compactness of positive-time history segments, and the retarded-equation LaSalle principle therefore give global convergence to zero. The same functional directly yields Lyapunov stability from small sup-norm histories.

For \(\mu<1\), the standard Halanay estimate is global because \(|\sin z|\le|z|\). For \(\mu>1\), the real characteristic function changes sign between zero and positive infinity, giving a positive real root and instability.

At the endpoint the characteristic equation is
\[
\lambda+1-e^{-\lambda h}=0.
\]
The modulus estimate in RESULT.md proves that zero is the only root in the closed right half-plane, and its derivative there is \(1+h\), so it is simple. The exact observable
\[
Q=x(t)+\int_{t-h}^{t}x(s)\,ds
\]
satisfies \(Q'=\sin x(t-h)-x(t-h)\). Normalizing \(u=Q/(1+h)\) and using the odd one-dimensional center manifold gives
\[
u'=-u^3/[6(1+h)]+O(u^5).
\]
Standard stable-foliation theory then yields the stated generic
\(\sqrt t\,x(t)\to\pm\sqrt{3(1+h)}\) law, with exponential decay on the strong-stable manifold. The \(h=0\) limit agrees with the direct scalar ODE asymptotic.

## Originality

**PASS, to the best of our knowledge.** Nardone--Mandel--Kapral (1986) studies stability boundaries for steady and periodic Ikeda states. Kubyshkin--Moriakova (2018) studies equilibrium and periodic-solution bifurcations. Their 2020 paper is the closest checked source: it explicitly treats the zero-phase \(\mu=1\) special case through a singular large-delay normal-form construction and develops nearby periodic bifurcations.

The strict \(\mu<1\) stability region and the \(\mu>1\) linear instability are not treated as novel contributions here. Exact and synonymous searches were made for global asymptotic stability, the critical endpoint, Lyapunov/Lyapunov--Krasovskii functionals, center-manifold reductions and algebraic critical decay for the Ikeda equation. No checked source states the combination of the exact critical dissipation identity, global endpoint attraction for arbitrary fixed delay, and the sharp coefficient \(\sqrt{3(1+h)}\).

The main residual risk is substantive. The 2020 local normal form analyzes the same degenerate equilibrium and may implicitly encode the cubic zero-mode coefficient after translating its singular scaling. Older general absolute-stability or Razumikhin/Lyapunov results for scalar delay equations may also imply the endpoint convergence without naming the Ikeda model. Accordingly, originality is intentionally restricted to the explicit endpoint package as stated, not to the surrounding standard stability facts.

## Value

**PASS.** The theorem gives a delay-independent iff stability boundary and resolves what happens exactly at the nonhyperbolic threshold rather than only on either side. The exact functional is simple enough to reuse, while the center observable turns the neutral linear mode into a quantitative nonlinear critical-slowing law. The coefficient \(\sqrt{3(1+h)}\) shows explicitly how delay changes the slow relaxation even though it does not shift the stability threshold.

## Scientific limitations

Only the zero-phase equation is covered. Nothing here classifies the rich dynamics for \(\mu>1\), nor does it establish properties of nonzero equilibria or periodic attractors. For positive delay, exceptional strong-stable histories decay exponentially rather than with the generic algebraic law. The center asymptotic relies on standard smooth center-manifold and stable-foliation theory for retarded functional differential equations. The checked literature is not exhaustive, and the 2020 special-case normal-form paper remains the strongest possible source of implicit overlap.
