# Log-periodic Hilbert matrices have an exact Jacobi essential norm

## Finding

For every \(\omega>0\) and every real \(-1<\varepsilon<1\), define an operator on \(\ell^2(\mathbb N)\) by
\[
 (H_{\varepsilon,\omega}a)_k
 =\bigl(1+\varepsilon\cos(\omega\log k)\bigr)
 \sum_{n=1}^{\infty}\frac{a_n}{k+n},\qquad k\ge1.
\]
Put \(c_j=\pi\operatorname{sech}(\pi\omega j)\) for \(j\in\mathbb Z\), and let the compact, generally non-self-adjoint, bilateral Jacobi operator \(B_{\varepsilon,\omega}\) on \(\ell^2(\mathbb Z)\) be
\[
 (B_{\varepsilon,\omega}v)_j
 =c_jv_j+\frac{\varepsilon}{2}
 \bigl(c_{j-1}v_{j-1}+c_{j+1}v_{j+1}\bigr).
\]
**The exact essential norm is**
\[
 \boxed{\|H_{\varepsilon,\omega}\|_{\mathrm{ess}}
 =\|B_{\varepsilon,\omega}\|.}
\]
If \(P_N\) selects \(|j|\le N\), \(N\ge1\), this identity has the exponentially convergent, certified finite-section approximation
\[
 0\le\|H_{\varepsilon,\omega}\|_{\mathrm{ess}}
    -\|P_NB_{\varepsilon,\omega}P_N\|
 \le (1+|\varepsilon|)c_{N+1}
       +\frac{|\varepsilon|}{2}c_N.
\]
The resulting log-periodic essential norm satisfies, for \(0<|\varepsilon|<1\),
\[
 \pi\sqrt{1+\varepsilon^2/2}
 \le\|H_{\varepsilon,\omega}\|_{\mathrm{ess}}
 \le\pi(1+|\varepsilon|).
\]
Writing \(r_\omega=\operatorname{sech}(\pi\omega)\), its **sharp small-modulation curvature** is
\[
 \boxed{\|H_{\varepsilon,\omega}\|_{\mathrm{ess}}
 =\pi\left[1+
 \frac{1+3r_\omega^2}{4(1-r_\omega^2)}\varepsilon^2
 +O_\omega(\varepsilon^4)\right]\quad(\varepsilon\to0).}
\]
In particular, the quadratic inflation varies continuously with the logarithmic frequency, not just with the mean square of the multiplier.

## Assumptions and scope

The coefficient field is complex; \(\varepsilon\) is real and has absolute value strictly smaller than one, ensuring a positive output multiplier. The logarithm is natural. The operator acts on the usual unweighted Hilbert sequence space. Its essential norm is the distance in operator norm to the compact operators on this space. All identities concern these precisely specified row-modulated Hilbert matrices; no assertion about general \(\ell^p\) or arbitrary symbols is made. The remainder \(O_\omega(\varepsilon^4)\) is for fixed positive frequency and is not claimed uniform as \(\omega\downarrow0\).

## Proof

**1. A compact equivalence from the matrix to Carleman's integral.** Let \(\mathcal L=L^2([1/2,\infty))\), let \(I_k=[k-1/2,k+1/2)\), and let \(J:\ell^2(\mathbb N)\to\mathcal L\) send the \(k\)-th unit vector to \(\mathbf1_{I_k}\). Its range projection is the averaging operator \(P=JJ^*\). On \(\mathcal L\) put
\[
 (Cf)(x)=\int_{1/2}^\infty\frac{f(y)}{x+y}\,dy.
\]
This positive bounded Carleman compression has norm at most \(\pi\). Define \(\widetilde m(x)=1+\varepsilon\cos(\omega\log k)\) on \(I_k\). The matrix of \(PM_{\widetilde m}CP\) in the range of \(J\) has entries \(\widetilde m_k\int_{I_k}\int_{I_n}(x+y)^{-1}\,dy\,dx\). As \(|(x+y)-(k+n)|\le1\) on these cells and \(k+n\ge2\), the difference from the defining Hilbert matrix entry is \(O_{\varepsilon}((k+n)^{-2})\). Since
\[
 \sum_{k,n\ge1}(k+n)^{-4}<\infty,
\]
the two extensions to \(\mathcal L\) differ by a Hilbert--Schmidt operator.

