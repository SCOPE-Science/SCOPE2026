# A sharp trace-norm correction for high-order fractional Volterra integration

## Finding
For every real \(\alpha>3\), consider the Riemann–Liouville integral operator \(I^\alpha\) on complex \(L^2(0,1)\), normalized as \(T_\alpha=\Gamma(\alpha+1)I^\alpha\). Its trace norm obeys
\[
\boxed{\|T_\alpha\|_{\mathcal S_1}=\frac12+\frac{1}{4\alpha}+O(\alpha^{-2})\qquad(\alpha\to\infty).}
\]
The optimal rank-one nuclear approximation error has the sharp rate
\[
\boxed{\inf_{\operatorname{rank}R\le1}\|T_\alpha-R\|_{\mathcal S_1}=\frac{1}{8\alpha}+O(\alpha^{-2}).}
\]
The proof additionally identifies the signed first-order spectrum after Hankel reflection: the leading positive eigenvalue is \(1/2+1/(8\alpha)+O(\alpha^{-2})\), the sole first-order negative eigenvalue is \(-1/(8\alpha)+O(\alpha^{-2})\), and the total nuclear mass of all remaining eigenvalues is \(O(\alpha^{-2})\).

## Assumptions and scope
The underlying space is complex \(L^2(0,1)\) with Lebesgue measure. For real \(\alpha>3\), define
\[
(I^\alpha f)(x)=\frac1{\Gamma(\alpha)}\int_0^x(x-t)^{\alpha-1}f(t)\,dt,
\qquad T_\alpha=\Gamma(\alpha+1)I^\alpha.
\]
Here \(\|\cdot\|_{\mathcal S_1}\) denotes the sum of singular values (the nuclear or trace-class norm). All asymptotics are for real \(\alpha\to+\infty\), not merely integer powers. The infimum is over all complex-linear rank-at-most-one operators on this Hilbert space. No claim is made about general Volterra convolution kernels or a complete second-order nuclear expansion.

## Proof
**1. Exact Hankel equivalence.** Rescale the input variable by \(v=\alpha t\), reflect and rescale the output by \(u=\alpha(1-x)\), and extend by zero from \((0,\alpha)\) to \((0,\infty)\). These are unitary input/output transformations followed by an isometric zero extension, preserving every nonzero singular value. The resulting self-adjoint Hankel operator \(K_\alpha\) on \(L^2(0,\infty)\) has kernel
\[
k_\alpha(u+v)=\left(1-\frac{u+v}{\alpha}\right)_+^{\alpha-1}.
\]
In particular, signed eigenvalues of \(K_\alpha\) determine the singular values of \(T_\alpha\).

