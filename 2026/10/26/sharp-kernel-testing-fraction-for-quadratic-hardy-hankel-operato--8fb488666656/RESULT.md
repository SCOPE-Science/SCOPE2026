# Sharp kernel-testing fraction for quadratic Hardy Hankel operators

## Finding

Let \(H_{\overline\psi}:H^2(\mathbb D)\to H^2_-\) be the Hankel operator with \(\psi(z)=az+bz^2\), where \(a,b\in\mathbb C\) are not both zero and \(H^2_-=L^2(\mathbb T)\ominus H^2(\mathbb D)\). For the normalized Szegő kernels \(k_w(z)=\sqrt{1-|w|^2}/(1-\overline w z)\), define
\[
\mathcal K(H)=\sup_{w\in\mathbb D}\|Hk_w\|_2,\qquad \kappa(H)=\frac{\mathcal K(H)}{\|H\|}.
\]
Then
\[
\boxed{\frac{5}{3\sqrt3}\,\|H_{\overline\psi}\|\le\mathcal K(H_{\overline\psi})\le\|H_{\overline\psi}\|.}
\]
The lower coefficient is the largest possible uniform coefficient for this entire two-coefficient family. Equality on the left holds **exactly** when \(b\ne0\) and \(|a|=|b|/\sqrt6\); there is no restriction on coefficient phases. The maximizing kernel in that case is unique, with
\[
|w|=\frac1{\sqrt6},\qquad \frac{w}{|w|}=\frac{a\overline b}{|a||b|}.
\]
The two endpoint monomial families \(a=0\) and \(b=0\) instead have \(\kappa(H)=1\).

Equivalently, for the degree-two analytic symbol, the Garsia kernel-testing seminorm is always at least \(5/(3\sqrt3)\) times the Nehari norm, with a complete characterization of the sharpest quadratic deficit.

## Assumptions and scope

The Hardy norm is the unweighted \(H^2\) norm, with \(\{1,z,z^2,\ldots\}\) orthonormal. The operator is \(H_{\overline\psi} f=P_-(\overline\psi f)\), where \(P_-\) retains strictly negative Fourier powers. All supremums range over every \(w\) in the **open** unit disk; the zero operator is excluded only from the normalized quotient. No analytic coefficients beyond degree two are admitted. Both coefficients may be complex.

## Proof

**Exact operator norm.** On the input span of \(1,z\) and the output span of \(\overline z,\overline{z}^{\,2}\), the matrix is
\[
\begin{pmatrix}\overline a&\overline b\\\overline b&0\end{pmatrix},
\]
and it vanishes on \(z^2H^2\). Its largest singular value is
\[
\|H_{\overline\psi}\|=\frac{|a|+\sqrt{|a|^2+4|b|^2}}2. \tag{1}
\]
The expression follows directly by computing the eigenvalues of the positive matrix product; diagonal unitaries remove the phases.

**Exact kernel envelope.** Expansion of the normalized Szegő kernel gives
\[
H_{\overline\psi}k_w=\sqrt{1-|w|^2}\left[(\overline a+\overline b\,\overline w)\overline z+\overline b\,\overline z^{\,2}\right].
\]
For \(r=|w|\), maximizing over the argument of \(w\) yields
\[
\mathcal K(H_{\overline\psi})^2=
\max_{0\le r\le1}(1-r^2)\left((|a|+|b|r)^2+|b|^2\right). \tag{2}
\]
Here extension to the closed radius interval introduces a zero endpoint and therefore does not change the supremum over the open disk. If either coefficient vanishes, equations (1)–(2) give \(\kappa=1\).

**One-variable global optimization.** Suppose both coefficients are nonzero; set \(t=|a|/|b|>0\), \(x=(t+\sqrt{t^2+4})/2>1\), and
\[
F(t,r)=(1-r^2)((t+r)^2+1),\quad M(t)=\max_{0\le r\le1}F(t,r),\quad R(t)=M(t)/x^2.
\]
The positive root \(x\) satisfies \(t=x-x^{-1}\). For fixed \(t>0\), differentiation gives
\[
\tfrac12\partial_rF=t-t^2r-3tr^2-2r^3.
\]
This polynomial strictly decreases on \(r\ge0\), is positive at zero and negative at one, so it has a unique zero \(r(t)\in(0,1)\), the unique maximizer. The implicit function theorem and envelope differentiation apply.

