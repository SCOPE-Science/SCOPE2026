# A repeated component-indexing error invalidates two printed SEIAR convergence claims
## Finding
The Caputo SEIAR model defines the five right-hand sides
\[
\begin{aligned}
F_3&=(1-\theta)\omega E-(\tau+\mu)I,\\
F_4&=\theta\rho E-(\gamma+\mu)A,\\
F_5&=\tau I+\gamma A-\mu R.
\end{aligned}
\]
Consequently the exact Volterra representation of the last two components is
\[
A(t)=A(0)+I^\alpha F_4(t,y),\qquad
R(t)=R(0)+I^\alpha F_5(t,y).
\]
The source states these correct identities in Eqs. (5.4)–(5.5) and restates the definitions of \(F_3,F_4,F_5\) in Eq. (5.24). But Eqs. (5.10)–(5.11) shift both component labels down by one:
\[
A(t_n)=A(0)+I^\alpha F_3(t_n,y),\qquad
R(t_n)=R(0)+I^\alpha F_4(t_n,y).
\]
The displayed corrector formulas (5.15)–(5.16) repeat the same shift, while the recovered predictor (5.21) also uses \(F_4\) instead of \(F_5\). Therefore the printed scheme does not discretize the printed SEIAR system in its last two components.

More precisely, if the quadrature weights are used consistently with the right-hand sides that the printed formulas supply, then refinement can only approach the shifted Volterra equations, not the target equations, whenever \(F_3\not\equiv F_4\) or \(F_4\not\equiv F_5\). Thus the stated component errors
\[
|A(t_n)-A_n|=O\!\left(h^{\min\{\alpha+1,2\}}\right),\qquad
|R(t_n)-R_n|=O\!\left(h^{\min\{\alpha+1,2\}}\right)
\]
and the associated assertion that all printed approximations converge to the exact SEIAR model as \(h\to0\) cannot hold for the formulas as written.

An exact nonnegative witness uses
\[
\theta=\frac12,\quad \rho=2,\quad \gamma=\mu=\omega=\tau=1,
\quad E(0)=1,\quad I(0)=A(0)=R(0)=0.
\]
Then
\[
F_3(0)=\frac12,\qquad F_4(0)=1,\qquad F_5(0)=0.
\]
For every \(0<\alpha\le1\), continuity of the right-hand sides gives
\[
I^\alpha g(t)=\frac{g(0)}{\Gamma(\alpha+1)}t^\alpha+o(t^\alpha)
\quad(t\downarrow0).
\]
Hence, relative to the target model, the printed integral mapping has
\[
A_{\rm printed}(t)-A_{\rm target}(t)
=-\frac{t^\alpha}{2\Gamma(\alpha+1)}+o(t^\alpha),
\]
\[
R_{\rm printed}(t)-R_{\rm target}(t)
=\frac{t^\alpha}{\Gamma(\alpha+1)}+o(t^\alpha).
\]
These leading discrepancies are properties of the continuous integral equations and do not vanish merely by shrinking the numerical step.

## Assumptions and scope
The fractional order satisfies \(0<\alpha\le1\). The claim uses the model, component definitions, Volterra equations, predictor–corrector formulas, and convergence statements exactly as displayed in the motivating article. The witness uses nonnegative initial data and positive epidemiological parameters; the remaining parameters in the first two equations may be chosen arbitrarily within the model's admissible positive range because they do not enter the displayed mismatch at the initial instant.

The conclusion is about the printed mathematics. No source code is supplied with the article, so the claim does not infer that the plotted trajectories were necessarily generated with the same shifted indices. It also does not challenge the model's equilibrium or stability calculations, which are separate from this numerical indexing defect.

## Proof
For a Caputo equation \({}^CD_t^\alpha u(t)=f(t)\) with \(0<\alpha\le1\) and initial value \(u(0)\), the equivalent Volterra equation is
\[
u(t)=u(0)+I^\alpha f(t).
\]
Applying this componentwise to the source model gives the exact \(A\)- and \(R\)-equations with \(F_4\) and \(F_5\), respectively. This is also exactly what the source writes before discretization in Eqs. (5.4)–(5.5).

