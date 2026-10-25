# Two-scale singular-spectrum law for polynomially weighted Dirichlet dilations

## Finding

Let \(\beta\in\mathbb R\), let \(n\ge1\) be an integer, and let \(P(z)=\sum_{j=0}^{d}p_jz^j\) be a nonzero complex polynomial (the genuinely coupled case has at least two nonzero coefficients). On the coefficient-normalized Dirichlet Hilbert space
\[
\mathcal D_\beta=\left\{f(z)=\sum_{k\ge0}c_kz^k:\ \|f\|_\beta^2=\sum_{k\ge0}(k+1)^{1-\beta}|c_k|^2<\infty\right\},
\]
set \(T_\varepsilon f(z)=P(z)f^{(n)}(e^{-\varepsilon}z)\) for \(\varepsilon>0\). Each \(T_\varepsilon\) is compact and belongs to every Schatten class \(\mathcal S_p\), \(p>0\). Put \(g(x)=x^ne^{-x}\), \(G=(n/e)^n\|P\|_{L^\infty(\mathbb T)}\), and let \(s_j(T_\varepsilon)\) denote singular values with multiplicities in decreasing order.

**(I) Coupled two-variable spectral law.** For every \(y>0\),
\[
\lim_{\varepsilon\downarrow0}\varepsilon\#\{j:\varepsilon^ns_j(T_\varepsilon)>y\}=
\frac1{2\pi}\int_0^{2\pi}\left|\left\{x>0:g(x)|P(e^{i\theta})|>y\right\}\right|\,d\theta.
\]
The right side is zero for \(y\ge G\). For \(0<y<G\), where \(a=|P(e^{i\theta})|>y/(n/e)^n\), the inner interval has length
\[
-nW_{-1}\!\left(-\frac{(y/a)^{1/n}}n\right)
+nW_0\!\left(-\frac{(y/a)^{1/n}}n\right),
\]
and otherwise length zero. Here \(W_0,W_{-1}\) are the two real Lambert branches.

**(II) Every Schatten exponent and the operator-norm edge.** For all real \(p>0\), including \(0<p<1\),
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{np+1}\|T_\varepsilon\|_{\mathcal S_p}^p
=\frac{\Gamma(np+1)}{p^{np+1}}\,\frac1{2\pi}\int_0^{2\pi}|P(e^{i\theta})|^p\,d\theta,
\]
and
\[
\lim_{\varepsilon\downarrow0}\varepsilon^n\|T_\varepsilon\|=(n/e)^n\|P\|_{L^\infty(\mathbb T)}.
\]
These leading laws are independent of the coefficient-space index \(\beta\), although the operators themselves depend on it.

**(III) First index-sensitive correction.** Define \(A_P=\sum_{j=0}^d|p_j|^2\) and \(B_P=\sum_{j=0}^dj|p_j|^2\). Then the full first two terms of the squared Hilbert--Schmidt norm are
\[
\varepsilon^{2n+1}\|T_\varepsilon\|_{\mathcal S_2}^2=
\frac{(2n)!}{2^{2n+1}}A_P
+\varepsilon\frac{(2n-1)!}{2^{2n}}
\left[n(n+\beta)A_P-(\beta-1)B_P\right]+o(\varepsilon).
\]
Thus the first correction detects the Dirichlet index and the coefficient-weighted mean polynomial degree, information absent from the universal leading symbol.

For example, on \(\mathcal D_1=H^2\), with \(n=1\) and \(P(z)=1+z\), the limits are \(\varepsilon\|T_\varepsilon\|\to2/e\), \(\varepsilon^2\|T_\varepsilon\|_{\mathcal S_1}\to4/\pi\), and \(\varepsilon^3\|T_\varepsilon\|_{\mathcal S_2}^2=1/2+\varepsilon+o(\varepsilon)\).

## Assumptions and scope

The domain and codomain are the **same** coefficient Hilbert space \(\mathcal D_\beta\), with the displayed exact norm, and the symbols \(P\), \(n\), \(\beta\) remain fixed as \(\varepsilon\downarrow0\). The contraction is precisely \(z\mapsto e^{-\varepsilon}z\); differentiation occurs **before** composition. The polynomial may have arbitrary degree and complex coefficients. The pointwise counting limit holds for each fixed \(y>0\), not uniformly down to \(y=0\); there are infinitely many singular values tending to zero. No assertion about individual fixed-rank subleading eigenvalues is made.

## Proof

