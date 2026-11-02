# Sharp singular-edge variance constants and optimal antithetic shifted-grid pairing

## Finding
Let \(0<\alpha<1\), let \(g\in C^2([0,1])\) be strictly positive, and put \(f(x)=x^{-\alpha}g(x)\) for \(0<x\le1\). For a positive integer \(m\), set
\[
Q_m(u)=\frac1m\sum_{j=0}^{m-1}f\!\left(\frac{j+u}{m}\right),\qquad 0<u<1,
\]
and \(I=\int_0^1f(x)\,dx\). For any coupling \((U,V)\) whose two marginals are uniform on \((0,1)\), consider \(\overline Q_m=(Q_m(U)+Q_m(V))/2\). All these estimators are unbiased. For every \(m\ge1\) and every \(q>0\),
\[
\mathbb E|\overline Q_m-I|^q<\infty\quad\Longleftrightarrow\quad q<1/\alpha.
\]
Thus no dependence between two positive shifted-grid estimates repairs infinite variance when \(\alpha\ge1/2\).

If \(0<\alpha<1/2\), define the explicit positive constant
\[
C_\alpha=\frac{2\Gamma(1-\alpha)^2\zeta(2-2\alpha)}{(2\pi)^{2-2\alpha}},
\]
where the zeta function in this formula is the ordinary convergent Riemann series. Then
\[
\lim_{m\to\infty}m^{2-2\alpha}\operatorname{Var}(Q_m(U))=g(0)^2C_\alpha,
\]
\[
\lim_{m\to\infty}m^{2-2\alpha}\operatorname{Var}\!\left(\frac{Q_m(U)+Q_m(1-U)}2\right)
=g(0)^2C_\alpha\sin^2(\pi\alpha/2).
\]
For every \(m\), if \(f\) is strictly decreasing, the antithetic choice \(V=1-U\) uniquely minimizes the variance over all couplings with the prescribed uniform marginals (up to null sets). For arbitrary positive \(C^2\) multipliers \(g\), the same coupling is asymptotically minimizing:
\[
\lim_{m\to\infty}m^{2-2\alpha}\inf_{(U,V)}\operatorname{Var}(\overline Q_m)
=g(0)^2C_\alpha\sin^2(\pi\alpha/2).
\]
Two **independent** shifts of the same \(m\)-point rule instead have limiting variance coefficient \(g(0)^2 C_\alpha/2\). At equal cost \(2m\), the limiting optimal-antithetic/independent variance ratio is therefore exactly
\[
\boxed{2\sin^2(\pi\alpha/2)<1\quad(0<\alpha<1/2).}
\]
The ratio is \(1-1/\sqrt2\) at \(\alpha=1/4\). This is a property of two independently *marginally* uniform global shifts, not of independently randomized individual cells.

## Assumptions and scope
The integer \(m\ge1\) is arbitrary; \(U\) and \(V\) individually have the uniform law on \((0,1)\) and may be arbitrarily dependent. The positive function \(g\) extends twice continuously differentiably to \([0,1]\), so \(0<\min g\le\max g<\infty\). The moment statement applies for \(0<\alpha<1\); the variance asymptotics, minimization and gain factor require \(0<\alpha<1/2\). For exact finite-grid optimality, one additionally assumes that \(f\) is strictly decreasing, which holds in particular when \(g\) is nonincreasing. No claim is made for a general choice of nonuniform marginal shifts, unequal estimator weights, importance transformations, or negative correction weights.

