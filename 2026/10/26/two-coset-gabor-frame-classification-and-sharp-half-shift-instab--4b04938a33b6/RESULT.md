# Two-coset Gabor frame classification and sharp half-shift instability for an odd rational window

## Finding
For the real odd window
\[
g(t)=\frac{t}{(t^2+1)(t^2+4)},\qquad t\in\mathbb R,
\]
consider, for each \(0<\delta<1\), the two-frequency-coset Gabor family
\[
\mathcal G_\delta=\{e^{2\pi i\nu t}g(t-n):n\in\mathbb Z,\ \nu\in\mathbb Z\cup(\mathbb Z+\delta)\}.
\]
Then \(\mathcal G_\delta\) is a frame of \(L^2(\mathbb R)\) **if and only if** \(\delta\ne\tfrac12\). Let \(A(\delta)\) denote its optimal lower frame bound, understood to be zero at the nonframe parameter. With \(q=e^{-2\pi}\), put
\[
 c_0=\frac{4\pi^4}{9}\left(\frac{1-q}{1+q}\right)^2,\qquad
 c_h=\frac{16\pi^4q}{9}\frac{(1-\sqrt q)^4}{(1-q^2)^2}.
\]
Its sharp critical degeneration is
\[
 \lim_{\varepsilon\to0}\frac{A(\tfrac12+\varepsilon)}{\varepsilon^2}
 =\frac{c_0c_h}{c_0+c_h}=0.269312334495964\ldots.
\]
The key structural fact is that the integer Zak transform of \(g\) has precisely three zero points on the unit torus:
\[
 \{(x,\omega):Zg(x,\omega)=0\}
 =\{(0,0),(\tfrac12,0),(0,\tfrac12)\}\quad\pmod{\mathbb Z^2}.
\]
At the exceptional offset, the quadratic asymptotic is sharp rather than merely an upper or lower growth estimate.

## Assumptions and scope
Use the convention \(Zf(x,\omega)=\sum_{n\in\mathbb Z}f(x-n)e^{2\pi in\omega}\) and \(M_\nu f(t)=e^{2\pi i\nu t}f(t)\), \(T_nf(t)=f(t-n)\). The window has cubic decay, so its Zak series converges locally uniformly and gives a continuous function of the torus variables, with the conventional quasiperiodicity in \(x\). A Gabor frame means that finite strictly positive constants \(A,B\) satisfy \(A\|f\|_2^2\le\sum_{\gamma\in\mathcal G_\delta}|\langle f,\gamma\rangle|^2\le B\|f\|_2^2\) for every \(f\in L^2(\mathbb R)\). All constants refer to the unnormalized window displayed above and to the exponent \(2\pi i\nu t\).

## Proof
**1. Exact Zak formula.** Decompose \(g(t)=\tfrac13[t/(t^2+1)-t/(t^2+4)]\). Under the stated Fourier convention its transform is
\[
\widehat g(\xi)=-\frac{i\pi}{3}\operatorname{sgn}(\xi)
       (e^{-2\pi|\xi|}-e^{-4\pi|\xi|}).
\]
For \(0\le\omega\le1\) let \(z=e^{2\pi ix}\), \(r=e^{2\pi\omega}\), \(q=e^{-2\pi}\), and define
\[
\begin{split}
B(z,r)={}&\frac{rqz}{1-qz}-\frac{r^2q^2z}{1-q^2z}\\
&-\frac{r^{-1}}{1-q/z}+\frac{r^{-2}}{1-q^2/z}.
\end{split}
\]
Poisson summation in the integer index, followed by summation of four convergent geometric series, gives
\[
Zg(x,\omega)=\frac{i\pi}{3}e^{2\pi i\omega x}\,\overline{B(z,r)}.
\]
The endpoint limits are valid because \(\widehat g(0)=0\). Thus \(|Zg|=(\pi/3)|B|\).

