# A gamma-convolution spectral law for shrinking product collars on symmetrized polydiscs

## Finding

Let \(d\ge2\), \(\alpha>-1\), \(p=\alpha+1\), and \(a>0\). On the weighted analytic Bergman space of the symmetrized polydisc \(\mathbb G_d\), let \(\mathcal P_N\) be the holomorphic polynomials of ordinary degree at most \(N\) in the lift variables. Equivalently, \(\mathcal P_N\) is the span of the Schur functions indexed by partitions \(\nu=(\nu_1\ge\cdots\ge\nu_d\ge0)\) with \(\sum_i\nu_i\le N\). For \(\beta>0\) let \(T_{N,\beta}(a)\) be the positive compression to \(\mathcal P_N\) of the indicator of the product collar
\[
\Omega_{N,\beta}(a)=\left\{w\in\mathbb G_d:|w_d|^2\le \exp(-a/N^\beta)\right\},
\]
where \(w_d\) is the final elementary-symmetric coordinate, namely the product of the \(d\) original disk coordinates. (The set is the *complement of the outermost product collar*.)

Write
\[
\Sigma_d=\left\{u_1>u_2>\cdots>u_d>0:\ \sum_{i=1}^d u_i<1\right\},\qquad |\Sigma_d|=(d!)^{-2}.
\]
For \(\boldsymbol u\in\Sigma_d\), take independent \(G_i\) with gamma shape \(p\) and unit rate, and set
\[
F_{p,d}(a;\boldsymbol u)=\Pr\!\left\{\sum_{i=1}^d\frac{G_i}{u_i}\ge a\right\}.
\]
The principal theorem consists of the following conclusions, with all parameters \(d,p,a\) fixed as \(N\to\infty\):

1. **Exact finite-dimensional diagonalization.** For each strictly decreasing integer tuple \(m_1>\cdots>m_d\ge0\) satisfying \(\sum_i m_i\le N+d(d-1)/2\), there is one eigenvalue
\[
\lambda_{\boldsymbol m,N,\beta}=\Pr\!\left\{\sum_{i=1}^d[-\log R_i]\ge a/N^\beta\right\},
\]
where the \(R_i\) are independent beta random variables \(R_i\sim\mathrm{Beta}(m_i+1,p)\). These eigenvalues comprise the entire spectrum, with multiplicities from distinct tuples.

2. **Critical spectral law and sharp scale.** At \(\beta=1\), for every continuous \(h:[0,1]\to\mathbb R\),
\[
\lim_{N\to\infty}N^{-d}\operatorname{Tr}h(T_{N,1}(a))
=\int_{\Sigma_d}h(F_{p,d}(a;\boldsymbol u))\,d\boldsymbol u.
\]
The dimension satisfies \(\dim\mathcal P_N\sim N^d/(d!)^2\). The normalized empirical spectral measure thus converges to the pushforward of uniform probability measure on \(\Sigma_d\) by \(F_{p,d}\). For every \(0<\tau<1\), the same limit holds for threshold counting after replacing \(h\) by \(\mathbf1_{[\tau,1]}\). In contrast, when \(0<\beta<1\) the empirical spectrum tends to the point mass at \(0\); when \(\beta>1\) it tends to the point mass at \(1\).

3. **Positive, sharp projection-defect coefficient and two exact endpoints.** Define
\[
C_{p,d}(a)=\int_{\Sigma_d}F_{p,d}(a;\boldsymbol u)\bigl(1-F_{p,d}(a;\boldsymbol u)\bigr)\,d\boldsymbol u>0.
\]
Then \(\operatorname{Tr}(T_{N,1}(a)[I-T_{N,1}(a)])\sim N^d C_{p,d}(a)\). Moreover,
\[
C_{p,d}(a)\sim
\frac{\Gamma(p+1)^d}{d!\,\Gamma(dp+1)\,\Gamma(d(p+1)+1)}\,a^{dp}
\quad(a\downarrow0),
\]
and
\[
C_{p,d}(a)\sim
\frac{\Gamma(p+1/2)}{\sqrt\pi\,\Gamma(p)((d-1)!)^2}\,a^{-1}
\quad(a\to\infty).
\]
In the ordinary Bergman symmetrized bidisc (\(d=2\), \(\alpha=0\)), the same coefficient consequently has the two explicit limits \(C_{1,2}(a)\sim a^2/96\) as \(a\downarrow0\) and \(C_{1,2}(a)\sim1/(2a)\) as \(a\to\infty\).

