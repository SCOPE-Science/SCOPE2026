# Polylogarithmic geometry of the canonical ideal-Bose condensate right tail
## Finding
For the right-tail regime of the canonical ideal-Bose-gas large-deviation theorem of Deuchert and Li, assume \(\alpha>1\) and \(b>b_c\). Define
\[
r=\left(\frac{b_c}{b}\right)^\alpha\in(0,1),\qquad
\eta_{\max}=\frac{r}{1-r}.
\]
For every \(0<\eta<\eta_{\max}\), define \(z=z(\eta)\in(0,1)\) by the uniquely solvable fugacity equation
\[
\operatorname{Li}_{\alpha}(z)=\zeta(\alpha)\left(1-\frac{1-r}{r}\eta\right).
\]
Then the positive right-tail large-deviation rate is
\[
J(\eta)=\frac{r}{\zeta(\alpha)}\left[\zeta(\alpha+1)-\operatorname{Li}_{\alpha+1}(z)\right]
+\left[r-(1-r)\eta\right]\log z.
\]
It is strictly increasing and strictly convex on \((0,\eta_{\max})\), with
\[
J'(\eta)=-(1-r)\log z>0,
\qquad
J''(\eta)=\frac{(1-r)^2\zeta(\alpha)}{r\operatorname{Li}_{\alpha-1}(z)}>0.
\]
The interior rate has the finite one-sided endpoint cost
\[
\lim_{\eta\uparrow\eta_{\max}}J(\eta)
= r\,\frac{\zeta(\alpha+1)}{\zeta(\alpha)},
\qquad
J'(\eta)\longrightarrow+\infty.
\]
At the typical point, the local rate has a sharp three-regime phase diagram:
\[
J(\eta)\sim
\begin{cases}
C_{\alpha,r}\eta^{\alpha/(\alpha-1)},&1<\alpha<2,\\
\dfrac{(1-r)^2\zeta(2)}{2r}\dfrac{\eta^2}{|\log\eta|},&\alpha=2,\\
\dfrac{(1-r)^2\zeta(\alpha)}{2r\zeta(\alpha-1)}\eta^2,&\alpha>2,
\end{cases}
\]
where
\[
C_{\alpha,r}=\frac{\alpha-1}{\alpha}(1-r)
\left[\frac{\zeta(\alpha)(1-r)}{r[-\Gamma(1-\alpha)]}\right]^{1/(\alpha-1)}.
\]
Thus the right-tail rate is nonquadratic for \(1<\alpha<2\), has the critical logarithmic weakening at \(\alpha=2\), and becomes genuinely quadratic only for \(\alpha>2\).

