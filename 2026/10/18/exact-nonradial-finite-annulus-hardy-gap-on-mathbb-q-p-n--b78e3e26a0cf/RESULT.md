# Exact nonradial finite-annulus Hardy gap on \(\mathbb Q_p^n\)

## Finding
Fix a prime \(p\), an integer \(n\ge1\), and a real order \(0<\alpha<n\). Write \(\|x\|_p=\max_j|x_j|_p\), normalize Haar measure by \(|\mathbb Z_p^n|=1\), and put
\[
C_{n,\alpha}=\frac{p^\alpha-1}{1-p^{-n-\alpha}},\qquad
C_{p,n,\alpha}^{\sharp}=\left(\frac{1-p^{-(n-\alpha)/2}}{1-p^{-(n+\alpha)/2}}\right)^2.
\]
For a Bruhat--Schwartz function \(u\) define
\[
\mathcal E_\alpha[u]=\frac{C_{n,\alpha}}2\iint\frac{|u(x)-u(y)|^2}{\|x-y\|_p^{n+\alpha}}\,dx\,dy,\quad
W_\alpha[u]=\int\|x\|_p^{-\alpha}|u(x)|^2\,dx,
\quad \Delta_\alpha[u]=\mathcal E_\alpha[u]-C_{p,n,\alpha}^{\sharp}W_\alpha[u].
\]
For any integer \(K\) and any integer \(M\ge1\), let \(S_k=\{x:\|x\|_p=p^{-k}\}\) and \(A_{K,M}=\bigcup_{j=0}^{M-1}S_{K+j}\). Set
\[
r=p^{-(n+\alpha)/2},\qquad B=C_{n,\alpha}(1-p^{-n}),\qquad s=\frac{1+r}{1-r}.
\]
There is a unique \(\theta_M\in(0,\pi/(M+1))\) satisfying
\[
\cos\!\left(\frac{M+1}{2}\theta_M\right)
=r\cos\!\left(\frac{M-1}{2}\theta_M\right).
\]
Then the **sharp full (not only radial) annular Hardy improvement** is
\[
\boxed{\ \mathcal E_\alpha[u]\ge (C_{p,n,\alpha}^{\sharp}+\mu_M)W_\alpha[u]\quad
(\operatorname{supp}u\subseteq A_{K,M}),\ }
\]
where
\[
\boxed{\ \mu_M=B\left[s-\frac{1-r^2}{1-2r\cos\theta_M+r^2}\right].\ }
\]
The value is independent of the annulus location \(K\). Equality for nonzero \(u\) holds **only** for scalar multiples of the radial function
\[
u_*(x)=\|x\|_p^{-(n-\alpha)/2}\cos\!\left(\left(j-\frac{M-1}{2}\right)\theta_M\right),\qquad x\in S_{K+j},\ 0\le j<M,
\]
continued by zero outside the annulus. In particular no angular, nonradial competitor can improve the radial infimum.

There is also an **exact full-function stability identity**. Set \(h(x)=\|x\|_p^{-(n-\alpha)/2}\) and \(\phi(x)=u_*(x)/h(x)\) on the annulus. For every such \(u\),
\[
\boxed{\begin{aligned}
\Delta_\alpha[u]-\mu_M W_\alpha[u]
=\frac{C_{n,\alpha}}2\iint_{A_{K,M}^2}
\frac{h(x)h(y)\phi(x)\phi(y)}{\|x-y\|_p^{n+\alpha}}
\left|\frac{u(x)}{h(x)\phi(x)}-\frac{u(y)}{h(y)\phi(y)}\right|^2\,dx\,dy.
\end{aligned}}
\]
Finally the exact finite-width gap is strictly decreasing in \(M\) and satisfies the sharp asymptotic
\[
\boxed{\ \mu_M=\frac{B\,\pi^2r(1+r)}{(1-r)^3(M+s)^2}+O_{p,n,\alpha}(M^{-4}).\ }
\]
Thus \(\lim_{M\to\infty}M^2\mu_M=B\pi^2r(1+r)/(1-r)^3\).

## Assumptions and scope
All scalar-valued functions may be complex. The energy and Fourier normalization are those of Sun, arXiv:2610.04463v1. The assertion holds for every Bruhat--Schwartz function supported on the complete union of exactly \(M\) consecutive valuation shells; it imposes **no radiality assumption**. Such annuli exclude the origin, and all displayed integrals are finite. The equality profile is locally constant and compactly supported, hence is an admissible test function. The theorem does not address nonconsecutive shell masks, nonquadratic exponents, or functions extending outside the annulus.

