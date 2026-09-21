# Sharp sign-sensitive Gaussianization thresholds for equal-spectrum second-chaos maxima

## Result

Let \(p\to\infty\), put \(L=\log p\), and let \(m=m_p\to\infty\) be even. Consider the two variance-one second-Gaussian-chaos laws
\[
Q_m^{+}=\frac1{\sqrt{2m}}\sum_{r=1}^m(Z_r^2-1),
\]
and
\[
Q_m^{0}=\frac1{\sqrt{2m}}
\left\{
\sum_{r=1}^{m/2}(Z_r^2-1)-
\sum_{r=m/2+1}^{m}(Z_r^2-1)
\right\},
\]
where the \(Z_r\) are independent standard Gaussians. For each row take \(p\) independent copies and write their maxima as \(M_{p,m}^{+}\) and \(M_{p,m}^{0}\). Let \(G_p=\max_{j\le p}N_j\) for independent \(N_j\sim N(0,1)\), and define the standard Gaussian extreme-value normalizations
\[
s_p=\sqrt{2L},\qquad
d_p=\sqrt{2L}-\frac{\log L+\log(4\pi)}{2\sqrt{2L}}.
\]
Let \(\Lambda\) denote a standard Gumbel variable, with distribution function \(\exp(-e^{-x})\).

The two chaos families have **identical fourth-order effective rank**
\[
r_4=\frac{(\sum_r\lambda_r^2)^2}{\sum_r\lambda_r^4}=m
\]
and identical fourth cumulant \(12/m\), but their maxima have different sharp Gaussianization scales.

### Positive equal spectrum

Assume \(m/L\to\infty\). If
\[
\frac{L^3}{m}\to\tau\in[0,\infty),
\]
then
\[
\boxed{
 s_p(M_{p,m}^{+}-d_p)
 \Rightarrow
 \Lambda+\frac43\sqrt{\tau}.
}
\]
Consequently,
\[
\boxed{
 d_K(M_{p,m}^{+},G_p)
 \longrightarrow
 D\!\left(\frac43\sqrt\tau\right),
}
\]
where for \(\delta\ge0\)
\[
D(\delta)=
\begin{cases}
0,&\delta=0,\\[2mm]
\displaystyle
\exp\!\left[-\frac{\delta}{e^\delta-1}\right](1-e^{-\delta}),&\delta>0.
\end{cases}
\]
If instead \(L^3/m\to\infty\) while \(m/L\to\infty\), then
\[
d_K(M_{p,m}^{+},G_p)\to1.
\]
Thus, in this moderate-deviation regime,
\[
\boxed{
 d_K(M_{p,m}^{+},G_p)\to0
 \iff
 m\gg(\log p)^3.
}
\]

### Balanced signed equal spectrum

Again assume \(m/L\to\infty\). If
\[
\frac{L^2}{m}\to\tau\in[0,\infty),
\]
then
\[
\boxed{
 s_p(M_{p,m}^{0}-d_p)
 \Rightarrow
 \Lambda+2\tau,
}
\]
and hence
\[
\boxed{
 d_K(M_{p,m}^{0},G_p)
 \longrightarrow D(2\tau).
}
\]
If \(L^2/m\to\infty\) while \(m/L\to\infty\), then
\[
d_K(M_{p,m}^{0},G_p)\to1.
\]
Therefore
\[
\boxed{
 d_K(M_{p,m}^{0},G_p)\to0
 \iff
 m\gg(\log p)^2.
}
\]

The conclusion is that fourth-order effective rank alone does not determine the **sharp** Gaussianization boundary for maxima of signed quadratic Gaussian chaoses: two spectra with the same \(r_4=m\) have thresholds separated by one full logarithmic power. Spectral sign balance removes the cubic Cramér correction and exposes the quartic one.

## Proof

### 1. Cumulant mechanism

For the positive spectrum,
\[
K_+(t):=\log \mathbb E e^{tQ_m^+}
=-t\sqrt{m/2}-\frac m2\log\!\left(1-\sqrt{2/m}\,t\right),
\]
so, uniformly for \(|t|=o(\sqrt m)\),
\[
K_+(t)
=\frac{t^2}{2}+\frac{\sqrt2}{3\sqrt m}t^3
 +\frac{1}{2m}t^4+O\!\left(\frac{|t|^5}{m^{3/2}}\right).
\]
In particular
\[
\kappa_3(Q_m^+)=\frac{2\sqrt2}{\sqrt m},
\qquad
\kappa_4(Q_m^+)=\frac{12}{m}.
\]