**2. Complete zero set.** Write \(\theta=2\pi x\), \(D_j=|1-q^jz|^2=1-2q^j\cos\theta+q^{2j}\). On \(|z|=1\), direct conjugate-denominator rationalization yields
\[
B(z,r)=\frac{A_1z-C_1}{D_1}-\frac{A_2z-C_2}{D_2},
\]
where
\[
A_1=q(r+r^{-1}),\ C_1=q^2r+r^{-1},\quad
A_2=q^2(r^2+r^{-2}),\ C_2=q^4r^2+r^{-2}.
\]
Suppose \(0<\omega<1\) and \(\sin\theta\ne0\). Separating imaginary and real parts of \(B=0\) gives simultaneously \(A_1/D_1=A_2/D_2\) and \(C_1/D_1=C_2/D_2\). Eliminating the denominators and writing \(y=r^2\) gives
\[
 (q-1)(qy-1)(q^2y^2+q^2y+2qy+y+1)=0.
\]
The last factor is strictly positive and \(0<q<1\), so \(r=q^{-1/2}\), i.e. \(\omega=1/2\). At precisely this frequency \(A_j=C_j\), whence
\[
B(z,q^{-1/2})=(z-1)
\left(\frac{\sqrt q(1+q)}{D_1}-\frac{q(1+q^2)}{D_2}\right).
\]
The bracket is strictly positive: \(D_1/D_2\le(1+q)^2/(1+q^2)^2\), since differentiation of the ratio with respect to \(\cos\theta\) is negative; furthermore \(1+q^2>\sqrt q(1+q)\), as \(1+q^2-\sqrt q(1+q)=(1-\sqrt q)(1-q^{3/2})>0\). Hence \(B=0\) at \(\omega=1/2\) only when \(z=1\).

At \(z=1\), a direct factorization is
\[
B(1,r)=\frac{(r-1)(qr-1)(qr^2-1)}{r^2(q-1)(q+1)}.
\]
For \(1<r<q^{-1}\), this vanishes exactly at \(r=q^{-1/2}\), and at the boundary \(r=1,q^{-1}\) it also vanishes. At \(z=-1\), put \(a=qr,b=r^{-1}\) (so \(0<a,b<1\)); then
\[
B(-1,r)=-\frac{a+b}{1+ab}+\frac{a^2+b^2}{1+a^2b^2}<0,
\]
because the difference of the numerators upon cross multiplication equals
\[
(a-1)(b-1)(a^2b+ab^2+2ab+a+b)>0.
\]
Finally, on the frequency boundary \(\omega=0\) (equivalently \(\omega=1\)), \(B\) is purely imaginary, with imaginary part
\[
\operatorname{Im}B(z,1)=2\sin\theta
 \left(\frac{q}{D_1}-\frac{q^2}{D_2}\right).
\]
The parenthesis is positive since \(D_2-qD_1=(1-q)(1-q^3)>0\). Thus the only boundary zeros are \(z=\pm1\). The cases cover the full unit torus and establish exactly the three zeros stated.

**3. Frame classification.** Integer Zak transformation is unitary from \(L^2(\mathbb R)\) to \(L^2([0,1)^2)\). For each critical-lattice window, Parseval on the torus identifies the Gabor frame operator with multiplication by its Zak magnitude squared. Because
\[
Z(M_\delta g)(x,\omega)=e^{2\pi i\delta x}Zg(x,\omega-\delta),
\]
our two-coset family's exact frame symbol is
\[
S_\delta(x,\omega)=|Zg(x,\omega)|^2+|Zg(x,\omega-\delta)|^2.
\]
Consequently \(A(\delta)=\min_{[0,1]^2}S_\delta\). The two summands simultaneously vanish for \(0<\delta<1\) if and only if \(\delta=1/2\): the only pair of distinct zero frequencies at the same spatial coordinate is \(0,1/2\) at \(x=0\). Compactness gives a strictly positive minimum at all other offsets, and continuity gives a finite upper frame bound for every offset.

