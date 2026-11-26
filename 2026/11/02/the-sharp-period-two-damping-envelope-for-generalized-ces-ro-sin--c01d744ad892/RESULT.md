# The endpoint finite part for two-periodic damping of generalized Cesàro singular values

## Finding

Let \(a,b\ge0\), \(a+b>0\), and let \(0\le t<1\). On \(\ell^2(\mathbb N_0)\) consider the row-damped generalized Cesàro operator
\[
(T_{t;a,b}x)_n=\frac{w_n}{n+1}\sum_{j=0}^{n}t^{n-j}x_j,\qquad w_{2k}=a,\quad w_{2k+1}=b.
\]
Write \(\mathcal C_t(a,b)=\lim_{n\to\infty}n s_n(T_{t;a,b})\) for its first-order singular-value coefficient. Put \(\beta=a^2+b^2\), \(P=\sqrt{2\beta}\), and \(\kappa=2ab/\beta\). The endpoint law is
\[
\mathcal C_t(a,b)
 =\frac{P}{2\pi}\log\frac{8}{1-t^2}
  + F(a,b)+o(1),\qquad
F(a,b)=\frac{P}{4\pi}\int_0^\pi
     \frac{\kappa\,du}{\sqrt{1+\kappa\sin u}+1},
\qquad t\uparrow1.
\tag{1}
\]
In particular, after dividing by the logarithmic scale factor \(P\), the endpoint offset is strictly increasing in \(\kappa\) and ranges from zero at one-parity damping to \(\log 2/(2\pi)\) at equal weights. The contribution is the explicit two-weight finite part at the endpoint. The first-order law at each fixed \(t\) follows from the classical Birman–Solomyak Weyl theorem; its fixed-budget extrema and quadratic onset are included below for context.

## Assumptions and scope

Singular values are in decreasing order on complex Hilbert space. The parameter \(t\) is held fixed in the singular-index limit; (1) concerns the resulting coefficient, not a joint limit. The weights may include zero. No statement is made about the operator at \(t=1\), longer periods, or a second-order expansion of individual singular values.

## Proof

**1. First-order coefficient from the Weyl theorem.** Let \(S e_n=e_{n+1}\) and \(W=\operatorname{diag}(a,b,\ldots)\). Then \(T=D W(I-tS)^{-1}\) for \(D=\operatorname{diag}((n+1)^{-1})\), so \(T\) is compact. Group coordinates \((x_{2k},x_{2k+1})\) into the nonnegative Fourier modes of \(L^2(\mathbb T;\mathbb C^2)\). In this representation the right factor is multiplication on these modes by the smooth analytic matrix symbol
\[
B_t(e^{i\theta})=\operatorname{diag}(a,b)(I-tU(\theta))^{-1},\qquad
U(\theta)=\begin{pmatrix}0&e^{i\theta}\\1&0\end{pmatrix}.
\]
The diagonal of the left factor on mode \(k\) is \(\operatorname{diag}((2k+1)^{-1},(2k+2)^{-1})\). Replacing it by \((2k+2)^{-1}I_2\) changes the product by a trace-class operator since the denominator difference is \(O((k+1)^{-2})\) and multiplication by \(B_t\) is bounded.

Let \(Q_+\) be projection onto the nonnegative Fourier modes and \(M_{B_t}\) denote multiplication by \(B_t\). Extend the replacement by zero on negative modes: it is \(L_+M_{B_t}Q_+\), with \(L_+\) the multiplier \((2k+2)^{-1}I_2\) for \(k\ge0\) and zero otherwise. These Fourier multipliers are classical pseudodifferential operators of orders \(-1\) and \(0\), respectively: on each of the two cotangent rays their symbols have the stated large-mode expansions, unaffected by finitely many frequencies. The product has principal symbol \(B_t(e^{i\theta})/(2|\xi|)\) on \(\xi>0\) and zero on \(\xi<0\). Apply the matrix/vector-bundle form of Birman–Solomyak's Weyl law (Ponge, Theorem 6.1, dimension one and order \(-1\)). The cosphere over the circle has the two unit cotangent directions, only one of which contributes. Thus the singular-value coefficient is \((4\pi)^{-1}\int_0^{2\pi}\operatorname{tr}|B_t(e^{i\theta})|\,d\theta\). A trace-class perturbation leaves it unchanged: its counting function is \(o(\varepsilon^{-1})\), and the two singular-value counting inequalities comparing an operator and its perturbation preserve the asymptotic after letting the relative threshold error tend to zero.

For \(R_t(\theta)=|1-t^2 e^{i\theta}|\), the squared Hilbert–Schmidt norm of \(B_t\) is \(\beta(1+t^2)/R_t^2\) and the absolute determinant is \(ab/R_t\). Squaring the sum of its two singular values gives the sum of these squared singular values plus twice their product. Therefore
\[
\mathcal C_t(a,b)=\frac1{4\pi}\int_0^{2\pi}
 \frac{\sqrt{\beta(1+t^2)+2ab R_t(\theta)}}{R_t(\theta)}\,d\theta.
\tag{2}
\]
The coefficient is positive. In particular, \(T\) is weak Schatten-one but not trace class, is in \(\mathcal S_q\) for \(q>1\), and its singular-value partial sums divided by \(\log N\) tend to \(\mathcal C_t(a,b)\).

