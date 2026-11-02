# A sharp essential-spectral gap for polynomial Toeplitz outlier polygons

## Finding

Let \(\mathcal H_h^2\) be the complex harmonic Bergman space on the unit disk, with normalized area measure, and let \(\mathbb T_p=P_hM_p|_{\mathcal H_h^2}\). For every integer \(n\ge4\), consider the analytic polynomial
\[
p_a(z)=z^n+az,\qquad a\in\mathbb C\setminus\{0\}.
\]
Define
\[
C_n=\frac{n(n+5)}6,
\]
and let \(r_n>1\) be the unique positive solution of
\[
1+r_n+\cdots+r_n^{n-1}=C_n.
\]
Put \(t=(|a|/C_n)^{1/(n-1)}\). Whenever
\[
\boxed{\ r_n^{-1}<t<1\ },
\]
the operator \(\mathbb T_{p_a}\) has **at least \(n-1\) distinct, geometrically simple, isolated eigenvalues**
\[
\boxed{\ \lambda_j=\left(1-\frac1{C_n}\right)a\alpha_j,
\qquad \alpha_j^{n-1}=-\frac a{C_n},\qquad 0\le j<n-1.\ }
\]
These points form a regular polygon and lie strictly inside the central disk missed by the essential spectrum. Their *exact common Euclidean distance to the essential spectrum* is
\[
\boxed{\ \Delta_n(t)=C_nt^{n-1}-1-(C_n-1)t^n>0.\ }
\]
The parameter window is sharp for this explicitly constructed branch to have its associated polynomial root unique in the disk and its spectrum strictly separated from the essential curve. No assertion is made that other isolated eigenvalues cannot occur.

The distance is **uniquely maximized within this branch** at
\[
\boxed{\ t_{*,n}=\frac{(n-1)C_n}{n(C_n-1)},\qquad
|a|_{*,n}=C_nt_{*,n}^{n-1},\qquad
\Delta_{*,n}=\frac{C_n}{n}t_{*,n}^{n-1}-1.\ }
\]
Its large-degree behavior is
\[
\boxed{\ \lim_{n\to\infty}\frac{\Delta_{*,n}}n=\frac1{6e},\qquad
\lim_{n\to\infty}\frac{|a|_{*,n}}{n^2}=\frac1{6e}.\ }
\]
At the lower endpoint, the exact coefficient threshold satisfies
\[
\boxed{\ \frac{n}{C_nr_n^{-(n-1)}}=\log n+\log\log n-\log6+o(1).\ }
\]
Thus an unbounded number of genuinely isolated spectral points already occurs in a two-term analytic symbol, and its optimal separation from the essential spectral curve grows linearly with the degree.

## Assumptions and scope

The domain is the unit disk \(\mathbb D\). The normalized area measure is \(dA=\pi^{-1}dx\,dy\). The Hilbert space \(\mathcal H_h^2\) is the closed space of square-integrable complex-valued harmonic functions on \(\mathbb D\), and \(P_h\) is the orthogonal projection onto it. The ordinary analytic Bergman space and its projection are \(A^2\) and \(P_B\). A fixed integer \(n\ge4\) and any nonzero complex parameter \(a\) are allowed. The indicated eigenvalue formulas are asserted only under \(r_n^{-1}<(|a|/C_n)^{1/(n-1)}<1\). The distance in the theorem is to \(\sigma_{\mathrm e}(\mathbb T_{p_a})\), not to all other spectral points. Geometric simplicity means one-dimensional eigenspace; algebraic simplicity is not asserted.

## Proof

**1. The root geometry.** Write \(C=C_n\). The polynomial \(Q_n(w)=1+w+\cdots+w^{n-1}-C\) has a unique positive real root \(r>1\), since its positive-real coefficients give strict monotonicity and \(C>n\). Any complex root \(w\) obeys
\[
C-1=|w+\cdots+w^{n-1}|\le\sum_{k=1}^{n-1}|w|^k.
\]
Consequently \(|w|\ge r\). Equality forces every term \(w^k\) to have the same positive real argument; since \(n\ge4\), this forces \(w=r\). Thus \(r\) is the sole smallest-modulus root.

