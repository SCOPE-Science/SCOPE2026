# Three-mode disk localization and triangular spectral resonances in the second-excited Hermite sector

## Finding

For every real \(x>0\), the concentration spectrum of a centered Gaussian disk in the second-excited Hermite sector is determined by three candidate eigenvalues. Put
\[
F_n(t)=t^2-2nt+n(n-1),\qquad
r_{\pm}(x)=x+\frac12\pm\sqrt{x+\frac14}.
\]
The sharp concentration constant is
\[
\|T_x\|=\max\left\{\lambda_0(x),\lambda_{\lceil r_-(x)\rceil}(x),\lambda_{\lceil r_+(x)\rceil}(x)\right\}.
\]
Here \(\lambda_n(x)\) is the exact diagonal eigenvalue given below. The sequence has at most three local-maximum plateaux, and precisely three local maxima occur at \(x=3\), at indices \(0,2,6\).

Further, for every integer \(n\ge1\),
\[
\lambda_{n-1}(x)=\lambda_n(x)=\lambda_{n+1}(x)
\iff x=n\pm\sqrt n>0.
\]
There exist two distinct triple-eigenvalue plateaux at the same radius if and only if
\[
x=a(a+1),\qquad a\in\mathbb Z_{\ge1},
\]
and their centers are exactly \(a^2\) and \((a+1)^2\). No four consecutive eigenvalues agree when \(x>0\). This is an infinite exact sequence of simultaneous spectral resonances, not an assertion that both plateaux maximize the norm.

## Assumptions and scope