**4. Exact quadratic coefficient.** At the two common-zero points when \(\delta=1/2\), the spatial derivative \(\partial_x Zg\) is real and nonzero and the frequency derivative \(\partial_\omega Zg\) is purely imaginary and nonzero; this follows directly by differentiating the displayed rational formula at \(z=1\), using positivity of the bracket in step 2 and, at frequency zero, positivity of \(q/D_1-q^2/D_2\). Their real inner products vanish. Frequency differentiation of \(B(1,r)\), using \(dr/d\omega=2\pi r\), gives
\[
|\partial_\omega Zg(0,0)|^2=c_0,\qquad
|\partial_\omega Zg(0,\tfrac12)|^2=c_h.
\]
Both constants are strictly positive. In local coordinates \(x=\varepsilon v\), \(\omega=\varepsilon u\), \(\delta=\tfrac12+\varepsilon\) around \((0,0)\), the uniform second-order Taylor expansion on bounded \((u,v)\) sets is
\[
\varepsilon^{-2}S_{1/2+\varepsilon}(\varepsilon v,\varepsilon u)
\longrightarrow (d_0^2+d_h^2)v^2+c_0u^2+c_h(u-1)^2,
\]
where \(d_0,d_h\) are the nonzero spatial-derivative magnitudes. Around \((0,1/2)\) the \(c_0,c_h\) roles are exchanged and the limiting minimum is identical. Each quadratic form is positive definite in \((u,v)\) and its minimum is \(c_0c_h/(c_0+c_h)\). The exact finite zero set from step 2, compactness away from its two shared-zero points, and local nondegeneracy imply that every minimizer of \(S_{1/2+\varepsilon}\) lies at distance \(O(|\varepsilon|)\) of one of those points: comparison with the trial point \((x,\omega)=(0,0)\) gives \(A=O(\varepsilon^2)\), and the invertible local first derivatives bound the sum below by a positive multiple of squared distance to the displaced zero points. Hence minimization passes to the two limiting quadratic forms, proving the exact coefficient and the stated two-sided limit.

## Verification
The accompanying standalone Python checker `check.py` evaluates the Poisson/Zak formula against direct lattice sums, checks the exact two polynomial identities used in the zero classification, differentiates the Zak transform numerically at the two common zeros, and compares optimized finite-offset lower symbols with the analytic critical coefficient. Successful execution prints `CHECK_OK`. These tests are consistency checks; all quantified infinite claims follow from the analytical proof above.

## Relationship to prior work
Ghosh [1] analyzes rectangular-lattice frames for the very same odd rational window, develops a Zak/polynomial-matrix method, and establishes substantial rational-density frame regions. The present theorem is for a *union of two translated frequency cosets* rather than a rectangular lattice; neither the positive all-offset classification nor the sharp half-shift constant is supplied by those lattice results. Ulanovskii and Zlotnikov [2, Theorem 3.1 and Corollary 3.2] give parity-based nonframe obstructions on periodic sets for odd or even generators, which relate to the already expected exceptional half-shift but cannot imply the frame property at every other shift or its sharp stability constant. Classical Zak-zero methods for different generators, such as [3], are also acknowledged. The odd-window zero-set computation is the essential specialized ingredient.

## Limitations
The result is restricted to the displayed rational window, unit integer translations, and exactly two frequency cosets. It does not determine the optimal upper frame bound or give a global closed form for the lower frame bound away from the half-shift. The numerical approximation to the asymptotic coefficient is not a substitute for the exact expression. Priority against all historical and unindexed time-frequency literature is not independently established; there has been no independent scientific audit.

## References
[1] R. Ghosh, *Gabor Frames for Rational Windows with Symmetric Poles*, arXiv:2608.10568 (first public version 2026-08-11), https://arxiv.org/abs/2608.10568.

[2] A. Ulanovskii and I. Zlotnikov, *Periodic Non-uniqueness Sets for Shift-invariant Spaces and Parity-Based Obstructions to the Frame Property for Gabor Systems*, arXiv:2606.31450 (2026-06-30), https://arxiv.org/abs/2606.31450.

[3] T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013), https://arxiv.org/abs/1311.7359.
