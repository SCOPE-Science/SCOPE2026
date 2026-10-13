# The published WSG-Kumaraswamy density is not normalized
## Finding
Let
\[
\delta>0,\qquad \alpha>0,\qquad 0<y<1,
\]
and define
\[
\theta(y)=\frac{\pi}{2}(1-y^\delta)^\alpha.
\]
The 2026 WSG-Kumaraswamy article gives the CDF
\[
F(y)=\cos\theta(y)\exp\{1-\cos\theta(y)\}.
\]

Its displayed Eq. (4), however, uses
\[
f_{\mathrm{pub}}(y)
=
\frac{\pi}{2}\delta\alpha y^{\delta-1}(1-y^\delta)^{\alpha-1}
\cos\theta(y)\,e^{1-\cos\theta(y)}[1-\cos\theta(y)].
\]
This is not the derivative of the displayed CDF and is not normalized.

Differentiating the CDF gives the corrected density
\[
\boxed{
f(y)
=
\frac{\pi}{2}\delta\alpha y^{\delta-1}(1-y^\delta)^{\alpha-1}
\sin\theta(y)\,e^{1-\cos\theta(y)}[1-\cos\theta(y)].
}
\]
The correction is a single trigonometric factor:
\[
\boxed{\cos\theta(y)\ \longrightarrow\ \sin\theta(y).}
\]

The corrected density integrates exactly to one. In contrast, the total mass of the published Eq. (4) is independent of \(\delta\) and \(\alpha\) and equals
\[
\boxed{
I=\int_0^{\pi/2}\cos t\,e^{1-\cos t}(1-\cos t)\,dt
=0.344992796947\ldots .
}
\]
Thus the displayed Eq. (4) loses about \(65.5\%\) of the required probability mass.

The same cosine factor is carried into the paper's raw-moment integral and log-likelihood. Therefore those displayed formulas are not moments or a likelihood for the displayed CDF. In particular, the parameter-dependent trigonometric term in the correct log-likelihood is
\[
\sum_i\log\sin\theta(y_i),
\]
not
\[
\sum_i\log\cos\theta(y_i).
\]

The quantile equation, which is derived directly from the CDF, is not affected by this density correction.

## Assumptions and scope
The claim concerns the exact CDF and PDF printed for the WSG-Kumaraswamy model in the 2026 source. No alternative parameterization is introduced.

The correction does not assert that every reported numerical table was necessarily computed from the erroneous printed density. The implementation code used for all numerical experiments was not independently reconstructed. The scientific statement is narrower: the displayed CDF, displayed PDF, moment integral, hazard numerator, and displayed likelihood do not define one coherent probability model as written.

The prior 2024 new weighted sine-G construction is used only as a structural cross-check. Its general PDF contains
\[
\cos\!\left(\frac{\pi}{2}G(y)\right).
\]
For the Kumaraswamy baseline,
\[
G(y)=1-(1-y^\delta)^\alpha,
\]
so
\[
\cos\!\left(\frac{\pi}{2}G(y)\right)
=
\sin\!\left(\frac{\pi}{2}(1-y^\delta)^\alpha\right),
\]
which is exactly the corrected factor.

## Proof
Write
\[
\theta=\theta(y)=\frac{\pi}{2}(1-y^\delta)^\alpha.
\]
The source's CDF is
\[
F(y)=z e^{1-z},\qquad z=\cos\theta.
\]
Since
\[
\frac{d}{dz}\{z e^{1-z}\}=e^{1-z}(1-z),
\]
\[
\frac{dz}{d\theta}=-\sin\theta,
\]
and
\[
\frac{d\theta}{dy}
=-\frac{\pi}{2}\delta\alpha y^{\delta-1}(1-y^\delta)^{\alpha-1},
\]
the chain rule gives
\[
F'(y)
=
\frac{\pi}{2}\delta\alpha y^{\delta-1}(1-y^\delta)^{\alpha-1}
\sin\theta\,e^{1-\cos\theta}(1-\cos\theta).
\]
This proves the corrected density formula and shows pointwise that the published cosine factor is inconsistent with the CDF.

