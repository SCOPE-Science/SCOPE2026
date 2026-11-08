# A Gaussian interior-edge correction for two-tap Hardy composition–differentiation operators

## Finding
On the classical complex Hardy space \(H^2(\mathbb D)\), let \(d,m\) be fixed positive integers, \(c\in\mathbb C\setminus\{0\}\), and \(0<r<1\). Consider the compact weighted composition–differentiation operator
\[
(T_r f)(z)=(1+c z^m)f^{(d)}(rz).
\]
Put \(a=|c|\), \(\varepsilon=-\log r\), and \(A_d=(d/e)^d\). Then the *sharp first-order spectral-edge law* is
\[
\boxed{\displaystyle
\|T_r\|=\frac{(1+a)A_d}{\varepsilon^d}
\left[1+\varepsilon\left(\frac{d+1}{2}-
\frac{m\sqrt a}{2(1+a)\sqrt d}\right)+o(\varepsilon)\right]}
\qquad (r\uparrow1).
\]
The limit is pointwise for each fixed \(d,m,c\); no uniformity as these parameters vary is claimed. The first correction depends on the *tap separation* \(m\), although the leading constant does not. In particular, for \(d=1\) and \(a=1\), the coefficient is \(1-m/4\): positive at \(m<4\), zero at \(m=4\), and negative at \(m>4\). At the zero case the claim is only an \(o(\varepsilon)\) remainder, not a second-order expansion.

## Assumptions and scope
The Hardy norm is the coefficient norm \(\|\sum_{k\ge0}\xi_kz^k\|^2=\sum_{k\ge0}|\xi_k|^2\). The input and output spaces are both \(H^2(\mathbb D)\). The operator acts by differentiating **before** composing with \(z\mapsto rz\), then multiplying by \(1+c z^m\). The parameters \(d,m\) must be positive integers, and the complex coefficient \(c\) is fixed and nonzero. The case \(d=0\) is a boundary-edge rather than an interior-edge problem and is excluded. For each \(r<1\), the factorial-polynomial coefficient growth times \(r^n\) gives compactness. No assertion of an exact finite-\(r\) norm, complete singular-value distribution, or sharp next remainder is made.

## Proof
**1. Exact coefficient and quadratic-form reduction.** Let \(e_k(z)=z^k\) be the Hardy orthonormal basis and \(S e_k=e_{k+1}\) the unilateral shift on \(\ell^2(\mathbb N_0)\). For every \(n\ge0\),
\[
T_re_{n+d}=\frac{(n+d)!}{n!}r^n(e_n+c e_{n+m}),
\qquad T_re_k=0\quad(0\le k<d).
\]
Thus, after omitting the null domain summand, \(\varepsilon^d T_r\) has the same nonzero singular values as \((I+c S^m)D_\varepsilon\), where
\[
D_\varepsilon e_n=b_\varepsilon(n)e_n,\qquad
b_\varepsilon(n)=e^{-\varepsilon n}\prod_{j=1}^{d}(\varepsilon n+j\varepsilon).
\]
A diagonal unitary conjugation removes the argument of \(c\). Hence we may assume \(c=a>0\). Set \(B_\varepsilon=\max_{n\ge0}b_\varepsilon(n)\) and let \(L_\varepsilon=\|(I+aS^m)D_\varepsilon\|^2\). The isometry of \(S^m\) gives, **exactly for every \(h\in\ell^2\)**,
\[
\|(I+aS^m)h\|^2=(1+a)^2\|h\|^2-a\|(I-S^m)h\|^2.
\]
Consequently
\[
(1+a)^2B_\varepsilon^2-L_\varepsilon
=\inf_{\|f\|=1}\left\{(1+a)^2\sum_{n\ge0}
(B_\varepsilon^2-b_\varepsilon(n)^2)|f_n|^2
+a\|(I-S^m)D_\varepsilon f\|^2\right\}.
\tag{1}
\]
The residue classes modulo \(m\) reduce both terms of (1). In particular, there are no hidden interactions between these classes.