Choose any \(\alpha\) with \(\alpha^{n-1}=-a/C\), and write \(|\alpha|=t\). Direct factorization gives
\[
p_a(z)-p_a(\alpha)=(z-\alpha)\alpha^{n-1}Q_n(z/\alpha).
\]
If \(r^{-1}<t<1\), the first root \(\alpha\) is in \(\mathbb D\), while every other root is outside \(\overline{\mathbb D}\). The interior root \(\alpha\) is simple, since \(Q_n(1)=n-C\ne0\). Therefore \(\lambda=p_a(\alpha)=(1-1/C)a\alpha\) is not in the boundary image \(p_a(\partial\mathbb D)\).

**2. Direct construction of the eigenfunction.** The analytic Bergman reproducing kernel at \(\bar\alpha\) is \(g_\alpha(z)=(1-\alpha z)^{-2}\). An elementary monomial projection gives, for every integer \(k\ge0\),
\[
P_B(z^k\bar z^\ell)=\begin{cases}\dfrac{k-\ell+1}{k+1}z^{k-\ell},&0\le\ell\le k,\\0,&\ell>k.\end{cases}
\]
Expanding \(g_\alpha(\bar z)\) and subtracting \(p_a(\alpha)\), one obtains
\[
P_B\big[(p_a(z)-\lambda)g_\alpha(\bar z)\big]
=z\big[a+h_n(z,\alpha)\big],
\]
where
\[
h_n(z,w)=\sum_{\ell=0}^{n-1}
\frac{(\ell+1)(n-\ell+1)}{n+1}z^{n-1-\ell}w^\ell.
\]
Summing the coefficients gives \(h_n(\alpha,\alpha)=C\alpha^{n-1}=-a\). Thus the numerator in
\[
f_\alpha(z)=-z\,\frac{a+h_n(z,\alpha)}{p_a(z)-\lambda}
\]
vanishes at the unique interior zero of the denominator. All remaining denominator zeros lie strictly outside the closed disk. The pole is removable, so \(f_\alpha\in zA^2\). The harmonic function
\[
u_\alpha(z)=f_\alpha(z)+g_\alpha(\bar z)
\]
is nonzero. The analytic component of \(P_h[(p_a-\lambda)u_\alpha]\) vanishes by the displayed projection identity. The anti-analytic component vanishes because reflection converts it into \(P_B[(p_a(\bar z)-\lambda)g_\alpha(z)]\), the Bergman Toeplitz adjoint eigenvector equation at \(\alpha\). The constant term is zero since \(p_a(\alpha)=\lambda\). Hence \((\mathbb T_{p_a}-\lambda)u_\alpha=0\). With exactly one zero of \(p_a-\lambda\) in the disk, the anti-analytic kernel is one dimensional, and the analytic component is uniquely fixed, so the eigenspace is one dimensional.

The established harmonic-Bergman essential-spectrum theorem gives
\[
\sigma_{\mathrm e}(\mathbb T_{p_a})=p_a(\partial\mathbb D).
\]
The October 2026 polynomial-symbol spectral theorem further states that only finitely many spectral points can lie outside that curve. Therefore each constructed eigenvalue is isolated of finite multiplicity. The \(n-1\) distinct roots \(\alpha_j\) yield \(n-1\) distinct eigenvalues.

**3. Exact distance to the essential curve.** Let \(a=s e^{i\varphi}\) and \(\alpha=t e^{i\theta}\). The root relation forces \(e^{i(n-1)\theta}=-e^{i\varphi}\). The smallest modulus of a point of the curve \(p_a(\partial\mathbb D)\) is \(s-1\), since \(s>1\), and it is attained at
\[
p_a(e^{i\theta})=(s-1)e^{i(\varphi+\theta)}.
\]
The constructed eigenvalue is \(\lambda=(1-1/C)st\,e^{i(\varphi+\theta)}\). Hence, once \((1-1/C)st<s-1\), the reverse triangle inequality and the displayed boundary point prove that the exact Euclidean distance is
\[
(s-1)-(1-1/C)st=\Delta_n(t).
\]
Substitution of \(s=Ct^{n-1}\) yields the stated expression. At \(t=1/r\), the relation \(r^n=1+C(r-1)\) gives \(\Delta_n(t)=0\); at \(t=1\), it also vanishes. Its derivative is
\[
\Delta_n'(t)=t^{n-2}[(n-1)C-n(C-1)t].
\]
The bracket has exactly one zero. By equality of the endpoint values, that zero lies strictly between the two endpoints, the derivative is first positive and then negative, and \(\Delta_n(t)>0\) throughout the open window. Therefore the preceding distance formula holds and its only maximum is at \(t_{*,n}\), with the stated maximum value.

