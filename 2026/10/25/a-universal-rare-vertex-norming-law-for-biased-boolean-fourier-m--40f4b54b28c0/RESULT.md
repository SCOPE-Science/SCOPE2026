# A universal rare-vertex norming law for biased Boolean Fourier multipliers

## Finding
Let \(n\ge1\), let \(\mu=\bigotimes_{i=1}^n\mathrm{Bernoulli}(p_i)\) on \(\{0,1\}^n\), with \(0<p_i<1\), and let \(\lambda_S\in\mathbb C\) for every \(S\subseteq[n]\). Define the orthonormal biased characters
\[
\chi_i(x_i)=\frac{x_i-p_i}{\sqrt{p_i(1-p_i)}},\qquad
\chi_S(x)=\prod_{i\in S}\chi_i(x_i),\qquad \chi_\varnothing=1.
\]
Consider the Fourier-diagonal operator
\[
T_\lambda f(x)=\sum_{S\subseteq[n]}\lambda_S\chi_S(x)\,\mathbb E_\mu[\chi_S(Y)f(Y)].
\]
Set \(\alpha_i=\min(p_i,1-p_i)\), \(\rho_i=(1-\alpha_i)/\alpha_i\), and let \(r_i\) be the less-probable value of the \(i\)-th Bernoulli coordinate (choose either value when \(p_i=1/2\)). Let \(U_i\) be independent variables with
\[
\mathbb P(U_i=\rho_i)=\alpha_i,\qquad
\mathbb P(U_i=-1)=1-\alpha_i.
\]
**Universal rare-vertex convex ordering:** For every convex function \(\Phi:\mathbb C\to\mathbb R\) and every evaluation point \(x\in\{0,1\}^n\), writing \(K_\lambda(x,y)=\sum_S\lambda_S\chi_S(x)\chi_S(y)\),
\[
\mathbb E_\mu\Phi(K_\lambda(x,Y))\le
\mathbb E_\mu\Phi(K_\lambda(r,Y)).
\]
In particular, the two endpoint operator norms on the full complex function spaces coincide and admit the **same exact norming row for every spectral mask and every complex multiplier**:
\[
\boxed{\|T_\lambda\|_{L^1(\mu)\to L^1(\mu)}
=\|T_\lambda\|_{L^\infty(\mu)\to L^\infty(\mu)}
=\mathbb E\left|\sum_{S\subseteq[n]}\lambda_S\prod_{i\in S}U_i\right|.}
\]
The displayed value is nonincreasing in each rare-atom probability \(\alpha_i\in(0,1/2]\), with the multiplier coefficients and other rare-atom probabilities fixed. Taking \(\lambda_S\in\{0,1\}\) recovers **every orthogonal Fourier spectral projection**, not only low-degree truncations or coordinate-symmetric masks.

As an explicit consequence, fix \(0<\alpha\le1/2\), set \(\rho=(1-\alpha)/\alpha\), and take the projection \(P_{\le2}^{(n,\alpha)}\) onto all Fourier levels of degree at most two for homogeneous Bernoulli bias whose less-probable outcome has probability \(\alpha\). For \(n\ge2\), define \(s_j=j/\alpha-n\). Then
\[
\boxed{\|P_{\le2}^{(n,\alpha)}\|=
\sum_{j=0}^n\binom nj\alpha^j(1-\alpha)^{n-j}
\left|1+s_j+\frac{s_j^2-j\rho^2-(n-j)}2\right|.}
\]
For fixed \(\alpha>0\), its sharp leading asymptotic is
\[
\boxed{\lim_{n\to\infty}\frac{\|P_{\le2}^{(n,\alpha)}\|}{n}
=\frac{1-\alpha}{\alpha}\sqrt{\frac2{\pi e}}.}
\]
The homogeneous quadratic corollary illustrates the general multiplier law; the core new statement is the universal convex ordering for **all** biased-product Fourier multipliers.

## Assumptions and scope
All coordinates are genuinely random: \(0<p_i<1\). The discrete measure \(\mu\) has full support. Complex multiplier coefficients are allowed and need not be positive or real; the operator is not required to be a projection. \(\Phi\) is ordinary convexity on \(\mathbb C\cong\mathbb R^2\). The stated monotonicity changes the product measure and its corresponding normalized character system while keeping the numerical coefficients \(\lambda_S\) fixed. The rare vertex need not be the unique maximizing row. Norms are of the specified canonical diagonal operators, not minimum projection constants over all possible projections.