At any interior stationary point of \(R(t)\), its logarithmic derivative vanishes. Using \(\frac{d}{dt}\log x=1/\sqrt{t^2+4}\) gives
\[
\frac{t+r}{(t+r)^2+1}=\frac1{\sqrt{t^2+4}}=\frac1{x+x^{-1}}.
\]
Set \(s=t+r\). The resulting quadratic factorization \((s-x)(s-x^{-1})=0\) has two branches. If \(s=x\), then \(r=x^{-1}\) and the radial stationarity polynomial above equals \(-2/x\), impossible. If \(s=x^{-1}\), then \(r=2/x-x\) and that polynomial equals \(2(2x^2-3)/x^3\). Therefore the only possible stationary point is
\[
x^2=\tfrac32,\qquad t=r=\frac1{\sqrt6}.
\]
It is admissible and indeed satisfies the radial equation. The continuous ratio has \(\lim_{t\downarrow0}R(t)=1\), since \(F(0,r)=1-r^4\), and \(\lim_{t\to\infty}R(t)=1\): the bound \(R(t)\le1\) follows from \(\|Hk_w\|\le\|H\|\), while \(R(t)\ge(t^2+1)/x^2\to1\). Since the only interior stationary point is the displayed value, it is the global minimum (or, equivalently, the minimum is attained there by direct substitution and the limiting values). At the minimizer,
\[
F(1/\sqrt6,1/\sqrt6)=\frac{25}{18},\qquad x^2=\frac32,
\]
so \(\min R=25/27\). Taking square roots proves the claimed coefficient.

**Equality and phases.** The uniqueness of \(t\) and \(r(t)\) forces \(|a|/|b|=1/\sqrt6\) and \(|w|=1/\sqrt6\) in every lower-bound equality case. Equality in the triangle inequality \(|a+bw|\le|a|+|b||w|\) forces \(w/|w|=a\overline b/(|a||b|)\). Conversely those choices attain the constant, proving all directions.

## Verification

The finite-dimensional Hankel matrix and kernel formulas are exact. The radial polynomial and stationary-branch reductions were also independently simplified symbolically. `CHECKER.py` implements deterministic finite sampling of the globally sharp inequality and complex phase witnesses, plus the exact rational evaluation \((25/18)/(3/2)=25/27\). It requires only Python's standard library and is run with `python3 CHECKER.py` in the directory containing this document. Numerical sampling is neither exhaustive nor a substitute for the analytic proof.

## Relationship to prior work

Dyakonov's 2026 Problem 1 asks for equality of the Hankel operator norm and the Szegő-kernel testing norm. His paper exhibits the quadratic family \(cz+z^2\) as a strict-inequality example, and its addendum (after communication from Brevig) records the complete **qualitative** classification of norm-attaining equality symbols, including monomial rigidity. Neither yields the quantitative minimax constant \(5/(3\sqrt3)\) or its full coefficient and kernel equality cases. The older Garsia-norm work of Dyakonov develops the analytic seminorm and its equality with the supremum norm; it concerns a different denominator. The minimal/maximal-norm Hankel papers of Brevig and of Brevig–Seip compare the operator norm to the analytic \(H^2\) and supremum norms, not the sharp two-coefficient Garsia-to-operator ratio. Related published finite-rank and logarithmic Hilbert Hankel examples likewise study distinct quantitative or qualitative statements. The present result is an optimal exact benchmark for the **first nonmonomial finite-rank family**, not a general improvement to the full reproducing-kernel thesis.

## Limitations

There is no assertion of the same universal coefficient for symbols with three or more nonzero Taylor coefficients, for general Hankel operators, or for different Hardy or Bergman norms. The historical priority comparison cannot exclude an unindexed earlier two-parameter calculation. Some older full texts, including Bonsall's 1984 foundational paper, were not accessible for complete inspection. The calculation uses the ordinary Szegő-kernel test family and the unweighted Hardy norm throughout.

## References

1. K. M. Dyakonov, *The Strong Reproducing Kernel Thesis for Hankel Operators and the Garsia Norm*, arXiv:2609.33242, first posted 2026-09-27; full v3 text inspected (2026-10-18), especially Problem 1, the quadratic example, and Section 3 addendum.
2. K. M. Dyakonov, *Extremal Problems in BMO and VMO Involving the Garsia Norm*, arXiv:2404.05565 (2024), subsequently J. Funct. Anal. 288 (2025), 110833; accessible early sections and principal statements inspected.
3. O. F. Brevig, *Minimal Norm Hankel Operators*, arXiv:2107.01680 (2021), Proc. Amer. Math. Soc. 150 (2022), 4383–4391.
4. O. F. Brevig and K. Seip, *Maximal Norm Hankel Operators*, arXiv:2301.07937 (2023), J. Math. Anal. Appl. 529 (2024), 127221.
5. F. F. Bonsall, *Boundedness of Hankel Matrices*, J. London Math. Soc. s2-29 (1984), 289–300, doi:10.1112/jlms/s2-29.2.289; full text unavailable in this review.
