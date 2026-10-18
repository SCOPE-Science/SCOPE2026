# A sharp two-outlier window for odd cubic harmonic-Bergman Toeplitz operators

## Finding
Let \(\mathcal H_h^2(\mathbb D)\) be the complex harmonic Bergman space of the unit disk with normalized area measure, and let \(\mathbb T_{p_a}=P_hM_{p_a}|_{\mathcal H_h^2}\) have analytic symbol \(p_a(z)=z^3+az\), where \(a\in\mathbb C\). Set
\[
r_*=\frac{14+2\sqrt{13}}9,
\qquad E_a=p_a(\partial\mathbb D).
\]
Then its **entire spectrum**, including all possible isolated eigenvalues, is
\[
\sigma(\mathbb T_{p_a})=
\begin{cases}
E_a\cup\left\{\dfrac{3a}{8}\sqrt{-a},-\dfrac{3a}{8}\sqrt{-a}\right\},&r_*<|a|<4,\\[3pt]
E_a,&|a|\le r_*\ \text{or}\ |a|\ge4.
\end{cases}
\]
The unordered two-point set does not depend on the choice of square-root branch. In the open window these points lie outside \(E_a\), are isolated eigenvalues, and each has geometric multiplicity one. At both endpoint values they merge into \(E_a\), rather than surviving as isolated outliers. In particular, the exact number of spectral points outside the essential curve is **two or zero**. The spectrum is disconnected exactly in the open window.

## Assumptions and scope
The harmonic Bergman space consists of complex-valued harmonic functions on \(\mathbb D\) square-integrable with respect to \(dA(z)=\pi^{-1}dx\,dy\). Its Toeplitz operator is orthogonal harmonic projection of multiplication by the bounded polynomial symbol. The conclusion applies to every complex parameter \(a\), without assuming the operator is normal. Its essential spectrum is \(p_a(\partial\mathbb D)\), and outside this curve the Fredholm index is zero, by the standard harmonic-Bergman Toeplitz Fredholm theorem [2]. The public motivating source [1] first appeared on 2026-10-07.

## Proof
**1. Reduction to a nonnegative parameter.** The disk rotation \(U_\theta f(z)=f(e^{i\theta}z)\) is unitary on harmonic Bergman space, and
\[
U_\theta\mathbb T_{p_a}U_\theta^{-1}
=e^{3i\theta}\mathbb T_{z^3+a e^{-2i\theta}z}.
\]
For \(a\ne0\), choosing \(2\theta=\arg a\) reduces the spectral problem to \(a=t=|a|>0\). At the end rotate the eigenvalues back. For \(a=0\), \(p_a=z^3\); the classical monomial result or the all-roots-in/all-roots-out argument below yields only the unit circle.

**2. Finite zero-matching criterion.** Fix \(t>0\), put \(p(z)=z^3+tz\), and take \(\lambda\notin p(\partial\mathbb D)\). The Fredholm-index-zero statement implies that \(\lambda\) is spectral exactly when \(\mathbb T_{p-\lambda}\) has nonzero kernel. Splitting a harmonic vector into analytic and coanalytic summands (with the analytic summand vanishing at zero) and applying the Bergman reproducing-kernel projection gives the following criterion; it is also the specialization of [1, equations (3.2)–(3.6)]. Write
\[
h(z,w)=z^2+\frac32zw+\frac32w^2+t.
\]
When \(p-\lambda\) has \(N\) distinct roots \(\alpha_1,\ldots,\alpha_N\) in the open disk, the coanalytic component of a kernel vector is a linear combination of \(k_{\alpha_j}(\bar z)=(1-\alpha_j\bar z)^{-2}\). The analytic component is
\[
f(z)=-\frac{z\sum_{j=1}^Nc_jh(z,\alpha_j)}{p(z)-\lambda}.
\]
It belongs to analytic Bergman space if and only if every pole at an interior root is removable. For \(N=1,2\), this is precisely the singularity of the matrix \(\bigl[h(\alpha_i,\alpha_j)\bigr]\). No kernel exists for \(N=0\). For \(N=3\) and \(\lambda\ne0\), removability forces the degree-at-most-two polynomial \(B(z)=\sum_jc_jh(z,\alpha_j)\) to vanish at three roots, hence to vanish identically; its coefficient Vandermonde map forces every \(c_j=0\). If \(\lambda=0\), zero itself is one of the roots, the condition \(f(0)=0\) additionally forces \(B(0)=0\), and cancellation at the remaining roots again forces \(B=0\). This covers three roots counted with multiplicity, using the corresponding Hermite derivative conditions. The coefficient map remains nonsingular for confluent roots.

**3. The one-interior-root alternatives.** With a single interior root \(\alpha\), the criterion reads
\[
h(\alpha,\alpha)=4\alpha^2+t=0.
\]
Thus \(\alpha=\pm i\sqrt t/2\) and
\[
\lambda=p(\alpha)=\frac{3t}{4}\alpha
=\pm i\frac{3t^{3/2}}8.
\]
The other two roots of \(p(z)-\lambda\) have moduli
\[
\frac{\sqrt{13}-1}{4}\sqrt t,
\qquad
\frac{\sqrt{13}+1}{4}\sqrt t.
\]
Consequently exactly the displayed candidate root is inside \(\mathbb D\), with the other two strictly outside, if and only if
\[
\frac{\sqrt t}{2}<1
\quad\text{and}\quad
\frac{\sqrt{13}-1}{4}\sqrt t>1,
\]
which is equivalent to \(r_*<t<4\). Here the numerator factors as \(h(z,\alpha)=(z-\alpha)(z+\tfrac52\alpha)\); the displayed formula for \(f\) has poles only outside \(\overline{\mathbb D}\) and therefore gives a genuine kernel vector. Its coanalytic part is a one-dimensional kernel, proving geometric multiplicity one. At \(t=r_*\) or \(4\), a root lies on \(\partial\mathbb D\), so the candidate belongs to the essential curve and is not an additional isolated spectral point.

