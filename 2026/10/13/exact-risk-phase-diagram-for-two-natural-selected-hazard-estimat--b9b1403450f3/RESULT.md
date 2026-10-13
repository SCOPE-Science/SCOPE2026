# Exact risk phase diagram for two natural selected-hazard estimators
## Finding
Consider two independent exponential populations with hazard rates
\[
\sigma_1,\sigma_2>0.
\]
From each population take \(n\ge2\) iid observations, let \(Y_i\) denote the sample sum from population \(i\), and select the population indexed by
\[
Y_J=\max(Y_1,Y_2).
\]
Under entropy loss
\[
L(\sigma,d)
=
\frac{d}{\sigma_J}
-
\log\!\left(\frac{d}{\sigma_J}\right)
-
1,
\]
compare the maximum-likelihood estimator
\[
\delta_{\mathrm{ML}}=\frac{n}{Y_J}
\]
with the BSEE analogue from the motivating paper,
\[
\delta_{\mathrm{N2}}=\frac{n-1}{Y_J}.
\]

Put
\[
r=\frac{\sigma_1}{\sigma_2},
\qquad
x(r)=\frac{r}{(1+r)^2}.
\]
Then
\[
R(\sigma,\delta_{\mathrm{ML}})
-
R(\sigma,\delta_{\mathrm{N2}})
=
\frac1{n-1}
-
\log\!\frac n{n-1}
-
\frac{x(r)^{n-1}}
{(n-1)^2B(n,n-1)}.
\tag{1}
\]

Define
\[
q_n=
\left[
(n-1)B(n,n-1)
\left\{
1-(n-1)\log\!\frac n{n-1}
\right\}
\right]^{1/(n-1)}
\]
and
\[
\rho_n=
\frac{1+\sqrt{1-4q_n}}
{1-\sqrt{1-4q_n}}.
\tag{2}
\]
Then \(0<q_n<1/4\), so \(\rho_n>1\), and the complete phase diagram is
\[
\begin{cases}
R(\sigma,\delta_{\mathrm{ML}})
<
R(\sigma,\delta_{\mathrm{N2}}),
&
\max(\sigma_1/\sigma_2,\sigma_2/\sigma_1)<\rho_n,
\\[2mm]
R(\sigma,\delta_{\mathrm{ML}})
=
R(\sigma,\delta_{\mathrm{N2}}),
&
\max(\sigma_1/\sigma_2,\sigma_2/\sigma_1)=\rho_n,
\\[2mm]
R(\sigma,\delta_{\mathrm{ML}})
>
R(\sigma,\delta_{\mathrm{N2}}),
&
\max(\sigma_1/\sigma_2,\sigma_2/\sigma_1)>\rho_n.
\end{cases}
\]
Thus the two estimators are not globally comparable, but their ordering is governed by one explicit hazard-ratio threshold.

Numerically,
\[
\rho_2=4.284376516357\ldots,
\qquad
\rho_5=2.679141980534\ldots,
\qquad
\rho_8=2.287831457726\ldots.
\]

## Assumptions and scope
The result is for exactly two populations and a common sample size \(n\ge2\). Each population is exponential with no location parameter and positive hazard rate. Selection is by the larger sample sum, equivalently the larger sample mean because the sample sizes agree.

The loss is the entropy loss used in the motivating paper. The result compares only the two natural estimators \(\delta_{\mathrm{ML}}\) and \(\delta_{\mathrm{N2}}\); it does not claim either one is admissible among all estimators. In fact, the motivating paper derives improved estimators for each.

## Proof
Let
\[
X_i=\sigma_iY_i.
\]
Then \(X_1,X_2\) are iid gamma variables with shape \(n\) and rate \(1\). Write
\[
S=X_1+X_2,
\qquad
T=\frac{X_1}{X_1+X_2}.
\]
The beta-gamma factorization gives
\[
S\sim\operatorname{Gamma}(2n,1),
\qquad
T\sim\operatorname{Beta}(n,n),
\]
with \(S\) and \(T\) independent.

Population \(1\) is selected exactly when
\[
\frac{X_1}{\sigma_1}>
\frac{X_2}{\sigma_2},
\]
or equivalently
\[
T>a,
\qquad
a=\frac{r}{1+r}.
\]
Also,
\[
\sigma_JY_J
=
\begin{cases}
X_1,&T>a,\\
X_2,&T\le a.
\end{cases}
\]
Therefore
\[
E\!\left[\frac1{\sigma_JY_J}\right]
=
E\!\left[
\frac1{X_1}\mathbf 1_{\{T>a\}}
+
\frac1{X_2}\mathbf 1_{\{T\le a\}}
\right].
\]
Since \(E[S^{-1}]=1/(2n-1)\),
\[
E\!\left[\frac1{\sigma_JY_J}\right]
=
\frac1{(2n-1)B(n,n)}
\left[
\int_a^1 t^{n-2}(1-t)^{n-1}\,dt
+
\int_0^a t^{n-1}(1-t)^{n-2}\,dt
\right].
\tag{3}
\]

