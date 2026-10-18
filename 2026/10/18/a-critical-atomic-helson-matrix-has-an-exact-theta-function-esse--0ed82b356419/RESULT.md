# A critical atomic Helson matrix has an exact theta-function essential band

## Finding
For every fixed \(b>1\), \(\delta>0\), and \(\beta>0\), define a positive finite atomic measure
\[
\mu_\beta=2\delta\sum_{j=1}^{\infty}b^{-\beta j}\,\delta_{s_j},\qquad s_j=\tfrac12+\delta b^{-j},
\]
where \(\delta_{s_j}\) denotes unit mass at \(s_j\). Its positive Helson form on the finitely supported vectors in \(\ell^2(\mathbb N)\) is
\[
h_\beta[x,y]=\sum_{m,n\ge1}\alpha_\beta(mn)x_n\overline{y_m},\qquad
\alpha_\beta(t)=2\delta\sum_{j\ge1}b^{-\beta j}t^{-s_j}.
\]
There is a sharp operator-class trichotomy: the form yields a positive trace-class operator for \(\beta>1\), a bounded but noncompact operator for \(\beta=1\), and no bounded operator for \(0<\beta<1\). At the critical exponent let \(\eta=b^{-1/2}\), and define
\[
\vartheta_3(0,\eta)=1+2\sum_{r=1}^{\infty}\eta^{r^2},\qquad
\vartheta_4(0,\eta)=1+2\sum_{r=1}^{\infty}(-1)^r\eta^{r^2}.
\]
Then the *exact positive essential spectrum*, in the Weyl/Fredholm sense, is
\[
\boxed{\sigma_{\mathrm{ess}}(H_1)\cap(0,\infty)
=\big[\vartheta_4(0,\eta)^2,\,\vartheta_3(0,\eta)^2\big].}
\]
In particular, \(\|H_1\|_{\mathrm{ess}}=\vartheta_3(0,\eta)^2\); the nondegenerate positive band depends on \(b\) but not on \(\delta\). At \(b=2\), the endpoints are approximately \(0.0000237448480108\) and \(9.06472028366994\).

## Assumptions and scope
The underlying Hilbert space is the complex \(\ell^2(\mathbb N)\) with indices beginning at one. Parameters \(b>1\), \(\delta>0\) are fixed independently of \(\beta>0\). For an unbounded form, saying there is no bounded extension means that no bounded operator has this quadratic form on all finitely supported vectors. Essential spectrum refers to non-Fredholm spectral parameters of the bounded critical operator. The theorem deliberately gives its *positive* essential spectrum, without classifying zero or isolated eigenvalues. The other two phases are auxiliary context for the critical spectral result.

## Proof
**1. Gram reduction.** For each \(j\ge1\), put \(u_j=(n^{-s_j})_{n\ge1}\in\ell^2(\mathbb N)\). On finitely supported vectors the form is
\[
h_\beta[x,x]=\sum_{j\ge1}2\delta b^{-\beta j}|\langle x,u_j\rangle|^2.
\]
The sum converges for each such vector because \(\sum_j 2\delta b^{-\beta j}<\infty\) and \(|\langle x,u_j\rangle|\le\sum_{n\in\mathrm{supp}(x)}|x_n|\). Moreover
\[
\|u_j\|^2=\sum_{n\ge1}n^{-2s_j}
=\zeta(1+2\delta b^{-j})
\sim\frac{b^j}{2\delta}\quad(j\to\infty).
\]
For \(\beta>1\), the sum \(\sum_j2\delta b^{-\beta j}\|u_j\|^2\) converges. Thus \(H_\beta=\sum_j 2\delta b^{-\beta j}|u_j\rangle\langle u_j|\) converges absolutely in trace norm, giving a positive trace-class operator. If \(0<\beta<1\), positivity implies for every \(j\) that the form dominates the rank-one form \(2\delta b^{-\beta j}|\langle x,u_j\rangle|^2\). Its norm is \(2\delta b^{-\beta j}\|u_j\|^2\sim b^{(1-\beta)j}\to\infty\). Finite truncations of the unit vector \(u_j/\|u_j\|\) show that no uniform bounded quadratic-form constant exists on the finitely supported domain.

**2. Critical Toeplitz model modulo trace class.** Take \(\beta=1\), and for finite sequences \(c\in\ell^2(\mathbb N_j)\) define
\[
(Mc)_n=\sum_{j\ge1}\sqrt{2\delta}\,b^{-j/2}n^{-s_j}c_j.
\]
The column Gram matrix is initially defined algebraically by
\[
G_{jk}=(M^*M)_{jk}=2\delta b^{-(j+k)/2}
\zeta\big(1+\delta(b^{-j}+b^{-k})\big).
\]
Write \(g(t)=\zeta(1+t)-t^{-1}\), continuously extended by \(g(0)=\gamma_{\mathrm E}\). Since \(g\) is bounded on \([0,2\delta/b]\),
\[
G_{jk}=c_{j-k}+E_{jk},\quad
c_h=\frac{2}{b^{h/2}+b^{-h/2}}
=\operatorname{sech}\!\left(\tfrac12|h|\log b\right),\quad
E_{jk}=2\delta b^{-(j+k)/2}
 g\big(\delta(b^{-j}+b^{-k})\big).
\]
Here \(\sum_{j,k\ge1}|E_{jk}|<\infty\), so \(E\) is trace class: its absolutely convergent expansion in matrix units converges in trace norm. The coefficients \(c_h\) are in \(\ell^1(\mathbb Z)\), making the half-line Toeplitz matrix \(T_c=(c_{j-k})_{j,k\ge1}\) bounded. It follows that \(G=T_c+E\) is bounded and positive. The column-defined \(M\) consequently extends to a bounded operator, and \(H_1=MM^*\) agrees on finite vectors with the Helson form. Its companion \(G=M^*M\) has the same nonzero spectral values and multiplicities, via the polar decomposition of \(M\). In particular, their essential spectra agree at every strictly positive number.