## Proof
**1. Unbiasedness and sharp moments.** For each cell, \(\mathbb E f((j+U)/m)=m\int_{j/m}^{(j+1)/m}f(x)\,dx\); summing proves \(\mathbb EQ_m(U)=I\). Each \(Q_m\) is positive. Continuity and positivity of \(g\) imply, as \(u\downarrow0\),
\[
Q_m(u)=m^{\alpha-1}g(0)u^{-\alpha}+O_m(1)+o_m(u^{-\alpha}).
\]
The constant-order terms arise from cells other than the first; equivalently \(Q_m(u)\asymp_m u^{-\alpha}\) near zero. Hence its \(q\)-moment is finite precisely for \(q\alpha<1\). The bound \(\overline Q_m\ge Q_m(U)/2\) makes every higher moment infinite for **every** coupling. Conversely \((a+b)^q\le K_q(a^q+b^q)\) for nonnegative \(a,b\), and both marginals have finite \(q\)-moments below the threshold. Subtracting the finite constant \(I\) does not change moment finiteness. This proves the first assertion, including equality \(q\alpha=1\).

**2. A universal singular profile.** First take \(f(x)=x^{-\alpha}\). Write
\[
H_m(u)=\sum_{j=0}^{m-1}(j+u)^{-\alpha}-\frac{m^{1-\alpha}}{1-\alpha}.
\]
Exactly, \(H_m(u)=m^{1-\alpha}(Q_m(u)-I)\). The difference \(H_{m+1}(u)-H_m(u)\) is uniformly \(O(m^{-1-\alpha})\), since it compares \((m+u)^{-\alpha}\) with \(\int_m^{m+1}x^{-\alpha}\,dx\). Thus \(H_m\) has a limit \(H_\alpha\) on \((0,1)\), with uniform remainder \(O(m^{-\alpha})\); this is the standard zero-mean Hurwitz-zeta continuation \(\zeta(\alpha,u)\). Also \(H_\alpha(u)=u^{-\alpha}+O(1)\) near zero, hence \(H_m\to H_\alpha\) in \(L^2(0,1)\) exactly when \(\alpha<1/2\). Since \(\int_0^1H_m(u)\,du=0\), the limit has zero mean.

For general \(f\), decompose \(f(x)=g(0)x^{-\alpha}+h(x)\), where \(h(x)=x^{-\alpha}(g(x)-g(0))\). The derivative of \(h\) is \(O(x^{-\alpha})\) at zero and is integrable, so \(h\) has bounded total variation. On each cell, comparing a point value with the cell integral bounds its shifted-grid quadrature error by \(\operatorname{Var}_{[0,1]}(h)/m\), uniformly in \(u\). Consequently
\[
m^{1-\alpha}(Q_m(u)-I)=g(0)H_\alpha(u)+o_{L^2}(1).
\]

**3. Exact Fourier coefficients and the variance constant.** For each nonzero integer \(k\), changing variables cell by cell yields
\[
\int_0^1H_m(u)e^{-2\pi iku}\,du=\int_0^m x^{-\alpha}e^{-2\pi ikx}\,dx.
\]
Dirichlet convergence, or damping by \(e^{-\varepsilon x}\) followed by \(\varepsilon\downarrow0\), evaluates the right-hand limit as
\[
\widehat H_\alpha(k)=\Gamma(1-\alpha)(2\pi|k|)^{\alpha-1}
\exp\!\left[-\tfrac{i\pi}{2}(1-\alpha)\operatorname{sgn}(k)\right].
\]
Parseval, valid since \(\alpha<1/2\), gives
\[
\|H_\alpha\|_{L^2}^2=\sum_{k\ne0}|\widehat H_\alpha(k)|^2=C_\alpha.
\]
Reflection \(u\mapsto1-u\) conjugates each Fourier coefficient; averaging \(H_\alpha(u)\) and \(H_\alpha(1-u)\) retains exactly its real part. For positive \(k\), this part is \(\Gamma(1-\alpha)(2\pi k)^{\alpha-1}\sin(\pi\alpha/2)\). Parseval now gives \(C_\alpha\sin^2(\pi\alpha/2)\). Independent copies halve the original variance.