**1. Exact banded coefficients and a negligible error.** The vectors \(e_k(z)=(k+1)^{(\beta-1)/2}z^k\) form an orthonormal basis. For \(k<n\), \(T_\varepsilon e_k=0\). For \(k\ge n\),
\[
\varepsilon^nT_\varepsilon e_k=\sum_{j=0}^d p_j a_\varepsilon(k)
\left(\frac{k+1}{k-n+j+1}\right)^{(\beta-1)/2}e_{k-n+j},\qquad
 a_\varepsilon(k)=\varepsilon^n\frac{k!}{(k-n)!}e^{-\varepsilon(k-n)}.
\]
Identify this basis with \(\ell^2(\mathbb N_0)\), let \(S\) be its ordinary unilateral shift, and set \(D_\varepsilon e_k=a_\varepsilon(k)e_k\) for \(k\ge n\) (zero otherwise). Define \(B_\varepsilon=P(S)S^{*n}D_\varepsilon\) and \(A_\varepsilon=\varepsilon^nT_\varepsilon\). Because \(\left((k+1)/(k-n+j+1)\right)^{(\beta-1)/2}=1+O((k+1)^{-1})\), with constants depending only on the fixed data, the finite-band error \(E_\varepsilon=A_\varepsilon-B_\varepsilon\) satisfies
\[
\|E_\varepsilon\|=O(\varepsilon),\qquad
\varepsilon\|E_\varepsilon\|_{\mathcal S_q}^{q}=O(\varepsilon^{q})\quad(q>0).
\]
Indeed each error diagonal has magnitude at most \(C\varepsilon^nk^{n-1}e^{-\varepsilon(k-n)}\) for large \(k\), and its finite initial segment is \(O(\varepsilon^n)\). A single partial-shift diagonal has Schatten \(q\)-quasi-power equal to the sum of its coefficient \(q\)-powers. Finite-sum Schatten inequalities give the displayed bound for all \(q>0\). The same calculation, without the extra reciprocal power of \(k\), gives
\[
\sup_{0<\varepsilon<1}\varepsilon\|A_\varepsilon\|_{\mathcal S_q}^q<\infty
\quad\text{and}\quad \sup_{0<\varepsilon<1}\|A_\varepsilon\|<\infty
\quad(q>0).
\]
This also proves compactness and all-Schatten membership for fixed \(\varepsilon>0\).

**2. Trace moments of a slowly varying band matrix.** The Gram operator \(B_\varepsilon^*B_\varepsilon\) has bandwidth at most \(d\). Apart from finitely many boundary indices, its \((k,k+h)\) entry equals \(a_\varepsilon(k)a_\varepsilon(k+h)\) times the autocorrelation coefficient of \(P\) at displacement \(h\), and it vanishes for \(|h|>d\). For each fixed integer \(m\ge1\), the diagonal of its \(m\)-th power is a finite sum over closed index walks with increments between \(-d\) and \(d\). For \(k=\lfloor x/\varepsilon\rfloor\), \(x>0\), and any such fixed walk, all the factors \(a_\varepsilon(k+h)\) tend to \(g(x)=x^ne^{-x}\). The sum over closed walks is the constant Fourier coefficient of \(|P(e^{i\theta})|^{2m}\). Exponential tail bounds and a Riemann sum therefore give
\[
\lim_{\varepsilon\downarrow0}\varepsilon\operatorname{Tr}
(B_\varepsilon^*B_\varepsilon)^m
=\frac1{2\pi}\int_0^{2\pi}|P(e^{i\theta})|^{2m}\,d\theta
\int_0^\infty x^{2nm}e^{-2mx}\,dx.
\]
This argument explicitly includes \(k\) near zero (negligible after multiplying by \(\varepsilon\)) and the exponentially decaying upper tail.

