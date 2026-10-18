# Exact Calkin power norms and Perron spectral disks for toric bidisc composition

## Finding

Let \(A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) be a \(2\times2\) matrix with **strictly positive integer entries** and \(\det A\ne0\). Set \(\varphi_A(z_1,z_2)=(z_1^az_2^c,z_1^bz_2^d)\) and \(C_Af=f\circ\varphi_A\). Let \(\rho(A)>1\) be the Perron eigenvalue of \(A\). On the normalized weighted bidisc Bergman space \(A^2_\beta(\mathbb D^2)\), for every real \(\beta>-1\), put \(\delta=\beta+1\). The same statements hold at \(\beta=-1\) for the Hardy space \(H^2(\mathbb D^2)\), with \(\delta=0\).

For **every integer \(n\ge1\)**, writing \(A^n=\begin{pmatrix}a_n&b_n\\c_n&d_n\end{pmatrix}\),
\[
\boxed{\|C_A^n\|_{\mathrm{ess}}=(\sqrt{a_nd_n}+\sqrt{b_nc_n})^{-\delta}.}
\]
Moreover,
\[
\boxed{r_{\mathrm{ess}}(C_A)=\rho(A)^{-\delta},\qquad
\sigma_{\mathrm{ess}}(C_A)=\{\lambda\in\mathbb C:|\lambda|\le\rho(A)^{-\delta}\},}
\]
and
\[
\boxed{\sigma(C_A)=\{1\}\cup\{\lambda\in\mathbb C:|\lambda|\le\rho(A)^{-\delta}\}.}
\]
Here \(\sigma_{\mathrm{ess}}\) is the Fredholm essential spectrum. If \(\beta>-1\), the projection \(P_0f=f(0,0)\cdot1\) satisfies
\[
\|C_A^n-P_0\|=\Theta_{A,\beta}(\rho(A)^{-n\delta}),
\]
so \(1\) is a simple isolated eigenvalue. On the Hardy endpoint, \(\|C_A^n-P_0\|=1\) for every \(n\ge1\): the nonconstant subspace is an isometric rather than an operator-norm mixing component.

In particular, for \(A=\begin{pmatrix}1&1\\1&2\end{pmatrix}\), where \(\rho(A)=(3+\sqrt5)/2\), and the Fibonacci numbers satisfy \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\),
\[
\|C_A^n\|_{\mathrm{ess}}=(\sqrt{F_{2n}^2+1}+F_{2n})^{-\delta}
\sim(\sqrt5/2)^\delta\,\rho(A)^{-n\delta}.
\]

## Assumptions and scope

The weighted Bergman norm uses the probability measure \((\beta+1)(1-|z|^2)^\beta\,dA(z)/\pi\) on each disc, where \(dA\) is unnormalized planar area; the bidisc measure is the product. At \(\beta=-1\) we use boundary Haar measure on the torus, not a formal integral with zero prefactor. The matrix must have four positive integer entries and nonzero determinant. The determinant condition ensures disjoint monomial images, and strict positivity ensures an expanding rooted-orbit decomposition. Neither assumption is claimed unnecessary.

The one-variable monomial moments and their Hardy endpoint are
\[
h_\beta(j)=\frac{\Gamma(\beta+2)\Gamma(j+1)}{\Gamma(j+\beta+2)}\quad(\beta>-1),\qquad h_{-1}(j)=1,
\]
for nonnegative integers \(j\). The normalized monomials \(e_{m,k}=z_1^mz_2^k/\sqrt{h_\beta(m)h_\beta(k)}\) form an orthonormal basis. The essential norm means distance to the compact operators; the essential spectral radius is the spectral radius of the Calkin class.

## Proof

**1. Weighted-monomial model and the Calkin norm.** For \(\nu=(m,k)\in\mathbb N_0^2\), composition gives
\[
C_Ae_\nu=w_A(\nu)e_{A\nu},\qquad
w_A(\nu)^2=\frac{h_\beta((A\nu)_1)h_\beta((A\nu)_2)}{h_\beta(m)h_\beta(k)}.
\]
The same holds with \(A^n\) for \(C_A^n\). Distinct input multiindices have distinct output multiindices because \(\det A\ne0\). Each component of \(A\nu\) is at least \(m+k\), so the decreasing property of \(h_\beta\) shows \(0<w_A(\nu)\le1\). Thus \(C_A\) is a norm-one contraction because it fixes the constant monomial. Since the nonzero columns are orthogonal, removing finitely many columns gives optimal compact approximations, and
\[
\|C_A^n\|_{\mathrm{ess}}=\limsup_{m+k\to\infty}w_{A^n}(m,k).
\]
For \(\beta=-1\) every weight is \(1\), proving the formula immediately. Henceforth let \(\delta>0\). The gamma quotient satisfies \(h_\beta(j)=\Gamma(\beta+2)j^{-\delta}(1+O(j^{-1}))\) as \(j\to\infty\) and \(h_\beta(j)\asymp(j+1)^{-\delta}\) uniformly for nonnegative integers.

