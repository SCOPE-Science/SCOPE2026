# Exact eigenvalue coefficient for geometric atomic Helson matrices

## Finding

Fix parameters \(q>1\), \(\varepsilon>0\), and \(r>0\). Define \(\delta_j=\varepsilon q^{-j}\), \(s_j=\tfrac12+\delta_j\), and the finite positive atomic measure
\[
\mu=\sum_{j=1}^{\infty}2\delta_jj^{-r}\,\delta_{s_j}.
\]
For integers \(m,n\ge1\), define the multiplicative Hankel (Helson) matrix
\[
H_{mn}=\alpha(mn),\qquad
\alpha(N)=\sum_{j=1}^{\infty}2\delta_jj^{-r}N^{-s_j}.
\]
This matrix defines a positive compact operator \(H\) on \(\ell^2(\mathbb N)\). Put \(a=(\log q)/2\) and define the strictly positive, continuous periodic symbol
\[
f_q(\theta)=\sum_{k\in\mathbb Z}\frac{e^{ik\theta}}{\cosh(ak)}
=\frac{\pi}{a}\sum_{m\in\mathbb Z}
\frac{1}{\cosh\!\left(\frac{\pi(\theta+2\pi m)}{2a}\right)}.
\]
With eigenvalues listed in nonincreasing order, including multiplicity, the exact asymptotic is
\[
\boxed{\lim_{n\to\infty}n^r\lambda_n(H)
=\left(\frac1{2\pi}\int_{-\pi}^{\pi}f_q(\theta)^{1/r}\,d\theta\right)^r.}
\]
The coefficient is independent of the initial boundary scale \(\varepsilon\). In particular, the following are equivalent for every \(p>0\): \(H\in\mathcal S_p\) and \(pr>1\). At \(p=1/r\) the operator belongs to the weak Schatten class \(\mathcal S_{p,\infty}\), but not to \(\mathcal S_p\). Furthermore,
\[
\lim_{N\to\infty}\frac{1}{\log N}\sum_{n=1}^{N}
\lambda_n(H)^{1/r}=\frac1{2\pi}\int_{-\pi}^{\pi}f_q(\theta)^{1/r}\,d\theta.
\]
For \(r=1\), the leading eigenvalue coefficient is exactly \(1\) for every \(q>1\). For \(r=\tfrac12\) it equals
\[
\left(1+2\sum_{k=1}^{\infty}\operatorname{sech}^{2}(ak)\right)^{1/2}.
\]

## Assumptions and scope

The sequence indices \(j,m,n\) begin at \(1\). Parameters \(q,\varepsilon,r\) are fixed, independent of the eigenvalue index. The symbol uses the Fourier convention \(f_q(\theta)=\sum_{k\in\mathbb Z}c_ke^{ik\theta}\), where \(c_k=\operatorname{sech}(ak)\). All spectral asymptotics concern the single infinite-dimensional compact positive operator, not the eigenvalues of an arbitrary growing finite truncation. Positivity and compactness of \(H\) are proved below; no prior boundedness assumption is necessary. The Schatten statement for \(p<1\) refers to the usual quasi-ideal defined by \(\sum_n s_n(H)^p<\infty\).

## Proof

**1. Gram reduction and the exactly identified limiting kernel.** Let \(u_j\in\ell^2(\mathbb N)\) be the vector \(u_j(n)=\sqrt{2\delta_j}\,n^{-s_j}\). For each finite vector \(c\), the squared norm of \(\sum_jc_ju_j\) is the quadratic form of
\[
G_{jk}=2\sqrt{\delta_j\delta_k}\,\zeta(1+\delta_j+\delta_k).
\]
The integral test for the decreasing function \(x^{-1-t}\), \(t>0\), gives the uniform inequality
\[
0\le\zeta(1+t)-\frac1t\le1.
\]
Consequently \(G=K+E\), where
\[
K_{jk}=\frac{2\sqrt{\delta_j\delta_k}}{\delta_j+\delta_k}
=\operatorname{sech}(a(j-k)),\qquad
|E_{jk}|\le2\sqrt{\delta_j\delta_k}.
\]
Because \(\sum_j\delta_j<\infty\), the operator \(E\) is Hilbert--Schmidt. Moreover \(K\) is a bounded Toeplitz operator: its diagonal Fourier coefficients are absolutely summable. Thus \(G\) is bounded and the map \(B:\ell^2(\mathbb N)\to\ell^2(\mathbb N)\) initially defined by \(Be_j=u_j\) extends to a bounded operator. Write \(D=\operatorname{diag}(j^{-r})\), a positive compact operator. The proposed matrix is exactly \(H=BDB^*\), hence defines a bounded positive compact operator. Its nonzero eigenvalues, including multiplicities, agree with those of
\[
A=D^{1/2}GD^{1/2}=A_0+R,\quad
A_0=D^{1/2}KD^{1/2},\quad R=D^{1/2}ED^{1/2}.
\]