**3. Spectral distribution and quasi-Schatten powers.** The operators \(B_\varepsilon\) are uniformly bounded and have \(\varepsilon\operatorname{Tr}(B_\varepsilon^*B_\varepsilon)=O(1)\). For a continuous function \(F\) supported away from zero, approximate \(F(\sqrt t)/t\) uniformly by polynomials on the bounded spectrum and use Step 2. This proves convergence of \(\varepsilon\sum_jF(s_j(B_\varepsilon))\) to the integral of \(F(g(x)|P(e^{i\theta})|)\). Every positive level set has limiting measure zero: for each fixed \(\theta\), \(x^ne^{-x}|P(e^{i\theta})|=y>0\) has at most two solutions in \(x>0\). Thus positive-threshold counts converge. The perturbation \(E_\varepsilon\) does not change the limit: singular-value counting inequalities bound the change in any threshold count using \(\#\{j:s_j(E_\varepsilon)>\eta\}\le\eta^{-q}\|E_\varepsilon\|_{\mathcal S_q}^q\), and \(\varepsilon\|E_\varepsilon\|_{\mathcal S_q}^q\to0\).

For every \(p>0\), choose \(0<q<p\). By Step 1,
\[
\varepsilon\sum_{s_j(A_\varepsilon)<\eta}s_j(A_\varepsilon)^p
\le \eta^{p-q}\varepsilon\|A_\varepsilon\|_{\mathcal S_q}^q,
\]
so small singular values contribute uniformly negligibly as \(\eta\downarrow0\); large values are uniformly bounded. Integrating the established positive-threshold distribution yields the claimed Schatten \(p\)-moment and evaluates its radial integral as \(\Gamma(np+1)/p^{np+1}\), valid equally for \(p<1\). Solving \(x^ne^{-x}=y/|P(e^{i\theta})|\) using the two real Lambert branches gives the stated counting profile.

**4. Norm edge.** Since \(\|P(S)\|=\max_{|z|=1}|P(z)|\) and \(\|D_\varepsilon\|\to\max_{x\ge0}g(x)=(n/e)^n\), Step 1 gives the upper bound. For a maximizing angle \(\theta\), take unit plane-wave vectors of length \(L_\varepsilon=\lfloor\varepsilon^{-1/2}\rfloor\), supported on indices near \(n/\varepsilon\), with phase chosen to realize \(P(e^{i\theta})\). The weight \(D_\varepsilon\) is asymptotically constant on this block, and its finitely many shifted boundary coordinates carry vanishing mass. Hence \(\liminf\|B_\varepsilon\|\ge(n/e)^n\|P\|_\infty\); Step 1 transfers this to \(A_\varepsilon\).

**5. First Hilbert--Schmidt correction.** Orthogonality of the different monomial outputs in each column gives the exact identity
\[
\|T_\varepsilon\|_{\mathcal S_2}^2=\sum_{j=0}^d|p_j|^2\sum_{k=n}^\infty
\left(\frac{k!}{(k-n)!}\right)^2e^{-2\varepsilon(k-n)}
\left(\frac{k+1}{k-n+j+1}\right)^{\beta-1}.
\]
For fixed \(n,\beta,j\), as \(k\to\infty\), the product of the nonexponential factors equals
\[
k^{2n}\left[1+\frac{(\beta-1)(n-j)-n(n-1)}k+O(k^{-2})\right].
\]
The finitely many small-\(k\) contributions are \(o(\varepsilon)\) after multiplying by \(\varepsilon^{2n+1}\). The integrated \(O(k^{-2})\) remainder is \(O(\varepsilon^2)\). Using the smooth trapezoidal/Riemann expansions
\[
\varepsilon^{2n+1}\sum_{k\ge1}k^{2n}e^{-2\varepsilon k}
=\frac{(2n)!}{2^{2n+1}}+O(\varepsilon^2),\quad
\varepsilon^{2n+1}\sum_{k\ge1}k^{2n-1}e^{-2\varepsilon k}
=\varepsilon\frac{(2n-1)!}{2^{2n}}+O(\varepsilon^2),
\]
and \(e^{2n\varepsilon}=1+2n\varepsilon+O(\varepsilon^2)\), the coefficient of \(\varepsilon\) simplifies to \((2n-1)!2^{-2n}[n(n+\beta)A_P-(\beta-1)B_P]\). This proves (III).

## Verification

The accompanying `verify.py` independently reconstructs exact basis entries using rational arithmetic and checks finite matrix singular values for the coupled two-term example. It also checks the first Hilbert--Schmidt correction across four parameter choices and several small positive \(\varepsilon\). Run `python verify.py` with Python 3, NumPy and SciPy installed. A successful execution reports the number of supplementary finite checks. These finite checks cannot verify the limiting quantifiers; Steps 1--5 contain the infinite-dimensional proof.

## Relationship to prior work

Barik, Sen and Paul (arXiv:2605.00213, first version April 30, 2026) characterize boundedness, compactness and Hilbert--Schmidt membership on weighted Dirichlet spaces and calculate ordinary norms for special unweighted differentiation-composition symbols. Sun and Liu (arXiv:2610.19658, October 14, 2026), especially Theorem 9.2, determine exact singular values for **monomial** weights and linear composition symbols; their wider trace-ideal results yield membership and comparisons, not the formulas (I)--(III) for coupled polynomial weights. The classical generalized locally Toeplitz framework predicts leading distributions for appropriately truncated slowly varying band matrices; the bulk-limit method here is related to that framework and is not claimed as a new general spectral-distribution principle. The exact infinitely supported operator-family specialization, all positive Schatten exponents, and particularly the explicit index-sensitive first correction in (III) are the assessed combined contribution. This has not been independently established as publication-priority novel.

## Limitations

All asymptotics fix \(\beta,n,P\) while \(\varepsilon\downarrow0\). The operator norm and Schatten formulas are leading order except for the explicitly stated Hilbert--Schmidt correction; no error rate for the counting function, no other Schatten correction, and no extension to nonpolynomial weights are asserted. The leading distribution is a specialization of known locally Toeplitz machinery, and additional older applications or asymptotic expansions may contain overlapping results. Independent mathematical verification and comprehensive publication-priority certification have not been performed.

## References

1. S. Barik, A. Sen and K. Paul, *Weighted Composition-differentiation operators on weighted Dirichlet spaces*, arXiv:2605.00213v1 (April 30, 2026); relevant revised full text arXiv:2605.00213v2, Sections 5, 7 and 8.
2. J. Sun and J. Liu, *Weighted composition--differentiation operators on mixed-norm, derivative Hardy and F(p,q,s) spaces*, arXiv:2610.19658v1 (October 14, 2026), especially Section 9.2 and Theorem 9.2.
3. C. Garoni and S. Serra-Capizzano, *Generalized Locally Toeplitz sequences: a review and an extension*, 2017, for the classical local-symbol spectral-distribution framework.
4. B. Simon, *Trace Ideals and Their Applications*, second edition, 2005, for Schatten ideal and singular-value inequalities.
