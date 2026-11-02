# Sharp cyclic Bergman kernel zero thresholds and a logarithmic symmetry-order law

## Finding
For each integer \(d\ge2\) and each \(1<\lambda\le2\), let \(\mathcal H_\lambda\) be the weighted analytic Bergman space on \(\mathbb D\) with reproducing kernel \((1-z\overline w)^{-\lambda}\), and let \(\mathcal H_{\lambda,d}\) be its closed subspace of functions invariant under \(z\mapsto e^{2\pi i/d}z\). Its kernel is
\[
\mathcal K_{\lambda,d}(z,w)=F_{\lambda,d}((z\overline w)^d),\qquad
F_{\lambda,d}(x)=\sum_{n=0}^{\infty}\frac{(\lambda)_{dn}}{(dn)!}x^n.
\]
For \(d=2\), this kernel is zero-free for every \(1<\lambda\le2\). For each \(d\ge3\), there is a unique \(\lambda_d\in(1,2)\) determined by
\[
\frac1d\sum_{j=0}^{d-1}\left(1-e^{(2j+1)\pi i/d}\right)^{-\lambda_d}=0,
\]
using the principal complex power and pairing conjugate terms. For \(1<\lambda\le\lambda_d\), the kernel has no zeros in \(\mathbb D\times\mathbb D\). For \(\lambda_d<\lambda\le2\), the scalar function \(t\mapsto F_{\lambda,d}(t^d)\) has **exactly \(d\) simple zeros** in \(|t|<1\), located at
\[
t=\rho_{d,\lambda}^{1/d}e^{(2j+1)\pi i/d},\quad 0\le j<d,
\]
where \(0<\rho_{d,\lambda}<1\) is the unique solution of \(F_{\lambda,d}(-\rho)=0\). Thus there are precisely \(d\) admissible scalar products \(z\overline w\) producing kernel zeros. As the symmetry order tends to infinity,
\[
\boxed{\lim_{d\to\infty}(\lambda_d-1)\log d=\log2.}
\]
For \(d=3\), the threshold is the unique root in \((1,2)\) of \(2\cos(\pi\lambda/3)+2^{-\lambda}=0\), namely \(\lambda_3\approx1.6525214566647722\). Every assertion also extends to \(\lambda=1\) with the Hardy-kernel interpretation, but this is not needed for the Bergman statement.

## Assumptions and scope
The normalization is \(\|f\|_\lambda^2=(\lambda-1)\pi^{-1}\int_{\mathbb D}|f(z)|^2(1-|z|^2)^{\lambda-2}\,dA(z)\). The Pochhammer symbol is \((\lambda)_n=\Gamma(\lambda+n)/\Gamma(\lambda)\). The scalar disk variable is \(t=z\overline w\); the quotient coordinate is \(x=t^d\), both lying in the open unit disk. The boundary equation means the continuous radial boundary value at \(x=-1\), not the potentially divergent termwise boundary sum. For \(d=2\), the zero at \(x=-1\) when \(\lambda=2\) is on the boundary and is not a kernel zero. All counts are for distinct scalar zeros; each corresponds to many pairs \((z,w)\).

## Proof
**Kernel projection.** The normalized monomials in \(\mathcal H_\lambda\) have squared coefficient \((\lambda)_n/n!\). The cyclicly invariant subspace retains precisely monomials of degrees divisible by \(d\). Orthogonal projection therefore gives the stated series \(F_{\lambda,d}\). The root-of-unity filter gives, for \(|t|<1\),
\[
F_{\lambda,d}(t^d)=\frac1d\sum_{j=0}^{d-1}(1-e^{2\pi i j/d}t)^{-\lambda}.
\]

**Positive half-plane orientation.** At \(\lambda=2\), a geometric derivative shows
\[
F_{2,d}(x)=\sum_{n\ge0}(dn+1)x^n=\frac{1+(d-1)x}{(1-x)^2}=:Q_d(x).
\]
For \(0<\lambda<2\), let \(U\) have the beta distribution with parameters \((\lambda,2-\lambda)\). Then \(\mathbb E U^{dn}=(\lambda)_{dn}/(2)_{dn}\), and absolute convergence for \(|x|<1\) yields the exact positive representation
\[
F_{\lambda,d}(x)=\mathbb E\,Q_d(U^d x).
\]
The endpoint \(\lambda=2\) corresponds to \(U\equiv1\). Direct complex algebra gives
\[
\operatorname{Im}Q_d(v)=\frac{\operatorname{Im}v\,[(d+1)-2\operatorname{Re}v-(d-1)|v|^2]}{|1-v|^4}.
\]
The square bracket is strictly positive for \(|v|<1\), since it is at least \((1-|v|)[d+1+(d-1)|v|]\). Hence \(\operatorname{Im}F_{\lambda,d}(x)\) has the strict sign of \(\operatorname{Im}x\), and no zero has nonreal \(x\). Positivity of the Taylor coefficients excludes \(0\le x<1\).

