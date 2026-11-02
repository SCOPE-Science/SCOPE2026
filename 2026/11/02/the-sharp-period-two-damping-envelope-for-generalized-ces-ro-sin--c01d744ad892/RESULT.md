# The sharp period-two damping envelope for generalized Cesàro singular values

## Finding
For \(0\le t<1\) and \(a,b\ge0\) with \(a+b>0\), consider the compact operator \(T_{t;a,b}\) on complex \(\ell^2(\mathbb N_0)\) defined by
\[
(T_{t;a,b}x)_n=\frac{w_n}{n+1}\sum_{j=0}^{n}t^{n-j}x_j,\qquad w_{2k}=a,\quad w_{2k+1}=b.
\]
Its decreasing singular values have the *exact first-order coefficient*
\[
\lim_{n\to\infty}n\,s_n(T_{t;a,b})=\mathcal C_t(a,b):=\frac1{4\pi}\int_0^{2\pi}\frac{\sqrt{(a^2+b^2)(1+t^2)+2ab\,R_t(\theta)}}{R_t(\theta)}\,d\theta,
\quad R_t(\theta)=|1-t^2e^{i\theta}|.
\tag{1}
\]
Consequently \(T_{t;a,b}\) is weak Schatten-one, belongs to every \(\mathcal S_q\) for \(q>1\), is not trace class, and
\[
\lim_{N\to\infty}\frac1{\log N}\sum_{n=1}^N s_n(T_{t;a,b})=\mathcal C_t(a,b).
\tag{2}
\]
At fixed total row weight \(s=a+b>0\) and each \(0<t<1\), this coefficient is **uniquely minimized by equal weights**, and **maximized exactly at the two one-parity profiles**. Both sharp values are explicit:
\[
\frac{s}{\pi(1+t)}K\!\left(\frac{2\sqrt t}{1+t}\right)
\ \le\ \mathcal C_t(a,b)\ \le\ 
\frac{s}{\pi\sqrt{1+t^2}}K\!\left(\frac{2t}{1+t^2}\right),
\tag{3}
\]
where equality on the left holds precisely when \(a=b=s/2\) and on the right precisely when \(ab=0\). Here \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2u)^{-1/2}\,du\). For \(t=0\), all profiles give \(s/2\). The strict penalty turns on quadratically at zero:
\[
\mathcal C_t(a,b)-\mathcal C_t(s/2,s/2)=\frac{(a-b)^2}{8s}t^2+O_{a,b}(t^4)\qquad(t\downarrow0).
\tag{3a}
\]

There is also a two-term endpoint law. Set \(\beta=a^2+b^2\), \(P=\sqrt{2\beta}\), \(\kappa=2ab/\beta\), and
\[
F(a,b)=\frac{P}{4\pi}\int_0^\pi\frac{\sqrt{1+\kappa\sin u}-1}{\sin u}\,du
=\frac{P}{4\pi}\int_0^\pi\frac{\kappa}{\sqrt{1+\kappa\sin u}+1}\,du.
\]
Then
\[
\boxed{\mathcal C_t(a,b)=\frac{P}{2\pi}\log\frac8{1-t^2}+F(a,b)+o(1)\quad(t\uparrow1).}
\tag{4}
\]
Under fixed \(a+b>0\), the ratio of the largest to the smallest coefficients in (3) tends to \(\sqrt2\) as \(t\uparrow1\). This change from equal coefficients at \(t=0\) to a strict damping-contrast penalty at \(t>0\), with an exact endpoint finite part, is the main distinction from the unweighted case.

## Assumptions and scope
All Hilbert spaces are complex, although the same singular values arise for the real matrix acting on real \(\ell^2\). Coordinates begin at zero. The parameter \(t\) is fixed below one when the singular-index limit is taken; (4) is a subsequent limit of its coefficient, not a joint scaling theorem. The limiting extrema allow zero rows; if \(a,b>0\) are required, the upper value is a sharp supremum but is not attained. Neither a singular-value expansion beyond first order nor the spectrum at \(t=1\) is claimed.