## Proof
**1. Orthogonality and kernel.** Each \(\chi_i(Y_i)\) has mean zero and second moment one. Products \(\chi_S\) are an orthonormal basis by independence, and the operator kernel with respect to \(\mu\) is
\[
K_\lambda(x,y)=\sum_{S\subseteq[n]}\lambda_S\chi_S(x)\chi_S(y).
\]
For finite full-support \(\mu\), the \(L^\infty\) norm is \(\max_x\mathbb E_\mu|K_\lambda(x,Y)|\); pointwise complex phases of the input attain each row sum. The kernel is symmetric **algebraically** in \(x,y\), also for complex \(\lambda_S\), so the \(L^1\) norm is the same maximum of absolute column sums.

**2. A two-point convex-order lemma.** For \(\rho\ge1\) let \(W_\rho\) equal \(\rho\) with probability \(1/(1+\rho)\) and \(-1\) otherwise. Let \(V_\rho\) equal \(1/\rho\) with probability \(\rho/(1+\rho)\) and \(-1\) otherwise. Both have expectation zero, while \(V_\rho\in[-1,\rho]\). For any convex \(g:\mathbb R\to\mathbb R\), the chord inequality
\[
g(v)\le\frac{\rho-v}{\rho+1}g(-1)+\frac{v+1}{\rho+1}g(\rho),\qquad -1\le v\le\rho,
\]
combined with \(\mathbb EV_\rho=0\) gives \(\mathbb Eg(V_\rho)\le\mathbb Eg(W_\rho)\). This applies to \(g(v)=\Phi(A+Bv)\) with arbitrary \(A,B\in\mathbb C\). Furthermore, if \(1\le\rho\le\rho'\), the variable \(W_\rho\) also has support in \([-1,\rho']\) and mean zero, so the same chord argument proves \(W_\rho\preceq_{\mathrm{cx}}W_{\rho'}\).

**3. Rare-coordinate replacement.** Fix an index \(i\), all other evaluation coordinates, and all \(Y_j\) with \(j\ne i\). Splitting the kernel into subsets that do and do not contain \(i\) gives
\[
K_\lambda(x,Y)=A+\chi_i(x_i)\chi_i(Y_i)B,
\]
where \(A,B\in\mathbb C\) are independent of \(Y_i\). If \(x_i=r_i\), the product \(\chi_i(x_i)\chi_i(Y_i)\) has law \(W_{\rho_i}\); if \(x_i\ne r_i\), it has law \(V_{\rho_i}\). The convex-order lemma therefore says that replacing one nonrare coordinate of \(x\) by its rare value cannot decrease \(\mathbb E\Phi(K_\lambda(x,Y))\). Repeating this for all coordinates yields the universal ordering without any assumption on which subsets have nonzero coefficients or the signs/phases of those coefficients. At \(x=r\), independence gives \(K_\lambda(r,Y)\overset d=\sum_S\lambda_S\prod_{i\in S}U_i\), proving the exact norm formula. The second convex-order comparison from Step 2, conditioned successively on all other \(U_j\), proves rare-probability monotonicity. No uniqueness of a maximizing point is required.

**4. Quadratic formula.** With homogeneous \(\alpha\), the rare-vertex variables \(U_i\) take the values \(\rho\) and \(-1\) with respective probabilities \(\alpha\) and \(1-\alpha\). If \(J\) counts the \(\rho\)-valued variables, then \(J\sim\operatorname{Bin}(n,\alpha)\) and
\[
\sum_iU_i=\frac{J}{\alpha}-n,
\qquad \sum_iU_i^2=J\rho^2+(n-J).
\]
The identity \(\sum_{i<j}U_iU_j=((\sum_iU_i)^2-\sum_iU_i^2)/2\) gives exactly the displayed binomial expectation for the degree-at-most-two kernel \(1+\sum_iU_i+\sum_{i<j}U_iU_j\).

**5. Sharp asymptotic.** For fixed \(\alpha\in(0,1/2]\), one has \(\mathbb EU_i=0\) and \(\mathbb EU_i^2=\rho\). The central limit theorem gives \(\sum_iU_i/\sqrt{n\rho}\Rightarrow Z\), with \(Z\) standard Gaussian. The law of large numbers gives \(n^{-1}\sum_iU_i^2\to\rho\) in probability. Consequently, the normalized quadratic kernel converges in distribution to \(\rho(Z^2-1)/2\). Its absolute values are uniformly integrable: for fixed \(\alpha\), the fourth moments of the normalized sums are bounded, the second moments of \(n^{-1}\sum_iU_i^2\) are bounded, and the first-order term is negligible in \(L^2\). Hence their first absolute moments converge to \(\rho\mathbb E|Z^2-1|/2=\rho\sqrt{2/(\pi e)}\), as asserted. The fixed-positive-bias condition is essential to this particular central-limit statement.

## Verification
The standalone `verify.py` uses exact rational arithmetic throughout the finite tests. It compares the complete operator-kernel row sums and the rare-vertex formula on \(60\) heterogeneous product spaces with independently chosen signed spectral coefficients, checking \(744\) individual rows; compares two independent finite formulas on \(65\) homogeneous quadratic parameter pairs; and checks \(60\) independent coordinatewise-bias monotonicity instances. A further large-dimension numerical diagnostic at \(\alpha=1/5\), \(n=10000\) gives the normalized Gaussian coefficient \(0.483895011\) versus \(\sqrt{2/(\pi e)}=0.483941449\). These finite computations do not replace the convex-order proof or the asymptotic argument.

## Relationship to prior work
Nayar's 2013 article sets up the normalized biased Fourier basis and proves an FKN-type stability theorem for Boolean functions; it does not establish the endpoint norm or convex ordering of Fourier-diagonal multipliers. O'Donnell's 2014 book gives the biased Fourier product framework, including heterogeneous biases; its foundational discussion does not supply an arbitrary-spectrum universal row-maximization law. Defant, Galicer, Mansilla, Mastyło, and Muro give an integral expression for projection constants and the homogeneous quadratic Gaussian limit on the **uniform** Boolean group. Translation symmetry makes all rows equivalent in that setting; it cannot provide a preferred rare row for nonuniform product measures. Published exact formulas for the second Hamming primitive projector include the special law corresponding to rare probability \(1/q\) at integer \(q\) in the homogeneous, degree-exactly-two case; those special cases are acknowledged as covered, and no separate novelty is claimed for them.

The nearest available related earlier calculation for the canonical affine projector over heterogeneous Bernoulli products already gives its rare-vertex norm and bias monotonicity. That is the special coefficient pattern \(\lambda_S=\mathbf1_{\{|S|\le1\}}\) and is **not** claimed as new. The present theorem covers the entire Fourier multiplier algebra, including arbitrarily sparse, asymmetric, high-degree, signed and complex spectral patterns; its single universal norming vertex and joint convex ordering hold independently of the chosen coefficients. The finite homogeneous quadratic example only illustrates this structural extension.

## Limitations
This is a finite-product theorem; it does not directly treat infinite products, nonproduct measures or non-Fourier-diagonal operators. No uniqueness of the rare-vertex extremizer is claimed. The Gaussian limit fixes the bias parameter as dimension grows and gives no uniform rate as \(\alpha\downarrow0\). The statement does not identify the **minimum** norm among all possible projections onto a spectral subspace. The universal chord argument is short, and an equivalent result under a general convex-order or product-experiment formulation could be unindexed in older literature. The earlier affine projector case and uniform-group projection formulas are explicitly excluded from novelty claims. No independent validation has been performed.

## References
1. P. Nayar, *FKN Theorem on the biased cube*, arXiv:1311.3179v1, publicly posted 13 November 2013; Colloquium Mathematicum 137 (2014), 253–261. https://arxiv.org/abs/1311.3179
2. R. O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press, 2014, Section 8.4 (biased Fourier analysis); electronic full text at https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf
3. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233, especially Theorems 3.1 and 4.1. https://arxiv.org/abs/2302.00233
4. *A lattice-phase second term for second-chaos projection constants on the Boolean cube*, published 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-lattice-phase-second-term-for-second-chaos-projection-constant--ec79809353f9
5. *Exact degree-two Hamming projection norms and the Gaussian–Poisson crossover*, published 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-degree-two-hamming-projection-norms-and-the-gaussian-poiss--cd09d9ad5ea2