**2. Localization of the coefficient maximum.** For continuous \(x\ge0\), extend the coefficients by
\[
b_\varepsilon(x)=e^{-x}\prod_{j=1}^{d}(x+j\varepsilon).
\]
Its logarithmic derivative is \(-1+\sum_{j=1}^d(x+j\varepsilon)^{-1}\), a strictly decreasing function of \(x\). Its unique positive maximum tends to \(x=d\). Taylor expansion near \(d\), followed by rounding to the grid \(x=\varepsilon n\), gives
\[
B_\varepsilon^2=A_d^2[1+(d+1)\varepsilon+O(\varepsilon^2)].
\tag{2}
\]
Indeed \(x^d e^{-x}\) has its unique nondegenerate maximum \(A_d\) at \(d\), and \(\sum_{j=1}^d j/d=(d+1)/2\). If \(y=\sqrt\varepsilon(n-d/\varepsilon)\) remains in a fixed bounded interval, the second, localized expansion is
\[
\frac{B_\varepsilon^2-b_\varepsilon(n)^2}{\varepsilon}
\longrightarrow\frac{A_d^2}{d}y^2,
\tag{3}
\]
uniformly on bounded \(y\)-intervals. Moreover there are constants \(C,C' ,\varepsilon_0>0\), depending on \(d\), such that for every \(0<\varepsilon<\varepsilon_0\) and every integer \(n\ge0\),
\[
B_\varepsilon^2-b_\varepsilon(n)^2\ge
C\min\{(\varepsilon n-d)^2,1\}-C'\varepsilon^2.
\tag{4}
\]
To justify (4), use strict quadratic concavity near the continuous maximizer \(x_\varepsilon=d+O(\varepsilon)\), the positive off-peak gap on compact sets, and exponentially decaying tails. The discrete-maximum rounding and the shift \(x_\varepsilon-d=O(\varepsilon)\) necessitate the explicit subtractive error \(C'\varepsilon^2\). In general the same bound without this error is false at a maximizing lattice index.

**3. A discrete harmonic-oscillator limit.** Define \(\mathcal E_\varepsilon\) as the right side of (1). We claim
\[
\boxed{\displaystyle
\lim_{\varepsilon\downarrow0}\frac{\mathcal E_\varepsilon}{\varepsilon}
=A_d^2\,m(1+a)\sqrt{a/d}.}
\tag{5}
\]
For the upper bound take one residue class modulo \(m\), put \(h_\varepsilon=m\sqrt\varepsilon\), and sample a normalized Schwartz function \(u\) at
\(y_n=\sqrt\varepsilon(n-d/\varepsilon)\) as
\(f_n=\sqrt{h_\varepsilon}\,u(y_n)\) on this class and \(f_n=0\) otherwise, with asymptotically negligible renormalization. Equations (3) and dominated Riemann-sum convergence yield
\[
\lim_{\varepsilon\downarrow0}\frac{\text{energy of }f}{\varepsilon}
=A_d^2\left[a m^2\int_{\mathbb R}|u'(y)|^2\,dy
+\frac{(1+a)^2}{d}\int_{\mathbb R}y^2|u(y)|^2\,dy\right]
\tag{6}
\]
for \(\|u\|_{L^2}=1\). The discrete gradient contribution follows from
\(\|(I-S^m)D_\varepsilon f\|^2\): the physical step in the variable \(y\) is \(m\sqrt\varepsilon\), while \(b_\varepsilon(n)\to A_d\) in the localized window.

For the matching lower bound, choose nearly minimizing unit vectors with energy at most \(C_0\varepsilon\), as provided by the upper trial. Inequality (4) implies tightness in the variable \(y\): for fixed \(R\ge1\), the mass on \(\{|y_n|>R\}\) is bounded by \(C_1/R^2+o(1)\). On each residue class interpolate the samples \(b_\varepsilon(n)f_n/(A_d\sqrt{h_\varepsilon})\) linearly at the successive \(y_n\)'s. The gradient term bounds their local \(H^1\)-norms, and the potential term bounds their second moments. Local compact Sobolev embedding, a diagonal subsequence and tightness give strong \(L^2(\mathbb R)\) limits \(u_0,\ldots,u_{m-1}\), with total squared norm \(1\). Lower semicontinuity of the interpolated gradients and (3) give
\[
\liminf\frac{\mathcal E_\varepsilon}{\varepsilon}
\ge A_d^2\sum_{j=0}^{m-1}\left[
 a m^2\|u_j'\|_2^2
+\frac{(1+a)^2}{d}\|y u_j\|_2^2\right].
\tag{7}
\]
Here the interpolation is made on the whole real line by extending with zero past the remote lower boundary \(y=-d/\sqrt\varepsilon\); on every fixed compact interval this boundary is absent. The norm and tightness estimates prevent loss of mass.

The sharp one-dimensional oscillator (Heisenberg) inequality,
\[
A\|u'\|_2^2+B\|yu\|_2^2\ge\sqrt{AB}\,\|u\|_2^2,
\qquad A,B>0,
\]
follows by completing the square \(\|\sqrt A\,u'+\sqrt B\,yu\|_2^2\ge0\) and integrating \(2\operatorname{Re}\int y u'\overline u=-\|u\|_2^2\). Equality is attained by a normalized Gaussian. Applying it in (6) and (7) with \(A=am^2\), \(B=(1+a)^2/d\) proves (5) in both directions. All uses of compactness above are for the newly rescaled test vectors; no finite-section extrapolation is substituted for the argument.

**4. Extraction of the sharp coefficient.** Combining (1), (2), and (5),
\[
L_\varepsilon=A_d^2\left[(1+a)^2+
\varepsilon\left((1+a)^2(d+1)-m(1+a)\sqrt{a/d}\right)
+o(\varepsilon)\right].
\]
Taking the positive square root and recalling \(\|T_r\|=\varepsilon^{-d}\sqrt{L_\varepsilon}\) yields the boxed assertion.

## Verification
The independent finite identities in `edge_check.py` test the exact shift quadratic form over rational vectors. The same script numerically diagonalizes residue-class Jacobi matrices for several \(d,m,a\) and verifies convergence of the measured first-order coefficient toward the formula. It records 918 exact identities and 35 finite-section diagnostics (953 assertions total). Finite checks corroborate the formula; equations (1)–(7), the localization bound, and the oscillator inequality supply the infinite-dimensional proof. The script requires Python 3, NumPy and SciPy; run `python edge_check.py` in the directory containing that file.

## Relationship to prior work
Sun and Liu, arXiv:2610.19658 (first public 2026-10-14), study \(D_{\phi,\varphi}^{d}\) extensively, including exact singular values for **monomial** weight \(\phi(z)=z^k\) and linear \(\varphi\) (Theorem 9.2). A sum \(1+c z^m\) destroys the orthogonality of monomial outputs; their quoted exact sequence does not give the first norm correction here. Fatehi, arXiv:2108.05645, obtains general norm bounds and an exact unweighted composition–differentiation norm with linear symbol, not the two-tap interior-edge coefficient. The separate undifferentiated two-tap problem has a different boundary-edge scaling when \(d=0\), and does not imply the \(d\ge1\) harmonic-oscillator constant. Classical Kac–Murdock–Szegő distribution theorems give bulk spectral statistics for slowly varying band matrices, but not this first correction to a single top singular value; their general framework helps explain the appearance of a continuum symbol. The proof here is self-contained and establishes the exact coefficient in this family.

## Limitations
Originality is provisional pending exhaustive specialized semiclassical-Jacobi bibliography review: a general theorem on first eigenvalues of slowly varying Jacobi matrices could imply the displayed law without naming composition–differentiation operators. The theorem treats only fixed finite tap separation and fixed positive derivative order; it does not cover a joint limit with growing \(m\), symbols with more than two taps, or a higher-order expansion at the cancellation point. No independent mathematical audit has been performed.

## References
1. J. Sun and J. Liu, *Weighted composition–differentiation operators on mixed-norm, derivative Hardy and \(F(p,q,s)\) spaces*, arXiv:2610.19658, first public 2026-10-14; especially Section 9.2, Theorem 9.2.
2. M. Fatehi, *Weighted Composition–Differentiation Operator on the Hardy and Weighted Bergman Spaces*, arXiv:2108.05645, first public 2021-08-12; especially Section 3.
3. A. Bourget, A. Alvarez Loya and T. McMillen, *Spectral asymptotics for Kac–Murdock–Szegő matrices*, arXiv:1610.00084, first public 2016-10-01; bulk distribution and determinant framework.
4. S. Becker, J. Wittsten and M. Zworski, *Discrete vs. continuous in the semiclassical limit*, arXiv:2406.05934, first public 2024-06-09; related discrete Schrödinger comparison in a different setting.
