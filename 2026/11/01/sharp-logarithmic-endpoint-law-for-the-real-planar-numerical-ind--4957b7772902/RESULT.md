# Sharp logarithmic endpoint law for the real planar numerical index

## Finding
For each real exponent \(1<p<\infty\), let \(n_p=n(\ell_p^2(\mathbb R))\) be the numerical index and put
\[
 \eta=\left|1-\frac2p\right|\in[0,1),\qquad
 \mathcal N(\eta)=\max_{z\ge0}\frac{\sinh(\eta z)}{\cosh z}.
\]
Then \(n_p=\mathcal N(\eta)\), with the endpoint extension \(\mathcal N(0)=0\), \(\mathcal N(1)=1\). The identity with the scalar maximization is an algebraic reformulation of known numerical-index formulas, **not** claimed to be new. The new quantitative conclusion is the following sharp two-term singular endpoint law, including the moving extremizer.

Let \(\varepsilon=1-\eta\) and \(L=\log(4/\varepsilon)\). As \(\varepsilon\downarrow0\),
\[
\boxed{1-\mathcal N(1-\varepsilon)
 =\frac{\varepsilon}{2}(L+1)
 -\frac{\varepsilon^2}{8}(L^2+1)
 +O(\varepsilon^3 L^3).}
\tag{1}
\]
For every \(0<\eta<1\), the maximizer \(z_\eta\) is unique and is characterized by
\[
 \tanh(\eta z_\eta)\tanh z_\eta=\eta.
\tag{2}
\]
Its sharp endpoint displacement is
\[
\boxed{z_{1-\varepsilon}=\frac L2+\frac{\varepsilon}{4}(L-1)
 +O(\varepsilon^2 L^2).}
\tag{3}
\]
Consequently, as \(p\to\infty\),
\[
\boxed{1-n_p=\frac{\log(2p)+1}{p}
-\frac{\log^2(2p)+1}{2p^2}
+O\!\left(\frac{\log^3p}{p^3}\right).}
\tag{4}
\]
By conjugate-exponent duality, the same law holds as \(p\downarrow1\) when \(p\) is replaced by \(q=p/(p-1)\). In particular, the leading normalized deficit tends to one:
\[
\lim_{p\to\infty}\frac{p(1-n_p)}{\log p}=1.
\]
The parameter profile \(\mathcal N\) is continuous and strictly increasing and strictly convex on \([0,1]\), real analytic on \((0,1)\). If \(z_*\) denotes the unique positive solution of \(z_*\tanh z_*=1\), then a complementary sharp smooth-end expansion is
\[
\mathcal N(\eta)=\frac{z_*}{\cosh z_*}\eta
+\frac{z_*^3}{6\cosh z_*}\eta^3+O(\eta^5)
\quad(\eta\downarrow0),
\tag{5}
\]
so \(n_p\sim[z_*/(2\cosh z_*)]|p-2|\) as \(p\to2\).

## Assumptions and scope
All spaces and operators are over the **real** field. For a Banach space \(X\), define the numerical radius of \(T\in\mathcal L(X)\) by
\[
v(T)=\sup\{|x^*(Tx)|:x\in S_X,\ x^*\in S_{X^*},\ x^*(x)=1\},
\]
and the numerical index by \(n(X)=\inf\{v(T):\|T\|=1\}\). The theorem concerns only \(X=\ell_p^2(\mathbb R)\). At \(p=1,\infty\), define \(n_p=1\), consistently with the limit of the interior formula. Error terms in (1) and (3) are uniform for all sufficiently small positive \(\varepsilon\); the constants are absolute. The source numerical-index theorem is Chiclana's 2026 equality \(n_p=v(J)\) for the quarter-turn matrix \(J\); the elementary scalar formula for \(v(J)\) was already known. Equations (1), (3), (4), and (5) are the quantitative refinements under investigation.