**Exact negative-axis count.** For \(0\le v<1\),
\[
Q_d(-v)=\frac{1-(d-1)v}{(1+v)^2},\qquad
\frac{d}{dv}Q_d(-v)=\frac{-(d+1)+(d-1)v}{(1+v)^3}<0.
\]
Consequently \(\rho\mapsto F_{\lambda,d}(-\rho)=\mathbb E Q_d(-U^d\rho)\) is strictly decreasing on \([0,1]\), including the degenerate endpoint, and starts at \(1\). Define \(h_d(\lambda):=F_{\lambda,d}(-1)\), with the boundary value taken through the root-of-unity formula. The family \(\mathrm{Beta}(\lambda,2-\lambda)\) increases *strictly in stochastic order* with \(\lambda\): the likelihood ratio of densities for parameters \(\lambda_2>\lambda_1\) is proportional to \((u/(1-u))^{\lambda_2-\lambda_1}\), a strictly increasing function. Since \(u\mapsto Q_d(-u^d)\) is strictly decreasing, \(h_d\) is continuous and strictly decreasing. At \(\lambda=1\), the root-of-unity sum equals \(F_{1,d}(x)=1/(1-x)\), giving \(h_d(1)=1/2\); at \(\lambda=2\), \(h_d(2)=(2-d)/4\). Thus for \(d=2\), \(h_d\) is nonnegative on \([1,2]\), and for each \(d\ge3\) it vanishes at precisely one \(\lambda_d\in(1,2)\). Strict monotonicity in \(\rho\) gives no interior negative root at or below the threshold and exactly one for larger \(\lambda\). Its derivative is nonzero, hence the root is simple. The nonzero change of variables \(x=t^d\) yields \(d\) distinct simple scalar zeros on the asserted rays.

**Large-order threshold.** For any fixed \(\eta\ge0\), put \(\lambda_d(\eta)=1+\eta/\log d\) for sufficiently large \(d\). The beta integral gives
\[
h_d(\lambda_d(\eta))=\mathbb E(1+U^d)^{-2}-(d-1)\mathbb E\frac{U^d}{(1+U^d)^2}.
\]
The first expectation tends to \(1\), by bounded convergence and the fact that these beta laws converge weakly to the uniform law. In the second, set \(u=1-y/d\), \(0<y<d\). The beta density is \(u^{\lambda-1}(1-u)^{1-\lambda}/B(\lambda,2-\lambda)\), while \(d^{\lambda-1}=e^\eta\), \(u^d\to e^{-y}\), and \(B(\lambda,2-\lambda)\to1\). For \(\eta\) fixed and large \(d\), the rescaled integrand is dominated by a constant times \(\max(1,y^{-1/2})e^{-y}\), so dominated convergence yields
\[
\lim_{d\to\infty}(d-1)\mathbb E\frac{U^d}{(1+U^d)^2}
=e^\eta\int_0^\infty\frac{e^{-y}}{(1+e^{-y})^2}\,dy=\frac{e^\eta}{2}.
\]
Thus \(h_d(1+\eta/\log d)\to1-e^\eta/2\). For any \(0\le\eta_-<\log2<\eta_+\), the limiting signs are respectively positive and negative. By the uniqueness and monotonicity of \(h_d\), \(\eta_-<(\lambda_d-1)\log d<\eta_+\) eventually. Shrinking the bracket proves the limit.

## Verification
The standalone `checker.py` checks the exact integer-exponent rational formula, the root-of-unity boundary identity, the unique real root and sign switch in representative finite cases, and numerical agreement with the claimed large-order asymptotic. The checks are finite corroboration only. The analytic beta representation, strict half-plane sign, stochastic-order and dominated-convergence arguments prove all infinitely quantified assertions.

## Relationship to prior work
Ghosh, *The Weighted Bergman spaces and Pseudoreflection groups* (arXiv:2104.14162, first public 2021-04-29), develops relative-invariant Bergman subspaces and group-averaged kernels. Ghosh and Narayanan, *Toeplitz operators on the weighted Bergman spaces of quotient domains* (arXiv:2202.03184, first public 2022-02-04), studies quotient-domain Toeplitz identities and gives invariant kernel formulas. Those representation mechanisms imply the initial projection but do not supply the beta-mixture positivity, the full zero count, the uniquely parameterized threshold or its \(\log2/\log d\) law. Miña-Díaz, *A representation for the reproducing kernel of a weighted Bergman space* (arXiv:2212.08118, first public 2022-12-15), addresses Blaschke-factor weighted spaces and kernel representations rather than cyclicly invariant power kernels. General Lu Qi-Keng zero questions motivate deciding zero-free parameters, but no assertion of complete historical priority is made.

## Limitations
The result treats the trivial cyclic-isotypic sector only and the kernel exponent \(1<\lambda\le2\). It does not classify zeros for \(\lambda>2\), arbitrary finite group representations or non-power radial weights. The threshold is implicit rather than elementary for general \(d\), and the symmetry-order asymptotic is first order without a uniform error rate. Independent validation and exhaustive historical-priority confirmation have not been performed.

## References
- G. Ghosh, *The Weighted Bergman spaces and Pseudoreflection groups*, arXiv:2104.14162, first public 2021-04-29. https://arxiv.org/abs/2104.14162
- G. Ghosh and E. K. Narayanan, *Toeplitz operators on the weighted Bergman spaces of quotient domains*, arXiv:2202.03184, first public 2022-02-04. https://arxiv.org/html/2202.03184v3
- E. Miña-Díaz, *A representation for the reproducing kernel of a weighted Bergman space*, arXiv:2212.08118, first public 2022-12-15. https://arxiv.org/abs/2212.08118