**4. Two distinct interior roots cannot produce an eigenvalue.** If \(u,v\) are two distinct roots in \(\mathbb D\), direct expansion gives
\[
\det\!\begin{pmatrix}h(u,u)&h(u,v)\\h(v,u)&h(v,v)\end{pmatrix}
=-\frac34(u-v)^2\bigl(-2t+2u^2+9uv+2v^2\bigr).
\]
Put \(s=u+v\) and \(q=uv\). The remaining root is \(-s\) and Vieta gives \(q-s^2=t\). Vanishing of the determinant would require \(2s^2+5q-2t=0\), hence \(7s^2+3t=0\). Consequently
\[
|s|=\sqrt{\frac{3t}{7}},\quad
\{|u|,|v|\}=
\left\{\frac{\sqrt{19}-\sqrt3}{2\sqrt7}\sqrt t,
\frac{\sqrt{19}+\sqrt3}{2\sqrt7}\sqrt t\right\}.
\]
The larger of these two moduli is strictly greater than \(|s|\). Since the third root \(-s\) must lie outside the closed disk when exactly two roots are inside, it is impossible for both \(u,v\) to be interior. Therefore no two-root candidate occurs.

**5. Repeated roots do not introduce exceptions.** If \(p-\lambda\) has a double root \(\alpha\), then \(p'(\alpha)=0\), so \(3\alpha^2+t=0\), and
\[
p(z)-\lambda=(z-\alpha)^2(z+2\alpha).
\]
For a double root in \(\mathbb D\) and a third root outside, the coanalytic kernel is spanned by the ordinary kernel \(K_{\bar\alpha}\) and its parameter derivative. Removability to order two is equivalent to a zero determinant of the confluent matrix
\[
\begin{pmatrix}
 h(\alpha,\alpha)&\partial_wh(\alpha,\alpha)\\
 \partial_zh(\alpha,\alpha)&\partial_z\partial_wh(\alpha,\alpha)
\end{pmatrix}.
\]
Its determinant equals \(19t/4\ne0\), so there is no kernel. If all three roots are interior, the degree argument in Step 2 excludes a kernel. If none is interior, invertibility is immediate. Root-on-circle cases are already in \(p(\partial\mathbb D)\). This exhausts all multiple-root possibilities for \(t>0\). The case \(t=0\) was handled in Step 1.

Combining the cases and reversing the unitary rotation completes the spectral classification. At \(t=r_*\), the smaller exterior root reaches the circle, whereas at \(t=4\), the eigenfunction kernel root itself reaches the circle. Thus both interval boundaries are sharp.

## Verification
The accompanying `check.py` uses symbolic algebra to independently expand the two-root determinant, the one-root numerator factorization, the confluent determinant, the critical cubic factorization, and the exact threshold identity. Six rational parameter samples on both sides of the transitions exercise the root-modulus inequalities. Run `python check.py` after installing the dependency in `requirements.txt`. These checks verify algebraic reduction and sample ordering, not the infinite-dimensional Fredholm premise; the latter is an explicit cited theorem and the analytic kernel argument is given above.

## Relationship to prior work
Huang, Wang, and Zhao [1, Theorem 3.1] prove that every analytic-polynomial harmonic-Bergman Toeplitz spectrum is the essential curve plus finitely many eigenvalues, with an upper bound of \((n-1)2^{n-1}\); their full accessible text provides the zero-matching matrix but does not state the present sharp two-threshold classification. At cubic degree their general counting bound is eight, whereas this natural odd-cubic family has exactly zero or two additional points. Wang and Zhao [3] previously treated Weyl's theorem for polynomials through degree three and exhibited a quadratic disconnected-spectrum example; the full 2021 text could not be consulted here. The result is a specific exact phase diagram, not a claim to the general Fredholm criterion or general finiteness theory.

## Limitations
The classification is restricted to the sparse odd cubic symbols \(z^3+az\) on the unweighted complex harmonic Bergman space. It does not classify arbitrary cubic coefficients or multiplicities on the essential curve. It establishes geometric but not algebraic multiplicity of the isolated eigenvalues. The 2021 primary predecessor was not available in full, leaving a residual publication-priority risk; no independent audit has been performed.

## References
[1] M. Huang, J. Wang, X. Zhao, *The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space*, arXiv:2610.09638 (first posted 2026-10-07), https://arxiv.org/abs/2610.09638.

[2] K. Guo and D. Zheng, *Toeplitz algebra and Hankel algebra on the harmonic Bergman space*, J. Math. Anal. Appl. **276** (2002), 213–230, https://doi.org/10.1016/S0022-247X(02)00429-8.

[3] C. Wang and X. Zhao, *Weyl's theorem for Toeplitz operators with polynomial symbols on the harmonic Bergman space*, J. Math. Anal. Appl. **495** (2021), 124770, https://doi.org/10.1016/j.jmaa.2020.124770.