## Assumptions and scope

Let \(s:\mathbb D^d\to\mathbb G_d\) denote the elementary-symmetric map. The normalized base measure on \(\mathbb D^d\) is the product of \(p(1-|z_i|^2)^{p-1}dA(z_i)/\pi\). The quotient measure on \(\mathbb G_d\) is its pushforward after multiplication by \(|J_s|^2/d!\), renormalized by a positive constant. This is the canonical quotient Bergman measure of Misra, Shyam Roy and Zhang (2011), with their kernel parameter \(p+1\); constant rescalings of the Hilbert norm do not affect any compression eigenvalue.

The degree is the ordinary total degree of the symmetric polynomial \(f(s(z))\) in the original \(d\) variables, assigning degree \(j\) to the quotient coordinate \(w_j\). It is **not** unweighted degree in the quotient coordinates. For \(d=2\), the Schur index \(\nu=(\nu_1,\nu_2)\) has lift degree \(\nu_1+\nu_2\). The spectral law concerns this specific finite section and these product-coordinate collars; it makes no assertion about generic non-radial symbols, arbitrary quotient domains, or an independent audit.

## Proof

**Step 1: unitary lift and exact eigenvalues.** Multiplication by the complex Jacobian \(J_s(z)=\prod_{i<j}(z_i-z_j)\) intertwines the quotient Bergman space with the antisymmetric subspace of the weighted product Bergman space. Its orthogonal basis is the alternating monomial family
\[
A_{\boldsymbol m}(z)=\det\bigl(z_i^{m_j}\bigr)_{i,j=1}^d,
\qquad m_1>\cdots>m_d\ge0,
\]
with \(m_i=\nu_i+d-i\). Both the quotient indicator \(\mathbf1_{\Omega_{N,\beta}(a)}\) and its lift \(\mathbf1_{\{\prod_i|z_i|^2\le e^{-a/N^\beta}\}}\) are invariant under separate coordinate rotations and coordinate permutations. In each inner product of two alternants, integrate the angular variables first. Every mixed permutation term vanishes unless the exponent tuples agree up to permutation. Strictly decreasing tuples admit no such agreement across different indices. For a fixed tuple, cross permutation terms also vanish; the remaining \(d!\) diagonal integrals are identical by permutation invariance. Thus the entire finite compression is diagonal.

For one radial monomial factor, put \(R=|z|^2\). Its normalized weighted density under monomial degree \(m\) is
\[
\frac{r^m(1-r)^{p-1}}{B(m+1,p)}\,dr,
\quad 0<r<1.
\]
The product-cutoff integral therefore equals exactly the stated independent-beta probability. This proves diagonalization, all multiplicities, and \(0<\lambda_{\boldsymbol m,N,\beta}<1\).

