# A sharp cubic-scale escape transition for boundary Sobolev circle zeros

## Finding

Consider the normalized Haar probability measure \(m_{\mathbb T}\) on the unit circle. For \(\lambda>0\), let \(P_{n,\lambda}\) denote the unique monic polynomial of degree \(n\ge2\) orthogonal to all lower-degree polynomials for
\[
\langle f,g\rangle_\lambda=\int_{\mathbb T}f(z)\overline{g(z)}\,dm_{\mathbb T}(z)+\lambda f'(1)\overline{g'(1)}.
\]
Set
\[
S_n=\frac{n(n-1)(2n-1)}6,\quad
A_{n,\lambda}=\frac{n\lambda}{1+\lambda S_n},\quad
\lambda_c(n)=\frac{6}{n(n^2-1)}.
\]
Then
\[
P_{n,\lambda}(z)=z\left[z^{n-1}-A_{n,\lambda}\sum_{k=1}^{n-1}kz^{k-1}\right].
\]
Besides its simple zero at the origin, it has one distinguished **simple positive real** zero \(r_{n,\lambda}\); all its other \(n-2\) zeros lie strictly in \(|z|<1\) for every \(\lambda>0\). The distinguished zero is strictly increasing with \(\lambda\), and
\[
r_{n,\lambda}<1\iff\lambda<\lambda_c(n),\qquad
r_{n,\lambda}=1\iff\lambda=\lambda_c(n),\qquad
r_{n,\lambda}>1\iff\lambda>\lambda_c(n).
\]
Thus at most one zero can leave the closed disk, and the exact threshold has cubic size, \(\lambda_c(n)\sim6n^{-3}\).

There is also a complete moving-mass asymptotic. For \(\tau>0\), \(s\ge0\), put \(\lambda_n=\tau n^{-s}\) and \(u_n=n\log r_{n,\lambda_n}\). Let \(H:\mathbb R\to(0,\infty)\) be the increasing bijection
\[
H(u)=\left(\int_0^1t e^{-u(1-t)}\,dt\right)^{-1}
=\frac{u^2}{u-1+e^{-u}},\quad H(0)=2,
\]
where the displayed quotient is interpreted continuously at zero. Then:

* For \(0\le s<3\), \(u_n\to u_\infty\), the unique solution of \(H(u_\infty)=3\), with \(u_\infty=1.3607795323\ldots>0\).
* For \(s=3\), \(u_n\to H^{-1}(3\tau/(\tau+3))\), negative, zero or positive according as \(\tau<6\), \(\tau=6\), or \(\tau>6\).
* For \(s>3\), \(u_n\to-\infty\), and in fact
\[
-n\log r_{n,\lambda_n}=(s-3)\log n+2\log\log n+2\log(s-3)-\log\tau+o(1).
\]
The limit for \(s=3,\tau=6\) is zero even though the **finite-degree** zero remains strictly inside: \(6n^{-3}<\lambda_c(n)\).

## Assumptions and scope

The inner product uses **a point derivative mass exactly at the boundary point \(1\)**, not an absolutely continuous derivative measure. Both parameters \(n\) and \(\lambda\) have the ranges stated above; in the asymptotic claim \(\tau\) and \(s\) are fixed while \(n\to\infty\). Zeros are counted with algebraic multiplicity. The monic polynomial exists uniquely because the inner product is positive definite on polynomials. Rotation gives the analogous statement for a positive derivative mass at any other fixed point of \(\mathbb T\).

## Proof