**2. A trace-norm Hankel estimate.** Let \(h\in C^2[0,\infty)\) satisfy \(h(s),h'(s)\to0\) at infinity and \(\int_0^\infty t^2|h''(t)|\,dt<\infty\). Twice integrating the derivative gives
\[
h(s)=\int_s^\infty(t-s)h''(t)\,dt.
\]
For fixed \(t>0\), the Hankel kernel \((t-u-v)_+\) is the zero extension of \(R_tJ_t^2\) on \(L^2(0,t)\), where \(J_t f(x)=\int_0^x f(y)\,dy\) and \(R_t f(x)=f(t-x)\). Schatten Hölder and \(\|J_t\|_{\mathcal S_2}^2=t^2/2\) show \(\|R_tJ_t^2\|_{\mathcal S_1}\le t^2/2\). The Bochner integral therefore yields the quantitative lemma
\[
\boxed{\|H_h\|_{\mathcal S_1}\le\frac12\int_0^\infty t^2|h''(t)|\,dt,}
\]
where \(H_h\) denotes the Hankel operator with kernel \(h(u+v)\). This proves trace-class membership rather than merely a Hilbert–Schmidt bound.

**3. A genuinely nuclear remainder.** Put \(\varepsilon=\alpha^{-1}\) and \(f_1(s)=s-s^2/2\). The first two Hankel kernels are \(k_0(s)=e^{-s}\) and \(k_1(s)=e^{-s}f_1(s)\). Define \(h_\alpha(s)=k_\alpha(s)-k_0(s)-\varepsilon k_1(s)\). For \(0\le s<\alpha\), exact differentiation gives
\[
k_\alpha''(s)=\frac{(\alpha-1)(\alpha-2)}{\alpha^2}\left(1-\frac{s}{\alpha}\right)^{\alpha-3}.
\]
For \(s\ge\alpha\), this derivative vanishes (\(\alpha>3\)). Expanding the logarithm and the displayed prefactor, uniformly for \(0\le s\le\alpha^{1/5}\), gives
\[
k_\alpha''(s)=e^{-s}\left[1+\frac{-3+3s-s^2/2}{\alpha}\right]
+O\bigl(\alpha^{-2}(1+s^6)e^{-s/2}\bigr).
\]
The bracketed first correction equals \((e^{-s}f_1(s))''\). For \(\alpha^{1/5}\le s\le\alpha\), the elementary bound \((1-s/\alpha)^{\alpha-3}\le e^{-s/2}\) applies for all sufficiently large \(\alpha\), and the same exponential bound controls derivatives of the subtracted terms. Integrating the weighted remainder in these two regions gives
\[
\int_0^\infty s^2|h_\alpha''(s)|\,ds=O(\alpha^{-2}).
\]
The lemma from step 2 proves the essential stronger conclusion
\[
\boxed{\|K_\alpha-K_0-\varepsilon K_1\|_{\mathcal S_1}=O(\varepsilon^2).}
\]
A Hilbert–Schmidt remainder alone would not imply this nuclear estimate.

**4. Explicit first-order singular spectrum.** Let \(\phi(u)=\sqrt2e^{-u}\), let \(P=|\phi\rangle\langle\phi|\), and set \(Q=I-P\). Direct evaluation of exponential moments gives
\[
K_0=\tfrac12 P,\qquad\langle\phi,K_1\phi\rangle=\tfrac18,
\qquad QK_1Q=-|g\rangle\langle g|,
\quad g(u)=(u-\tfrac12)e^{-u},\quad\|g\|_2^2=\tfrac18.
\]
Indeed, expand \(f_1(u+v)=f_1(u)+f_1(v)-uv\). Compression by \(Q\) removes the two summands that factor through \(e^{-u}\), leaving the negative rank-one term. Ordinary perturbation of the isolated positive eigenvalue of \(K_0\) gives \(\lambda_+(K_0+\varepsilon K_1)=\tfrac12+\varepsilon/8+O(\varepsilon^2)\). The complementary compression has exactly one eigenvalue \(-\varepsilon/8+O(\varepsilon^2)\); its other first-order eigenvalues vanish. Because \(K_1\) has finite rank, the sum of absolute values of the remaining eigenvalues of \(K_0+\varepsilon K_1\) is \(O(\varepsilon^2)\). The nuclear estimate in step 3 transfers these statements to \(K_\alpha\), using the Ky Fan–Mirsky inequality for singular-value sums (and the corresponding ordered self-adjoint eigenvalues).

Consequently,
\[
\|T_\alpha\|_{\mathcal S_1}=\|K_\alpha\|_{\mathcal S_1}
=\left(\frac12+\frac\varepsilon8\right)+\frac\varepsilon8+O(\varepsilon^2)
=\frac12+\frac\varepsilon4+O(\varepsilon^2).
\]
The nuclear-rank-one approximation theorem says that the optimum is the sum of all singular values except the first. As \(s_1(T_\alpha)=\tfrac12+\varepsilon/8+O(\varepsilon^2)\), the second boxed formula follows.

## Verification
Run the accompanying `check.py` using Python 3 and NumPy. It checks the exact polynomial coefficients and exponential moments with rational arithmetic, including \(\langle\phi,K_1\phi\rangle=1/8\) and \(\|g\|_2^2=1/8\), and separately evaluates finite Nyström approximations of the exact Hankel kernel for six large real orders. Numerical discretizations illustrate the trace-norm coefficient but do not prove the infinite-dimensional nuclear remainder; the estimate in steps 2–3 supplies that proof.

## Relationship to prior work
Eveson (2003), *Norms of Iterates of Volterra Operators on \(L^2\)*, proves the qualitative equivalence \(\|T_\alpha\|_{\mathcal S_1}\sim1/2\) for real large order and explicitly asks in its final section whether the optimal rank-one nuclear error has rate closer to \(1/\alpha\) than its existing \(\alpha^{-1/2+\delta}\) bound. The present result gives the sharp coefficient and an \(O(\alpha^{-2})\) remainder for this specific classical family. Thorpe (1998) treats operator and Hilbert–Schmidt norms of the fractional integral, not the claimed trace-class correction in its accessible abstract. Lyubich–Tsedenbayar (2010) treats singular values of *fixed polynomials* of the classical Volterra operator; the inspected scope does not furnish the high-order nuclear coefficient. The result is about the full singular-value sum, not merely the first two singular values or a square-summable tail.

## Limitations
The expansion is asymptotic and concerns only the normalized classical Riemann–Liouville family. No complete second-order trace-norm coefficient, finite-order exact nuclear norm, general weighted Volterra kernel, or independent priority certification is claimed. The historical literature could contain an equivalent formula under different nomenclature. A relevant earlier operator-norm paper by Thorpe was accessible only through its abstract; its full text was not inspected.

## References
1. S. P. Eveson, *Norms of Iterates of Volterra Operators on \(L^2\)*, Journal of Operator Theory **50** (2003), 369–386, especially Sections 3, 8, and 9. Full text: https://jot.theta.ro/jot/archive/2003-050-002/2003-050-002-010.pdf.
2. B. Thorpe, *The Norm of Powers of the Indefinite Integral Operator on (0, 1)*, Bulletin of the London Mathematical Society **30** (1998), 543–548, doi:10.1112/S0024609398004810.
3. Y. Lyubich and D. Tsedenbayar, *The norms and singular numbers of polynomials of the classical Volterra operator in \(L_2(0,1)\)*, Studia Mathematica **199** (2010), 171–184, doi:10.4064/sm199-2-3.
