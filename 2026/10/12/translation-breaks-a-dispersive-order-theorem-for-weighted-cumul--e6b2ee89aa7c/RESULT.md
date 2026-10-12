# Translation breaks a dispersive-order theorem for weighted cumulative residual quantile extropy
## Finding
Theorem 7 of Sahu, Chaudhary, and Gupta (2026) is false under its stated hypotheses. Let
\[
X\sim\operatorname{Uniform}(0,1),\qquad Y=X+2\sim\operatorname{Uniform}(2,3),
\]
and use the same weight for both variables,
\[
w_1=w_2=w,\qquad w(x)=e^{-x}.
\]
The weight is positive, integrable on each support, and strictly decreasing. The quantile functions and quantile densities are
\[
Q_X(p)=p,\quad Q_Y(p)=p+2,\qquad q_X(p)=q_Y(p)=1.
\]
Therefore, for every \(0<u<v<1\),
\[
Q_X(v)-Q_X(u)=v-u=Q_Y(v)-Q_Y(u),
\]
so \(X\leq_{\mathrm{disp}}Y\) (indeed, the two laws are equivalent in dispersive order).

The paper defines the weighted cumulative residual quantile extropy by
\[
\Phi_Q^w(u)=-\frac{1}{2(1-u)^2}\int_u^1 w(Q(p))(1-p)^2q(p)\,dp.
\]
For the translated uniforms,
\[
w(Q_Y(p))q_Y(p)=e^{-(p+2)}=e^{-2}e^{-p}=e^{-2}w(Q_X(p))q_X(p),
\]
and hence, for every \(0<u<1\),
\[
\Phi_{Q_Y}^w(u)=e^{-2}\Phi_{Q_X}^w(u).
\]
Because the integral in the definition is strictly positive,
\[
\Phi_{Q_X}^w(u)<0,
\]
so \(0<e^{-2}<1\) gives
\[
\Phi_{Q_X}^w(u)<\Phi_{Q_Y}^w(u),
\]
which is the strict reverse of the theorem's asserted inequality \(\Phi_{Q_X}^{w_1}(u)\geq\Phi_{Q_Y}^{w_2}(u)\).

## Assumptions and scope
The counterexample uses non-negative, absolutely continuous laws with strictly increasing continuous distribution functions on their supports, square-integrable densities, differentiable quantile functions, and a non-negative integrable weight. These are the standing assumptions stated in the source. The equality \(w_1=w_2\) satisfies the hypothesis \(w_1(x)\leq w_2(x)\), while \(w(x)=e^{-x}\) is strictly decreasing.

The claim concerns Theorem 7 as printed in the public 28 September 2026 version. It does not assert that no strengthened stochastic-order theorem is possible. In particular, adding a suitable location/support condition can block the translation counterexample.

## Proof
By the quantile definition of dispersive order, \(X\leq_{\mathrm{disp}}Y\) means
\[
Q_X(v)-Q_X(u)\leq Q_Y(v)-Q_Y(u)
\]
for all \(0<u<v<1\). Here both differences equal \(v-u\), so the premise holds exactly.

Substituting the two quantile functions into the source's equation for weighted cumulative residual quantile extropy gives
\[
\Phi_{Q_X}^w(u)
=-\frac{1}{2(1-u)^2}\int_u^1 e^{-p}(1-p)^2\,dp
\]
and
\[
\Phi_{Q_Y}^w(u)
=-\frac{1}{2(1-u)^2}\int_u^1 e^{-(p+2)}(1-p)^2\,dp
=e^{-2}\Phi_{Q_X}^w(u).
\]
The first integral is strictly positive for \(0<u<1\), hence \(\Phi_{Q_X}^w(u)<0\). Multiplication by \(e^{-2}\in(0,1)\) moves this negative value toward zero, proving
\[
\Phi_{Q_X}^w(u)<\Phi_{Q_Y}^w(u)
\]
for every \(0<u<1\).

The proof in the source tries to infer \(X\geq_{\mathrm{st}}Y\) from \(X\leq_{\mathrm{disp}}Y\). That implication is not valid under the theorem's stated assumptions: in the present example \(Q_X(p)=p<Q_Y(p)=p+2\), so instead \(X\leq_{\mathrm{st}}Y\). The earlier unweighted quantile-survival-extropy literature invokes the corresponding dispersive-to-stochastic comparison only together with endpoint conditions; those conditions are absent from Theorem 7.

## Verification
The counterexample is symbolic and does not depend on finite enumeration or numerical approximation. Each hypothesis can be checked directly from the two uniform laws and the exponential weight. The sign reversal follows pointwise under the integral and therefore holds for every \(u\in(0,1)\), not merely at a sampled threshold.

For an explicit closed form,
\[
\int_u^1 e^{-p}(1-p)^2\,dp=e^{-u}(u^2+1)-2e^{-1},
\]
which is positive for \(0<u<1\) because it is the integral of a positive function. This recovers the same strict inequality.

## Relationship to prior work
Sahu, Chaudhary, and Gupta introduce the weighted cumulative residual quantile extropy and state Theorem 7 as a dispersive-order comparison under a decreasing weight. The source's proof uses a dispersive-to-usual-stochastic-order implication without stating a location or endpoint hypothesis.

A closely related earlier paper by Khammar, Amir Jahanshahi, and Zarei studies the unweighted quantile-based dynamic survival extropy. In its Theorem 2.14 proof, the dispersive-to-stochastic comparison is used only after imposing a common right endpoint, which is precisely the kind of location information absent from the 2026 theorem. That earlier paper does not contain the weighted translation counterexample above.

Standard references describe dispersive order through interquantile ranges, making its invariance under translations immediate. Thus the failure is structurally tied to combining a translation-invariant premise with a value-dependent weight.

## Limitations
The result refutes the theorem as stated; it does not classify all additional assumptions under which a weighted dispersive-order inequality is valid. A natural repair is to require the quantile-location inequality actually used in the proof, such as \(Q_X(p)\geq Q_Y(p)\) for all relevant \(p\), together with the dispersive comparison, but no maximal repaired hypothesis is claimed here.

The public source is very recent. A later corrigendum or revised version could supersede the inspected theorem; no such correction was located in the searches used for this finding.

## References
1. P. K. Sahu, S. K. Chaudhary, and N. Gupta, “Quantile-based reliability analysis of weighted extropy,” Probability in the Engineering and Informational Sciences, published online 28 September 2026. DOI: 10.1017/S0269964826100394.
2. A. H. Khammar, S. M. Amir Jahanshahi, and H. Zarei, “On quantile-based dynamic survival extropy and its applications,” Hacettepe Journal of Mathematics and Statistics 52 (2023), 1349–1366. DOI: 10.15672/hujms.823331.
3. J. Jeon, S. Kochar, and C. G. Park, “Dispersive ordering—Some applications and examples,” Statistical Papers 47 (2006), 227–247. DOI: 10.1007/s00362-005-0285-4.