Use the probability Gaussian measure \(d\gamma(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\) on \(\mathbb C\). Let \(\mathcal F_{(3)}\) be the true polyanalytic Fock subspace of antiholomorphic order exactly two, with orthonormal complex Hermite basis
\[
\Phi_n(z)=\frac{z^{n-2}}{\sqrt{2n!}}F_n(|z|^2),\qquad n=0,1,2,\dots.
\]
At \(n=0,1\) the apparent negative power cancels with the radial polynomial, giving \(\Phi_0(z)=\overline z^{\,2}/\sqrt2\) and \(\Phi_1(z)=\overline z(|z|^2-2)/\sqrt2\).

Let \(P\) be orthogonal projection onto \(\mathcal F_{(3)}\). The positive compact disk concentration operator is \(T_x=P\mathbf1_{\{|z|^2\le x\}}P\) restricted to \(\mathcal F_{(3)}\). Angular orthogonality makes it diagonal in this basis; polar integration gives, for every integer \(n\ge0\) and real \(x>0\),
\[
\lambda_n(x)=\frac{1}{2n!}\int_0^x e^{-t}t^{n-2}F_n(t)^2\,dt.
\]
At small indices the integrands are polynomials after cancellation. The sequence is positive and tends to zero as \(n\to\infty\) for each fixed \(x>0\).

## Proof

**1. Exact adjacent differences.** Define
\[
H_n(t)=\frac{t^{n-1}F_n(t)F_{n+1}(t)}{2(n+1)!},
\]
interpreted by cancellation for \(n=0\). Elementary polynomial differentiation, using \(F_{n+1}(t)=F_n(t)-2t+2n\), gives, for every integer \(n\ge0\),
\[
H_n'(t)-H_n(t)=\frac{t^{n-2}F_n(t)^2}{2n!}-\frac{t^{n-1}F_{n+1}(t)^2}{2(n+1)!}.
\]
The expression \(H_n(t)\) tends to zero at \(t=0\), including for \(n=0,1\). Integrating the derivative of \(e^{-t}H_n(t)\) yields
\[
\boxed{\lambda_n(x)-\lambda_{n+1}(x)=\frac{e^{-x}x^{n-1}}{2(n+1)!}F_n(x)F_{n+1}(x).}
\]
Every factor outside the two polynomials is positive for \(x>0\).

**2. The three-candidate norm certificate.** For fixed \(x>0\), the polynomial in the integer index has the factorization
\[
F_n(x)=n^2-(2x+1)n+x^2=(n-r_-(x))(n-r_+(x)).
\]
Both roots are positive. As integer \(n\) increases, the sign pattern of \(F_n(x)\) has at most three blocks: positive, negative, positive, allowing zero boundary terms. Thus the sign of \(\lambda_n-\lambda_{n+1}\) is positive except at the two block boundaries, where a negative difference can occur; an integer root instead produces a two-step zero difference. On each of the resulting monotonic runs, a maximum must be attained at index \(0\), \(\lceil r_-(x)\rceil\), or \(\lceil r_+(x)\rceil\). Integer-root ties do not add candidates because the adjacent value equals the root-index value. Since \(\lambda_n(x)\to0\), this proves the asserted exact operator-norm formula and the bound of three local-maximum plateaux. For \(x=3\), the signs of \(F_n(3)\) are positive at indices \(0,1\), negative at indices \(2,3,4,5\), and positive at all indices \(n\ge6\), producing exactly three strict local maxima at \(n=0,2,6\).

**3. Three-term equalities.** Both adjacent differences vanish at a central index \(n\ge1\) if \(F_n(x)=0\). Conversely, if they vanish and \(F_n(x)\ne0\), then \(F_{n-1}(x)=F_{n+1}(x)=0\). We now show that different integer-index polynomials cannot share a positive root with index difference two.

The positive real roots of \(F_n(x)\), for positive integer \(n\), are \(n\pm\sqrt n\), with the nonpositive zero at \(n=1\) excluded. Both functions of \(n\), \(n+\sqrt n\) and \(n-\sqrt n\), are strictly increasing for integers \(n\ge1\). If \(F_n(x)=F_m(x)=0\) for distinct positive indices \(n<m\), the only possible equality is
\[
n+\sqrt n=m-\sqrt m,
\]
so \(\sqrt n+\sqrt m=m-n\) is an integer. Solving this equation for \(\sqrt n\) shows it is rational, hence \(n=a^2\) for an integer \(a\ge1\); similarly \(m=b^2\). Equality becomes \(a(a+1)=b(b-1)\), which by strict increase implies \(b=a+1\). Therefore every repeated positive root occurs at \(x=a(a+1)\), exactly for the two index values \(a^2\) and \((a+1)^2\), whose difference is \(2a+1\ge3\). In particular, roots at indices separated by two cannot coincide. The converse triple-equality implication follows, and four consecutive equal eigenvalues would force two successive common-root centers, which is impossible.

At \(x=2\) the two triple plateaux are \(\lambda_0=\lambda_1=\lambda_2\) and \(\lambda_3=\lambda_4=\lambda_5\); these levels are distinct, with \(\lambda_0-\lambda_3=2/(3e^2)\).

## Verification

The bundled standalone `verification/check.py` uses exact symbolic polynomial differentiation and incomplete-Gamma integral identities for low indices, and independently evaluates the three-candidate formula against 100 spectral values at eleven positive radii. It reports 161 successful assertion groups (see `verification/results.txt`). These are finite consistency checks; the all-index and all-radius assertions follow from the analytical arguments above. The evaluator requires Python, SymPy and mpmath and can be run with `python verification/check.py`.

## Relationship to prior work

Abreu–Speckbacher (arXiv:1808.02258, initial posting 2018-08-07), especially the disk radial-orthogonality identities, motivates precise Hermite-window concentration questions. Maximenko–Tellería-Romero (arXiv:1905.00978, 2019) gives general Laguerre-square eigenvalue formulas for radial Toeplitz operators on true polyanalytic Fock spaces. Those formulas supply the spectral framework; the particular adjacent-index factorization, uniform three-candidate norm certificate and triangular simultaneous resonance classification are not stated in the inspected relevant sections. A theorem implicit under a different normalization or in older special-function literature cannot be excluded without further bibliographic checking.

## Limitations

The theorem is specific to the true third polyanalytic Fock sector and centered disk masks. The three-candidate formula computes the norm but does not classify, by explicit radius intervals, which candidate is globally dominant. The analytic proof concerns only this fixed Hermite sector; historical-priority coverage is not exhaustive, especially in older Laguerre spectral literature.

## References

1. L. D. Abreu and M. Speckbacher, *Donoho–Logan Large Sieve Principles for Modulation and Polyanalytic Fock Spaces*, arXiv:1808.02258 (2018), relevant disk Laguerre orthogonality and Hermite-window concentration.
2. E. A. Maximenko and A. M. Tellería-Romero, *Radial operators on polyanalytic Bargmann–Segal–Fock spaces*, arXiv:1905.00978 (2019), radial Toeplitz diagonalization and Laguerre-square eigenvalues, especially Proposition 6.3.