## Assumptions and scope
The source assumes a non-interacting Bose gas in the canonical ensemble whose one-particle counting function has the high-energy asymptotic \(\#\{j:E_j\leq\lambda\}\sim L\lambda^\alpha\), and it derives the right-tail large-deviation formula in the condensed regime. The present statement uses only its \(\alpha>1\), \(b>b_c\) right-tail theorem, where \(b_c^\alpha=L\alpha\Gamma(\alpha)\zeta(\alpha)\), and the source's admissible interval \(0<\eta<[(b/b_c)^\alpha-1]^{-1}=r/(1-r)\).

The claim concerns the rate function inside that open interval. The exact boundary event at \(\eta=\eta_{\max}\) is deliberately excluded: Deuchert and Li explain that its probability can depend on finer spectral information not contained in the sole counting-law hypothesis. The result here is the one-sided limit of the universal interior rate as the threshold is approached.

## Proof
Write the source variational exponent as
\[
\phi_{\eta,b}(s)=L\alpha b^{-\alpha}
\int_0^\infty x^{\alpha-1}\log\!\left(\frac{1-e^{-x}}{1-e^{s-x}}\right)\,dx
-\left[r-\eta(1-r)\right]s,
\qquad s<0.
\]
For \(z=e^s\in(0,1)\), expand both logarithms into absolutely convergent geometric-logarithmic series and integrate term by term. Since
\[
\int_0^\infty x^{\alpha-1}e^{-nx}\,dx=\frac{\Gamma(\alpha)}{n^\alpha},
\]
one obtains
\[
\int_0^\infty x^{\alpha-1}\log\!\left(\frac{1-e^{-x}}{1-ze^{-x}}\right)\,dx
=\Gamma(\alpha)\left[\operatorname{Li}_{\alpha+1}(z)-\zeta(\alpha+1)\right].
\]
Using \(L\alpha\Gamma(\alpha)b^{-\alpha}=r/\zeta(\alpha)\), this gives
\[
\phi_{\eta,b}(\log z)=\frac{r}{\zeta(\alpha)}
\left[\operatorname{Li}_{\alpha+1}(z)-\zeta(\alpha+1)\right]
-\left[r-\eta(1-r)\right]\log z.
\]
The source proves strict convexity of \(\phi_{\eta,b}\) and existence of a unique minimizer. Differentiating with respect to \(s=\log z\), using
\[
\frac{d}{ds}\operatorname{Li}_{\nu}(e^s)=\operatorname{Li}_{\nu-1}(e^s),
\]
shows that the minimizer is the unique \(z\in(0,1)\) satisfying
\[
\operatorname{Li}_{\alpha}(z)=\zeta(\alpha)\left(1-\frac{1-r}{r}\eta\right).
\]
Because the probability exponent is \(\inf_{s<0}\phi_{\eta,b}(s)\), the positive rate is \(J=-\inf\phi\), which yields the displayed formula.

For derivatives, the envelope theorem gives
\[
J'(\eta)=-(1-r)\log z.
\]
Differentiating the fugacity equation gives
\[
\operatorname{Li}_{\alpha-1}(z)\frac{d}{d\eta}\log z
=-\frac{1-r}{r}\zeta(\alpha),
\]
and therefore the displayed positive expression for \(J''\). This also proves strict increase and strict convexity.

At \(\eta\uparrow\eta_{\max}\), the right side of the fugacity equation tends to zero, hence \(z\downarrow0\). Since \(\operatorname{Li}_{\alpha+1}(z)\to0\) and \(z\log z\to0\), the endpoint limit is \(r\zeta(\alpha+1)/\zeta(\alpha)\); meanwhile \(-\log z\to\infty\), so \(J'\to\infty\).

For the local phase diagram write \(z=e^{-t}\), \(t\downarrow0\), and \(\kappa=(1-r)/r\). The fugacity equation becomes
\[
\zeta(\alpha)-\operatorname{Li}_{\alpha}(e^{-t})=\zeta(\alpha)\kappa\eta.
\]
The standard polylogarithm expansions give
\[
\zeta(\alpha)-\operatorname{Li}_{\alpha}(e^{-t})\sim
\begin{cases}
-\Gamma(1-\alpha)t^{\alpha-1},&1<\alpha<2,\\
t|\log t|,&\alpha=2,\\
\zeta(\alpha-1)t,&\alpha>2.
\end{cases}
\]
Solving for \(t\), inserting it into \(J'(\eta)=(1-r)t\), and integrating from \(0\) to \(\eta\) yields the three asymptotic formulas and the stated constant \(C_{\alpha,r}\).

## Verification
The accompanying `verify.py` evaluates the fugacity equation and closed rate at representative \(\alpha\) values in all three regimes, checks the derivative identities by high-precision finite differences, checks strict convexity, verifies convergence to the endpoint constant, and verifies the three small-\(\eta\) asymptotic ratios. The numerical checks are not substitutes for the analytic proof; they are independent consistency tests of its normalization and constants.

As a concrete normalization check, for \(r=2/5\) the script tests \(\alpha=3/2,2,3\). It separately checks that the variational expression evaluated at the polylogarithmic saddle equals \(-J\), preventing a sign convention error between the source's negative probability exponent and the positive rate used here.

## Relationship to prior work
Deuchert and Li establish the canonical ideal-gas condensate large-deviation theorem, state the right-tail exponent as an infimum over \(s<0\), prove strict convexity, and characterize its minimizer by an integral equation. Their article does not rewrite this saddle in polylogarithmic coordinates, does not give the derivative formulas above, and does not extract the \(\alpha<2\), \(\alpha=2\), and \(\alpha>2\) local rate regimes or the universal one-sided endpoint cost.

Chatterjee and Diaconis rigorously characterize canonical condensate fluctuation orders and limiting laws for non-interacting bosons in broad trapping geometries. Their fluctuation theory is not a fixed-deviation large-deviation formula. The local phase diagram above is mathematically compatible with the familiar transition from non-Gaussian anomalous fluctuations to logarithmically corrected and Gaussian scales, but no uniform moderate-deviation theorem is asserted here.

Rademacher studies large deviations for bounded one-particle observables in a weakly interacting Bose-gas ground state. That setting is interacting, zero-temperature, and concerns a different class of observables and rate estimates; it neither implies nor tabulates the canonical ideal-gas condensate rate derived here.

## Limitations
The result inherits the source theorem's spectral counting hypothesis and condensed-regime assumptions. It concerns only the right tail and only \(\alpha>1\). The formulas do not determine the probability exactly at \(\eta=\eta_{\max}\), where finer spectral data can matter. The small-\(\eta\) expansions describe the local geometry of the fixed-deviation rate function; without a uniform error estimate in the source large-deviation theorem, they are not by themselves a proof of moderate-deviation or central-limit scaling.

The literature comparison did not reveal an equivalent published polylogarithmic phase diagram for this exact canonical right-tail theorem, but absence from targeted searches is not a proof of global novelty.

## References
1. A. Deuchert and X. Li, “Large Deviations for the Bose--Einstein Condensate of the Ideal Gas in the Canonical Ensemble,” arXiv:2608.26378v1 (2026); revised as arXiv:2608.26378v2.
2. S. Chatterjee and P. Diaconis, “Fluctuations of the Bose-Einstein condensate,” Journal of Physics A: Mathematical and Theoretical 47 (2014), 085201, doi:10.1088/1751-8113/47/8/085201.
3. S. Rademacher, “Large Deviations for the Ground State of Weakly Interacting Bose Gases,” Annales Henri Poincaré 26 (2025), 1239–1289, doi:10.1007/s00023-024-01463-w.
