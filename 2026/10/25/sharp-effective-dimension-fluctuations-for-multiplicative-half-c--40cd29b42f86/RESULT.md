# Sharp effective-dimension fluctuations for multiplicative half-Cauchy shrinkage

## Finding

For a fixed shrinkage parameter \(0<\zeta<1\), put \(d=-\log\zeta>0\). Let \(\eta_1=1\), and let
\[
\eta_h=\prod_{j=2}^{h}\zeta U_j,\qquad h\ge2,
\]
where the \(U_j\) are independent standard half-Cauchy random variables with density \(2/[\pi(1+u^2)]\) for \(u>0\). For \(0<\varepsilon<1\) define the **total effective dimension**, including late rebounds,
\[
N_\varepsilon=\#\{h\ge1:\eta_h>\varepsilon\},\qquad L=\log(1/\varepsilon).
\]
There exists \(\delta_\zeta>0\) such that
\[
\boxed{\mathbb E N_\varepsilon=\frac Ld+\frac12+\frac{\pi^2}{8d^2}+O_\zeta(e^{-\delta_\zeta L}).}
\]
Moreover,
\[
\boxed{\frac{N_\varepsilon-L/d}{\sqrt L}\ \Longrightarrow\ \mathcal N\!\left(0,\frac{\pi^2}{4d^3}\right).}
\]
The exponential error is for each *fixed* \(\zeta\), not uniform as \(\zeta\uparrow1\). The Gaussian limit is for the infinite sequence, not for a fixed finite truncation.

## Assumptions and scope

No independence is asserted among the indicators \(\mathbf1\{\eta_h>\varepsilon\}\); the independence is solely that of the multiplicative factors. Strict versus non-strict thresholding is immaterial for individual positive thresholds since each log-coordinate has a continuous law. The first coordinate is deterministically one. Write \(Y_j=\log U_j\); its density is \(1/(\pi\cosh y)\), its variance is \(v=\pi^2/4\), and its moment transform is \(\mathbb E e^{sY_j}=\sec(\pi s/2)\) for \(|\Re s|<1\). Define \(X_j=d-Y_j\) and \(T_n=X_1+\cdots+X_n\) for \(n\ge1\), with \(T_0=0\). Relabeling the factors, \(N_\varepsilon=\sum_{n=0}^{\infty}\mathbf1\{T_n<L\}\), which is almost surely finite by the strong law \(T_n/n\to d\).

## Proof