**3. The whole positive essential band.** Let the continuous real Fourier symbol of \(T_c\) be
\[
F_b(\theta)=\sum_{h\in\mathbb Z}c_h e^{ih\theta}
=1+2\sum_{h=1}^{\infty}
\frac{2\eta^h}{1+\eta^{2h}}\cos(h\theta),\qquad \eta=b^{-1/2}.
\]
The elementary Fourier quadratic form identity gives \(\min F_b\,I\le T_c\le\max F_b\,I\). Conversely, for any \(\theta\), unit plane-wave segments supported on successive far-out blocks of increasing lengths constitute a Weyl sequence for \(T_c\) at \(F_b(\theta)\): this follows first for a finite-support convolution kernel from the vanishing fraction of boundary entries, and then for the absolutely summable kernel by uniform norm approximation. Hence
\[
\sigma_{\mathrm{ess}}(T_c)=F_b([0,2\pi])
=[\min_\theta F_b(\theta),\max_\theta F_b(\theta)].
\]
Weyl's compact perturbation theorem transfers this to \(G\). With Jacobi's elliptic nome \(\eta\), complete elliptic integral \(K\), and modulus \(0<k<1\), the Fourier series for the Jacobi function \(\operatorname{dn}\) gives
\[
F_b(\theta)=\frac{2K}{\pi}\operatorname{dn}\left(\frac{K\theta}{\pi},k\right).
\]
The function \(\operatorname{dn}(u,k)\) decreases from \(1\) to the complementary modulus \(k'\) as \(u\) runs from \(0\) to \(K\), and is symmetric on a full period. The standard identities \(2K/\pi=\vartheta_3(0,\eta)^2\) and \(k'=\vartheta_4(0,\eta)^2/\vartheta_3(0,\eta)^2\) therefore give precisely
\[
\min F_b=\vartheta_4(0,\eta)^2>0,
\qquad \max F_b=\vartheta_3(0,\eta)^2.
\]
Thus the positive essential spectrum of \(H_1\) is the stated nondegenerate interval. Positivity and the spectral description show its essential norm equals the upper endpoint (possible inclusion of zero does not affect this maximum).

## Verification
The independent computational check supplied as `check.py` evaluates the Gram-to-Toeplitz identity, the Jacobi theta endpoints against direct Fourier summation, and finite-block near-symbol Rayleigh quotients for several geometric ratios. Numerical checks test constants but do not establish compactness, Fredholm essential spectrum, or the infinite-parameter trichotomy; those assertions follow from the proof above. Reproduction: run `python check.py` in a Python environment with `mpmath` available.

## Relationship to prior work
Ma, Lu and Zu's 2026 work develops the moment-operator theory and trace-class characterization for positive Helson forms. Perfekt and Pushnitski's earlier work gives general nonnegativity and boundedness characterizations. Neither accessible source statement supplies an explicit positive essential band for the critical *geometric atomic* measure above. An earlier geometric-atomic model with extra mass damping \(j^{-r}\), \(r>0\), has a compact spectral asymptotic governed by the hyperbolic-secant Fourier symbol; its positive-damping conclusion does not determine the undamped \(r=0\) essential spectrum. This theorem identifies the structurally different, noncompact critical endpoint and its exact theta-function band. The classical Toeplitz and Jacobi Fourier tools are not claimed as new.

## Limitations
The full text of the motivating October 2026 preprint was not accessible for a definitive line-by-line priority comparison; its available abstract was reviewed. General weighted sampling and Carleson-measure literature may contain equivalent spectral descriptions. The present result does not describe the multiplicity of any isolated eigenvalues or determine whether zero belongs to the essential spectrum. The trichotomy is for the specific two-parameter geometric atomic family, not arbitrary measures; the result is subject to independent specialist verification.

## References
1. T. Ma, Y. Lu and C. Zu, *Unbounded Helson Forms with a Moment Representation*, arXiv:2610.12252v1 (first posted 2026-10-08), https://arxiv.org/abs/2610.12252.
2. K.-M. Perfekt and A. Pushnitski, *On Helson matrices: moment problems, non-negativity, boundedness, and finite rank*, arXiv:1611.03772, https://arxiv.org/abs/1611.03772.
3. NIST Digital Library of Mathematical Functions, §§22.2 and 22.11, including formulas 22.2.2 and 22.11.3, https://dlmf.nist.gov/22.2 and https://dlmf.nist.gov/22.11.