## Proof
**1. Exact reduction and uniqueness.** A published numerical-radius formula, combined with the proved identity \(n_p=v(J)\), states
\[
 n_p=\max_{0\le t\le1}\frac{|t^{p-1}-t|}{1+t^p}.
\tag{6}
\]
For any \(1<p<\infty\), substitute \(t=e^{-2z/p}\) and set \(\eta=|1-2/p|\). Direct cancellation yields
\[
\frac{|t^{p-1}-t|}{1+t^p}
=\frac{\sinh(\eta z)}{\cosh z}=:F_\eta(z).
\tag{7}
\]
For \(0<\eta<1\), \(F_\eta(0)=0\), \(F_\eta(z)>0\) for positive \(z\), and \(F_\eta(z)\to0\) as \(z\to\infty\). Differentiation gives \(F_\eta'(z)=0\) if and only if (2). Its right-hand side \(\tanh(\eta z)\tanh z\) increases strictly from \(0\) to \(1\), so there is exactly one stationary point; this is the unique global maximizer.

**2. Profile geometry.** If \(0<\eta_1<\eta_2\le1\), then \(F_{\eta_1}(z)<F_{\eta_2}(z)\) for \(z>0\). Maximizing at \(\eta_1\) proves strict increase; limits follow from \(F_0=0\) and \(\sup_{z\ge0}F_1(z)=\sup\tanh z=1\), together with monotone convergence of the suprema. For fixed \(z>0\), the function \(\eta\mapsto F_\eta(z)\) is strictly convex on \([0,1]\), since it is a positive multiple of \(\sinh(\eta z)\). For any two distinct parameters and an interior convex combination \(\eta_\theta<1\), evaluate strict pointwise convexity at the unique maximizer \(z_{\eta_\theta}\); the resulting value is strictly below the same convex combination of the two suprema. This also covers an endpoint parameter equal to \(1\). The implicit-function theorem applied to (2) gives real analyticity of \(z_\eta\) and \(\mathcal N(\eta)\) on \((0,1)\). Finally, for fixed positive \(z\), the function \(\tanh(\eta z)/\eta\) decreases strictly in \(\eta>0\), whereas its product with \(\tanh z\) increases strictly in \(z\). Thus \(z_\eta\) increases strictly with \(\eta\).

**3. Hilbert-end expansion.** Divide (2) by \(\eta\). The left side converges locally uniformly, with its derivatives, to \(z\tanh z\). The latter is strictly increasing from \(0\) to infinity and equals \(1\) uniquely at \(z_*\). Implicit differentiation in the variable \(\eta^2\) yields \(z_\eta=z_*+O(\eta^2)\). Taylor expansion of \(F_\eta(z)=\eta z/\cosh z+\eta^3 z^3/(6\cosh z)+O(\eta^5)\) is uniform on a compact neighborhood of \(z_*\). The derivative of \(z/\cosh z\) vanishes at \(z_*\), so replacing \(z_\eta\) by \(z_*\) in the leading term introduces only \(O(\eta^5)\). This proves (5).

**4. Polyhedral-end boundary layer.** Write \(\eta=1-\varepsilon\), \(z=z_{1-\varepsilon}\), \(u=e^{-2z}\), \(v=e^{-2(1-\varepsilon)z}=u^{1-\varepsilon}\). The exact critical identity (2) is equivalent to
\[
 \varepsilon=\frac{2(u+v)}{(1+u)(1+v)}.
\tag{8}
\]
Here \(0<u\le v<1\). Because the denominator lies between \(1\) and \(4\), (8) gives \(u+v=O(\varepsilon)\); more precisely
\(u+v=\varepsilon/2+O(\varepsilon^2)\). The inequalities \(v\ge u\) and \(u=v^{1/(1-\varepsilon)}\) then show \(u,v\asymp\varepsilon\). Consequently \(z=O(\log(1/\varepsilon))\) and \(v/u=\exp(2\varepsilon z)=1+O(\varepsilon L)\). Substitution back into (8) yields \(u=\varepsilon/4\,[1+O(\varepsilon L)]\) and \(z=L/2+O(\varepsilon L)\).

Insert this preliminary estimate into the exact relation \(v=u\exp(\varepsilon\log(1/u))\). Expanding both sides of (8), using uniform Taylor remainders because \(\varepsilon L\to0\), gives
\[
 u=\frac\varepsilon4\left[1+\frac\varepsilon2(1-L)+O(\varepsilon^2L^2)\right],
\qquad
 v=\frac\varepsilon4\left[1+\frac\varepsilon2(1+L)+O(\varepsilon^2L^2)\right].
\tag{9}
\]
For clarity, the coefficient in the first bracket follows by setting \(u=(\varepsilon/4)[1+\varepsilon U+O(\varepsilon^2L^2)]\). Then \(v=(\varepsilon/4)[1+\varepsilon(U+L)+O(\varepsilon^2L^2)]\), while (8) says \(u+v=\varepsilon/2+\varepsilon^2/4+O(\varepsilon^3L^2)\); hence \(2U+L=1\). Taking \(-\frac12\log u\) proves (3).

The exact value at the maximizer satisfies
\[
 \mathcal N(1-\varepsilon)
 =e^{-\varepsilon z}\frac{1-v}{1+u}.
\tag{10}
\]
Use (3) and (9) in the logarithm of (10). Expansion of \(\log(1-v)\) and \(\log(1+u)\), with remainders bounded by absolute constants times the next powers because \(u,v=O(\varepsilon)\), yields
\[
 \log\mathcal N(1-\varepsilon)
 =-\frac\varepsilon2(L+1)-\frac{\varepsilon^2L}{4}
 +O(\varepsilon^3L^3).
\tag{11}
\]
The quadratic term in the exponential of (11) gives (1). For \(p>2\), \(\varepsilon=2/p\) and \(L=\log(2p)\), yielding (4). For \(1<p<2\), the conjugate \(q=p/(p-1)>2\) gives the same \(\eta\), proving the conjugate-end statement.

## Verification
The standalone `verify.py` checks the direct coordinate substitution against the original scalar formula at paired conjugate exponents, residuals of the stationary equation, strict parameter ordering on a finite grid, numerical convexity on a finite grid, and the predicted Hilbert and polyhedral asymptotic errors. It uses only Python's standard library and reports a deterministic pass count. These tests are **finite consistency checks**, not an exhaustive analytic proof. The proof above supplies the necessary quantifiers, uniform error terms, and endpoint arguments.

## Relationship to prior work
Martín and Merí (2009), Lemma 2, derive (6) for the numerical radius of the rotation and establish bounds on the numerical index. Merí and Quero's first-public 2022 preprint proves equality with the rotational radius on a restricted interval of exponents and studies its maximizer. Chiclana's first-public June 2026 paper settles equality \(n_p=v(J)\) for every \(p\), and §7 already records (2) in its positive exponent branch. Those identities are **prior work**; the claimed additions are the uniform two-term logarithmic endpoint expansion, the order-corrected maximizing coordinate, and the global strict-convexity and near-Hilbert expansion for the fully identified numerical-index profile. In particular, a known exact one-parameter maximization logically determines its values, but locating a maximizer moving to infinity and extracting the coefficients of the nonanalytic \(\varepsilon\log(1/\varepsilon)\) boundary layer requires an additional argument.

A related published result about Chmieliński's global \(C\)-approximate Birkhoff symmetry on Hilbert-valued \(\ell_p\)-sums has a *different* hyperbolic denominator and a near-Hilbert coefficient numerically equal to \(z_*/\cosh z_*\). Its formula concerns reverse orthogonality, not the numerical index, and does not yield the logarithmic polyhedral-end law here. Accessible literature records and mathematical findings were compared by the underlying functions, not merely by titles. A differently parametrized treatment of the same singular maximization in earlier literature cannot be ruled out; originality and priority remain best-knowledge assessments, not independent certification.

## Limitations
The theorem applies to the real plane \(\ell_p^2\), not complex scalars, higher dimensions, or infinite-dimensional \(L_p\). The existing exact numerical-index and optimizer formulas are credited and not claimed as new. The \(O\)-terms are qualitative with uniformity only sufficiently near the specified endpoints; no global certified error constant is asserted. The coefficient of the third logarithmic correction is not determined. Numerical checks are supplementary, and independent validation and publication-priority checks have not been performed.

## References
1. R. Chiclana, *The Numerical Index of Two-Dimensional Real \(\ell_p\) Spaces*, arXiv:2606.01675v1 (first public 1 June 2026), https://arxiv.org/abs/2606.01675. Theorem 1.1 and §7.
2. J. Merí and A. Quero, *On the numerical index of the real two-dimensional \(L_p\) space*, arXiv:2205.08807v1 (first public May 2022), https://arxiv.org/abs/2205.08807. Lemma 1 and §2.
3. M. Martín and J. Merí, *A note on the numerical index of the \(L_p\) space of dimension two*, 2009, https://www.ugr.es/~mmartins/Curriculum/Papers/2009-MartinMeri-Lp.pdf. Lemma 2 and Theorem 1.
4. *Sharp \(C\)-symmetry of two Hilbert summands and its near-Hilbert slope*, public mathematical record (2026), https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-c-symmetry-of-two-hilbert-summands-and-its-near-hilbert-sl--4c68c3cb1287/RESULT.md. Comparison is for distinguishable invariants and their near-Hilbert coefficients.