**1. Exact coefficient reduction.** Write \(P_{n,\lambda}(z)=z^n+\sum_{j=0}^{n-1}c_jz^j\). Haar orthogonality of monomials gives
\[
0=\langle P_{n,\lambda},z^j\rangle_\lambda=c_j+\lambda jP'_{n,\lambda}(1)
\quad(0\le j<n).
\]
As \(\sum_{j=1}^{n-1}j^2=S_n\), differentiation at one yields \(P'_{n,\lambda}(1)=n/(1+\lambda S_n)\). Therefore \(c_0=0\), \(c_j=-A_{n,\lambda}j\) for \(j\ge1\), proving the polynomial formula. Put \(m=n-1\), \(A=A_{n,\lambda}\), \(T_m(z)=\sum_{k=1}^{m}kz^{k-1}\), and \(Q_m(z)=z^m-AT_m(z)\). Since \(Q_m(0)=-A\), the zero of \(P\) at zero is simple.

**2. The distinguished zero.** The real polynomial \(Q_m\) has leading coefficient \(1\) and all lower coefficients strictly negative. Descartes' rule (counting multiplicities) gives one simple positive zero. Equivalently it solves \(F_m(r)=A\), where
\[
F_m(r)=\frac{r^m}{T_m(r)}=\left(\sum_{k=1}^mkr^{k-1-m}\right)^{-1}\quad(r>0).
\]
Each term in the denominator strictly decreases with \(r\), so \(F_m\) is strictly increasing from zero to infinity. Since \(A_{n,\lambda}\) increases strictly with \(\lambda\), so does \(r_{n,\lambda}\). At \(r=1\), \(F_m(1)=2/[m(m+1)]\). Solving \(A_{n,\lambda}=F_m(1)\) gives exactly \(\lambda=6/[n(n^2-1)]\), yielding the trichotomy for the positive zero.

**3. Every other zero is trapped in the open disk.** Let \(A_*=2/[m(m+1)]\). If \(0<A<A_*\), on \(|z|=1\),
\[
|AT_m(z)|\le A\sum_{k=1}^m k=A\frac{m(m+1)}2<|z^m|.
\]
Rouché's theorem puts all \(m\) zeros of \(Q_m\) inside. At \(A=A_*\), the triangle inequality is strict for every \(|z|=1\), \(z\ne1\) (for \(m=1\), the conclusion follows directly from \(Q_1(z)=z-A\)); the only boundary zero is the simple positive root \(1\). Its derivative can also be read off directly:
\[
Q_m'(1)=m-\frac{2}{m(m+1)}\sum_{k=1}^m k(k-1)=\frac{m+2}{3}>0.
\]
Continuity of roots then puts the other \(m-1\) zeros in the open disk at the threshold.

For \(A>A_*\) there are **no** zeros on the unit circle. Indeed the finite geometric-derivative identity
\[
(1-z)^2T_m(z)=1-(m+1)z^m+mz^{m+1}
\]
gives, for \(|z|=1\), \(z\ne1\),
\[
(1-z)^2Q_m(z)=z^m B_{m,A}(z)-A,\quad
B_{m,A}(z)=(1-z)^2+A(m+1)-Amz.
\]
Writing \(x=\operatorname{Re}z<1\), direct multiplication proves the exact **strict positivity certificate**
\[
|B_{m,A}(z)|^2-A^2=
2(1-x)\Big\{A\big[Am(m+1)-2\big]
+2(1-x)\big[A(m+1)+1\big]\Big\}>0.
\]
Thus \(z^mB_{m,A}(z)\ne A\). At \(z=1\), \(Q_m(1)=1-A/A_*<0\). No root crosses \(|z|=1\) as \(A\) varies in \((A_*,\infty)\). Immediately above \(A_*\), exactly the simple positive zero moves outside; the remaining \(m-1\) are inside. Hence this remains true for the entire positive range of \(A\), and in particular its accessible interval \(0<A<n/S_n\). This also completes the assertion about all zeros of \(P_{n,\lambda}\).

**4. The cubic-scale limit.** Set \(u_n=n\log r_{n,\lambda_n}\). The equation \(F_{n-1}(r)=A_{n,\lambda_n}\) is equivalent to
\[
\frac{1}{n^2A_{n,\lambda_n}}=
\frac1{n^2}\sum_{k=1}^{n-1}k\exp\!\left(-u_n\bigl(1-k/n\bigr)\right).
\]
For bounded real \(u\), the right side converges locally uniformly to \(\int_0^1t e^{-u(1-t)}dt\), by Riemann sums. Also,
\[
n^2A_{n,\lambda_n}=\frac{\tau n^{3-s}}{1+\tau n^{3-s}(S_n/n^3)},\qquad S_n/n^3\to\frac13.
\]
Because \(H\) is continuous and strictly increasing onto \((0,\infty)\), monotone inversion gives the asserted finite limits for \(s\le3\). In particular \(H(0)=2\), and \(3\tau/(\tau+3)=2\) precisely at \(\tau=6\).

If \(s>3\), put \(a=s-3>0\), \(v_n=-u_n\). Then \(n^2A_{n,\lambda_n}\sim\tau n^{-a}\to0\), so \(v_n\to\infty\). Comparison at trial points \(v=c\log n\), using the same Riemann sums uniformly for \(c\) in compact positive intervals, shows \(v_n/\log n\to a\). Here uniformity follows by comparing the sum with the integral of \(t e^{-vt}\): for \(v=O(\log n)\) its relative Riemann-sum error is \(O((1+v)^2/n)=o(1)\). Consequently,
\[
n^2A_{n,\lambda_n}=
\frac{v_n^2e^{-v_n}}{1-(1+v_n)e^{-v_n}}(1+o(1))
=v_n^2e^{-v_n}(1+o(1)).
\]
Taking logarithms yields \(v_n-2\log v_n=a\log n-\log\tau+o(1)\). Substituting \(v_n\sim a\log n\) into \(\log v_n\) produces the claimed logarithm-plus-loglog expansion.

## Verification

`CHECK.py` is a standalone supplementary Python checker (NumPy and SymPy required). It tests exact rational Haar orthogonality and the threshold for many degrees and masses; symbolically verifies the unit-circle strict positivity identity; numerically counts all roots of moderate-degree polynomials on each side of the exact threshold; and tests finite-degree approximations to the cubic and logarithmic asymptotic regimes. The checker reports 13705 passed assertions in the recorded execution. The all-degree and moving-parameter statements above are justified by the analytical proof, **not** by finite tests. Run `python CHECK.py` in the folder containing the extracted file.

## Relationship to prior work

The rank-one reproducing-kernel perturbation formula itself is **known**, e.g. the general discrete Sobolev polynomial representation in *Spectral Problems and Orthogonal Polynomials on the Unit Circle*, §5.2, equation (5.33). The new assertion here is the complete **finite-degree disk-zero classification at a boundary derivative mass**, including a sharp cubic threshold, an exact no-secondary-escape certificate, and a logarithmic moving-parameter asymptotic. In the same thesis, the quoted outside-support zero theorem concerns derivative evaluation points \(|\alpha|>1\), not the boundary point \(\alpha=1\).

Castillo–Garza–Marcellán (2012) study zeros for the **same general discrete derivative Sobolev inner product**. Their abstract was examined, but the full 13-page article was not accessible. Its potential overlap with the exact boundary special case is the largest remaining literature risk: we do **not** assert full-text noncoverage.

Majumder–Swaminathan (arXiv:2610.31994v1, first public October 22, 2026) study degree-varying Sobolev inner products on \(\mathbb T\) with **absolutely continuous** derivative measures, obtaining asymptotics at their natural quadratic scaling. Their assumptions do not include the point derivative mass used here. Their full relevant preprint text and zero-location discussion were examined; the present cubic boundary-atom transition is not a consequence of the statements inspected there.

## Limitations

The theorem treats one first-derivative point mass at a boundary point and Haar base measure. It does not classify higher derivatives, several masses, general base measures, or off-circle mass points. The asymptotic logarithmic expansion holds for fixed positive \(\tau\) and fixed \(s>3\), not uniformly as \(s\downarrow3\). The inaccessible 2012 article represents a substantive originality uncertainty. No independent external mathematical audit has been performed.

## References

1. S. Majumder and A. Swaminathan, *Sobolev Orthogonal Polynomials on the Unit Circle with Varying Inner Product*, arXiv:2610.31994v1 (first public 2026-10-22), https://arxiv.org/abs/2610.31994.
2. *Spectral Problems and Orthogonal Polynomials on the Unit Circle*, doctoral thesis, §5.2 (especially equation (5.33) and Theorem 5.2.4), https://e-archivo.uc3m.es/rest/api/core/bitstreams/f06d13f9-e2eb-4a0b-a057-ed68d2c23e68/content.
3. K. Castillo, L. E. Garza and F. Marcellán, *Zeros of Sobolev Orthogonal Polynomials on the Unit Circle*, Numerical Algorithms **60** (2012), 669–681, https://doi.org/10.1007/s11075-012-9594-6. Full text not examined.
4. K. Castillo, L. E. Garza and F. Marcellán, *Asymptotic Behaviour of Sobolev Orthogonal Polynomials on the Unit Circle*, Integral Transforms and Special Functions **24** (2013), 23–38, https://doi.org/10.1080/10652469.2011.649751. Abstract inspected.