The difference between the bracket in (3) and
\[
B(n-1,n)
\]
is
\[
\int_0^a
t^{n-2}(1-t)^{n-2}(2t-1)\,dt
=
-\frac{[a(1-a)]^{n-1}}{n-1}.
\]
Using
\[
a(1-a)=\frac{r}{(1+r)^2}=x(r)
\]
and the beta-function recurrence gives
\[
E\!\left[\frac1{\sigma_JY_J}\right]
=
\frac1{n-1}
-
\frac{x(r)^{n-1}}
{(n-1)^2B(n,n-1)}.
\tag{4}
\]

For an estimator \(\delta_c=c/Y_J\), entropy risk can be written as
\[
R(\sigma,\delta_c)
=
c\,E\!\left[\frac1{\sigma_JY_J}\right]
-\log c
+
E[\log(\sigma_JY_J)]
-1.
\]
Subtracting the cases \(c=n\) and \(c=n-1\) cancels the last two common terms and proves (1).

It remains to prove the unique threshold. Put \(m=n-1\). As \(r\to0\) or \(r\to\infty\), the last term in (1) tends to zero, while
\[
\frac1m-\log\!\left(1+\frac1m\right)>0.
\tag{5}
\]
At \(r=1\),
\[
x(1)=\frac14.
\]
Using
\[
B(m+1,m)=\frac1{m\binom{2m}{m}},
\]
equation (1) becomes
\[
\frac{1-c_m}{m}
-
\log\!\left(1+\frac1m\right),
\qquad
c_m=\frac{\binom{2m}{m}}{4^m}.
\tag{6}
\]
Now
\[
\log(1+1/m)>\frac1{m+1},
\]
so
\[
1-m\log(1+1/m)<\frac1{m+1}.
\]
Also
\[
c_m\ge\frac1{2\sqrt m}\ge\frac1{m+1}.
\]
The first inequality follows by induction from
\[
\frac{c_{m+1}}{c_m}
=
\frac{2m+1}{2m+2}
\ge
\sqrt{\frac m{m+1}},
\qquad
c_1=\frac12.
\]
Hence the quantity in (6) is strictly negative.

Finally, if
\[
\rho=\max(r,1/r)\ge1,
\]
then
\[
x(r)=\frac{\rho}{(1+\rho)^2}
\]
is strictly decreasing in \(\rho\). Thus the risk difference (1) is strictly increasing in \(\rho\), starts negative at \(\rho=1\), and tends to the positive limit (5). It has exactly one zero. Solving
\[
\frac{\rho}{(1+\rho)^2}=q_n
\]
gives (2), completing the proof.

## Verification
The standalone script `verify.py` recomputes the threshold constants, independently compares the closed form (4) with numerical beta integration over deterministic test cases, checks the center and extreme sign pattern through many sample sizes, and verifies that substituting \(\rho_n\) into (1) gives zero to numerical precision.

A successful run ends with
`VERIFY_OK rho2=4.284376516357 rho5=2.679141980534 rho8=2.287831457726`.

The numerical checks are reproducibility checks only. The risk formula and uniqueness of the crossover are proved analytically above.

## Relationship to prior work
Jha, Mahapatra, and Kayal study exactly this two-population exponential selection problem under entropy loss as a special case of their general setup. They define
\[
\delta_{\mathrm{ML}}=\frac n{Y_J},
\qquad
\delta_{\mathrm{N2}}=\frac{n-1}{Y_J},
\]
derive an integral representation for
\[
E[(\sigma_JY_J)^{-1}],
\]
and use it to establish an admissible interval within the scale-equivariant class. Their numerical section explicitly reports that they could not obtain a hierarchy between \(\delta_{\mathrm{N2}}\) and \(\delta_{\mathrm{ML}}\) because the two are not globally comparable. Formula (1) sharpens that observation into an exact analytic partition of the full two-dimensional hazard parameter space.

The authors' earlier 2020 paper treats the same selection rule under quadratic loss, so its risk comparisons do not imply the entropy-loss phase diagram. A later paper in the same estimation-after-selection program under entropy loss uses a different selection rule and reports simulation comparisons; the inspected material does not state the threshold (2).

Targeted semantic searches using the estimator names, exact risk comparison, hazard-ratio threshold, beta-function form, and selected-exponential aliases did not locate a published statement of (1) or (2).

## Limitations
The result concerns only the comparison between the MLE and the BSEE analogue. The motivating paper already shows that improved estimators can dominate these natural estimators, so the phase diagram should not be interpreted as an optimality theorem over all decision rules.

Only the two-population case is treated. For more than two populations the beta reduction becomes a higher-dimensional gamma-ratio integral and the one-threshold structure need not survive.

An equivalent short calculation could exist in older estimation-after-selection literature under different scale-versus-hazard parametrization; this remains the main residual bibliographic risk.

## References
1. B. K. Jha, A. K. Mahapatra, and S. Kayal, “Inadmissibility Results for the Selected Hazard Rates,” arXiv:2107.03848v1, 8 July 2021; *Statistics* 55 (2021), 580–594. DOI: 10.1080/02331888.2021.1954924.
2. B. K. Jha, A. K. Mahapatra, and S. Kayal, “Estimation of Hazard Rate of a Selected Exponential Population,” *Journal of Statistical Theory and Practice* 14 (2020), 47. DOI: 10.1007/s42519-020-00112-9.
3. “Improving on Admissible Estimators Under Entropy Loss Function,” preprint first posted in 2024; the inspected public manuscript classifies the problem under MSC 62F07 (primary), 62F10, and 62F15.