**2. Strict positivity of the Toeplitz symbol and control of the remainder.** Put \(a=(\log q)/2>0\). The Fourier transform of \(x\mapsto\operatorname{sech}(ax)\) is \(\xi\mapsto(\pi/a)\operatorname{sech}(\pi\xi/(2a))\); integration after the substitution \(u=e^{2ax}\) proves this transform by the beta integral. Poisson summation, justified by exponential decay of both functions, yields the displayed second representation of \(f_q\). Every summand is positive, so \(0<\min f_q\le\max f_q<\infty\), and \(K=T(f_q)\ge(\min f_q)I\).

If \(P_J\) projects onto the first \(J\) coordinates, the entry bound for \(R\) and \(r>0\) imply
\[
\|R-P_JRP_J\|_{\mathcal S_2}^2
\le4\sum_{\substack{j,k\ge1\\\max(j,k)>J}}
\delta_j\delta_kj^{-r}k^{-r}=O(q^{-J}).
\]
Therefore \(s_{J+1}(R)=O(q^{-J/2})\). In particular \(R\) is spectrally negligible at every polynomial eigenvalue scale.

**3. Weighted Toeplitz eigenvalue counting lemma.** We prove the following special case, rather than invoking a spectral-asymptotic theorem. If \(f\) is strictly positive and continuous on the circle, with absolutely summable Fourier coefficients, then the compact positive operator \(A_f=D^{1/2}T(f)D^{1/2}\), with \(D=\operatorname{diag}(j^{-r})\), satisfies
\[
\lim_{t\downarrow0}t^{1/r}N(t;A_f)
=\frac1{2\pi}\int_{-\pi}^{\pi}f(\theta)^{1/r}\,d\theta,
\quad N(t;A_f)=\#\{n:\lambda_n(A_f)>t\}.
\]
First, approximate \(f\) uniformly by real trigonometric polynomials \(g\) with \(g>0\). For \(\eta>\|f-g\|_\infty\), the operator inequalities \(A_{g-\eta}\le A_f\le A_{g+\eta}\) follow from positivity of Toeplitz quadratic forms. It suffices to prove the asserted limit for strictly positive real trigonometric polynomials, then let \(\eta\downarrow0\).

Fix such a \(g\) with bandwidth \(L\). Set \(t=M^{-r}\), \(M\to\infty\). Remove indices \(j\le hM\), which changes every eigenvalue counting function by at most \(\lfloor hM\rfloor\), for any \(h>0\). Remove the tail \(j>RM\), where \(R>\|g\|_\infty^{1/r}\): the tail compression has norm at most \(R^{-r}\|g\|_\infty M^{-r}<t\), and cutting the cross-boundary couplings changes the counting function by at most \(2L\). On the remaining indices in \([hM,RM]\), partition into consecutive blocks of length \(\lfloor M^{1/2}\rfloor\). Deleting all off-block entries is a self-adjoint perturbation of rank at most \(2L\) per boundary, hence total rank \(o(M)\). On each block the matrix \(M^rD^{1/2}T(g)D^{1/2}\) differs in norm by \(o(1)\), uniformly for \(hM\le j\le RM\), from \((j_0/M)^{-r}T_b(g)\), where \(j_0\) is the block's first index and \(T_b(g)\) is its \(b\)-by-\(b\) Toeplitz matrix. Indeed, relative changes of \(j^{-r/2}\) across a block are \(O(b/(hM))\).

For each fixed real polynomial symbol \(g\), the finite Toeplitz eigenvalue distribution converges to the pushforward of uniform angular measure by \(g\). To see this without a black-box theorem, the normalized traces of every fixed power of \(T_b(g)\) converge to the constant Fourier coefficient of the corresponding power of \(g\): only the uniformly bounded number of boundary rows differs from the translation-invariant Laurent product. Polynomial approximation on the common bounded spectral interval then yields convergence for continuous test functions. For the threshold comparison at a given macroscopic position \(x>0\), discontinuity may occur only where \(g(\theta)=x^r\); integrated over \(x\in[h,R]\), this exceptional set has planar measure zero by Fubini. Hence the normalized block count converges to
\[
\int_h^R\frac1{2\pi}\left|\{\theta:g(\theta)>x^r\}\right|dx.
\]
The head contributes at most \(h\) to the normalized count; the tail contributes none, and every deleted boundary contributes \(o(1)\). Letting \(h\downarrow0\), \(R\uparrow\infty\), and applying Tonelli's theorem gives the exact count \((2\pi)^{-1}\int g(\theta)^{1/r}d\theta\). Sandwiching between \(g\pm\eta\) and using uniform convergence proves the lemma for \(f\).

