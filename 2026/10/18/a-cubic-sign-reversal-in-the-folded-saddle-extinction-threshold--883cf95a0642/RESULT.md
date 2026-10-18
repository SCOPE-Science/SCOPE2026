# A cubic sign reversal in the folded-saddle extinction threshold

## Finding

Fix an Allee parameter \(a\in(0,1)\), and set \(b=1-a\), \(c=2-a=1+b\). In the singular reduced, ramped predator–prey system specified below, let \(r_{\mathrm{crit}}(\delta,a)\) denote the positive ramp rate for which the initial point \((u,\phi)=(1,c^{-1}+\delta)\) lies on the stable separatrix of the ecologically relevant folded saddle. For each fixed \(a\), as \(\delta\downarrow0\), this locally unique rate satisfies

\[
\boxed{r_{\mathrm{crit}}(\delta,a)=\frac{bc}{2}\delta+\frac{bc^3}{2}\delta^2+\frac{c^4(4b^3+b^2-1)}{8b}\delta^3+O_a(\delta^4).}
\]

The first two coefficients are established in Corollary 10 of Hennessy–Popović–Sattar. The new cubic coefficient changes sign **at exactly one** Allee parameter
\[
\boxed{a_0=1-b_0\approx0.4433069049675944,\qquad 4b_0^3+b_0^2=1,\quad b_0\in(0,1).}
\]
For \(a<a_0\) the cubic correction is positive; for \(a>a_0\) it is negative; at \(a=a_0\) it vanishes. Accordingly, for every fixed \(a\ne a_0\), the **sign of the error of the published quadratic approximation** is precisely the sign above for all sufficiently small positive \(\delta\). No assertion is made about the next nonzero coefficient when \(a=a_0\).

## Assumptions and scope

Take the source model's \(\varepsilon=0\) desingularized reduced flow, in its source time \(s\):
\[
\frac{du}{ds}=f(u,\phi;r):=-(u-a)\big[(1-\phi u)(u-1)+ru\big],\qquad
\frac{d\phi}{ds}=g(u,\phi;r):=-r(1+a\phi-2\phi u).
\]
The parameter \(a\) is fixed in the open interval \((0,1)\). The displacement \(\delta>0\) and rate \(r>0\) are sufficiently small, with all asymptotic remainder constants allowed to depend on \(a\). The folded saddle used is the equilibrium \((u_*(r),\phi_*(r))\) converging to \((1,c^{-1})\) as \(r\to0^+\). Its local stable manifold is written \(\phi=h_r(u)\) around \(u=1\). The threshold is defined by \(h_r(1)=c^{-1}+\delta\); identification with tracking versus tipping for the reduced flow follows from the cited source. This is a statement for the **singular reduced flow**, not a uniform claim for positive \(\varepsilon\) or for \(a\) approaching either endpoint.

## Proof

**1. Equilibrium jet.** The equilibrium equations, on the branch near \(u=1\), give \(\phi_*=1/(2u_*-a)\) and
\[
(u_*-a)(u_*-1)+r u_*(2u_*-a)=0.
\]
Since the derivative with respect to \(u_*\) at \((u_*,r)=(1,0)\) is \(b>0\), the implicit-function theorem provides a smooth branch. Expanding \(u_*=1+u_1r+u_2r^2+u_3r^3+O_a(r^4)\), coefficient comparison yields
\[
\begin{aligned}
u_1&=-c/b,\\
u_2&=c(b^2+2b-1)/b^3,\\
u_3&=-c(b^4+5b^3+b^2-5b+2)/b^5.
\end{aligned}
\]
Consequently
\[
\phi_*=c^{-1}+\frac{2}{bc}r+\frac{2(1-b)}{b^3}r^2+\frac{2(1-b)^2(b+2)}{b^5}r^3+O_a(r^4).
\]