For normalization, use \(\theta\) as the integration variable. Because \(\theta\) decreases from \(\pi/2\) to \(0\) as \(y\) increases from \(0\) to \(1\),
\[
\int_0^1 f(y)\,dy
=
\int_0^{\pi/2}\sin t\,e^{1-\cos t}(1-\cos t)\,dt.
\]
With
\[
u=1-\cos t,
\]
this becomes
\[
\int_0^1 u e^u\,du=1.
\]

For the published kernel,
\[
\int_0^1 f_{\mathrm{pub}}(y)\,dy
=
I
=
\int_0^{\pi/2}\cos t\,e^{1-\cos t}(1-\cos t)\,dt.
\]
This mass is independent of both model parameters. It is rigorously less than one. Set \(s=\sin t\). Then
\[
I
=
\int_0^1 x(s)e^{x(s)}\,ds,
\qquad
x(s)=1-\sqrt{1-s^2}\in[0,1].
\]
Since \(x e^x\le e x\) on \([0,1]\),
\[
I
\le
 e\int_0^1\left(1-\sqrt{1-s^2}\right)ds
=
 e\left(1-\frac{\pi}{4}\right)
<1.
\]
Thus Eq. (4) cannot be a probability density. High-precision quadrature gives
\[
I=0.3449927969472642938\ldots .
\]

Finally, the source's moment integral and log-likelihood explicitly inherit the same published cosine factor. Replacing that factor by the derivative-required sine factor gives the corresponding corrected formulas.

## Verification
The accompanying checker performs four independent checks from the actual formulas.

First, it differentiates the CDF numerically and compares the derivative with the corrected density at multiple parameter values and interior points.

Second, it integrates the corrected density for several \((\delta,\alpha)\) pairs and obtains unit mass.

Third, it integrates the published Eq. (4) for the same parameter pairs and obtains the same parameter-independent mass
\[
0.3449927969472642938\ldots .
\]

Fourth, it verifies the analytic upper bound
\[
I<e\left(1-\frac{\pi}{4}\right)<1.
\]

The numerical work is supplementary. The CDF/PDF incompatibility and non-normalization are proved analytically.

## Relationship to prior work
Genç and Özbilen introduce the WSG-Kumaraswamy distribution by applying the new weighted sine-G transform to the Kumaraswamy baseline. Their Eq. (3) gives the CDF, Eq. (4) is labeled as its corresponding PDF, the moment section uses the same cosine-based kernel, and Eq. (16) builds the likelihood from that kernel.

The model cites Heydari et al. as the source of the new weighted sine-G construction. That 2024 source gives the general transform
\[
T(G)=\sin\!\left(\frac{\pi}{2}G\right)
\exp\!\left\{1-\sin\!\left(\frac{\pi}{2}G\right)\right\}
\]
and its derivative contains
\[
\cos\!\left(\frac{\pi}{2}G\right).
\]
Substituting
\[
G=1-(1-y^\delta)^\alpha
\]
turns this cosine into the sine factor in the corrected density. Thus the cited generator and direct differentiation agree with each other and disagree with the specialized Eq. (4).

Focused searches using the exact DOI, the model name, CDF/PDF derivative terminology, sine/cosine substitution, normalization, likelihood, and correction/erratum terminology did not locate a published correction of this defect.

## Limitations
The finding establishes a formula-level inconsistency and its consequences for displayed analytic expressions. It does not reconstruct the unpublished implementation behind every simulation or empirical table.

If some numerical calculations used the derivative-correct density rather than the printed Eq. (4), those particular calculations may survive. If they used Eq. (4) or Eq. (16) as printed, they do not correspond to likelihood inference for the displayed CDF.

No independent re-estimation of the two real-data applications is claimed here.

## References
1. M. Genç and Ö. Özbilen, “A New Trigonometric-Inspired Probability Distribution: The Weighted Sine Generalized Kumaraswamy Model with Simulation and Applications in Epidemiology and Reliability Engineering,” Mathematics 14 (2026), 510. DOI: 10.3390/math14030510.
2. T. Heydari, K. Zare, S. Shokri, Z. Khodadadi, and Z. Almaspoor, “A New Sine-Based Probabilistic Approach: Theory and Monte Carlo Simulation with Reliability Application,” Journal of Mathematics (2024), 9593193. DOI: 10.1155/2024/9593193.