**4. Optimal coupling, including its quantifiers.** From the defining series,
\[
H_\alpha'(u)=-\alpha\sum_{j=0}^\infty(j+u)^{-1-\alpha}<0,
\]
so \(H_\alpha\) is continuous and strictly decreasing. The countermonotone rearrangement inequality says that, among all pairs of uniform random variables, \(\mathbb E[H_\alpha(U)H_\alpha(V)]\) is uniquely minimized by \(V=1-U\). One may first apply the bounded rearrangement inequality to truncated monotone functions and then pass to the limit in \(L^2\). Since both marginal means are zero and both marginal variances are fixed, this proves the claimed minimum for the limit profile.

The \(L^2\) approximation in step 2 holds in each marginal separately, and Cauchy--Schwarz bounds its contribution to the paired second moment uniformly over **all** couplings. Therefore taking the infimum commutes with passage to the leading asymptotic coefficient. If \(f\) itself is strictly decreasing, so is the finite sum \(Q_m(u)\); the same strict rearrangement argument applies directly at each \(m\), giving exact finite-grid optimality. This completes the proof.

## Verification
The included `verify.py` independently evaluates the limiting constants using high-precision numerical integration of the convergent Hurwitz-zeta profile and compares them with the gamma/zeta Fourier formulas. It also checks positive finite-grid antithetic variance and representative moment exponents. Numeric evaluation is diagnostic only: the infinite-family claims follow from the proof, not from finite sampling.

## Relationship to prior work
Wu's *A randomised trapezoidal quadrature* (first posted 2020) uses independent per-cell antithetic points and proves Sobolev-class convergence bounds. It does not analyze the two globally shifted rectangle lattices for integrable algebraic endpoint singularities. Ben-Ameur, L'Ecuyer and Lemieux (2004) already describe the combination of antithetic variates with randomized lattice points; neither the transformation \(U\mapsto1-U\) nor the general rearrangement principle is claimed as new. L'Ecuyer, Munger and Tuffin (2010) give a broad analysis of shifted-lattice error distributions, including smooth-integrand expansions, a baker's transform, and an unbounded-tail warning in their Example 12. That example does not quantify the singular-edge zeta variance constant or the optimal two-shift gain. Goda, Kazashi and Suzuki (first posted 2022) establish randomized trapezoidal optimal rates over Gaussian Sobolev classes, not the present paired-shift singular-edge constants. The contribution assessed here is the simultaneous sharp moment boundary, exact gamma/zeta leading coefficient, and universal **optimal-coupling gain** for this weakly singular quadrature class. Classical Fourier, antithetic and zeta identities are explicitly used rather than claimed as inventions.

## Limitations
The sharp asymptotic applies to fixed \(\alpha\) and fixed smooth positive multiplier \(g\) as the grid count tends to infinity; uniformity as \(\alpha\) approaches either endpoint is not proved. The two-shift class has equal positive weights, fixed uniform one-dimensional marginal shifts, and no importance sampling. Other correction schemes may restore finite second moments when \(\alpha\ge1/2\). The result does not determine optimal quadrature under arbitrary evaluation strategies or the effects of floating-point arithmetic. A specialized prior result on Hurwitz-zeta antithetic error constants outside the inspected literature cannot be excluded without independent priority review.

## References
1. Y. Wu, *A randomised trapezoidal quadrature*, arXiv:2011.15086, initial version 2020-11-30; *International Journal of Computer Mathematics*, DOI:10.1080/00207160.2021.1929194.
2. H. Ben-Ameur, P. L'Ecuyer and C. Lemieux, *Combination of General Antithetic Transformations and Control Variables*, *Mathematics of Operations Research* 29 (2004), 946–960, DOI:10.1287/moor.1040.0101.
3. P. L'Ecuyer, D. Munger and B. Tuffin, *On the distribution of integration error by randomly-shifted lattice rules*, *Electronic Journal of Statistics* 4 (2010), 950–993, DOI:10.1214/10-EJS574.
4. T. Goda, Y. Kazashi and Y. Suzuki, *Randomizing the trapezoidal rule gives the optimal RMSE rate in Gaussian Sobolev spaces*, arXiv:2212.11476, initial version 2022-12-22.