## Proof
**1. A periodic finite-band counting lemma.** Put \(D=\operatorname{diag}((n+1)^{-1})\), let \(S e_n=e_{n+1}\), and let \(W=\operatorname{diag}(a,b,a,b,\ldots)\). Write \(A_m=W\sum_{r=0}^m c_rS^r\), with arbitrary complex coefficients and \(M=\max(a,b)\sum_{r=0}^m|c_r|\). For a compact operator \(Y\), let \(N(\varepsilon;Y)=\#\{j:s_j(Y)>\varepsilon\}\). We show that
\[
\lim_{\varepsilon\downarrow0}\varepsilon N(\varepsilon;DA_m)=\frac1{4\pi}\int_0^{2\pi}\operatorname{tr}|B_m(\theta)|\,d\theta,
\quad B_m(\theta)=\begin{pmatrix}a&0\\0&b\end{pmatrix}\sum_{r=0}^mc_rU(\theta)^r,
\quad U(\theta)=\begin{pmatrix}0&e^{-i\theta}\\1&0\end{pmatrix}.
\tag{5}
\]
Choose an even block length \(B>2m\), with consecutive intervals \(I_k=\{kB,\ldots,(k+1)B-1\}\). Let \(Q_B\) denote the \(B\)-square within-block compression of \(A_m\) (it is identical for all blocks because the weights are two-periodic and \(B\) is even). The operator \(DA_m\) differs from \(H_B=\bigoplus_{k\ge1}(kB)^{-1}Q_B\) by three pieces: an operator of rank at most \(B\) from the first block, a trace-class within-block denominator error, and the cross-block band entries. Indeed, the trace norm of the within-block error is at most
\[
M\sum_{k\ge1}\sum_{r=0}^{B-1}\left|\frac1{kB+r+1}-\frac1{kB}\right|
\le M\sum_{k\ge1}\frac{B(B+1)}{2(kB)^2}<\infty.
\]
The cross-boundary piece is an orthogonal direct sum of rank-at-most-\(m\) pieces, each of norm no larger than \(M/(kB)\). Thus its counting function obeys \(\limsup_{\varepsilon\downarrow0}\varepsilon N(\varepsilon;R_B)\le mM/B\). By direct summation over \(k\),
\[
\lim_{\varepsilon\downarrow0}\varepsilon N(\varepsilon;H_B)=B^{-1}\|Q_B\|_1.
\]
Replace \(Q_B\) with the cyclic block matrix \(Z_B\) obtained by using the cyclic shift in the same polynomial. Their difference has rank at most \(m\), operator norm at most \(2M\), and trace norm at most \(2mM\). The length-\(B/2\) block Fourier transform diagonalizes \(Z_B\) into the matrices \(B_m(2\pi j/(B/2))\). Consequently
\[
\lim_{\substack{B\to\infty\\B\text{ even}}}B^{-1}\|Q_B\|_1
=\frac1{4\pi}\int_0^{2\pi}\operatorname{tr}|B_m(\theta)|\,d\theta.
\]
The singular-value counting inequalities \(N((1+\eta)\varepsilon;X+Y)\le N(\varepsilon;X)+N(\eta\varepsilon;Y)\), and their reverse comparisons, remove the boundary term by first sending \(B\) to infinity and then \(\eta\) to zero. A trace-class difference contributes \(o(\varepsilon^{-1})\). This proves (5), including \(m=0\).

**2. Geometric resolvent and the singular-index limit.** Since \(0\le t<1\), \(T_{t;a,b}=DW(I-tS)^{-1}\) and \(W(I-tS)^{-1}\) is the norm limit of the above band polynomials with \(c_r=t^r\). The tail after degree \(m\) has operator norm at most \(\delta_m=\max(a,b)t^{m+1}/(1-t)\). The singular-number product bound gives \(s_n(D(A-A_m))\le\delta_m/n\), so the upper counting coefficient of the discarded tail is at most \(\delta_m\). Applying the same counting comparison, then taking \(m\to\infty\) and the comparison tolerance to zero, extends (5) to the absolutely convergent matrix symbol
\[
B_t(\theta)=W_2(I-tU(\theta))^{-1}
=\frac1{1-t^2e^{-i\theta}}\begin{pmatrix}a&a t e^{-i\theta}\\bt&b\end{pmatrix},\qquad W_2=\operatorname{diag}(a,b).
\]
Thus \(\lim_{\varepsilon\downarrow0}\varepsilon N(\varepsilon;T_{t;a,b})=(4\pi)^{-1}\int\operatorname{tr}|B_t|\). For any complex \(2\)-square matrix \(B\), the sum of its singular values equals \(\sqrt{\operatorname{tr}(B^*B)+2|\det B|}\). In this case
\[
\operatorname{tr}(B_t^*B_t)=\frac{(a^2+b^2)(1+t^2)}{R_t^2},\qquad |\det B_t|=\frac{ab}{R_t}.
\]
This gives (1) at the counting-function level. Because the integral is strictly positive when \(a+b>0\), monotonicity of \(s_n\) converts the counting asymptotic to \(n s_n\to\mathcal C_t(a,b)\). Compactness follows from the compact diagonal factor \(D\). The product bound \(s_n(T)\le\max(a,b)/((1-t)n)\), together with the positive limit, proves the ideal assertions and logarithmic summation in (2).

**3. Optimal two-periodic profiles.** Write \(s=a+b\). The radicand in (1) is
\[
s^2(1+t^2)-2ab\bigl(1+t^2-R_t(\theta)\bigr).
\]
For \(0<t<1\), \(1+t^2-R_t(\theta)\) is positive except at \(\theta=\pi\) modulo \(2\pi\). The integral is therefore strictly decreasing in \(ab\) with \(s\) held fixed. Since \(0\le ab\le s^2/4\), balancing uniquely minimizes and placing all weight on one parity uniquely maximizes. For \(a=b=s/2\), the two Fourier channels simply unfold to the scalar symbol \((1-te^{i\varphi})^{-1}\), giving the first elliptic expression in (3). For \(ab=0\), the numerator in (1) becomes \(s\sqrt{1+t^2}\) and the elementary complete-elliptic evaluation of \(\int_0^{2\pi}R_t^{-1}\) gives the second expression. At \(t=0\), \(R_0=1\) and (1) is \(s/2\) identically. To get (3a), set \(q=t^2\) and expand \(R_t(\theta)=1-q\cos\theta+O(q^2)\) uniformly in angle. The integrand in (1) has angular average \(s+q(a^2+b^2)/(2s)+O(q^2)\). Thus \(\mathcal C_t(a,b)=s/2+(a^2+b^2)t^2/(4s)+O(t^4)\), and subtraction of the balanced case gives (3a).

**4. The exact endpoint finite part.** Set \(r=t^2\), \(\delta=1-r\), \(\beta=a^2+b^2\), and \(P=\sqrt{2\beta}\). Split the coefficient as
\[
\mathcal C_t(a,b)=\frac{P}{4\pi}\int_0^{2\pi}\frac{d\theta}{|1-re^{i\theta}|}
+\frac1{4\pi}\int_0^{2\pi}\frac{\sqrt{\beta(1+r)+2ab|1-re^{i\theta}|}-P}{|1-re^{i\theta}|}\,d\theta.
\]
The first integral equals \(4(1+r)^{-1}K(2\sqrt r/(1+r))=2\log(8/\delta)+o(1)\). In the second integral rationalize the numerator. Its absolute value is bounded uniformly as \(\delta\downarrow0\) because \(\delta\le|1-re^{i\theta}|\), and pointwise almost everywhere it converges to the integrand with \(r=1\). Dominated convergence, \(|1-e^{i\theta}|=2\sin(\theta/2)\), and the change \(u=\theta/2\) give precisely \(F(a,b)\). This proves (4). Under fixed \(a+b=s\), the leading factors are \(P=s\) when balanced and \(P=\sqrt2s\) at one-parity profiles, proving the sharp \(\sqrt2\) limit.

## Verification
The source code `check.py` performs independent finite-matrix singular-value comparisons with the block-symbol formula, checks the two extremal elliptic representations, evaluates the endpoint finite part, and tests finite-section singular values against the limiting coefficient. These are finite numerical consistency checks; Steps 1--4 above, not extrapolated computation, prove the infinite-dimensional and endpoint claims. Run with `python check.py` using Python, NumPy, and SciPy.

## Relationship to prior work
Albanese, Bonet, and Ricker (arXiv:2305.04805v1, first posted 8 May 2023) define and analyze the same scalar generalized Cesàro family, its compactness and its spectra, but do not study two-periodic row damping or sharp singular-number coefficients. A published later mathematical record, *Exact singular-value coefficient of generalized Cesàro operators on Hilbert space* (published-finding corpus, identifier `d56b622eed1d`), proves the special case \(a=b\) using a scalar Toeplitz counting lemma. That special case is prior work, not claimed as new. Finite-section Toeplitz singular-distribution theory (e.g. Ekström–Vassalos 2021 and older Avram–Parter-type results) motivates the block Fourier step but does not in the inspected statements assert the periodically damped compact-operator coefficient, its sharp fixed-budget anisotropy envelope, or the endpoint finite part. The present two-channel structure and its optimization are the claimed contribution, not the general existence of Toeplitz Fourier symbols. More general operator-symbol asymptotic theorems could imply portions of the formula; this remains a specific literature-priority risk.

## Limitations
The main coefficient is for exact period two, nonnegative real row multipliers, and fixed \(0\le t<1\); no uniformity in the singular index as \(t\uparrow1\) is asserted. The finite-part law describes the coefficient after taking the singular-index limit. The operator at \(t=1\), arbitrary longer periods, and second-order individual singular-value errors are outside scope. Generic matrix-valued asymptotic frameworks may subsume the Weyl-counting component; originality is claimed only for the combined explicit law, sharp extremal profiles, and endpoint finite part, subject to independent assessment.

## References
1. A. A. Albanese, J. Bonet and W. J. Ricker, *Spectral properties of generalized Cesàro operators in sequence spaces*, arXiv:2305.04805v1 (8 May 2023), https://arxiv.org/abs/2305.04805.
2. S.-E. Ekström and P. Vassalos, *A matrix-less method to approximate the spectrum and the spectral function of Toeplitz matrices with real eigenvalues*, *Numerical Algorithms* 89 (2022), 701–720; first online 24 June 2021, https://doi.org/10.1007/s11075-021-01130-9.
3. *Exact singular-value coefficient of generalized Cesàro operators on Hilbert space*, published published-finding corpus mathematical record, identifier `d56b622eed1d` (2026). Its scalar coefficient is prior coverage for balanced profiles.
4. H. Widom, *On the Singular Values of Toeplitz Matrices*, *Z. Anal. Anwend.* 8 (1989), 221–229, https://doi.org/10.4171/ZAA/350 (general finite-section context; not asserted to prove this compact-operator result).