The later formulas (5.10)–(5.11) instead insert \(F_3\) into the \(A\)-equation and \(F_4\) into the \(R\)-equation. The corrector formulas (5.15)–(5.16) use the same mismatched functions at the initial, history, and predicted-state terms. Therefore this is not a single endpoint typo: every quadrature contribution to those two displayed correctors is taken from the wrong component field. The \(A\)-predictor (5.20) uses \(F_4\), but the final \(A\)-corrector returns to \(F_3\); the \(R\)-predictor (5.21) uses \(F_4\), not \(F_5\).

A convergent product-integration or predictor–corrector quadrature approximates the Volterra integral of the function supplied to it. Garrappa's general formulation writes a system method with the vector field evaluated componentwise; it does not permit replacing one component by a different component's field. Thus a consistent implementation of the printed \(A\)-corrector approaches \(A(0)+I^\alpha F_3\), while the printed \(R\)-corrector approaches \(R(0)+I^\alpha F_4\).

It remains to show that these shifted equations are genuinely different from the target equations. At the stated witness,
\[
F_3(0)=\left(1-\frac12\right)\!\cdot1\cdot1-(1+1)\cdot0=\frac12,
\]
\[
F_4(0)=\frac12\cdot2\cdot1-(1+1)\cdot0=1,
\qquad
F_5(0)=1\cdot0+1\cdot0-1\cdot0=0.
\]
For continuous \(g\), write \(g(s)=g(0)+o(1)\) in
\[
I^\alpha g(t)=\frac1{\Gamma(\alpha)}\int_0^t(t-s)^{\alpha-1}g(s)\,ds.
\]
The constant part integrates to \(g(0)t^\alpha/\Gamma(\alpha+1)\), and the remainder is \(o(t^\alpha)\). Subtracting the target and shifted equations gives the two displayed leading discrepancies. Since their coefficients are nonzero, the shifted integral equations cannot coincide with the target solution on any sufficiently small positive time interval.

Accordingly, a step-refinement estimate against the exact target solution cannot have an error tending to zero for these printed mappings in general, much less the stated order, unless an implementation silently replaces the printed component fields by the correct ones.

## Verification
The bundled `verify.py` evaluates the three relevant component fields at the exact rational witness and verifies \(F_3(0)=1/2\), \(F_4(0)=1\), and \(F_5(0)=0\), together with the two nonzero leading-error coefficients. The source equations were checked directly in the open-access PDF at Eqs. (1.1), (5.4)–(5.5), (5.10)–(5.16), (5.20)–(5.24), and (5.28)–(5.29).

## Relationship to prior work
Sene and Mansal define the target SEIAR vector field correctly and cite Garrappa's predictor–corrector literature for the numerical method. Garrappa's 2018 survey formulates fractional multistep methods for scalar equations and systems through the same vector field \(f(t,y)\), including non-scalar systems; this supports the componentwise correspondence required by the target model rather than the shifted mapping printed in the SEIAR paper.

Targeted exact-title, component-alias, SEIAR predictor–corrector, and semantic database searches found no published result identifying this repeated \(F_3/F_4/F_5\) shift or deriving the resulting nonvanishing leading mismatch. Sene's 2022 chapter on Caputo SEIR numerical methods is closely related by author and subject, but a reliable full-text copy was not available in the inspected sources, so it is retained as an originality risk rather than used to assert noncoverage.

## Limitations
This finding establishes a defect in the printed equations and the convergence conclusion attached to those equations. It does not determine whether private or unavailable computational code corrected the indices before producing the figures. It does not prove anything about the accuracy of a repaired scheme, nor does it re-audit the article's equilibrium, reproduction-number, or stability results.

## References
1. N. Sene and F. Mansal, “Investigations on the fractional SEIAR epidemic model utilizing the Caputo derivative,” *Palestine Journal of Mathematics* 15(1) (2026), 200–213. Open-access PDF: https://pjm.ppu.edu/sites/default/files/papers/PJM_15(1)_2026_200_to_213.pdf
2. R. Garrappa, “Numerical Solution of Fractional Differential Equations: A Survey and a Software Tutorial,” *Mathematics* 6(2) (2018), 16. DOI: 10.3390/math6020016.
3. R. Garrappa, “On linear stability of predictor-corrector algorithms for fractional differential equations,” *International Journal of Computer Mathematics* 87(10) (2010), 2281–2290. DOI: 10.1080/00207160802624331.
4. N. Sene, “Numerical methods applied to a class of SEIR epidemic models described by the Caputo derivative,” in *Methods of Mathematical Modeling: Infectious Diseases* (2022), 23–40. DOI: 10.1016/B978-0-323-99888-8.00003-6.
