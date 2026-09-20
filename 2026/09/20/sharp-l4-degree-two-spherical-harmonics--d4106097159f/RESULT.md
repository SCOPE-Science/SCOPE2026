# Sharp L4/L2 norm and extremizers for degree-two spherical harmonics

## Statement

Let \(\mathcal H_2^{(n)}\) denote the complex-valued spherical harmonics of degree two on \(\mathbb S^{n-1}\subset\mathbb R^n\), and let \(\mu_n\) be normalized surface measure, \(\mu_n(\mathbb S^{n-1})=1\).

Define
\[
K_n^4:=\frac{3(n+2)(5n^2-13n+12)}{(n-1)(n+4)(n+6)},\qquad n\ge2.
\tag{1}
\]

### Theorem — exact degree-two reverse Hölder constant

For every \(Y\in\mathcal H_2^{(n)}\),
\[
\boxed{\ \|Y\|_{L^4(\mu_n)}\le K_n\,\|Y\|_{L^2(\mu_n)}.\ }
\tag{2}
\]
The constant \(K_n\) is sharp.

The equality cases are completely determined:

- If \(n=2\) or \(n=3\), equality holds exactly when \(Y\) has constant complex phase, i.e. \(Y=\gamma Y_0\) for some \(\gamma\in\mathbb C\setminus\{0\}\) and some nonzero real-valued \(Y_0\in\mathcal H_2^{(n)}\).
- If \(n\ge4\), equality holds exactly for the constant-phase zonal quadratics
  \[
  Y(\omega)=\gamma\left((v\cdot\omega)^2-\frac1n\right),
  \qquad \gamma\in\mathbb C\setminus\{0\},\quad v\in\mathbb S^{n-1}.
  \tag{3}
  \]

For real-valued harmonics there is an exact invariant formula. Write
\[
Y_A(\omega)=\omega^T A\omega,
\tag{4}
\]
where \(A\) is a nonzero real symmetric traceless \(n\times n\) matrix. Then
\[
\frac{\|Y_A\|_4^4}{\|Y_A\|_2^4}
=
\frac{3n(n+2)}{(n+4)(n+6)}
\left(
1+4\frac{\operatorname{tr}(A^4)}{\operatorname{tr}(A^2)^2}
\right),
\tag{5}
\]
and the sharp matrix inequality behind (2) is
\[
\frac{\operatorname{tr}(A^4)}{\operatorname{tr}(A^2)^2}
\le
\frac{n^2-3n+3}{n(n-1)}.
\tag{6}
\]
For \(n\ge4\), equality in (6) holds exactly when \(A\) has one eigenvalue of multiplicity one and the other eigenvalue of multiplicity \(n-1\); equivalently \(A\) is a nonzero scalar multiple of \(vv^T-I/n\). For \(n=2,3\), the left side of (6) is identically \(1/2\) on nonzero traceless symmetric matrices.

With unnormalized surface area \(dS\), (2) becomes
\[
\|Y\|_{L^4(dS)}
\le
|\mathbb S^{n-1}|^{-1/4}K_n\,\|Y\|_{L^2(dS)}.
\tag{7}
\]
In particular, on \(\mathbb S^2\),
\[
\sup_{0\ne Y\in\mathcal H_2^{(3)}}
\frac{\|Y\|_{L^4(dS)}}{\|Y\|_{L^2(dS)}}
=
\left(\frac{15}{28\pi}\right)^{1/4}.
\tag{8}
\]

## Proof

### 1. Degree-two harmonics are traceless quadratic forms

Every real homogeneous quadratic polynomial can be written as \(x^TAx\) with \(A\) real symmetric. Since
\[
\Delta(x^TAx)=2\operatorname{tr}A,
\]
it is harmonic exactly when \(\operatorname{tr}A=0\). Restricting to the sphere gives (4). A complex degree-two harmonic is \(Y_A+iY_B\) with \(A,B\) real symmetric traceless.

### 2. Exact second and fourth moments

Let \(\omega\) be uniform on \(\mathbb S^{n-1}\), let \(G\sim N(0,I_n)\), and write \(G=R\omega\). The radius \(R\) is independent of \(\omega\), with
\[
\mathbb E R^4=n(n+2),
\qquad
\mathbb E R^8=n(n+2)(n+4)(n+6).
\tag{9}
\]
For a traceless symmetric \(A\), standard Gaussian quadratic-form moments give
\[
\mathbb E(G^TAG)^2=2\operatorname{tr}(A^2),
\tag{10}
\]
and
\[
\mathbb E(G^TAG)^4
=12\operatorname{tr}(A^2)^2+48\operatorname{tr}(A^4).
\tag{11}
\]
Dividing by the corresponding radial moments yields
\[
\|Y_A\|_2^2
=
\frac{2\operatorname{tr}(A^2)}{n(n+2)},
\tag{12}
\]
\[
\|Y_A\|_4^4
=
\frac{12\operatorname{tr}(A^2)^2+48\operatorname{tr}(A^4)}
{n(n+2)(n+4)(n+6)}.
\tag{13}
\]
Taking the quotient proves (5).