Fix \(B=A^n=\begin{pmatrix}u&v\\w&s\end{pmatrix}\), whose entries are all positive. Along rays \((m,k)\to\infty\) with \(m/k\to t\in(0,\infty)\), the squared weights tend to
\[
\left[\frac{t}{(ut+v)(wt+s)}\right]^\delta.
\]
When the ratio tends to \(0\) or \(\infty\), the same uniform gamma bounds force the weights to tend to \(0\), including when one coordinate remains bounded. Thus the essential norm is the global positive-ray maximum. Minimizing
\[
\frac{(ut+v)(wt+s)}t=uwt+(us+vw)+\frac{vs}{t}
\]
over \(t>0\) gives the unique optimizer \(t=\sqrt{vs/(uw)}\) and minimum \((\sqrt{us}+\sqrt{vw})^2\). Substituting proves the exact essential-norm formula for every positive power.

**2. Perron growth and operator-norm mixing.** Because \(A\) is strictly positive, its Perron eigenvalue \(\rho>1\) is simple, has strictly positive left and right eigenvectors, and the other eigenvalue has modulus strictly below \(\rho\). Therefore all four entries of \(A^n\) lie between positive constant multiples of \(\rho^n\) for every \(n\ge1\). The exact formula above gives \(r_{\mathrm{ess}}(C_A)=\lim_n\|C_A^n\|_{\mathrm{ess}}^{1/n}=\rho^{-\delta}\).

For nonzero \(\nu=(m,k)\), the gamma-moment comparison and the componentwise lower bound \((A^n\nu)_i\ge c\rho^n(m+k)\) yield
\[
w_{A^n}(\nu)^2\le K\rho^{-2n\delta}
\left[\frac{(m+1)(k+1)}{(m+k)^2}\right]^\delta\le K'\rho^{-2n\delta}.
\]
The subspace \(H_0=\overline{\operatorname{span}}\{e_{m,k}:m+k>0\}\) is reducing, and \(C_A=P_0\oplus T\), where \(P_0\) acts as the identity on the one-dimensional constants. Hence \(\|T^n\|\le K''\rho^{-n\delta}\). For fixed \(\nu=(1,0)\), Perron asymptotics of both coordinates of \(A^n\nu\), together with the gamma quotient, give \(w_{A^n}(\nu)\asymp\rho^{-n\delta}\). This proves \(\|T^n\|\asymp\rho^{-n\delta}\), and consequently \(r(T)=\rho^{-\delta}\). At \(\delta=0\), \(T\) is an isometry and \(\|T^n\|=1\).

**3. Infinite unilateral-shift chains.** Since \(A\) has four positive integers, for nonzero \(\nu\), \(|A\nu|_1\ge2|\nu|_1\). There are no nonzero periodic orbits, and backward iteration along an existing integral predecessor must terminate. Injectivity gives a unique decomposition of \(\mathbb N_0^2\setminus\{0\}\) into disjoint one-sided orbits \(\{\nu_0,A\nu_0,A^2\nu_0,\ldots\}\), indexed by roots outside \(A\mathbb N_0^2\). There are infinitely many roots, for example every \((m,0)\) with \(m\ge1\).

On each chain, \(T\) is a unilateral weighted shift with weight sequence \(w_A(A^j\nu_0)\). Perron asymptotics and regular variation of \(h_\beta\) imply
\[
\lim_{j\to\infty}w_A(A^j\nu_0)=r:=\rho^{-\delta}>0.
\]
In the Hardy case the weights are identically one. A unilateral weighted shift whose positive weights tend to \(r\) has an adjoint eigenvector for every \(|\lambda|<r\): writing the adjoint recurrence recursively yields coefficients with eventually geometric ratio less than one. It is also a compact perturbation of \(rS\), where \(S\) is the unilateral shift. Thus its essential spectrum contains the circle \(|\lambda|=r\).