**2. Stable tangent and curvature.** Let \(m(r)=h'_r(u_*(r))\). For the Jacobian \(J=\left(\begin{smallmatrix} f_u&f_\phi\\g_u&g_\phi\end{smallmatrix}\right)\) at the equilibrium, invariance of the stable eigendirection \((1,m)\) gives
\[
(f_u-g_\phi)m+f_\phi m^2-g_u=0.
\]
At \(r=0\) the stable eigenvalue is \(-b^2/c\), separated from the zero eigenvalue, and the stable direction is horizontal. Expanding the slope in the root near zero gives
\[
\boxed{m(r)=-\frac{2}{b^2}r+\frac{4c}{b^3}r^2+O_a(r^3).}
\]

At \(r=0\), the levels \(\phi=\mathrm{constant}\) are invariant and the equilibrium line \(u=1\) is normally attracting near \(\phi=c^{-1}\). Smooth dependence of its local strong-stable fibers on the small parameter gives a \(C^4\)-smooth family of local graphs \(h_r\), with \(h_0\) constant. Thus \(h_r'''(u_*)=O_a(r)\) and higher derivatives are bounded on a common small neighborhood.

The graph invariance identity \(g(u,h_r(u);r)=h_r'(u) f(u,h_r(u);r)\), differentiated twice at the saddle, gives
\[
\begin{aligned}
\big(g_\phi-2f_u-3f_\phi m\big)h_r''(u_*)
={}&m\big(f_{uu}+2f_{u\phi}m+f_{\phi\phi}m^2\big)\\
&-\big(g_{uu}+2g_{u\phi}m+g_{\phi\phi}m^2\big).
\end{aligned}
\]
Here \(f_{uu}(1,c^{-1};0)=0\), \(g_{uu}=g_{\phi\phi}=0\), \(g_{u\phi}=2r\), and \(m=O_a(r)\). Therefore the right side is \(O_a(r^2)\), while the prefactor tends to \(2b^2/c>0\); hence \(h_r''(u_*)=O_a(r^2)\). Because \(1-u_*=O_a(r)\), the quadratic, cubic, and subsequent Taylor remainders in the stable-graph expansion around \(u_*\) are \(O_a(r^4)\). In particular,
\[
\boxed{h_r(1)=\phi_*(r)+m(r)(1-u_*(r))+O_a(r^4).}
\]
This curvature cancellation is critical: using an unspecified linear approximation to the separatrix would not justify the cubic coefficient.

**3. Intersection and series inversion.** Combining the preceding expansions gives
\[
\delta=h_r(1)-c^{-1}=\frac{2}{bc}r-\frac{4}{b^2}r^2+\frac{2(4b^3+7b^2+1)}{b^5}r^3+O_a(r^4).
\]
Its derivative at zero is \(2/(bc)>0\). The inverse-function theorem consequently gives a unique small positive \(r=r_{\mathrm{crit}}(\delta,a)\); inversion of the cubic Taylor polynomial yields exactly the coefficient formula in the Finding section.

**4. Unique crossover.** The factor \(c^4/(8b)\) is positive. The remaining factor \(P(b)=4b^3+b^2-1\) has \(P(0)=-1\), \(P(1)=4\), and \(P'(b)=12b^2+2b>0\) on \((0,1)\). Hence its zero \(b_0\) is unique and produces the stated strict sign partition. The \(O_a(\delta^4)\) remainder gives the asserted sign for sufficiently small \(\delta>0\) whenever \(a\ne a_0\).

## Verification

Run `python3 verify.py` from the package directory. Its standard-library rational arithmetic checks the equilibrium equation, reciprocal fold relation, stable-slope equation, crossing jet, cubic series inversion and the vanishing of the undeformed curvature input at 277 distinct rational choices of \(b\), totaling 1,939 groups of exact assertions. This is a regression check, **not an exhaustive proof over the continuum**. The all-parameter statement follows from the displayed algebraic formulas and invariant-manifold argument. Numerical saddle-to-section integrations at several small rates and at \(a=0.2,0.5,0.8\) independently exhibited fourth-order residual scaling; these exploratory integrations are not necessary for the proof.

## Relationship to prior work

Hennessy, Popović and Sattar, arXiv:2610.12319v1, Sections 4–5 and Appendix A.5–A.7, introduce this desingularized flow, identify the folded-saddle canard and prove the **linear and quadratic coefficients** (their Proposition 8 and Corollary 10). Their \(O(\delta^3)\) error does not determine the cubic coefficient or its sign. The present result retains those coefficients and adds the explicit cubic term, a proof of the stable-graph curvature order needed at that precision, and the unique Allee-parameter sign crossover.

Vanselow, Wieczorek and Feudel, arXiv:1908.05507v1, Appendix F, give the folded-saddle eigendirection approximation for a **different Rosenzweig–MacArthur system with Holling type-II response**, and discuss its agreement with numerical critical rates. That does not imply the present cubic coefficient for the strong-Allee type-I model. General canard theory supports the geometric framework but does not directly fix these model-specific coefficients.

## Limitations

The expansion is pointwise in each \(a\in(0,1)\); constants diverge as \(a\to1^-\). No positive-\(\varepsilon\) correction, finite-\(\delta\) global error bound, or assertion for finite ramp rates is established. The zero at \(a=a_0\) does not establish the sign of the fourth-order term. The priority of the exact cubic coefficient remains subject to independent bibliographic assessment, including the possibility of unpublished or implicitly equivalent calculations.

## References

1. B. Hennessy, N. Popović and Z. Sattar, *A minimal model for rate-induced tipping to extinction*, arXiv:2610.12319v1 (first posted 2026-10-08), https://arxiv.org/html/2610.12319v1. See Sections 4–5, Proposition 8, Corollary 10 and Appendix A.5–A.7.
2. A. Vanselow, S. Wieczorek and U. Feudel, *When very slow is too fast — collapse of a predator–prey system*, arXiv:1908.05507v1 (2019), https://arxiv.org/pdf/1908.05507. See Appendix F.
3. P. Szmolyan and M. Wechselberger, *Canards in \(\mathbb R^3\)*, Journal of Differential Equations 177 (2001), 419–453, DOI:10.1006/jdeq.2001.4001; cited for general folded-canard geometry, not a coefficient formula.