## Proof
**1. Ground state and shell normalization.** Sun's exact quadratic ground-state representation gives
\[
\Delta_\alpha[u]=\frac{C_{n,\alpha}}2\iint
\frac{h(x)h(y)}{\|x-y\|_p^{n+\alpha}}\,|v(x)-v(y)|^2\,dx\,dy,
\qquad v=u/h.
\]
If \(v=a_k\) on the full shell \(S_k\), with finite support, then \(|S_k|=(1-p^{-n})p^{-nk}\), \(\|x-y\|_p=p^{-\min(k,\ell)}\) for \(x\in S_k, y\in S_\ell, k\ne\ell\), and
\[
\Delta_\alpha[ha]=C_{n,\alpha}(1-p^{-n})^2
\sum_{k<\ell}r^{\ell-k}|a_k-a_\ell|^2,
\quad W_\alpha[ha]=(1-p^{-n})\sum_k|a_k|^2.
\]
The omitted same-shell integrals vanish for shell-constant \(a\). Extend a length-\(M\) vector \(a\) by zero outside its shell interval. The translation energy is
\[
\sum_{k<\ell\in\mathbb Z}r^{\ell-k}|a_k-a_\ell|^2
=\frac{2r}{1-r}\sum_{j=0}^{M-1}|a_j|^2
-\sum_{\substack{0\le i,j<M\\i\ne j}}r^{|i-j|}\overline{a_i}a_j.
\]
Consequently the radial Rayleigh matrix for \(\Delta_\alpha/W_\alpha\) is
\[
B\bigl(s I_M-T_M(r)\bigr),\qquad (T_M(r))_{ij}=r^{|i-j|}.
\]
This identity is the shell reduction, not yet the claimed nonradial optimality.

**2. Exact Perron eigenvalue.** For \(M\ge2\), \(T_M(r)^{-1}\) is the tridiagonal matrix with diagonal \((1,1+r^2,\ldots,1+r^2,1)/(1-r^2)\) and adjacent entries \(-r/(1-r^2)\). Put
\[
a_j=\cos\!\left(\left(j-\frac{M-1}2\right)\theta\right),\qquad 0\le j<M.
\]
The interior tridiagonal recurrence gives inverse eigenvalue
\((1-2r\cos\theta+r^2)/(1-r^2)\), while both endpoint equations reduce to \(\cos((M+1)\theta/2)=r\cos((M-1)\theta/2)\). On \((0,\pi/(M+1))\), the ratio of these cosines decreases strictly from \(1\) to \(0\), so the root exists uniquely. All components \(a_j\) are strictly positive; Perron--Frobenius therefore identifies the corresponding eigenvalue as the largest eigenvalue of the entrywise positive matrix \(T_M(r)\). For \(M=1\), the same formula follows directly from \(T_1(r)=[1]\) and \(\cos\theta_1=r\). The resulting radial minimum is exactly \(\mu_M\), uniquely attained by the positive vector \(a\) up to scalars.

**3. Extension to every angular mode.** Let \(A=A_{K,M}\). Define \(\phi=a_j>0\) on the shell \(S_{K+j}\) and set \(\phi=0\) on its complement. Let \(w(x)=\|x\|_p^{-n}\) and \(J(x,y)=h(x)h(y)/\|x-y\|_p^{n+\alpha}\). For \(x\in A\), the integral \(\int J(x,y)(\phi(x)-\phi(y))\,dy\) converges absolutely: its integrand is zero on the entire shell containing \(x\), and all other shells have summable geometric weights. The ultrametric shell calculation in step 1 yields **pointwise on every shell**
\[
C_{n,\alpha}\int J(x,y)(\phi(x)-\phi(y))\,dy
=\mu_M w(x)\phi(x).
\]
Now write \(v=\phi g\) inside \(A\), with \(v=0\) outside. The algebraic identity
\[
|\phi(x)g(x)-\phi(y)g(y)|^2-\phi(x)\phi(y)|g(x)-g(y)|^2
=(\phi(x)-\phi(y))\bigl(\phi(x)|g(x)|^2-\phi(y)|g(y)|^2\bigr)
\]
holds for real positive \(\phi\) and complex \(g\). Integrate symmetrically against \(C_{n,\alpha}J/2\) on the full product space, taking the second integrand as zero when either point lies outside \(A\). The preceding pointwise eigen-equation turns the right-hand side into \(\mu_M\int_A w|v|^2=\mu_MW_\alpha[u]\). The remaining term is precisely the nonnegative double integral displayed in the Finding. This proves the sharp inequality for **all** test functions, without replacing a function by its radial average.