**Exact transform and sharp mean.** For \(s\) with \(0<\Re s<r\), where \(r>0\) is sufficiently small, set
\[
M(s)=\mathbb E e^{-sX_1}=\frac{e^{-ds}}{\cos(\pi s/2)}.
\]
As \(M(0)=1\), \(M'(0)=-d<0\), we can choose \(r<1\) so \(|M(s)|<1\) throughout the vertical line \(\Re s=r\), since \(|M(r+it)|\le M(r)<1\). Set \(G(L)=\sum_{n\ge1}\mathbb P(T_n<L)\) for real \(L\). Tonelli's theorem, followed by integration of a half-line, gives the bilateral Laplace transform
\[
\int_{\mathbb R} e^{-sL}G(L)\,dL=\frac{M(s)}{s[1-M(s)]},\qquad \Re s=r.
\]
The sum defining \(G\) converges locally uniformly by the exponential Chernoff estimate \(\mathbb P(T_n<L)\le e^{rL}M(r)^n\). Thus \(G\) is continuous. The transform is integrable on its vertical line: \(|M(r+it)|\) decays exponentially as \(|t|\to\infty\), while \(|1-M(r+it)|\ge1-M(r)\).

The function \(M\) is analytic in \(|\Re s|<1\). For imaginary \(s=it\) with \(t\ne0\), \(|M(it)|=\operatorname{sech}(\pi |t|/2)<1\). At the origin the zero of \(1-M(s)\) is simple. Uniform exponential decay of \(M(s)\) for large \(|\Im s|\), combined with compactness on bounded imaginary ranges, therefore provides a \(\delta=\delta(d)>0\), with \(\delta<1\), such that \(1-M(s)\) has no zeros in the closed strip \(-\delta\le\Re s\le r\), except at \(s=0\). (After taking \(r>0\) small enough there are no other zeros near zero.)

Let \(a=(d^2+v)/2\). Taylor expansion yields
\[
M(s)=1-ds+as^2+O(s^3),\quad
\frac{M(s)}{s[1-M(s)]}=\frac1{ds^2}+\frac{a/d^2-1}{s}+O(1).
\]
Bilateral Laplace inversion and a rectangular contour shift from \(\Re s=r\) to \(\Re s=-\delta\) are justified by the vertical exponential decay just established. The horizontal sides tend to zero. For \(L>0\), the residue at zero is \(L/d+a/d^2-1\); the integral over the new vertical line is \(O_d(e^{-\delta L})\). Therefore
\[
G(L)=\frac Ld+\frac{d^2+v}{2d^2}-1+O_d(e^{-\delta L}).
\]
Adding the deterministic \(n=0\) term gives the asserted mean and its explicit constant \(\frac12+\pi^2/(8d^2)\).

**Gaussian fluctuations despite late rebounds.** Define \(\tau_L=\inf\{n\ge0:T_n\ge L\}\), the first crossing time of the positive-drift walk. By the strong law, \(\tau_L/L\to1/d\) almost surely. The increments have exponential moments in a neighborhood of zero. Consequently, for a fixed \(C>1/d\), on an event tending to probability one the overshoot is bounded above by \(\max_{1\le j\le CL}X_j^+=O_{\mathbb P}(\log L)=o_{\mathbb P}(\sqrt L)\). Donsker's invariance principle (or the random-index central limit theorem, using \(\tau_L/L\to1/d\)) applied to the centered partial sums \(T_n-dn\) gives
\[
\frac{\tau_L-L/d}{\sqrt L}\ \Longrightarrow\ \mathcal N\!\left(0,\frac v{d^3}\right).
\]
In particular the overshoot is negligible at this scale and no positivity assumption is made on the individual \(X_j\).

For the crucial distinction between the first passage and **all** threshold exceedances, observe that \(\sum_{n<\tau_L}1\{T_n<L\}=\tau_L\). With future increments independent of the past at \(\tau_L\), the remaining count
\[
D_L=N_\varepsilon-\tau_L=\sum_{j\ge1}\mathbf1\{T_{\tau_L+j}<L\}
\]
is stochastically dominated by \(V=\sum_{j\ge1}\mathbf1\{T'_j<0\}\) for an independent walk \(T'_j\) started at zero. Indeed the excess at first passage is nonnegative, so every subsequent visit below \(L\) entails \(T'_j<0\). Choose \(s\in(0,r)\); by Markov's inequality, \(\mathbb P(T'_j<0)\le M(s)^j\), and hence
\[
\mathbb E V\le\frac{M(s)}{1-M(s)}<\infty.
\]
Thus \(D_L=O_{\mathbb P}(1)\) uniformly in \(L\), so \(D_L/\sqrt L\to0\) in probability. Slutsky's theorem completes the stated central limit theorem with \(v=\pi^2/4\).

## Verification

The standalone program `verify.py` independently evaluates the exact finite-level formula \(\sum_{n\ge0}\mathbb P(T_n<L)\) using Gil–Pelaez Fourier inversion of \(\operatorname{sech}^n(\pi t/2)\); it checks the first-factor half-Cauchy CDF, the second-order mean coefficient at several \(L\), and the moment and residue constants. Fourier truncation and floating-point quadrature are finite consistency checks; all infinite claims follow from the preceding analytic argument. Run `python verify.py` with the packages in `requirements.txt`.

## Relationship to prior work

Kulkarni (2026), arXiv:2610.21136v1, establishes the centered log-scale law, almost-sure finiteness of each threshold exceedance count, a fixed-coordinate Gaussian limit, and the exact summation formula for \(\mathbb E N_\varepsilon\) (its Equation 19). Those assertions are assumed background, not claimed anew. They do not supply a small-threshold expansion with its finite constant and exponential error, or a Gaussian law for the random *total* number of exceedances after rebound. Daley (1980) gives bounds around a renewal-function moment center for general positive-drift random walks; those bounds are not an exponential asymptotic, nor the specialized Gaussian occupation-count statement. The arguments above apply analytically to the specified half-Cauchy increment law; they do not claim a new general renewal theorem.

## Limitations

The coefficient is not asserted uniformly in \(\zeta\) as \(\zeta\uparrow1\); \(\zeta=1\) is a different recurrence regime. This is a prior-law statement, not a posterior factor-selection guarantee. The classical renewal and first-passage machinery supplies strong conceptual antecedents; priority for this exact specialization and quantitative remainder merits independent checking. Numerical experiments alone would not prove either asymptotic, and the analytic proof does not yield an explicit optimal value of the exponent \(\delta_\zeta\).

## References

1. Kulkarni, S. (2026). *Pathwise Shrinkage and Probabilistic Calibration of the Multiplicative Half-Cauchy Process*. arXiv:2610.21136v1, initially submitted 2026-10-15. https://arxiv.org/abs/2610.21136
2. Daley, D. J. (1980). *Tight Bounds for the Renewal Function of a Random Walk*. *Annals of Probability* 8(3), 615–621. doi:10.1214/aop/1176994732.
3. Feller, W. (1971). *An Introduction to Probability Theory and Its Applications*, Volume II, second edition. Wiley (general renewal/first-passage background).