For the balanced spectrum the odd cumulants vanish. Pairing one positive and one negative eigenvalue gives the exact mgf
\[
K_0(t):=\log \mathbb E e^{tQ_m^0}
=-\frac m4\log\!\left(1-\frac{2t^2}{m}\right)
=\frac{t^2}{2}+\frac{t^4}{2m}
 +\frac{2t^6}{3m^2}+O\!\left(\frac{|t|^8}{m^3}\right).
\]
Hence
\[
\kappa_3(Q_m^0)=0,
\qquad
\kappa_4(Q_m^0)=\frac{12}{m}.
\]
Both spectra therefore have the same effective rank and fourth cumulant, while only the positive spectrum has a cubic Cramér correction.

### 2. Positive spectrum: the cubic correction

Since
\[
Q_m^+=\frac{Y-m/2}{\sqrt{m/2}},
\qquad Y\sim\Gamma(m/2,1),
\]
the growing-shape Gamma maximum theorem of Bose, Dasgupta and Maulik applies whenever \(m/L\to\infty\). It supplies a Gumbel centering \(b_{p,m}\sim\sqrt{2L}\) satisfying
\[
\log b_{p,m}+\frac12\log(2\pi)
+b_{p,m}\sqrt{m/2}
-\frac m2\log\!\left(1+b_{p,m}\sqrt{2/m}\right)=L,
\]
and
\[
s_p(M_{p,m}^{+}-b_{p,m})\Rightarrow\Lambda.
\]
Expanding the defining equation at \(b_{p,m}\asymp\sqrt L\) gives
\[
L=
\log b_{p,m}+\frac12\log(2\pi)
+\frac{b_{p,m}^2}{2}
-\frac{\sqrt2}{3\sqrt m}b_{p,m}^3
+O\!\left(\frac{b_{p,m}^4}{m}\right).
\]
The standard Gaussian centering obeys the same equation without the cubic term up to an \(o(1)\) error at Gumbel scale. Since \(m/L\to\infty\), the quartic remainder is smaller than the cubic correction by \(O(\sqrt{L/m})\). Therefore, whenever \(L^3/m\to\tau<\infty\),
\[
s_p(b_{p,m}-d_p)
=\frac43\frac{L^{3/2}}{\sqrt m}+o(1)
\to\frac43\sqrt\tau.
\]
Combining this with the Gamma maximum theorem yields the asserted shifted-Gumbel limit. If \(L^3/m\to\infty\), the same expansion shows that the chaos centering escapes to the right by infinitely many Gaussian Gumbel scales, which implies Kolmogorov separation tending to one.

### 3. Balanced spectrum: the quartic correction

Write \(k=m/2\). After an orthogonal change of variables,
\[
Q_m^0=\frac1{\sqrt k}\sum_{r=1}^k U_r,
\qquad
U_r=A_rB_r,
\]
where \(A_r,B_r\) are independent standard Gaussians. Thus the row law is a normalized sum of i.i.d. centered variance-one variables with analytic mgf
\[
\mathbb E e^{tU_1}=(1-t^2)^{-1/2}.
\]
Equivalently its normalized cgf is the exact \(K_0\) above.

Let \(I_m(x)=\sup_t\{tx-K_0(t)\}\). The saddle point is
\[
t_x=\frac{m}{4x}
\left(\sqrt{1+\frac{8x^2}{m}}-1\right)
=x-\frac{2x^3}{m}+\frac{8x^5}{m^2}
+O\!\left(\frac{x^7}{m^3}\right),
\]
which gives
\[
I_m(x)
=\frac{x^2}{2}-\frac{x^4}{2m}
 +\frac{4x^6}{3m^2}
 +O\!\left(\frac{x^8}{m^3}\right).
\]
A standard exponential-tilting/Laplace calculation for this analytic i.i.d. triangular array gives, uniformly for \(x\asymp\sqrt L\) under \(m/L\to\infty\),
\[
\mathbb P(Q_m^0>x)
=\frac{e^{-I_m(x)}}{x\sqrt{2\pi}}\{1+o(1)\}.
\]
The same prefactor occurs in Mills' ratio for \(\bar\Phi(x)\). Hence
\[
\log\frac{\mathbb P(Q_m^0>x)}{\bar\Phi(x)}
=\frac{x^4}{2m}
+O\!\left(\frac{x^6}{m^2}+\frac{x^2}{m}\right)+o(1).
\]
At a Gaussian extreme threshold
\[
x=d_p+\frac y{s_p},
\]
with fixed \(y\), one has \(x^2=2L+O(\log L)\). Therefore, if \(L^2/m\to\tau<\infty\),
\[
\frac{\mathbb P(Q_m^0>x)}{\bar\Phi(x)}\to e^{2\tau}.
\]
Since \(p\bar\Phi(d_p+y/s_p)\to e^{-y}\), it follows that
\[
p\,\mathbb P\!\left(Q_m^0>d_p+\frac y{s_p}\right)
\to e^{-(y-2\tau)},
\]
and independence across the \(p\) coordinates yields
\[
\mathbb P\{s_p(M_{p,m}^0-d_p)\le y\}
\to \exp\{-e^{-(y-2\tau)}\}.
\]
If \(L^2/m\to\infty\) but \(m/L\to\infty\), the quartic term diverges while the next term is smaller by \(O(L/m)\); the balanced maximum consequently shifts by infinitely many Gaussian Gumbel scales and the Kolmogorov distance tends to one.

