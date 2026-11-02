# Exact maximum-spacing–Greenwood dependence and a truncated quadratic-spacing law

## Finding
Let \(m\ge 2\), and let \((D_1,\ldots,D_m)\) be the \(m\) successive gaps, including both boundary gaps, cut out by \(m-1\) independent uniform points in \([0,1]\). Write
\[
M_m=\max_{1\le i\le m}D_i,\qquad G_m=\sum_{i=1}^m D_i^2,\qquad
H_m=\sum_{j=1}^m\frac1j,\quad H_m^{(2)}=\sum_{j=1}^m\frac1{j^2}.
\]
For any \(0\le t\le1\), put \(b_k(t)=(1-kt)_+\). The complete truncated first quadratic moment is
\[
\begin{aligned}
F_m(t)&=\Pr(M_m\le t)=\sum_{k=0}^m(-1)^k\binom mk b_k(t)^{m-1},\\
A_m(t)&=\mathbb E[G_m\mathbf1_{\{M_m\le t\}}]\\
&=\frac2{m+1}+\sum_{k=1}^m(-1)^k\binom mk b_k(t)^{m-1}
\left(kt^2+\frac{2kt\,b_k(t)}m+\frac{2b_k(t)^2}{m+1}\right).
\end{aligned}
\]
Here the \(k=0\) term in \(F_m\) is one. For \(t>1/m\), the exact regression on a maximum-spacing threshold is \(\mathbb E[G_m\mid M_m\le t]=A_m(t)/F_m(t)\).

In particular the mixed moment and covariance are
\[
\mathbb E[M_mG_m]=\frac{H_m^2+H_m^{(2)}+2(m+1)H_m}{m(m+1)(m+2)},\qquad
\boxed{\operatorname{Cov}(M_m,G_m)=\frac{H_m^2+H_m^{(2)}-2H_m}{m(m+1)(m+2)}>0.}
\]
The accompanying exact marginal variances yield
\[
\operatorname{Var}(M_m)=\frac{mH_m^{(2)}-H_m^2}{m^2(m+1)},\quad
\operatorname{Var}(G_m)=\frac{4(m-1)}{(m+1)^2(m+2)(m+3)},
\]
\[
\operatorname{Corr}(M_m,G_m)=\frac{\big(H_m^2+H_m^{(2)}-2H_m\big)\sqrt{(m+1)(m+3)}}{2\sqrt{(m+2)(m-1)(mH_m^{(2)}-H_m^2)}}
\sim\frac{\sqrt6}{2\pi}\frac{(\log m)^2}{\sqrt m}.
\]
Thus the covariance is positive for every finite \(m\ge2\), while the Pearson correlation approaches zero. For \(m=2\), \(\operatorname{Cov}(M_m,G_m)=1/48\) and \(\operatorname{Corr}(M_m,G_m)=\sqrt{15}/4\); for \(m=3\) the covariance is \(19/1080\).

## Assumptions and scope
The input sample consists of exactly \(m-1\) independent observations from the continuous uniform law on \([0,1]\), with ordered values augmented by 0 and 1. Equivalently, \(D=(D_1,\ldots,D_m)\) is uniform on the probability simplex, i.e. \(\operatorname{Dirichlet}(1,\ldots,1)\). All formulas concern this exact null law and \(m\ge2\), not arbitrary independent gaps, unequal Dirichlet concentrations, or a fitted distribution parameter. The normalized Greenwood sum used in some testing conventions is a deterministic multiple of \(G_m\); the covariance rescales accordingly, and the correlation does not.

## Proof
**1. Marked-threshold simplex identity.** For a fixed set \(I\subseteq\{1,\ldots,m\}\) of \(k\ge1\) gap indices and \(0\le t<1/k\), translation and rescaling of the uniform simplex show
\[
\Pr(D_i>t\text{ for all }i\in I)=(1-kt)^{m-1}.
\]
Conditional on this event, take a fresh uniform-simplex vector \(Y\). Then \(D_i=t+(1-kt)Y_i\) for \(i\in I\), and \(D_j=(1-kt)Y_j\) otherwise. Because \(\mathbb E Y_i=1/m\) and \(\mathbb E\sum_iY_i^2=2/(m+1)\), one gets
\[
\mathbb E[G_m\mid D_i>t\ (i\in I)]=kt^2+\frac{2kt(1-kt)}m+\frac{2(1-kt)^2}{m+1}.
\]
The probability and weighted moment vanish outside \(kt<1\). Applying inclusion–exclusion to \(\{M_m>t\}=\cup_i\{D_i>t\}\) proves both displayed truncated-moment expressions, with equality at breakpoints by continuity. The conditional threshold regression follows when the conditioning event has positive probability.