**2. Endpoint analysis.** Set \(r=t^2\), \(\delta=1-r\), and \(R=|1-re^{i\theta}|\). Split (2) into
\[
\frac{P}{4\pi}\int_0^{2\pi}\frac{d\theta}{R}
 +\frac1{4\pi}\int_0^{2\pi}\frac{\sqrt{\beta(1+r)+2abR}-P}{R}\,d\theta.
\]
Write \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2 u)^{-1/2}\,du\). The first integral without its prefactor is \(4(1+r)^{-1}K(2\sqrt r/(1+r))\). Its elliptic complementary modulus is \(\delta/(1+r)\), so the standard logarithmic asymptotic of \(K\) gives \(2\log(8/\delta)+o(1)\). For the second integral rationalize the numerator to get
\[
\frac{2ab-\beta\,\delta/R}{\sqrt{\beta(1+r)+2abR}+P}.
\]
This is bounded by \((2ab+\beta)/P\) in absolute value since \(\delta\le R\), including through the singular region near \(\theta=0\). For \(0<\theta<2\pi\) it tends to \(2ab/[P\bigl(\sqrt{1+\kappa\sin(\theta/2)}+1\bigr)]\). Dominated convergence followed by \(u=\theta/2\), using \(4ab/P=P\kappa\), gives (1). In the form \((\sqrt{1+\kappa\sin u}-1)/\sin u\), the normalized integrand is strictly increasing in \(\kappa\) for \(0<u<\pi\). The upper endpoint of the normalized finite part follows from the equal-weight scalar coefficient below: with \(s=a+b=P\), it grows as \(P\log(8/(1-t))/(2\pi)+o(1)\), so subtracting the scale in (1) leaves \(P\log 2/(2\pi)\).

**3. Fixed-budget context.** At \(s=a+b\) fixed, the radicand in (2) is \(s^2(1+t^2)-2ab(1+t^2-R_t)\). For \(0<t<1\) it strictly decreases with \(ab\) for almost every angle. The minimum is therefore uniquely at \(a=b=s/2\) and the maximum exactly at \(ab=0\). In the balanced case the two Fourier channels unfold to the scalar symbol \((s/2)(1-te^{i\varphi})^{-1}\). In the one-parity case the integrand reduces to \(s\sqrt{1+t^2}/R_t\). The respective extremal values are
\[
\frac{s}{\pi(1+t)}K\!\left(\frac{2\sqrt t}{1+t}\right),\qquad
\frac{s}{\pi\sqrt{1+t^2}}K\!\left(\frac{2t}{1+t^2}\right).
\]
They coincide at \(t=0\), where the coefficient is \(s/2\). The uniform expansion \(R_t=1-t^2\cos\theta+O(t^4)\) gives \(\mathcal C_t=s/2+\beta t^2/(4s)+O_{a,b}(t^4)\), so the gap from balancing is \((a-b)^2t^2/(8s)+O_{a,b}(t^4)\). The logarithmic coefficients in (1) have \(P=s\) when balanced and \(P=\sqrt2 s\) at one parity; hence the ratio of the maximum to the minimum tends to \(\sqrt2\).

## Reproducibility

The accompanying \(\texttt{check.py}\) (Python, NumPy and SciPy) provides finite numerical checks of the matrix symbol, elliptic extrema, and approach to the endpoint law, along with consistency checks on finite-section singular values. The Weyl law and the endpoint limiting argument, not these computations, establish the infinite assertions.

## Relationship to prior work

Albanese, Bonet and Ricker [1] study the underlying scalar generalized Cesàro family. Pushnitski [2, Theorem 1.2] gives a singular-value law for scalar banded matrices with constant leading coefficients on each diagonal; truncation and geometric tail control apply it in the balanced case, but distinct parity weights are not constant along a scalar diagonal. In full generality (2) is a specialization of Birman–Solomyak's classical Weyl law [3, Theorem 6.1], as shown above. The elliptic extrema and the small-\(t\) expansion follow directly from (2) and are not asserted as independent new theorems. The contribution in (1) is the exact finite part for varying normalized contrast at \(t\uparrow1\). The nearby weighted-space formulation [4] uses a geometric measure and a diagonal similarity, not multiplication of the output rows, and does not give this endpoint calculation. No claim of exhaustive priority is made for (1).

## References

1. A. A. Albanese, J. Bonet and W. J. Ricker, *Spectral properties of generalized Cesàro operators in sequence spaces*, https://arxiv.org/abs/2305.04805.
2. A. Pushnitski, *Spectral asymptotics for Toeplitz operators and an application to banded matrices*, §1.3, Theorem 1.2, https://arxiv.org/abs/1710.02652.
3. R. Ponge, *Connes’ integration and Weyl’s laws*, J. Noncommut. Geom. **17** (2023), §6.1, Theorem 6.1 (Birman–Solomyak), https://ems.press/content/serial-article-files/31026.
4. *Period-two geometric weights: singular Weyl law and contrast rigidity for Cesàro averaging*, Resultary `aa2e3f6295b0` (2026), Finding and Assumptions and scope.