We verify that \((I-P)C\) is compact, rather than asserting that stepwise averaging is norm-close to the identity. For bounded output \(x\), the kernel restricted to \(x\in[1/2,R]\), \(y\ge1/2\), is square-integrable, so the restricted operator is Hilbert--Schmidt. On \(x\ge R\), cellwise Poincaré and the derivative kernel \(\partial_x(x+y)^{-1}=-(x+y)^{-2}\) give
\[
 \|\mathbf1_{[R,\infty)}(I-P)C\|
 \le \left(\int_R^\infty\int_{1/2}^\infty(x+y)^{-4}\,dy\,dx\right)^{1/2}
 =O(R^{-1}).
\]
Here one may shift \(R\) by one cell to avoid splitting a cell, without changing the estimate. Thus \((I-P)C\) is compact, and so is its adjoint \(C(I-P)\). Since \(M_{\widetilde m}\) commutes with \(P\), the difference between \(PM_{\widetilde m}CP\) and \(M_{\widetilde m}C\) is compact. Finally put \(m(x)=1+\varepsilon\cos(\omega\log x)\). Uniform continuity of the log on large cells yields \(\widetilde m(x)-m(x)=O_{\varepsilon,\omega}(x^{-1})\) as \(x\to\infty\). Therefore \((M_{\widetilde m}-M_m)C\) is compact: truncate to bounded output \(x\) (Hilbert--Schmidt), while the norm of the remaining multiplier tends to zero. After extension by zero from \(J\ell^2\), we obtain the equality of essential norms
\[
 \|H_{\varepsilon,\omega}\|_{\mathrm{ess},\ell^2}
 =\|M_mC\|_{\mathrm{ess},\mathcal L}.
\]
Extending the matrix operator by zero does not change its essential norm: compress any compact approximation to the range of \(J\), and extend compact approximations in the reverse direction.

**2. Half-line and full-line logarithmic coordinates.** The unitary map \((Uf)(t)=e^{t/2}f(e^t)\) identifies \(\mathcal L\) with \(L^2([\log(1/2),\infty))\). It turns \(C\) into the restriction/compression of full-line convolution by
\[
 K(t)=\frac1{2\cosh(t/2)},\qquad
 \widehat K(\xi)=\frac{\pi}{\cosh(\pi\xi)},
\]
and changes \(m(x)\) into \(m_0(t)=1+\varepsilon\cos(\omega t)\). Write \(A=M_{m_0}(K*\cdot)\) on \(L^2(\mathbb R)\). The half-line compression has norm at most \(\|A\|\). Conversely, choose a compactly supported unit vector whose image under \(A\) nearly realizes \(\|A\|\), then translate it to the right by integer multiples of \(L=2\pi/\omega\). Periodicity leaves the full-line image norm unchanged, while omitted output left of the half-line tends to zero. The translations are weakly null, hence every compact operator sends them to vectors tending to zero. Consequently the half-line compression has essential norm exactly \(\|A\|\), and
\[
 \|H_{\varepsilon,\omega}\|_{\mathrm{ess}}=\|A\|.
\]

**3. A single Floquet fiber attains the norm.** Floquet decomposition by the period \(L\) decomposes \(A\) into fibers on one period, indexed by quasi-momentum \(\theta\). Their integral kernels are \(m_0(t)\sum_{q\in\mathbb Z}e^{iq\theta L}K(t-s+qL)\). Since \(K\ge0\) and \(m_0>0\), the absolute value of any fiber applied to a function is pointwise bounded by the zero-quasi-momentum fiber applied to its absolute value. Thus every fiber has norm at most that of the zero fiber, and continuity of the kernel in quasi-momentum shows that the direct-integral norm is achieved at \(\theta=0\). In the Fourier orthonormal basis \(e^{ij\omega t}/\sqrt L\), the zero fiber of convolution has eigenvalues \(c_j\), and multiplication by \(m_0\) couples only adjacent frequencies with coefficient \(\varepsilon/2\). Hence the zero fiber is exactly \(B_{\varepsilon,\omega}\), proving the boxed identity.

**4. Certified truncation and strict inflation.** Let \(D\) be the diagonal with entries \(c_j\), and \(X=(S+S^*)/2\) on \(\ell^2(\mathbb Z)\). Then \(B=(I+\varepsilon X)D\) is compact because \(c_j\to0\). For \(Q_N=I-P_N\),
\[
 \|BQ_N\|\le(1+|\varepsilon|)c_{N+1},
 \qquad\|Q_NBP_N\|\le |\varepsilon|c_N/2.
\]
The displayed finite-section error follows by \(B-P_NBP_N=BQ_N+Q_NBP_N\). Testing \(B\) on the zero-frequency vector gives \(\|Be_0\|=\pi\sqrt{1+\varepsilon^2/2}\), while \(\|B\|\le\|I+\varepsilon X\|\|D\|\le\pi(1+|\varepsilon|)\).