**4. Inversion and the small remainder.** Put \(C_{q,r}=(2\pi)^{-1}\int f_q^{1/r}\). The counting lemma gives \(N(t;A_0)\sim C_{q,r}t^{-1/r}\); monotone inversion yields \(\lambda_n(A_0)\sim C_{q,r}^{r}n^{-r}\). Choose \(k_n=\lceil\sqrt n\rceil\). The bound from step 2 yields \(s_{k_n}(R)=o(n^{-r})\). Weyl--Ky Fan inequalities sandwich \(\lambda_n(A_0+R)\) between \(\lambda_{n+k_n}(A_0)-s_{k_n}(R)\) and \(\lambda_{n-k_n}(A_0)+s_{k_n}(R)\), up to harmless index offsets. Both bounds have the same leading asymptotic. Since \(H\) and \(A\) have the same positive eigenvalues, the boxed formula follows.

**5. Ideal classification and explicit constants.** Since the coefficient is strictly positive, \(s_n(H)\sim C_{q,r}^{r}n^{-r}\); comparison with the \(p\)-series proves the Schatten and weak-endpoint claims for every \(p>0\). Raising to the power \(1/r\) and comparing with the harmonic series proves the logarithmic residue. Finally, Parseval gives \((2\pi)^{-1}\int f_q=1\) and \((2\pi)^{-1}\int f_q^2=\sum_{k\in\mathbb Z}\operatorname{sech}^2(ak)\), proving the two special coefficients.

## Verification

The accompanying `verify.py` checks the hyperbolic-secant covariance identity, the uniform zeta-remainder bound on specified finite pairs, positivity and Fourier moments of the symbol by numerical quadrature, and finite Toeplitz eigenvalue behavior for two distinct values of \(r\). Its output reports the examined finite dimensions and tolerances. The infinite-dimensional asymptotic follows from the analytic counting argument, not from these numerical checks. No external proof assistant or independent mathematical audit was used.

## Relationship to prior work

Ma, Lu, and Zu [1], first public October 8, 2026, prove the general positive Helson-form representation and the positive trace-class criterion. Applied to this measure, their trace criterion already gives the case \(r>1\); that implication is **not** claimed as new. The present theorem instead identifies an exact leading coefficient for each eigenvalue and the full singular-value scale, including all quasi-Schatten exponents and an explicit weak-endpoint residue.

Chavan, Sahu, and Sinha [2], whose first version appeared in July 2024, establish general norm estimates, scattering statements, and Schatten necessary/sufficient conditions (Appendix Proposition A), but those statements do not supply this geometric atomic eigenvalue coefficient. The weighted Bergman Toeplitz and banded-matrix asymptotics discussed by Koïta, Kupin, Naboko, and Touré [3] are important related mechanisms; our proof explicitly supplies the required weighted Toeplitz counting argument and its Helson realization instead of treating their distinct operator class as absent. The August 2026 manuscript [4] studies related weighted Helson forms, but its full text could not be inspected; an unadvertised equivalent specialization is a residual originality risk.

## Limitations

The result assumes geometrically approaching real atoms and exactly polynomial mass factors. It does not classify general positive measures, arbitrary atomic spacing, or signed Helson forms. The coefficient is asymptotic rather than an exact closed form for each finite-index eigenvalue. The infinite-dimensional proof is analytical; finite numerical experiments are corroboration only. Independent originality and mathematical audits remain unperformed. No claim is made that earlier general trace-class criteria or established Toeplitz spectral methods are novel.

## References

[1] T. Ma, Y. Lu, C. Zu, *Unbounded Helson Forms with a Moment Representation*, arXiv:2610.12252v1 (first public 2026-10-08), sections 1 and 3.4, Theorem 3.4 and Example 3.6; https://arxiv.org/html/2610.12252v1.

[2] S. Chavan, C. K. Sahu, K. B. Sinha, *Helson matrices induced by measures*, arXiv:2407.04124v2 (first public 2024-07-04), Theorem 2.1 and Appendix Proposition A; https://arxiv.org/pdf/2407.04124.

[3] M. Koïta, S. Kupin, S. Naboko, B. Touré, *On spectral properties of compact Toeplitz operators on Bergman space with logarithmically decaying symbol and applications to banded matrices*, arXiv:2006.02586v1 (2020), introduction, Theorem 0.2 and section 4.2; https://arxiv.org/pdf/2006.02586.

[4] T. Ma, Y. Lu, C. Zu, *Helson Forms and Integral Operators on Bergman Spaces of Dirichlet Series*, arXiv:2608.22882v1 (2026-08-24), abstract inspected; https://arxiv.org/abs/2608.22882.