### 4. Exact critical Kolmogorov profile

If \(F(y)=\exp(-e^{-y})\) and \(\delta>0\), then
\[
\sup_y|F(y-\delta)-F(y)|
=\exp\!\left[-\frac{\delta}{e^\delta-1}\right](1-e^{-\delta})
=:D(\delta).
\]
Weak convergence to a continuous distribution implies uniform convergence of the corresponding distribution functions. Since the affine map \(x\mapsto s_p(x-d_p)\) preserves Kolmogorov distance, the shifted-Gumbel limits above give the two stated critical profiles.

## Relation to recent work

Cai and Hu (2026) introduce the same fourth-order effective rank
\[
r_4=(\sum_r\lambda_r^2)^2/\sum_r\lambda_r^4
\]
for signed quadratic-chaos coordinates and prove the general bound
\[
d_K\!\left(\max_{j\le p}Q_j,\max_{j\le p}Z_j\right)
\lesssim r_{4,\min}^{-1/6}\log p.
\]
Thus \(r_{4,\min}/(\log p)^6\to\infty\) is a general sufficient condition for ordinary-Gaussian calibration. Their phase-transition diagram is explicitly described as schematic.

The result here does not improve that theorem uniformly over arbitrary signed spectra. Instead it resolves two equal-magnitude benchmark spectra sharply and shows that **the sharp boundary cannot be a function of \(r_4\) alone**. For the positive spectrum, nonzero skewness makes the cubic Cramér term visible at the maximum and the boundary is \((\log p)^3\). Exact sign balance kills that term, leaving the quartic correction and the smaller boundary \((\log p)^2\).

The positive-spectrum calculation is closely connected to the classical triangular-array Gamma maximum theory of Bose, Dasgupta and Maulik (2008), itself building on Anderson, Coles and Hüsler (1997). Classical Cramér-series methods therefore contain the moderate-deviation ingredients. The claimed contribution is the sharp **paired comparison at fixed fourth-order effective rank**, the explicit critical shifts and Kolmogorov profiles, and the resulting sign-sensitive obstruction to using \(r_4\) as a sharp one-parameter phase coordinate.

## Limitations

- The sharp equivalences are proved for independent coordinates and flat equal-magnitude spectra, not for arbitrary dependence or spectral decay.
- The balanced statement uses exact half-positive/half-negative signs; partially imbalanced spectra should interpolate through lower-order signed power sums but are not classified here.
- The separation statements are made inside the moderate-deviation regime \(m/\log p\to\infty\). Other regimes can have different extreme-value normalizations.
- The result concerns the chaos target itself. It does not include the additional finite-sample error incurred when a canonical \(U\)-statistic is approximated by that target.
- Anderson, Coles and Hüsler (1997) was not inspected in full text; its theorem is described through accessible secondary discussion and bibliographic records. An equivalent sharp fixed-\(r_4\) sign-comparison hidden in older Cramér-series or extreme-value literature remains the main originality risk.

## References

1. L. Cai and Q. Hu, *Approximation Theorems for High-Dimensional Canonical U-Statistics: Gaussian Chaos and Phase Transition*, arXiv:2609.20529 (2026).
2. A. Bose, A. Dasgupta and K. Maulik, *Maxima of Dirichlet and triangular arrays of gamma variables*, arXiv:0803.3518 (2008).
3. C. W. Anderson, S. G. Coles and J. Hüsler, *Maxima of Poisson-like variables and related triangular arrays*, Annals of Applied Probability 7 (1997), 953–971, doi:10.1214/aoap/1043862420.
4. E. Azmoodeh, P. Eichelsbacher and C. Thäle, *Optimal Variance-Gamma approximation on the second Wiener chaos*, Journal of Functional Analysis 282 (2022), 109450, doi:10.1016/j.jfa.2022.109450.