**Step 2: gamma scaling and counting lattice points.** Suppose \(m_i/N\to u_i>0\). For \(R_i\sim\mathrm{Beta}(m_i+1,p)\), the density of \(V_i=N(1-R_i)\) is
\[
\frac{N^{-p}(1-v/N)^{m_i}v^{p-1}}{B(m_i+1,p)}\mathbf1_{(0,N)}(v).
\]
The gamma ratio \(\Gamma(m_i+p+1)/\Gamma(m_i+1)\sim m_i^p\) shows that this density converges to \(u_i^p v^{p-1}e^{-u_i v}/\Gamma(p)\). This proves convergence in law to \(G_i/u_i\); also \(N[-\log R_i-(1-R_i)]\to0\) in probability because \(N(1-R_i)\) is tight. Independence gives
\[
N\sum_i[-\log R_i]\ \Rightarrow\ \sum_iG_i/u_i.
\]
The limit has a continuous strictly positive density on \((0,\infty)\), so there are no threshold atoms. The strict-partition lattice \(\boldsymbol m=\boldsymbol\nu+(d-1,\ldots,0)\) is an ordered lattice in \(N\Sigma_d\), apart from lower-dimensional boundary points. The standard mesh-counting argument gives \(\#\{\boldsymbol m\}\sim N^d|\Sigma_d|\), and bounded Riemann sums converge by excluding an arbitrarily thin boundary strip. The same argument yields the stated continuous-test-function spectral law.

For threshold counts, write \(\boldsymbol u=t\boldsymbol v\) with \(\sum_i v_i=1\). Then \(F_{p,d}(a;t\boldsymbol v)=\Pr(\sum_iG_i/v_i\ge at)\), a strictly decreasing function of \(t>0\). Thus every level set \(F_{p,d}=\tau\) meets each positive radial ray in at most one point; Fubini's theorem makes it a null set. The indicator-counting limit follows. For \(\beta\ne1\), the scaled comparison threshold is \(aN^{1-\beta}\), respectively tending to infinity or zero; the gamma law and the same Riemann-sum argument give the two point-mass limits.

**Step 3: the trace coefficient.** Apply Step 2 to \(h(t)=t(1-t)\). All gamma sums have probability strictly between zero and one of lying above \(a\), so \(C_{p,d}(a)>0\) and the trace limit is an asymptotic equivalence, not just an upper bound.

**Step 4: small-collar coefficient.** Write \(F=F_{p,d}(a;\boldsymbol u)\). Direct integration of the joint gamma density over \(y_i>0\), \(\sum_i y_i<a\), shows, uniformly for \(\boldsymbol u\in\Sigma_d\), that
\[
e^{-a}\frac{a^{dp}\prod_i u_i^p}{\Gamma(dp+1)}
\le 1-F\le
\frac{a^{dp}\prod_i u_i^p}{\Gamma(dp+1)}.
\]
Indeed, \(e^{-\sum_i u_i y_i}\) lies between \(e^{-a}\) and \(1\), while the remaining Dirichlet integral is exactly \(a^{dp}\Gamma(p)^d/\Gamma(dp+1)\). The uniform estimate also gives \(F(1-F)=(1-F)[1+O(a^{dp})]\). By symmetry and the Dirichlet simplex integral,
\[
\int_{\Sigma_d}\prod_i u_i^p\,d\boldsymbol u
=\frac{\Gamma(p+1)^d}{d!\,\Gamma(d(p+1)+1)}.
\]
The asserted small-\(a\) coefficient follows.

**Step 5: large-collar coefficient.** Order the coordinates so \(u_d\) is the smallest, and put \(v=a u_d\). For fixed \(v>0\) and fixed positive, strictly ordered \(u_1,\ldots,u_{d-1}\), the event defining \(F\) becomes
\[
\frac{G_d}{v}+\sum_{i<d}\frac{G_i}{a u_i}\ge1,
\]
whose probability tends to \(Q_p(v)=\Pr\{G_d\ge v\}\). Moreover, since \(u_i\ge u_d\), coupling with the *same* gamma variables gives
\[
0\le F_{p,d}(a;\boldsymbol u)\bigl(1-F_{p,d}(a;\boldsymbol u)\bigr)
\le F_{p,d}(a;\boldsymbol u)\le Q_{dp}(v),
\]
where \(Q_{dp}\) is the gamma survival function with shape \(dp\) and unit rate. Its integral over \((0,\infty)\) is \(dp\), permitting dominated convergence after this change of variable. The remaining ordered \((d-1)\)-simplex has volume \(((d-1)!)^{-2}\). Hence
\[
\lim_{a\to\infty}a C_{p,d}(a)
=\frac{1}{((d-1)!)^2}\int_0^\infty Q_p(v)(1-Q_p(v))\,dv.
\]
For independent \(G,H\sim\mathrm{Gamma}(p,1)\), the last integral equals \(\mathbb E(G-H)_+=\mathbb E|G-H|/2\). The beta-gamma decomposition \(G+H\sim\mathrm{Gamma}(2p,1)\), \(G/(G+H)\sim\mathrm{Beta}(p,p)\), and gamma duplication yield
\[
\int_0^\infty Q_p(v)(1-Q_p(v))\,dv
=\frac{\Gamma(p+1/2)}{\sqrt\pi\,\Gamma(p)}.
\]
This completes every part of the theorem.

## Verification

A standalone standard-library Python checker accompanies this document as `check.py`. It independently computes degree-two-product-collar eigenvalues by a direct convolution quadrature, verifies exact and asymptotic dimension counts, compares finite traces to a two-variable quadrature of the limit profile, checks the two boundary-collar coefficients for the ordinary symmetrized bidisc, and independently evaluates the gamma-tail identity for integer shapes. Its finite tests are supplements to, not substitutes for, Steps 1–5. Run with `python3 check.py`.

For the special case \(d=2,p=1\), the continuum profile is explicitly
\[
F_{1,2}(a;u,v)=\frac{u e^{-av}-v e^{-au}}{u-v},\qquad
F_{1,2}(a;u,u)=e^{-au}(1+au).
\]
For \(m>n\), the *exact finite* eigenvalue at critical scale is
\[
\lambda_{(m,n),N,1}=
\frac{(m+1)e^{-(n+1)a/N}-(n+1)e^{-(m+1)a/N}}{m-n}.
\]
These closed formulas allow independent implementation without the original checker.

## Relationship to prior work

Misra, Shyam Roy and Zhang (arXiv:1106.3868, first public June 20, 2011), especially §2.1 and Theorem 2.3, establish the antisymmetric-Schur orthogonal basis and quotient Bergman kernel. These are necessary starting points and are not claimed as new. Ghosh and Narayanan (arXiv:2202.03184, first public February 4, 2022), especially §5.1 and §6.2, transport Toeplitz-operator identities between quotient domains and their covers; they study commuting and zero-product properties, not the shrinking product-collar spectrum, critical scale, or its two trace-coefficient endpoints. The latter paper motivates the present finite-section spectral question.

Pérez-Esteva and Uribe (arXiv:1801.00366) prove singular Berezin–Toeplitz Szegő laws for Gaussian Fock spaces with densities supported on submanifolds, a different Hilbert-space family and symbol scaling. Miheisi and O'Loughlin (arXiv:2404.03087) study truncated Hardy Toeplitz operators on one-variable model spaces with boundary symbols, not product-coordinate collars on symmetric Bergman quotient domains. Thus those general results do not directly imply the exact beta-product diagonalization or the two gamma endpoint coefficients here. No assertion of comprehensive historical priority is made.

## Limitations

The precise finite section uses *lift degree*, the quotient measure uses the symmetric-map Jacobian, and the cutoff depends only on the last quotient coordinate. Changing any of these assumptions may change the law. The spectral convergence is asymptotic at fixed \(d,p,a\); the \(a\downarrow0\) and \(a\to\infty\) limits concern the already-defined continuum coefficient and are not claimed to be uniform two-parameter limits with \(N\). No quantitative finite-\(N\) error rate or eigenvector perturbation stability for non-radial symbols is asserted. Historical originality has been assessed against the cited sources and available indexed results, not independently audited.

## References

- G. Misra, S. Shyam Roy and G. Zhang, *Reproducing kernel for a class of weighted Bergman spaces on the symmetrized polydisc*, arXiv:1106.3868 (first public 2011-06-20); Proc. Amer. Math. Soc. 141 (2013), 2361–2370. https://arxiv.org/abs/1106.3868
- G. Ghosh and E. K. Narayanan, *Toeplitz operators on the weighted Bergman spaces of quotient domains*, arXiv:2202.03184 (first public 2022-02-04); Bull. Sci. Math. 188 (2023), 103340. https://arxiv.org/abs/2202.03184
- S. Pérez-Esteva and A. Uribe, *Szegö Limit Theorems for Singular Berezin-Toeplitz Operators*, arXiv:1801.00366 (first public 2017-12-31). https://arxiv.org/abs/1801.00366
- N. Miheisi and R. O'Loughlin, *Szegő Limit Theorem for Truncated Toeplitz Operators*, arXiv:2404.03087 (first public 2024-04-03). https://arxiv.org/abs/2404.03087