### 3. A sharp fourth-power inequality for zero-sum eigenvalues

Let \(\lambda_1,\dots,\lambda_n\) be the eigenvalues of \(A\). By homogeneity it suffices to prove
\[
\sum_{j=1}^n\lambda_j=0,\qquad
\sum_{j=1}^n\lambda_j^2=1
\quad\Longrightarrow\quad
\sum_{j=1}^n\lambda_j^4
\le
c_n:=\frac{n^2-3n+3}{n(n-1)}.
\tag{14}
\]
For \(n=2\), zero sum gives \((a,-a)\), hence the quotient is \(1/2\). For \(n=3\), if \(a+b+c=0\), then a direct Newton-identity calculation gives
\[
a^4+b^4+c^4=\frac12(a^2+b^2+c^2)^2,
\tag{15}
\]
so again the quotient is \(1/2=c_n\).

Assume now \(n\ge4\). The constraint set in (14) is compact, so a maximizer exists. At a maximizer, Lagrange multipliers \(\alpha,\beta\) give
\[
4\lambda_j^3=\alpha+2\beta\lambda_j,
\qquad 1\le j\le n.
\tag{16}
\]
Thus all coordinates are roots of one cubic and there are at most three distinct values.

Suppose first that three distinct roots \(r<s<t\) occur. Since the cubic in (16) has no quadratic term,
\[
r+s+t=0,
\qquad
\beta=r^2+s^2+t^2.
\tag{17}
\]
If a root \(z\in\{r,s,t\}\) occurs at least twice, vary two coordinates carrying that same value by \(+\varepsilon\) and \(-\varepsilon\). This is tangent to both constraints. The second-order necessary condition for a maximum therefore gives
\[
12z^2-2\beta\le0,
\qquad\text{hence}\qquad
5z^2\le\sum_{w\in\{r,s,t\}\setminus\{z\}}w^2.
\tag{18}
\]
Neither extreme root can satisfy (18). For example, writing \(r=-a<0\) and using \(s+t=a\) with \(-a<s<t<2a\), one has strictly
\[
s^2+t^2<5a^2=5r^2,
\]
and the argument for \(t\) is symmetric. Hence both extreme roots have multiplicity one. The middle root then has multiplicity \(n-2\), so the zero-sum constraint together with \(r+s+t=0\) gives
\[
r+(n-2)s+t=0,
\qquad r+s+t=0,
\]
and therefore \((n-3)s=0\). Thus \(s=0\) and \(r=-t\). Such a stationary point has
\[
\sum\lambda_j^4=\frac12
\tag{19}
\]
after \(\sum\lambda_j^2=1\).

If only two distinct values occur, with multiplicities \(m\) and \(n-m\), zero sum forces them to be proportional to \(n-m\) and \(-m\). Consequently
\[
\frac{\sum\lambda_j^4}{(\sum\lambda_j^2)^2}
=
\frac{n}{m(n-m)}-\frac3n.
\tag{20}
\]
This is maximized when \(m(n-m)\) is minimized, namely at \(m=1\) or \(m=n-1\), and the resulting value is exactly \(c_n\). Moreover,
\[
c_n-\frac12
=
\frac{(n-2)(n-3)}{2n(n-1)}>0
\qquad(n\ge4),
\tag{21}
\]
so the three-root stationary points in (19) cannot be global maximizers. This proves (14), including the equality classification. Equations (5) and (14) now give (1)–(2) for real-valued harmonics.

### 4. Complex harmonics have the same sharp constant