**4. Large-degree laws.** Since \(C_n/n^2\to1/6\) and
\[
t_{*,n}=\left(1-\frac1n\right)\left(1+\frac1{C_n-1}\right),
\]
we have \(t_{*,n}^{n-1}\to e^{-1}\). The exact expressions for \(\Delta_{*,n}\) and \(|a|_{*,n}\) then give both limits.

For the lower threshold write \(r_n=1+x_n/n\). The geometric-sum equation is
\[
\left(1+\frac{x_n}{n}\right)^n=1+\frac{C_n x_n}{n}.
\]
Comparing test values \(x=c\log n\) for fixed \(c<1\) and \(c>1\) shows \(x_n\sim\log n\). Taking logarithms, using \(x_n^2/n=o(1)\), and substituting \(C_n/n=n/6+O(1)\) gives
\[
x_n=\log n+\log\log n-\log6+o(1).
\]
The geometric-sum identity also yields \(C_nr_n^{-(n-1)}=r_n/(r_n-1+1/C_n)\). Consequently \(n/(C_nr_n^{-(n-1)})=x_n+o(1)\), as claimed.

## Verification

The accompanying standalone `checker.py` verifies the root intervals, distance identities, extremum formula, and boundary identities over many degrees. It also constructs the exact candidate eigenfunctions by synthetic division and checks finite truncations of the *actual harmonic-Bergman projected multiplication operator*, not merely the algebraic eigenvalue equation. Run `python3 checker.py` with the Python standard library. These are supplementary finite tests; no infinite spectral assertion is inferred solely from them.

For the fully rational example \(n=4\), the optimum is \(t_*=9/10\) and \(a_*=2187/500\). The three constructed eigenvalues form a regular triangle of modulus \(6561/2000\). The essential curve has minimum modulus \(1687/500\), so the exact gap is \(187/2000\).

## Relationship to prior work

Huang–Wang–Zhao (2026) prove the general *finite* isolated-eigenvalue theorem for analytic-polynomial symbols on the harmonic Bergman space and derive a polynomial root-determinant criterion. The present finding uses that foundational spectral theorem but adds a two-term all-degree construction of \(n-1\) genuine isolated points, their exact distance to the essential curve, a uniquely optimal coefficient, and high-degree sharp growth. The 2026 theorem gives an upper bound \((n-1)2^{n-1}\) for the number of isolated eigenvalues; it does not assert a matching family with linearly many points or the quantitative gap optimization.

Wang–Zhao (2021) treat analytic polynomial symbols of degree at most three and exhibit a quadratic disconnected-spectrum example. The present theorem is stated for degrees at least four to avoid claiming those cases. The earlier Guo–Zhao–Zheng (2020) study concerns the *analytic* Bergman space with a nonanalytic symbol \(\bar z+p(z)\), a different operator and projection, so its isolated eigenvalues do not directly cover this construction.

## Limitations

The result supplies **at least** \(n-1\) isolated spectral points; it does not classify other possible isolated eigenvalues of \(\mathbb T_{p_a}\). The maximization is over the explicitly constructed branch and coefficient interval, not over all analytic polynomials or all possible spectral components. The distance is to the essential spectrum, not necessarily to the remainder of the complete spectrum. Algebraic multiplicity is not calculated. The 2021 comparison was based on its accessible abstract and descriptions in the later full-text paper; its complete publisher text was not available for inspection. This leaves a residual publication-priority risk, and no independent validation is claimed.

## References

1. M. Huang, J. Wang and X. Zhao, *The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space*, arXiv:2610.09638v1, first public October 7, 2026. https://arxiv.org/html/2610.09638
2. C. Wang and X. Zhao, *Weyl's theorem for Toeplitz operators with polynomial symbols on the harmonic Bergman space*, Journal of Mathematical Analysis and Applications **495** (2021), 124770. https://doi.org/10.1016/j.jmaa.2020.124770
3. K. Guo, X. Zhao and D. Zheng, *The spectral picture of Bergman Toeplitz operators with harmonic polynomial symbols*, arXiv:2007.07532v1, July 15, 2020. https://arxiv.org/abs/2007.07532
4. Guo–Zheng's essential-spectrum theorem for harmonic-Bergman Toeplitz operators with continuous symbols, as quoted in Reference 1, Theorem 2.1.