For almost every distinct pair of points in \(A\), the kernel \(J(x,y)\phi(x)\phi(y)\) is strictly positive. Thus equality in the stability identity forces \(g\) to be a single scalar almost everywhere on the whole annulus, giving exactly the claimed radial equality class. The explicitly displayed \(u_*\) attains equality, proving sharpness.

**4. Monotonicity and the sharp width coefficient.** Strict increase of \(\lambda_{\max}(T_M(r))\) under the principal block extension \(M\mapsto M+1\) follows from the positive Perron vector and the nonzero added positive cross-column: equality in Rayleigh interlacing would require a zero-padded top eigenvector to be an eigenvector of the larger matrix, which it is not. Hence \(\mu_M\) strictly decreases. Rewriting the endpoint equation gives
\[
M\theta_M+2\arctan\!\left(s\tan\frac{\theta_M}2\right)=\pi.
\]
With fixed \(0<r<1\), Taylor expansion gives
\(\theta_M=\pi/(M+s)+O_r(M^{-4})\). Finally
\[
s-\frac{1-r^2}{1-2r\cos\theta+r^2}
=\frac{r(1+r)}{(1-r)^3}\theta^2+O_r(\theta^4).
\]
These identities establish the asserted two-term shifted-width approximation with \(O(M^{-4})\) error and the sharp leading coefficient.

## Verification
The standalone standard-library checker `checker.py` evaluates the unique angle by bisection, reconstructs the Perron eigenvector and its matrix residual, compares Rayleigh quotients for signed test vectors, checks the shifted-width asymptotic numerically, and tests a genuine nonradial one-shell perturbation. It passed 858 finite diagnostics at primes \(2,3,5,7\), several dimensions and fractional orders, and widths up to \(2500\). These are finite diagnostics, not a proof of the infinite-dimensional statement. The analytic ground-state identity and all-\(M\) Perron argument supply that proof.

## Relationship to prior work
Sun (arXiv:2610.04463v1, October 3, 2026) proves the global sharp quadratic Hardy inequality, the precise ground-state representation and annular minimizing sequences. A published mathematical result titled *Quadratic radial annular stability for the p-adic sharp Hardy deficit* (record identifier ending `0555d4d60a6a`, October 11, 2026) supplies the exact radial shell translation energy and two-sided nonsharp bounds of order \(M^{-2}\), while explicitly limiting its claim to radial functions. The present theorem determines the **sharp exact constant for each width** and proves that it also governs **all nonradial functions**, with a complete equality classification and a nonradial stability identity. Classical Kac--Murdock--Szegő spectral formulas provide the matrix evaluation; no novelty is claimed for the Toeplitz eigenvalue technique itself. Earlier work on hierarchical Schrödinger operators with singular potentials concerns critical coupling and Green functions rather than this exact finite-annulus functional inequality.

## Limitations
Only quadratic fractional energies with \(0<\alpha<n\) and a union of consecutive full \(p\)-adic valuation shells are treated. The theorem makes no claim about the full complex spectrum of the underlying Schrödinger operator, arbitrary nonconsecutive masks, arbitrary ultrametric spaces, or nonlinear \(L^q\) energies. The eigenvalue calculation uses established finite Toeplitz theory; the application to the sharp nonradial annular functional inequality is the claim. Independent specialist priority assessment has not been performed.

## References
1. Y. Sun, *Sharp Hardy inequalities for the Vladimirov--Taibleson operator on \(\mathbb Q_p^n\)*, arXiv:2610.04463v1 (first public October 3, 2026), Theorem 1.1 and Section 3.
2. *Quadratic radial annular stability for the p-adic sharp Hardy deficit*, published mathematical result, record `0555d4d60a6a` (October 11, 2026); radial shell identity, bounds and stated limitations.
3. M. Kac, W. L. Murdock and G. Szegő, *On the Eigen-values of Certain Hermitian Forms*, Journal of Rational Mechanics and Analysis 2 (1953), 767--800.
4. N. J. Higham, *What Is the Kac--Murdock--Szegő Matrix?* (July 6, 2021), explicit tridiagonal inverse, https://nhigham.com/2021/07/06/what-is-the-kac-murdock-szego-matrix/.
5. A. Bendikov, A. Grigor'yan and S. Molchanov, *Hierarchical Schrödinger Operators with Singular Potentials*, Proceedings of the Steklov Institute of Mathematics 323 (2023), 12--46.