Let \(Y=U+iV\), with \(U,V\) real degree-two harmonics, and define
\[
H_\theta=\operatorname{Re}(e^{-i\theta}Y)=U\cos\theta+V\sin\theta.
\]
Pointwise averaging in \(\theta\) gives
\[
\frac1{2\pi}\int_0^{2\pi}H_\theta(\omega)^4\,d\theta
=\frac38|Y(\omega)|^4,
\tag{22}
\]
so
\[
\frac1{2\pi}\int_0^{2\pi}\|H_\theta\|_4^4\,d\theta
=\frac38\|Y\|_4^4.
\tag{23}
\]
Put
\[
a=\|U\|_2^2,
\quad b=\|V\|_2^2,
\quad c=\langle U,V\rangle,
\quad m=\frac{a+b}{2},
\quad d=\frac{a-b}{2}.
\]
Then
\[
\|H_\theta\|_2^2=m+d\cos2\theta+c\sin2\theta,
\]
and hence
\[
\frac1{2\pi}\int_0^{2\pi}\|H_\theta\|_2^4\,d\theta
=m^2+\frac{d^2+c^2}{2}.
\tag{24}
\]
Cauchy–Schwarz gives \(c^2\le ab=m^2-d^2\), so
\[
\frac1{2\pi}\int_0^{2\pi}\|H_\theta\|_2^4\,d\theta
\le\frac32m^2
=\frac38\|Y\|_2^4.
\tag{25}
\]
Applying the sharp real inequality to every \(H_\theta\) and averaging,
\[
\frac38\|Y\|_4^4
\le
K_n^4\frac1{2\pi}\int_0^{2\pi}\|H_\theta\|_2^4\,d\theta
\le
\frac38K_n^4\|Y\|_2^4.
\tag{26}
\]
This proves (2) for complex harmonics.

Equality in (25) requires \(c^2=ab\), so \(U\) and \(V\) are linearly dependent. Thus an extremizing complex harmonic has constant phase times a real harmonic. Combining this with the real equality cases above gives the stated complete classification.

## Relation to the literature

Stanton and Weinstein studied the \(L^4/L^2\) extremal problem on \(\mathbb S^2\). Their 1981 paper proves that a highest-weight spherical harmonic is a local maximizer and, in its discussion of the global problem, explicitly asks what the global maximizer is. The present theorem gives the complete global answer in degree two and simultaneously treats \(\mathbb S^{n-1}\) in every ambient dimension \(n\ge2\).

Lu's 1987 note simplifies the local Hessian argument of Stanton–Weinstein. Sogge's 1986 theorem gives the sharp asymptotic order, as the harmonic degree tends to infinity, of \(L^q/L^2\) norms on spheres. Dai, Feng and Tikhonov later determined sharp asymptotic orders for a wider family of reverse Hölder ratios. Those results are asymptotic in the degree and do not supply the exact finite-degree-two constant (1) or the equality classification above.

A related 2013 paper of De Carli, Gorbachev and Tikhonov notes that exact norm-ratio suprema for spherical harmonics are generally difficult and records an unknown supremum in the sharp constant of a Pitt inequality. The quantity there is not identical to (2), but it provides additional context for why exact finite-dimensional norm ratios matter.

## Limitations

- The result is exact only for degree two; it does not determine the global \(L^4/L^2\) extremizer for arbitrary harmonic degree.
- The literature search found no statement matching (1)–(6), but an equivalent formulation could exist in invariant theory, matrix-moment inequalities, or older reverse Hölder literature under different notation.
- Duoandikoetxea's 1987 paper on reverse Hölder inequalities for spherical harmonics is particularly relevant because it gives degree-dependent dimension-free bounds for some exponent pairs; its full theorem text was not inspected here, so it remains a residual originality risk.
- Independent audit has not been performed.

## References

1. R. J. Stanton and A. Weinstein, “On the L4 norm of spherical harmonics,” *Mathematical Proceedings of the Cambridge Philosophical Society* **89** (1981), 343–358. DOI: https://doi.org/10.1017/S0305004100058229 .
2. J.-H. Lu, “A note on a theorem of Stanton-Weinstein on the L4-norm of spherical harmonics,” *Mathematical Proceedings of the Cambridge Philosophical Society* **102** (1987), 561–563. DOI: https://doi.org/10.1017/S0305004100067591 .
3. C. D. Sogge, “Oscillatory integrals and spherical harmonics,” *Duke Mathematical Journal* **53** (1986), 43–65. DOI: https://doi.org/10.1215/S0012-7094-86-05303-2 .
4. J. Duoandikoetxea, “Reverse Hölder inequalities for spherical harmonics,” *Proceedings of the American Mathematical Society* **101** (1987), 487–491. DOI: https://doi.org/10.2307/2046394 .
5. F. Dai, H. Feng and S. Tikhonov, “Reverse Hölder's inequality for spherical harmonics,” *Proceedings of the American Mathematical Society* **144** (2016), 1041–1051. DOI: https://doi.org/10.1090/proc/12986 .
6. L. De Carli, D. Gorbachev and S. Tikhonov, “Pitt and Boas inequalities for Fourier and Hankel transforms,” *Journal of Mathematical Analysis and Applications* **408** (2013), 762–774. DOI: https://doi.org/10.1016/j.jmaa.2013.06.045 .