**5. Sharp second variation.** The positive compact operator governing the norm is
\[
 B^*B=D(I+2\varepsilon X+\varepsilon^2 X^2)D.
\]
At zero amplitude its top eigenvalue \(c_0^2=\pi^2\) is simple, separated from the remaining eigenvalues \(c_j^2\) because \(\omega>0\). Analytic perturbation applies. The direct second-order diagonal term is \(\langle e_0,DX^2De_0\rangle=\pi^2/2\). At first order the only nonzero couplings from \(e_0\) are to \(e_{\pm1}\), each of magnitude \(\pi c_1\), so the second-order eigenvalue correction from the reduced resolvent is
\[
 2\frac{\pi^2c_1^2}{\pi^2-c_1^2}.
\]
Thus the top eigenvalue equals \(\pi^2[1+(1/2+2r_\omega^2/(1-r_\omega^2))\varepsilon^2+O_\omega(\varepsilon^4)]\). The absence of odd powers follows from the unitary conjugation \(\operatorname{diag}((-1)^j)B_{\varepsilon,\omega}\operatorname{diag}((-1)^j)=B_{-\varepsilon,\omega}\). Taking the positive square root gives the stated sharp coefficient.

## Verification

The accompanying standalone program `check_spectral.py` constructs the explicitly defined finite Jacobi sections, compares their largest singular values with the perturbative coefficient for several positive frequencies, and checks the rigorous finite-section error estimate. Each numerical test is supplementary; the proof above establishes the infinite-dimensional statements. To run the checker, install the dependency from `requirements.txt` and invoke `python check_spectral.py` from the extracted package directory. The checker prints computed values, analytic curvatures, and bounds, and fails if its diagnostic assertions do not hold.

## Relationship to prior work

David Norrbo, *The essential norm, block sizes, and some generalized Hilbert operators on \(\ell^p\)* (arXiv:2609.13403v1, 11 September 2026), studies exactly this row-coefficient Hilbert family and gives essential-norm values under convergent local block means and comparisons in the general case. For \(\varepsilon\ne0\), the present coefficients are genuinely log-periodic and do not have a single limiting fine-block magnitude: a fixed multiplicative dilation by \(e^{\pi/\omega}\) flips the limiting oscillatory phase. The present theorem instead identifies their exact essential norm by a compact Jacobi operator and computes its frequency-sensitive curvature.

Pushnitski and Sobolev, *Hankel operators with band spectra and elliptic functions* (arXiv:2307.09242), analyze self-adjoint, dilation-periodic Hankel kernels \(p(\log(x+y))/(x+y)\) and develop Floquet methods. Those kernels differ from the present generally non-self-adjoint **output-row modulation** \(p(\log x)/(x+y)\); their published fiber formulas do not yield the asserted specific zero-fiber norm identity or quadratic coefficient by direct substitution. Jin, *Generalized Hilbert matrix operators acting on weighted sequence spaces* (arXiv:2504.19743), treats positive-measure-induced generalized matrices and boundedness/norm criteria, not the output-row log-periodic essential norm considered here. Classical Carleman Fourier transforms, compactness theory, and Floquet decomposition are tools, not claimed as new.

## Limitations

The proof relies on the Hilbert-space Fourier decomposition and on positivity of \(1+\varepsilon\cos(\omega t)\); extension to arbitrary complex amplitudes or \(\ell^p\) is not established. Its essential-norm formula does not determine discrete eigenvalues of the full matrix, nor the full essential spectrum. The fixed-frequency asymptotic is not uniform at zero frequency. Historical abstract operator-theory results for periodic Mellin/Wiener--Hopf operators could subsume parts of the reduction; a remaining literature-priority risk is acknowledged.

## References

1. D. Norrbo, *The essential norm, block sizes, and some Generalized Hilbert operators on \(\ell^p\)*, arXiv:2609.13403v1 (first public 11 September 2026), https://arxiv.org/abs/2609.13403.
2. A. Pushnitski and A. Sobolev, *Hankel operators with band spectra and elliptic functions*, arXiv:2307.09242, https://arxiv.org/abs/2307.09242.
3. J. Jin, *Generalized Hilbert matrix operators acting on weighted sequence spaces*, arXiv:2504.19743, https://arxiv.org/abs/2504.19743.
4. M. W. Wong, *Spectral Analysis of Strongly Carleman Pseudo-Differential Operators*, J. Lond. Math. Soc. (1980), DOI: 10.1112/jlms/s2-21.3.527 (abstract-level priority risk only).