Every \(|\lambda|<r\) belongs to the spectrum of \(T\) (indeed the adjoint has eigenvectors on every one of infinitely many orthogonal chains). Conversely \(r(T)=r\), so \(\sigma(T)=\{\lambda:|\lambda|\le r\}\). For \(|\lambda|<r\), infinitely many independent adjoint eigenvectors mean \(T-\lambda\) is not Fredholm. For \(|\lambda|=r\), any one reducing chain is a compact perturbation of \(rS\) and is non-Fredholm; therefore the full direct sum is non-Fredholm. For \(|\lambda|>r\), \(T-\lambda\) is invertible. The extra constant one-dimensional block never changes Fredholmness, so \(\sigma_{\mathrm{ess}}(C_A)=\{\lambda:|\lambda|\le r\}\). Adding the constant eigenvalue gives the claimed full spectrum.

**4. Fibonacci example.** For \(A=\begin{pmatrix}1&1\\1&2\end{pmatrix}\), induction gives \(A^n=\begin{pmatrix}F_{2n-1}&F_{2n}\\F_{2n}&F_{2n+1}\end{pmatrix}\). Cassini's identity gives \(F_{2n-1}F_{2n+1}=F_{2n}^2+1\). Finally \(F_{2n}\sim\rho^n/\sqrt5\) implies \(\sqrt{F_{2n}^2+1}+F_{2n}\sim2\rho^n/\sqrt5\), proving the displayed closed form and constant.

## Verification

The derivation uses exact orthogonal-column singular values, the gamma quotient asymptotic, a one-variable maximization, the Perron–Frobenius theorem, and elementary weighted-shift Fredholm theory. The standalone script `CHECK.py` runs 3,203 finite diagnostics across positive invertible integer matrices, five radial exponents (including the Hardy endpoint), power-matrix identities, large-degree weight limits, and the Fibonacci closed formula. It returns `PASS: 3203 finite diagnostic checks; no infinite-proof certification.` The infinite-dimensional claims rest on the analytic arguments above, not on the numerical tests.

## Relationship to prior work

Bayart and Dorval's 2026 paper gives boundedness criteria for smooth polydisc composition operators, particularly on weighted Bergman spaces. Dorval's subsequent 2026 paper gives compactness criteria for such operators. Kosiński's earlier work supplies boundedness/rank conditions for Hardy and Bergman polydisc composition. The current result concerns an explicit, strictly positive integral monomial subfamily and gives the exact **all-power essential norms**, full **Fredholm essential spectrum**, and a **Hardy/Bergman power-convergence dichotomy**, conclusions not stated in the inspected results of those articles. The monomial orthogonal-column reduction is elementary; the formulas and entire spectral classification rely on the further optimization and orbit/Perron analysis. This priority assessment is not a proof that no earlier equivalent computation exists.

## Limitations

The theorem applies only to strictly positive, nonsingular, integral \(2\times2\) exponent matrices and normalized product radial weights of the specified forms. It does not treat singular matrices, zero exponent entries, other polydisc dimensions, mixed coordinate weights, non-Hilbert spaces, or arbitrary toric symbols. The numerical diagnostic script does not independently certify infinite-dimensional reasoning. A historical equivalent under generalized weighted-permutation or semigroup-composition terminology remains a publication-priority risk. Independent scientific audit has not been performed.

## References

1. Frédéric Bayart and Anne Dorval, *Composition operators on weighted Bergman spaces of the polydisc*, arXiv:2601.19308v1 (first publicly posted January 27, 2026), https://arxiv.org/abs/2601.19308.
2. Anne Dorval, *Compactness of composition operator on weighted Bergman spaces of the polydisc*, arXiv:2606.29969v1 (first publicly posted June 29, 2026), https://arxiv.org/html/2606.29969v1.
3. Łukasz Kosiński, *Composition operators on the polydisc*, arXiv:2206.14758v1 (first publicly posted June 29, 2022), https://arxiv.org/abs/2206.14758.
4. Clos, Čučković, and Şahutoğlu, *Compactness of composition operators on the Bergman space of the bidisc*, arXiv:2409.09529 (first publicly posted September 2024), https://arxiv.org/html/2409.09529v2.
5. Beslikas, *Composition operators and rational inner functions on the bidisc*, arXiv:2412.16593 (first publicly posted December 2024), https://arxiv.org/html/2412.16593v3.