**2. Mixed moment.** Since \(M_m\in[0,1]\), layer cake gives \(\mathbb E[M_mG_m]=\int_0^1\mathbb E[G_m\mathbf1_{\{M_m>t\}}]\,dt\). For a fixed \(k\)-subset, substitution \(u=kt\) in its weighted term gives
\[
\int_0^{1/k}(1-kt)^{m-1}
\left(kt^2+\frac{2kt(1-kt)}m+\frac{2(1-kt)^2}{m+1}\right)dt
=\frac{2}{m(m+1)(m+2)}\left(\frac1{k^2}+\frac{m+1}{k}\right).
\]
Use the binomial harmonic identities
\[
\sum_{k=1}^m(-1)^{k+1}\binom mk\frac1k=H_m,
\quad\sum_{k=1}^m(-1)^{k+1}\binom mk\frac1{k^2}=\frac{H_m^2+H_m^{(2)}}2.
\]
These identities follow by integrating \(\bigl(1-(1-u)^m\bigr)/u\) and its logarithm-weighted variant, or by induction. This establishes the mixed moment.

**3. Covariance and strict sign.** The usual maximum-spacing layer-cake calculation gives \(\mathbb E M_m=H_m/m\), while the Dirichlet second moments give \(\mathbb E G_m=2/(m+1)\). Subtraction yields the covariance formula. Let \(B_m=H_m^2+H_m^{(2)}-2H_m\). Then \(B_1=0\) and \(B_m-B_{m-1}=2(H_m-1)/m>0\) for every \(m\ge2\), proving strict positivity without numerical approximation.

**4. Variances and limiting correlation.** A second application of layer cake yields \(\mathbb E M_m^2=(H_m^2+H_m^{(2)})/[m(m+1)]\). The Dirichlet fourth-moment rule gives \(\mathbb E G_m^2=4(m+5)/[(m+1)(m+2)(m+3)]\). Subtracting squared means yields the displayed variances and correlation. Finally, \(H_m=\log m+\gamma+O(m^{-1})\) and \(H_m^{(2)}=\pi^2/6+O(m^{-1})\) imply \(B_m\sim(\log m)^2\), giving the stated asymptotic correlation.

## Verification
Run `python3 verify.py` using Python 3 with only the standard library. The verifier re-evaluates the inclusion–exclusion binomial sums and moments with exact fractions for all \(2\le m\le500\), independently integrates the two-dimensional uniform-simplex polynomial over maximal-coordinate sectors for \(m=3\), checks truncated moments at two rational thresholds by a separate geometric integration, verifies \(m=2\) boundary values and exact positivity, and evaluates the asymptotic normalization diagnostically. Successful execution prints `VERIFIED 2760 assertions`. These finite verifications do not prove the arbitrary-size result; its proof is the preceding simplex argument.

## Relationship to prior work
Fisher's maximum-spacing tail law, reviewed and extended for ordered gaps by Pinelis (2019), supplies the classical **unweighted** maximum-spacings distribution. Pyke's 1965 survey and later spacings surveys discuss Dirichlet gap moments, maximal spacings, and the Greenwood sum; Aaron–Cholaquidis–Fraiman (2014) analyzes maximal spacing for geometric goodness-of-fit, not quadratic gap energy. The present claim is a **weighted threshold moment** and its resulting exact finite-sample mixed covariance and correlation decay. These are not implied by an unweighted maximum-gap marginal formula alone. The simplex inclusion–exclusion method is classical, and no novelty is claimed for that method, marginal moments, or the Gumbel limit of the maximum.

## Limitations
Historical priority remains subject to specialized joint spacing-statistic literature, including parts of Pyke (1965) that were not accessible in full. No assertion is made that the two statistics are asymptotically independent: vanishing Pearson correlation by itself does not establish independence. The truncated first moment does not supply an exact joint tail distribution, and no combined-test calibration or power improvement is proved. The formulas require the uniform-simplex null model and the specific unscaled quadratic sum.

## References
- Aaron, C., Cholaquidis, A. and Fraiman, R. (2014), *A Generalization of the maximal-spacings in several dimensions and a convexity test*, arXiv:1411.2482v1, first submitted 2014-11-10; https://arxiv.org/abs/1411.2482 .
- Pinelis, I. (2019), *Order statistics on the spacings between order statistics for the uniform distribution*, arXiv:1909.06406; https://arxiv.org/abs/1909.06406 .
- Pyke, R. (1965), *Spacings*, Journal of the Royal Statistical Society B 27(3), 395–436; https://doi.org/10.1111/j.2517-6161.1965.tb00602.x .
- Das, S. and Maiti, S. I. (2021), *Uniform spacings—A Bird's-Eye View*, volume 19(2), pp. 217–230; https://ssca.org.in/media/16_19_2_2021_SA_Saran_Ishika_Maiti_Final.pdf .
- Huffer, F., *Divided differences and the joint distribution of linear combinations of spacings*, Journal of Applied Probability, archival journal record https://doi.org/10.2307/3214442 (linear, not quadratic, spacing combinations).
